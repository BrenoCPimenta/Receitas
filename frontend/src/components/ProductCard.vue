<template>
  <v-card
    class="mx-auto"
    max-width="344"
    color="#e7e9ec"
    rounded
    outlined
    depressed
    @click="goToRecipePage"
  >
    <v-img
      :src="img"
      height="200px"
    />

    <v-card-title class="d-flex">
      <v-tooltip top>
        <template v-slot:activator="{ on, attrs }">
          <p
            class="mycolor--text d-inline-block text-truncate text-center mb-0 flex-grow-1"
            v-bind="attrs"
            v-on="on"
          >
            {{ name }}
          </p>
        </template>
        <span>{{ name }}</span>
      </v-tooltip>
    </v-card-title>

    <!-- <v-card-actions>
      <v-btn
        color=mycolor
        text
      >
        Info
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions> -->
  </v-card>
</template>

<script>
export default {
  name: `ProductCard`,
  props: {
    img: {
      required: true,
      type: String,
    },
    name: {
      required: true,
      type: String,
    },
    url: {
      required: true,
      type: String,
    },
    // price: {
    //   required: true,
    //   type: String,
    // },
  },
  data: () => ({
    show: false,
  }),
  methods: {
    goToRecipePage() {
      window.open(this.url, `_blank`).focus();
    },
  },
};
</script>

<style>

.v-card {
  font-family: 'Ubuntu Condensed';
}

</style>
