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
    <!-- <hr>
    <v-container
      fill-height
      fluid
    >
      <v-row class="pt-2" justify="center">
        <v-btn
            color="mycolor"
            class="mx-2 white--text"
            depressed
            rounded
            outlined
          >
            <v-icon>mdi-chevron-down</v-icon>Filtros
          </v-btn>
      </v-row>
    </v-container> -->
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: ``,
    };
  },
  methods: {
    searchByText() {
      const { name } = this;
      this.$router.push({ query: { name } });
      axios
        .get(`http://localhost:8000/recipes/search/?name=${name}`)
        .then(response => (this.$store.dispatch(`setInfo`, response.data)))
        .catch(error => console.log(error)); // eslint-disable-line no-console
    },
  },

};
</script>

<style>

hr { background-color: #152348; height: 1px; border: 0; }

</style>
