<template>
  <v-card
    class="mx-auto"
    max-width="344"
    color="#e7e9ec"
    rounded
    outlined
    depressed
  >
    <v-img
      :src='img'
      height="200px"
    ></v-img>

    <v-card-title >
      
      <span
      class="mycolor--text d-inline-block text-truncate"
    >
      {{ name }}
    </span>
        
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

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text>
          I'm a thing. But, like most politicians, he promised more than he could deliver. You won't have time for sleeping, soldier, not with all the bed making you'll be doing. Then we'll go with that data file! Hey, you add a one and two zeros to that or we walk! You're going to do his laundry? I've got to find a way to escape.
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
import {
  UiCard,
  UiCardBody,
} from './ui/UiCard.vue';

export default {
  name: `ProductCard`,
  data: () => ({
      show: false,
    }),
  components: {
    UiCard,
    UiCardBody,
  },
  props: {
    img: {
      required: true,
      type: String,
    },
    name: {
      required: true,
      type: String,
    },
    // price: {
    //   required: true,
    //   type: String,
    // },
  },
};
</script>

<style>

.v-card {
  font-family: 'Ubuntu Condensed'; 
}

</style>
