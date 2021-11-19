<template>
  <div>
    <v-text-field
      v-model="queryString"
      clearable
      outlined
      placeholder="O que você quer comer hoje?"
      type="text"
      append-icon="mdi-magnify"
      class="pt-5"
      color="blue lighten-3"
      @click:append="searchByText"
      @keyup.enter="searchByText"
    />
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
