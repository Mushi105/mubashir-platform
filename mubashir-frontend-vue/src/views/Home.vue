<template>
  <div class="home-hero">
    <span class="badge">Solution Architect</span>
    <h1>Mubashir Hasan</h1>
    <p class="lead">Team Leader with 16+ Years in Banking Experience</p>
    
    <div class="stats-grid">
      <div class="stat-item">
        <span class="count">16+</span>
        <span class="label">Years Exp</span>
      </div>
      <div class="stat-item">
        <span class="count">AI/ML</span>
        <span class="label">AIOps L6</span>
      </div>
      <div class="stat-item">
        <span class="count">.NET</span>
        <span class="label">Backend Expert</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
.home-hero { text-align: center; padding: 100px 20px; }
.badge { background: #38bdf820; color: #38bdf8; padding: 5px 15px; border-radius: 20px; font-size: 0.9rem; border: 1px solid #38bdf840; }
h1 { font-size: 3.5rem; margin: 20px 0; color: white; }
.lead { font-size: 1.25rem; color: #94a3b8; }
.stats-grid { display: flex; justify-content: center; gap: 40px; margin-top: 50px; }
.stat-item { display: flex; flex-direction: column; }
.count { font-size: 2rem; font-weight: bold; color: #38bdf8; }
.label { color: #64748b; font-size: 0.8rem; text-transform: uppercase; }
</style>