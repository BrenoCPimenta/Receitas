import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  mode: `history`,
  base: process.env.BASE_URL,
  routes: [
    {
      path: `/home/`,
      // alias: `/home`,
      component: () => import(`./pages/PageHome.vue`),
      children: [
        {
          path: `/home/`,
          name: `home`,
          component: () => import(`./components/TextFilter.vue`),
        },
        {
          path: `/ingredients/`,
          component: () => import(`./components/IngredientFilter.vue`),
        },
      ],
      meta: {
        title: `Receitinhas`,
      },
    },
    {
      path: `/`,
      alias: `/login`,
      name: `login`,
      component: () => import(`./components/Login.vue`),
    },
    {
      path: `/dashboard`,
      name: `Dashboard`,
      component: () => import(`./pages/PageDashboard.vue`),
      meta: {
        title: `Receitinhas`,
      },
    },
  ],
});
