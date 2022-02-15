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

    <div>
      <v-app-bar
        v-if="username"
        color="blue-grey lighten-5"
        dense
        dark
        flat
        class="mycolor--text"
      >
        <v-app-bar-nav-icon color="mycolor"/>
        <v-avatar
          size="38"
          class="ml-3 mr-2"
        >
          <img
            src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blanko&eyeType=Default&eyebrowType=DefaultNatural%22"
          >
        </v-avatar>

        <v-toolbar-title>{{ username || 'Username' }}</v-toolbar-title>

        <v-spacer/>
        Logout
        <v-btn
          icon
          color="mycolor"
          class="ml-1"
          @click="clickLogout"
        >
          <v-icon>mdi-logout</v-icon>
        </v-btn>
      </v-app-bar>

      <v-app-bar
        v-else
        color="blue-grey lighten-5"
        dense
        dark
        flat
        class="mycolor--text"
      >
        <v-btn
          icon
          color="mycolor"
          class="mr-1"
          @click="clickLogout"
        >
          <v-icon>mdi-login</v-icon>
        </v-btn>
        Login
      </v-app-bar>
    </div>

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
        <SearchRating/>
        <ProductListingContainer :key="componentKey"/>
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
    SearchRating,
  },
  data() {
    return {
      currentTab: null,
      componentKey: 0,
      username: this.$route.params.username,
    };
  },
  watch: {
    '$store.state.info': function () {
      // console.log(this.$store.state.info);
      this.componentKey += 1;
    },
  },
  created() {
    this.tabs = [
      {
        text: `Busca Textual`,
        route: `/home/`,
        iconName: `mdi-magnify`,
      },
      {
        text: `Busca por Ingredientes`,
        route: `/ingredients/`,
        iconName: `mdi-format-list-checks`,
      },
    ];
  },
  methods: {
    clickLogout() {
      this.$router.replace({ name: `login` });
      console.log(this.$router);
    },
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
