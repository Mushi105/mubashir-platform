<template>
  <nav class="main-nav">
    <router-link to="/">Portfolio</router-link>
    <router-link to="/fintech">Fintech</router-link>
    <router-link to="/ai">AI Lab</router-link>
    <router-link to="/ecom">Store</router-link>
  </nav>
  <router-view></router-view>
</template>

<style>
.main-nav { background: #1e293b; padding: 15px; display: flex; gap: 20px; border-bottom: 1px solid #334155; }
.main-nav a { color: #94a3b8; text-decoration: none; font-weight: bold; }
.main-nav a.router-link-active { color: #38bdf8; }
</style>