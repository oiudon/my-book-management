import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

// Vuetify
import "vuetify/styles";
import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";

const vuetify = createVuetify({
  components,
  directives,
});

const app = createApp(App);

// $httpプロパティを追加
app.config.globalProperties.$http = (url, opts) => fetch(url, opts);

app.use(createPinia());
app.use(router);
// Vuetifyを登録
app.use(vuetify);

app.mount("#app");
