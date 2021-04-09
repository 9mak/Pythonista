window.addEventListener('load', init);

function init() {
const scene = newTHREE.Scene();
const camera = newTHREE.PerspectiveCamera(
  75,
  window.innerWidth / window.innerHeight,
  0.1,
  1000,
);

const renderer = newTHREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

const geometry = newTHREE.BoxGeometry();
const material = newTHREE.MeshBasicMaterial( { color:0x00ff00 } );
const cube = newTHREE.Mesh( geometry, material );
scene.add(cube);
camera.position.z = 5;

renderer.redner(scene, cmaera);
};
