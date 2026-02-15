<template>
  <div class="fintech-container">
    <h2>Fintech Operations Dashboard</h2>
    <div class="balance-card">
      <p>Current Balance (Encrypted at Rest)</p>
      <h3>{{ formattedBalance }}</h3>
    </div>
    
    <div class="actions">
      <button @click="initiateTransaction">New Transaction</button>
      <button @click="requestStatement">Export Statement</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const balance = ref(450000); // Sample data (4.5 Lac)
const formattedBalance = computed(() => {
  return new Intl.NumberFormat('en-PK', { style: 'currency', currency: 'PKR' }).format(balance.value);
});

const initiateTransaction = () => {
  console.log("Quantum-safe handshake initiated...");
};
</script>

<style scoped>
.fintech-container { padding: 20px; color: #38bdf8; }
.balance-card { background: #1e293b; padding: 20px; border-radius: 12px; border: 1px solid #334155; }
button { margin-right: 10px; padding: 10px 20px; background: #38bdf8; color: #0f172a; border: none; border-radius: 5px; cursor: pointer; }
</style>