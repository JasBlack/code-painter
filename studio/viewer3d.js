// ─────────────────────────────────────────────────────────────
//  3D object input: a small three.js viewer whose picture is fed to the painter like a live video.
//  Drag on the stage to turn the object (mouse or finger), scroll / pinch to zoom; it slowly turns by itself
//  when left alone. Loads .glb / .gltf (self-contained), .obj, .stl, .ply — or a demo object.
//  open(fileOrNull, dragElement) -> { video, name, dispose() }
// ─────────────────────────────────────────────────────────────
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OBJLoader } from 'three/addons/loaders/OBJLoader.js';
import { STLLoader } from 'three/addons/loaders/STLLoader.js';
import { PLYLoader } from 'three/addons/loaders/PLYLoader.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';

const SIZE = 1024;

// a colourful demo: a glossy, iridescent knot
function demo() {
  const g = new THREE.TorusKnotGeometry(1, 0.34, 360, 48, 2, 3);
  const m = new THREE.MeshPhysicalMaterial({ color: 0xb36bff, roughness: 0.18, metalness: 0.2, clearcoat: 1, clearcoatRoughness: 0.1, iridescence: 1, iridescenceIOR: 1.6, sheen: 0.4, sheenColor: 0x39ff88 });
  return new THREE.Mesh(g, m);
}
async function loadModel(file) {
  const url = URL.createObjectURL(file), ext = file.name.split('.').pop().toLowerCase();
  const plain = () => new THREE.MeshStandardMaterial({ color: 0xe8e4de, roughness: 0.45, metalness: 0.05 });
  try {
    if (ext === 'glb' || ext === 'gltf') return (await new GLTFLoader().loadAsync(url)).scene;
    if (ext === 'obj') { const o = await new OBJLoader().loadAsync(url); o.traverse(c => { if (c.isMesh && (!c.material || c.material.type === 'MeshPhongMaterial')) c.material = plain(); }); return o; }
    if (ext === 'stl' || ext === 'ply') {
      const geo = await (ext === 'stl' ? new STLLoader() : new PLYLoader()).loadAsync(url);
      if (!geo.attributes.normal) geo.computeVertexNormals();
      const mat = geo.attributes.color ? new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.5 }) : plain();
      return new THREE.Mesh(geo, mat);
    }
    throw new Error('use a .glb, .gltf, .obj, .stl or .ply file');
  } finally { setTimeout(() => URL.revokeObjectURL(url), 5000); }
}

export async function open(file, dragEl) {
  const obj = file ? await loadModel(file) : demo();
  const canvas = document.createElement('canvas'); canvas.width = canvas.height = SIZE;
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: true });
  renderer.setSize(SIZE, SIZE, false); renderer.toneMapping = THREE.ACESFilmicToneMapping; renderer.outputColorSpace = THREE.SRGBColorSpace;
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0c0c10);
  const pm = new THREE.PMREMGenerator(renderer); scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture;
  const key = new THREE.DirectionalLight(0xffffff, 1.6); key.position.set(-3, 4, 5); scene.add(key);
  const rim = new THREE.DirectionalLight(0xb36bff, 1.2); rim.position.set(4, -1, -3); scene.add(rim);
  // fit the object: centred, about 2 units across
  const box = new THREE.Box3().setFromObject(obj), size = box.getSize(new THREE.Vector3()), centre = box.getCenter(new THREE.Vector3());
  const k = 2.2 / Math.max(size.x, size.y, size.z, 1e-6);
  const holder = new THREE.Group(); obj.position.sub(centre); holder.add(obj); holder.scale.setScalar(k); scene.add(holder);
  const camera = new THREE.PerspectiveCamera(35, 1, 0.01, 100); camera.position.set(0.6, 0.5, 4.2);
  const controls = new OrbitControls(camera, dragEl);
  controls.enableDamping = true; controls.dampingFactor = 0.08; controls.autoRotate = true; controls.autoRotateSpeed = 1.2;
  controls.minDistance = 1.2; controls.maxDistance = 12;
  let idle = 0;
  controls.addEventListener('start', () => { controls.autoRotate = false; idle = 0; });
  controls.addEventListener('end', () => { idle = performance.now(); });
  renderer.setAnimationLoop(() => {
    if (!controls.autoRotate && idle && performance.now() - idle > 3000) controls.autoRotate = true;   // back to turning slowly
    controls.update(); renderer.render(scene, camera);
  });
  // the painter reads it like a live video
  const video = document.createElement('video'); video.muted = true; video.playsInline = true;
  video.srcObject = canvas.captureStream(30);
  await video.play();
  await new Promise(r => { if (video.videoWidth) r(); else video.onloadedmetadata = r; });
  dragEl.style.cursor = 'grab';
  return {
    video, canvas, name: file ? file.name.replace(/\.[^.]+$/, '') : '3D knot',
    dispose() {
      renderer.setAnimationLoop(null); controls.dispose(); dragEl.style.cursor = '';
      video.srcObject.getTracks().forEach(t => t.stop()); renderer.dispose(); pm.dispose();
    }
  };
}
