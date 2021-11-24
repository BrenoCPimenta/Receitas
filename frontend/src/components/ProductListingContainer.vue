<template>
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
    };
  },
  created() {
    this.endpoint = options => get({
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
