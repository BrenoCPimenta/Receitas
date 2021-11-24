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
            v-model="queryString"
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
  </div>
</template>

<script>
export default {
  data() {
    return {
      queryString: ``,
    };
  },
  methods: {
    searchByText() {
      const { queryString } = this;
      this.$router.push({ query: { queryString } });
    },
  },
};
</script>

<style>

</style>
