<template>
  <div
    id="home-root"
    :class="$style.wrap"
  >
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

      <div :class="$style.listing">
        <Dashboard/>
      </div>
    </div>
  </div>
</template>

<script>
import Dashboard from '../components/Dashboard.vue';

export default {
  name: `PageDashboard`,
  components: {
    Dashboard,
  },
};
</script>

<style lang="scss" module>
@import url("https://fonts.googleapis.com/css2?family=Montserrat+Alternates:wght@500&display=swap");

.intro {
  max-width: 37em;
  margin-right: auto;
  margin-left: auto;
  font-size: 1.25em;
}
</style>
