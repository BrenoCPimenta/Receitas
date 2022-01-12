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
      @selectA="selectA"
      @selectTR="selectTR"
      @selectP="selectP"
      @selectTP="selectTP"
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
      f_a: null,
      f_tr: null,
      f_p: null,
      f_tp: null,
    };
  },
  methods: {
    searchByText() {
      const { name } = this;
      const filters = [this.f_a, this.f_tr, this.f_p, this.f_tp].join(`,`);

      this.$router.push({ query: { name, filters } });
      this.show = 0;
    },
    clickFilters() {
      if (this.show === 0) {
        this.show = 1;
      } else {
        this.show = 0;
      }
    },
    selectA(e) {
      this.f_a = e;
    },
    selectTR(e) {
      this.f_tr = e;
    },
    selectP(e) {
      this.f_p = e;
    },
    selectTP(e) {
      this.f_tp = e;
    },
  },

};
</script>

<style>

hr { background-color: #152348; height: 1px; border: 0; }

</style>
