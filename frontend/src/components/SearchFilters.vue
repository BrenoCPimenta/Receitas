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
        <v-icon>mdi-message-star</v-icon>
        <v-select
          :items="items_a"
          label="Popularidade (mín.)"
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
        <v-icon>mdi-clock</v-icon>
        <v-select
          :items="items_tp"
          label="Preparo (mín.)"
          color="mycolor"
          class="pl-4 pr-4"
          dense
          @change="selectTP_min"
        />
        <v-select
          :items="items_tp"
          label="Preparo (máx.)"
          color="mycolor"
          class="pl-4 pr-4"
          dense
          @change="selectTP_max"
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
          label="Porções (mín.)"
          color="mycolor"
          class="pl-4 pr-4"
          dense
          @change="selectP_min"
        />
        <v-select
          :items="items_p"
          label="Porções (máx.)"
          color="mycolor"
          class="pl-4 pr-4"
          dense
          @change="selectP_max"
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
      items_a: [`5 favoritos`, `10 favoritos`, `20 favoritos`, `40 favoritos`, `80 favoritos`, `160 favoritos`],
      items_tr: [`Bolos e tortas doces`, `Lanches`, `Massas`, `Saladas, molhos e acompanhamentos`,
        `Doces e sobremesas`, `Alimentação Saudável`, `Carnes`, `Prato Único`, `Aves`,
        `Bebidas`, `Peixes e frutos do mar`, `Sopas`],
      items_p: [`1 porção`, `2 porções`, `3 porções`, `4 porções`, `5 porções`, `6 porções`, `7 porções`, `8 porções`, `9 porções`, `10 porções`, `11 porções`, `12 porções`],
      items_tp: [`5 minutos`, `10 minutos`, `15 minutos`, `20 minutos`, `25 minutos`, `30 minutos`, `45 minutos`, `1 hora`, `2 horas`],
    };
  },
  methods: {
    selectTR(e) {
      this.$emit(`selectTR`, e);
    },
    selectA(e) {
      this.$emit(`selectA`, e.match(/\d+/g));
    },
    selectTP_min(e) {
      this.$emit(`selectTP_min`, e.match(/\d+/g));
    },
    selectTP_max(e) {
      this.$emit(`selectTP_max`, e.match(/\d+/g));
    },
    selectP_min(e) {
      this.$emit(`selectP_min`, e.match(/\d+/g));
    },
    selectP_max(e) {
      this.$emit(`selectP_max`, e.match(/\d+/g));
    },

  },
};
</script>
