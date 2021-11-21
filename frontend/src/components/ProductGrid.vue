<template>
  <div>
    <v-row>
      <v-col class="text-left">
        <div class="text-h6 mycolor--text pl-0">
          Resultados da busca:
        </div>
      </v-col>
      <v-col class="text-right">
        <v-btn
          icon
          rounded
          disabled
          depressed
          large
          class="ma-2 white--text"
        >
          <v-icon>mdi-dots-grid</v-icon>
        </v-btn>
        <v-btn
          icon
          rounded
          depressed
          large
          color="mycolor"
          class="ma-2 white--text"
          @click="listView"
        >
          <v-icon>mdi-format-list-bulleted</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <UiGrid data-qa="product grid">
      <UiGridItem
        v-for="product in products"
        :key="product.name"
        :width="[`12/12`, `4/12@m`]"
        data-qa="product"
      >
        <ProductCard
          :img="product.img"
          :name="product.name"
        />
      </UiGridItem>
    </UiGrid>
  </div>
</template>

<script>
import {
  UiGrid,
  UiGridItem,
} from './ui/UiGrid.vue';
import ProductCard from './ProductCard.vue';

export default {
  name: `ProductGrid`,
  components: {
    ProductCard,
    UiGrid,
    UiGridItem,
  },
  props: {
    products: {
      default: () => [],
      type: Array,
    },
  },
  methods: {
    listView() {
      this.$emit(`listView`);
    },
  },
};
</script>
