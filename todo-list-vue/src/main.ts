import { createApp } from 'vue';
import App from './App.vue';
import store from './store/store';
import './style.css';

const app = createApp(App);
app.provide('store', store); // Fornece o store para os componentes
app.mount('#app');