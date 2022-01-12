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
          rounded
          depressed
          icon
          large
          color="mycolor"
          class="ma-2 white--text"
          @click="gridView"
        >
          <v-icon>mdi-dots-grid</v-icon>
        </v-btn>
        <v-btn
          rounded
          disabled
          depressed
          icon
          large
          class="ma-2 white--text"
        >
          <v-icon>mdi-format-list-bulleted</v-icon>
        </v-btn>
      </v-col>
    </v-row>
    <v-list nav>
      <v-list-item-group
        v-model="selectedItem"
        color="mycolor"
      >
        <template v-for="(item, index) in products">
          <v-subheader
            v-if="item.header"
            :key="item.header"
            v-text="item.header"
          />

          <v-divider
            v-if="false"
            :key="index"
            :inset="false"
          />

          <v-list-item
            :key="item.title"
          >
            <v-list-item-avatar
              tile
              height="60"
              width="80"
            >
              <v-img :src="item.images[0]"/>
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title v-html="item.recipe_title"/>
              <v-list-item-subtitle v-html="item.group"/>
            </v-list-item-content>

            <v-list-item-action>
              <!-- <v-btn icon>
            <v-icon color="grey lighten-1">mdi-information</v-icon>
          </v-btn> -->
            </v-list-item-action>
          </v-list-item>
        </template>
      </v-list-item-group>
    </v-list>
  </div>
</template>

<script>
export default {
  props: {
    products: {
      default: () => [],
      type: Array,
    },
  },
  methods: {
    gridView() {
      this.$emit(`gridView`);
    },
  },
};
</script>
