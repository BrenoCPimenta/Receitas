<template>
  <v-app>
    <LayoutDefault>
      <RouterView/>
    </LayoutDefault>
  </v-app>
</template>

<script>
import axios from 'axios';
import LayoutDefault from './layouts/LayoutDefault.vue';

export default {
  name: `App`,
  components: {
    LayoutDefault,
  },
  watch: {
    $route(to) {
      document.title = to.meta.title || `Receitinhas`;

      const query = to.fullPath.substring(to.fullPath.indexOf(`?`) + 1);
      const params = new URLSearchParams(query);
      [...params.entries()].forEach(([key, value]) => {
        if (!value) {
          params.delete(key);
        }
      });
      const cleaned = String(params);
      if (cleaned) {
        axios
          .get(`${process.env.VUE_APP_API_URL}/recipes/search/?${cleaned}`)
          .then(response => (this.$store.dispatch(`setInfo`, response.data)))
          .catch(error => console.log(error));
      }
    },
  },
};
</script>

<style lang="scss">
@import '~reset-css/sass/reset';

html {
  text-size-adjust: 100%;
}

body {
  line-height: 1.3;
  color: #222;
  font-family: sans-serif;
}

img {
  max-width: 100%;
  max-height: 100%;
  width: auto;
  vertical-align: middle;
}
</style>
