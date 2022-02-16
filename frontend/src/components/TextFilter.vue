<template>
  <div>
    <v-container
      fill-height
      fluid
    >
      <v-row
        class="pt-8"
        align="baseline"
        no-gutters
      >
        <v-col
          class="text-left"
          cols="12"
          md="11"
        >
          <v-text-field
            id="search_input"
            v-model="name"
            light
            clearable
            outlined
            label="O que você quer comer hoje?"
            type="text"
            class="mx-2 rounded-xl"
            color="mycolor"
            @keyup.enter="searchByText"
          />
        </v-col>
        <v-col
          class="text-right"
          cols="12"
          md="1"
        >
          <v-btn
            id="search_button"
            color="mycolor"
            class="mx-2 white--text"
            depressed
            rounded
            fab
            @click="searchByText"
          >
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>

    <SearchFilters
      v-if="show"
      @selectTR="selectTR"
      @selectA="selectA"
      @selectTP_min="selectTP_min"
      @selectTP_max="selectTP_max"
      @selectP_min="selectP_min"
      @selectP_max="selectP_max"
    />

    <hr>
    <v-container
      fill-height
      fluid
    >
      <v-row
        class="pt-2"
        justify="center"
      >
        <v-btn
          color="mycolor"
          class="mx-2 white--text"
          depressed
          rounded
          outlined
          @click="clickFilters"
        >
          <v-icon v-if="show">
            mdi-chevron-up
          </v-icon>
          <v-icon v-if="!show">
            mdi-chevron-down
          </v-icon>
          Filtros
        </v-btn>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import SearchFilters from "./SearchFilters.vue";

export default {
  name: `TextFilter`,
  components: {
    SearchFilters,
  },
  data() {
    return {
      name: ``,
      show: 0,
      group: null,
      favorites_min: null,
      favorites_max: null,
      time_min: null,
      time_max: null,
      portions_min: null,
      portions_max: null,
    };
  },
  methods: {
    searchByText() {
      const { name } = this;
      // const filters = [this.f_a, this.f_tr, this.f_p, this.f_tp].join(`,`);


      this.$router.push({
        query: {
          name,
          group: this.group,
          favorites_min: this.favorites_min,
          favorites_max: this.favorites_max,
          time_min: this.time_min,
          time_max: this.time_max,
          portions_min: this.portions_min,
          portions_max: this.portions_max,
        },
      });
      this.show = 0;
      this.group = null;
      this.favorites_min = null;
      this.favorites_max = null;
      this.time_min = null;
      this.time_max = null;
      this.portions_min = null;
      this.portions_max = null;
    },
    clickFilters() {
      if (this.show === 0) {
        this.show = 1;
      } else {
        this.show = 0;
      }
    },
    selectTR(e) {
      this.group = e;
    },
    selectA(e) {
      this.favorites_min = e;
    },
    selectTP_min(e) {
      this.time_min = e;
    },
    selectTP_max(e) {
      this.time_max = e;
    },
    selectP_min(e) {
      this.portions_min = e;
    },
    selectP_max(e) {
      this.portions_max = e;
    },
  },

};
</script>

<style>

hr { background-color: #152348; height: 1px; border: 0; }

</style>
