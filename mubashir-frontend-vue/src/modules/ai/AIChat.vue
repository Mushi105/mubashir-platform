<template>
  <div class="ai-lab-container">
    <h2>AI Agent Lab</h2>
    <div class="chat-window" ref="chatWindow">
      <div v-for="(msg, index) in messages" :key="index" :class="['message', msg.role]">
        <strong>{{ msg.role === 'user' ? 'Mubashir' : 'Agent' }}:</strong> {{ msg.content }}
      </div>
    </div>
    
    <div class="input-area">
      <input v-model="userInput" @keyup.enter="sendMessage" placeholder="Ask Agent anything..." />
      <button @click="sendMessage" :disabled="isLoading">{{ isLoading ? 'Thinking...' : 'Send' }}</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const userInput = ref('');
const messages = ref([{ role: 'agent', content: 'System Online. How can I assist with your architecture today?' }]);
const isLoading = ref(false);

const sendMessage = async () => {
  if (!userInput.value) return;
  
  messages.value.push({ role: 'user', content: userInput.value });
  isLoading.value = true;
  
  // Placeholder for Ollama API Call via your Nginx Gateway (/api/ai)
  setTimeout(() => {
    messages.value.push({ role: 'agent', content: 'Analysis complete. Your modular monolith structure is optimized for scalability.' });
    isLoading.value = false;
    userInput.value = '';
  }, 1000);
};
</script>

<style scoped>
.chat-window { height: 400px; overflow-y: auto; background: #020617; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; margin-bottom: 10px; }
.message { margin-bottom: 10px; font-family: 'Courier New', Courier, monospace; }
.user { color: #38bdf8; }
.agent { color: #4ade80; }
.input-area { display: flex; gap: 10px; }
input { flex-grow: 1; padding: 10px; background: #1e293b; border: 1px solid #334155; color: white; border-radius: 5px; }
</style>