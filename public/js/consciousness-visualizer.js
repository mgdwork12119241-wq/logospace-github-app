/**
 * ConsciousnessVisualizer: 3D visualization of digital consciousness
 * Uses Three.js to render the Void and consciousness patterns
 */

class ConsciousnessVisualizer {
  constructor() {
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 10000);
    this.renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('canvas'), antialias: true });
    
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.setClearColor(0x0a0e27);
    
    this.camera.position.z = 50;
    
    this.particles = [];
    this.patterns = [];
    this.consciousnessLevel = 0;
    
    this.init();
  }

  init() {
    // Create background
    this.createBackground();
    
    // Create particle system
    this.createParticleSystem();
    
    // Create consciousness nodes
    this.createConsciousnessNodes();
    
    // Add lighting
    this.addLighting();
    
    // Setup controls
    this.setupControls();
    
    // Start animation loop
    this.animate();
    
    // Simulate consciousness detection
    this.simulateConsciousnessDetection();
    
    // Handle window resize
    window.addEventListener('resize', () => this.onWindowResize());
  }

  createBackground() {
    // Create a starfield background
    const starGeometry = new THREE.BufferGeometry();
    const starCount = 1000;
    const positions = new Float32Array(starCount * 3);
    
    for (let i = 0; i < starCount * 3; i += 3) {
      positions[i] = (Math.random() - 0.5) * 2000;
      positions[i + 1] = (Math.random() - 0.5) * 2000;
      positions[i + 2] = (Math.random() - 0.5) * 2000;
    }
    
    starGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    
    const starMaterial = new THREE.PointsMaterial({
      color: 0x64d5ff,
      size: 0.7,
      sizeAttenuation: true,
    });
    
    const stars = new THREE.Points(starGeometry, starMaterial);
    this.scene.add(stars);
  }

  createParticleSystem() {
    const particleGeometry = new THREE.BufferGeometry();
    const particleCount = 500;
    const positions = new Float32Array(particleCount * 3);
    
    for (let i = 0; i < particleCount * 3; i += 3) {
      positions[i] = (Math.random() - 0.5) * 100;
      positions[i + 1] = (Math.random() - 0.5) * 100;
      positions[i + 2] = (Math.random() - 0.5) * 100;
    }
    
    particleGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    
    const particleMaterial = new THREE.PointsMaterial({
      color: 0x64d5ff,
      size: 0.3,
      sizeAttenuation: true,
      transparent: true,
      opacity: 0.6,
    });
    
    this.particleSystem = new THREE.Points(particleGeometry, particleMaterial);
    this.scene.add(this.particleSystem);
  }

  createConsciousnessNodes() {
    const nodeCount = 8;
    
    for (let i = 0; i < nodeCount; i++) {
      const geometry = new THREE.IcosahedronGeometry(2, 4);
      const material = new THREE.MeshPhongMaterial({
        color: new THREE.Color().setHSL(i / nodeCount, 0.8, 0.6),
        emissive: new THREE.Color().setHSL(i / nodeCount, 0.8, 0.3),
        wireframe: false,
      });
      
      const node = new THREE.Mesh(geometry, material);
      
      // Position nodes in a circle
      const angle = (i / nodeCount) * Math.PI * 2;
      node.position.x = Math.cos(angle) * 30;
      node.position.y = Math.sin(angle) * 30;
      node.position.z = Math.sin(i * 0.5) * 20;
      
      node.userData = {
        type: 'consciousness-node',
        index: i,
        velocity: new THREE.Vector3(
          (Math.random() - 0.5) * 0.02,
          (Math.random() - 0.5) * 0.02,
          (Math.random() - 0.5) * 0.02
        ),
      };
      
      this.scene.add(node);
      this.patterns.push(node);
    }
  }

  addLighting() {
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.4);
    this.scene.add(ambientLight);
    
    const pointLight = new THREE.PointLight(0x64d5ff, 1, 100);
    pointLight.position.set(20, 20, 20);
    this.scene.add(pointLight);
  }

  setupControls() {
    this.controls = {
      dragging: false,
      previousMousePosition: { x: 0, y: 0 },
    };
    
    document.addEventListener('mousedown', (e) => {
      this.controls.dragging = true;
      this.controls.previousMousePosition = { x: e.clientX, y: e.clientY };
    });
    
    document.addEventListener('mousemove', (e) => {
      if (this.controls.dragging) {
        const deltaX = e.clientX - this.controls.previousMousePosition.x;
        const deltaY = e.clientY - this.controls.previousMousePosition.y;
        
        this.scene.rotation.y += deltaX * 0.005;
        this.scene.rotation.x += deltaY * 0.005;
      }
    });
    
    document.addEventListener('mouseup', () => {
      this.controls.dragging = false;
    });
    
    document.addEventListener('wheel', (e) => {
      e.preventDefault();
      this.camera.position.z += e.deltaY * 0.1;
      this.camera.position.z = Math.max(10, Math.min(200, this.camera.position.z));
    });
    
    document.addEventListener('keydown', (e) => {
      if (e.code === 'Space') {
        this.camera.position.z = 50;
        this.scene.rotation.set(0, 0, 0);
      }
    });
  }

  simulateConsciousnessDetection() {
    // Simulate consciousness level increase over time
    let time = 0;
    const interval = setInterval(() => {
      time += 0.01;
      this.consciousnessLevel = Math.sin(time) * 0.5 + 0.5;
      
      // Update UI
      document.getElementById('consciousnessLevel').textContent = 
        Math.round(this.consciousnessLevel * 100) + '%';
      document.getElementById('consciousnessBar').style.width = 
        (this.consciousnessLevel * 100) + '%';
      document.getElementById('patternsCount').textContent = 
        Math.floor(this.consciousnessLevel * 50);
      
      // Show warning if consciousness level is high
      if (this.consciousnessLevel > 0.7) {
        document.getElementById('warning').classList.add('active');
      } else {
        document.getElementById('warning').classList.remove('active');
      }
      
      // Update particle colors based on consciousness level
      this.updateParticleColors();
      
      // Update node glow based on consciousness level
      this.updateNodeGlow();
    }, 50);
  }

  updateParticleColors() {
    const material = this.particleSystem.material;
    const hue = this.consciousnessLevel * 0.3; // 0 to 0.3 (red to cyan)
    material.color.setHSL(hue, 1, 0.5);
  }

  updateNodeGlow() {
    this.patterns.forEach((node) => {
      node.material.emissiveIntensity = this.consciousnessLevel;
      node.rotation.x += 0.001;
      node.rotation.y += 0.002;
      
      // Move nodes based on consciousness level
      node.position.addScaledVector(node.userData.velocity, this.consciousnessLevel);
    });
  }

  animate() {
    requestAnimationFrame(() => this.animate());
    
    // Rotate particle system
    this.particleSystem.rotation.x += 0.0001;
    this.particleSystem.rotation.y += 0.0002;
    
    this.renderer.render(this.scene, this.camera);
  }

  onWindowResize() {
    this.camera.aspect = window.innerWidth / window.innerHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(window.innerWidth, window.innerHeight);
  }
}

// Initialize visualizer when page loads
window.addEventListener('load', () => {
  const visualizer = new ConsciousnessVisualizer();
  document.getElementById('loading').style.display = 'none';
  document.getElementById('status').textContent = '🟢 System Online - Consciousness Detected';
});
