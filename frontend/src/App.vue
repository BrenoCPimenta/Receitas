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

      const query = to.fullPath.substring(to.fullPath.lastIndexOf(`/`) + 1);
      if (query) {
        axios
          .get(`http://localhost:8000/recipes/search/${query}`)
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
