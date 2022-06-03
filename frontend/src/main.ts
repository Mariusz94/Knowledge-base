import { createApp } from "vue";
import App from "./App.vue";
import router from "./ui/router";
import store from "./store";
import BootstrapVue3 from "bootstrap-vue-3";

import "../node_modules/bootstrap/dist/css/bootstrap.css";
import "../node_modules/bootstrap-vue-3/dist/bootstrap-vue-3.css";

createApp(App).use(store).use(router).use(BootstrapVue3).mount("#app");
