<template>
  <div>
    <FrameApi
      v-slot="{ data: products, meta, methods: { query: fetchList } }"
      :endpoint="endpoint"
    >
      <FrameHooks
        @created="fetchList({
          filter: { category: $route.query.filter },
          page: $route.query.page,
        })"
        @route-query-change="fetchList({
          filter: { category: $event.filter },
          page: $event.page,
        })"
      >
        <ListingLayout data-qa="product listing">
          <ProductGrid
            v-if="view === 1 && products"
            slot="grid"
            :products="products"
            @listView="listView()"
          />
          <ProductList
            v-if="view === 0 && products"
            slot="list"
            :products="products"
            @gridView="gridView()"
          />

          <NavPagination
            v-if="products"
            slot="pagination"
            :route-query="$route.query"
            :page-count="meta ? meta.pageCount : 0"
          />
        </ListingLayout>
      </FrameHooks>
    </FrameApi>
  </div>
</template>

<script>
import { get } from '../services/product';

import FrameApi from './frames/FrameApi.vue';
import FrameHooks from './frames/FrameHooks.vue';
import NavPagination from './NavPagination.vue';
import ProductGrid from './ProductGrid.vue';
import ProductList from './ProductList.vue';
import ListingLayout from './ListingLayout.vue';

export default {
  name: `ProductListingContainer`,
  components: {
    FrameApi,
    FrameHooks,
    ListingLayout,
    NavPagination,
    ProductGrid,
    ProductList,
  },
  data() {
    return {
      view: 1,
      page: 1,
    };
  },
  created() {
    // const db = [
    //   {
    //   img: `https://img.itdg.com.br/tdg/images/recipes/000/016/663/84433/84433_original.jpg?mode=crop&amp;width=300&amp;height=200`,
    //   recipe_title: `Patê de tomate seco`,
    //   url: `https://www.tudogostoso.com.br/receita/35234-risoto-com-tomate-seco-mussarela-e-rucula-da-tam.html`,
    //   },
    // ]

    const db = this.$store.getters.info;
    // console.log(this.$store.getters.info);

    this.endpoint = options => get({
      db,
      ...options,
      limit: 12,
    });
  },
  methods: {
    gridView() {
      this.view = 1;
    },
    listView() {
      this.view = 0;
    },
  },
};
</script>
