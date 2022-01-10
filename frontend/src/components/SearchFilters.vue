<template>
  <v-container
    fluid
    class="pt-0"
  >
    <v-row
      align="center"
      class="pb-4"
    >
      <v-col
        class="d-flex"
        cols="12"
        sm="6"
      >
        <v-icon>mdi-message-star</v-icon>
        <v-select
          :items="items_a"
          label="Avaliação"
          color="mycolor"
          class="pl-4 pr-4"
          dense
          @change="selectA"
        />
      </v-col>

      <v-col
        class="d-flex"
        cols="12"
        sm="6"
      >
        <v-icon>mdi-chef-hat</v-icon>
        <v-select
          :items="items_tr"
          label="Tipo de receitas"
          color="mycolor"
          class="pl-4 pr-4"
          dense
          @change="selectTR"
        />
      </v-col>

      <v-col
        class="d-flex"
        cols="12"
        sm="6"
      >
        <v-icon>mdi-account-multiple</v-icon>
        <v-select
          :items="items_p"
          label="Porções"
          color="mycolor"
          class="pl-4 pr-4"
          dense
          @change="selectP"
        />
      </v-col>

      <v-col
        class="d-flex"
        cols="12"
        sm="6"
      >
        <v-icon>mdi-clock</v-icon>
        <v-select
          :items="items_tp"
          label="Tempo de preparo"
          color="mycolor"
          class="pl-4 pr-4"
          dense
          @change="selectTP"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: `SearchFilters`,
  data() {
    return {
      items_a: [`5 estrelas`, `4 estrelas`, `3 estrelas`],
      items_tr: [`Bolos`, `Saladas`, `Aperitivos`],
      items_p: [`1 porção`, `2 porções`, `3 porções`],
      items_tp: [`5 minutos`, `15 minutos`, `30 minutos`, `1 hora`],
    };
  },
  methods: {
    selectA(e) {
      this.$emit(`selectA`, e);
    },
    selectTR(e) {
      this.$emit(`selectTR`, e);
    },
    selectP(e) {
      this.$emit(`selectP`, e);
    },
    selectTP(e) {
      this.$emit(`selectTP`, e);
    },
  },
};
</script>
