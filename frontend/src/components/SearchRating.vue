<template>
  <div class="d-flex flex-column align-center">
    <p>Quão satisfeito você ficou com o resultado dessa busca?</p>
    <v-rating
      v-if="!ratingSubmitted"
      background-color="grey"
      color="primary"
      empty-icon="mdi-star-outline"
      full-icon="mdi-star"
      hover
      length="5"
      size="24"
      :value="rating"
      @input="setRating"
    />
    <p v-else>
      Obrigado pela avaliação.
    </p>
  </div>
</template>

<script>
export default {
  name: `SearchRating`,
  computed: {
    rating() {
      return this.$store.getters.rating;
    },
    ratingSubmitted() {
      return this.rating !== null;
    },
  },
  methods: {
    setRating(value) {
      this.$store.dispatch(`setRating`, value);
    },
  },
};
</script>
