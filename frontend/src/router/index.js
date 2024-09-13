import { createRouter, createWebHistory } from "vue-router";
import IndexView from "../views/IndexView.vue";
import RegistrationView from "@/views/RegistrationView.vue";

const routes = [
  {
    path: "/",
    name: "index",
    meta: {
      title: "Главная"
    },
    component: IndexView,
  },
  {
    path: "/registration/:target",
    name: "registration",
    meta: {
      title: "Регистрация",
    },
    component: RegistrationView,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

const DEFAULT_TITLE = 'Педагогическая мастерская';
router.beforeEach((to) => {
  document.title = to.meta.title + " / " + DEFAULT_TITLE;
});

export default router;
