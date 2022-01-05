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
        <v-row
          align="center"
          justify="center"
        >
          <v-img
            src="../assets/receitinhas4.png"
            max-width="37em"
          />
        </v-row>
      </v-container>

      <v-tabs
        v-model="currentTab"
        grow
        centered
        icons-and-text
        color="mycolor"
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
        <SearchRating />
        <ProductListingContainer/>
      </div>
    </div>
  </div>
</template>

<script>
import ProductListingContainer from '../components/ProductListingContainer.vue';
import SearchRating from '../components/SearchRating.vue';

export default {
  name: `PageProducts`,
  components: {
    ProductListingContainer,
    SearchRating
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
  max-width: 37em;
  margin-right: auto;
  margin-left: auto;
  font-size: 1.25em;

}

</style>
