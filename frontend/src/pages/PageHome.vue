<template>
  <div
    id="home-root"
    :class="$style.wrap"
  >
    <!-- <div :class="$style.intro">
      <v-icon
        x-large
        color="blue lighten-3"
      >
        mdi-silverware-variant
      </v-icon>
      <h1 :class="$style.headline">
        Receitas
      </h1>
    </div> -->

    <div :class="$style.intro">
       <v-container>
        <v-row align="center" justify="center">
          <v-img
          src="../assets/receitinhas3.png"
          max-width="40em"
          
          ></v-img>
        </v-row>
      </v-container>
    </div>

    <v-tabs
      v-model="currentTab"
      grow
      centered
      icons-and-text
      color=mycolor
    >
      <v-tabs-slider/>
      <v-tab
        v-for="tab in tabs"
        :key="tab.route"
        :to="tab.route"
      >
        <p>{{ tab.text }}</p>
        <v-icon>{{ tab.iconName }}</v-icon>
      </v-tab>
    </v-tabs>

    <RouterView/>

    <div :class="$style.listing">
      <ProductListingContainer/>
    </div>
  </div>
</template>

<script>
import ProductListingContainer from '../components/ProductListingContainer.vue';

export default {
  name: `PageProducts`,
  components: {
    ProductListingContainer,
  },
  data: () => ({
    currentTab: null,
  }),
  created() {
    this.tabs = [
      {
        text: `Busca Textual`,
        route: `/`,
        iconName: `mdi-magnify`,
      },
      {
        text: `Busca por Ingredientes`,
        route: `/ingredientes?text=novo`,
        iconName: `mdi-format-list-checks`,
      },
    ];
  },
};
</script>

<style lang="scss" module>
@import url('https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@500&display=swap');

.intro {
  max-width: 32em;
  margin-right: auto;
  margin-left: auto;
  font-size: 1.25em;
  text-align: center;
}

.headline {
  margin-bottom: 0.5em;
  font-size: 1.75em;
  line-height: 1.2;
  font-family: 'Montserrat Alternates', sans-serif;
}

.listing,
.teaser {
  margin-top: 3em;
}
</style>
