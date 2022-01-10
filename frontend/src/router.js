import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  mode: `history`,
  base: process.env.BASE_URL,
  routes: [
    {
      path: `/`,
      alias: `/home`,
      name: `home`,
      component: () => import(`./pages/PageHome.vue`),
      children: [
        {
          path: `/`,
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
  ],
});
