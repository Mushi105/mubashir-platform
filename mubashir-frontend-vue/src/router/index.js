import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import FintechDashboard from '../modules/fintech/Dashboard.vue';
import AIChat from '../modules/ai/AIChat.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/fintech', component: FintechDashboard },
  { path: '/ai', component: AIChat }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;