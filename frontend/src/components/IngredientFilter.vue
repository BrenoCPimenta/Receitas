<template>
  <div>
    <v-container
      fill-height
      fluid
    >
      <v-row
        class="pt-8"
        align="baseline"
        no-gutters
      >
        <v-col
          class="text-left"
          cols="12"
          md="11"
        >
          <v-combobox
            v-model="model"
            :filter="filter"
            :hide-no-data="!search"
            :search-input.sync="search"
            :items="items"
            hide-selected
            label="Quais ingredientes você quer usar?"
            multiple
            small-chips
            outlined
            allow-overflow="false"
            class="mx-2 rounded-xl"
            color="mycolor"
            clearable
            attach
            light
          >
            <template v-slot:no-data>
              <v-list-item>
                <span class="subheading">Pressione enter para adicionar&nbsp;</span>
                <v-chip
                  :color="`${colors[nonce - 1]} lighten-4`"
                  label
                  class="ma-2 mycolor--text rounded-lg"
                >
                  {{ search }}
                </v-chip>
                <span class="subheading">&nbsp;à lista de ingredientes.</span>
              </v-list-item>
            </template>
            <template v-slot:selection="{ attrs, item, parent, selected }">
              <v-chip
                v-if="item === Object(item)"
                v-bind="attrs"
                :color="`${item.color} lighten-4`"
                :input-value="selected"
                label
                class="ma-2 mycolor--text rounded-lg"
              >
                <span class="pr-2">
                  {{ item.text }}
                </span>
                <v-icon
                  small
                  @click="parent.selectItem(item)"
                >
                  $delete
                </v-icon>
              </v-chip>
            </template>

            <template v-slot:item="{ index, item }">
              <v-text-field
                v-if="editing === item"
                v-model="editing.text"
                autofocus
                flat
                background-color="transparent"
                hide-details
                solo
                @keyup.enter="edit(index, item)"
              />
              <v-chip
                v-else
                :color="`${item.color} lighten-4`"
                label
                class="ma-2 mycolor--text rounded-lg"
              >
                {{ item.text }}
              </v-chip>
              <v-spacer/>
              <v-list-item-action @click.stop>
                <v-btn
                  icon
                  @click.stop.prevent="edit(index, item)"
                >
                  <v-icon>{{ editing !== item ? 'mdi-pencil' : 'mdi-check' }}</v-icon>
                </v-btn>
              </v-list-item-action>
            </template>
            <!-- <template v-slot:append>
          <v-btn
          class="searchBtn"
          height="auto"
          text
          rounded
          >
          <v-icon>mdi-magnify</v-icon>
          Buscar
          </v-btn>
        </template> -->
          </v-combobox>
        </v-col>
        <v-col
          class="text-right"
          cols="12"
          md="1"
        >
          <v-btn
            color="mycolor"
            class="mx-2 white--text"
            depressed
            rounded
            fab
            @click="searchByIngredients"
          >
            <v-icon>mdi-magnify</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>

    <SearchFilters
      v-if="show"
      @selectTR="selectTR"
      @selectA="selectA"
      @selectTP_min="selectTP_min"
      @selectTP_max="selectTP_max"
      @selectP_min="selectP_min"
      @selectP_max="selectP_max"
    />

    <hr>
    <v-container
      fill-height
      fluid
    >
      <v-row
        class="pt-2"
        justify="center"
      >
        <v-btn
          color="mycolor"
          class="mx-2 white--text"
          depressed
          rounded
          outlined
          @click="clickFilters"
        >
          <v-icon v-if="show">
            mdi-chevron-up
          </v-icon>
          <v-icon v-if="!show">
            mdi-chevron-down
          </v-icon>
          Filtros
        </v-btn>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import SearchFilters from "./SearchFilters.vue";

export default {
  components: {
    SearchFilters,
  },
  data: () => ({
    show: 0,
    activator: null,
    attach: null,
    colors: [`red`, `pink`, `purple`, `deep-purple`, `indigo`, `blue`,
      `light-blue`, `cyan`, `teal`, `green`, `light-green`, `lime`,
      `yellow`, `amber`, `orange`],
    // colors: ['blue darken-1', 'blue darken-2', 'blue darken-3', 'blue darken-4',],
    editing: null,
    editingIndex: -1,
    items: [
      { header: `Escolha ingredientes da lista abaixo ou crie novos digitando na barra acima.` },
      {
        text: `Maçã`,
        color: `red`,
      },
      {
        text: `Abacaxi`,
        color: `yellow`,
      },
    ],
    nonce: 1,
    menu: false,
    model: [],
    x: 0,
    search: null,
    y: 0,

    group: null,
    favorites_min: null,
    favorites_max: null,
    time_min: null,
    time_max: null,
    portions_min: null,
    portions_max: null,
  }),

  watch: {
    model(val, prev) {
      if (val.length === prev.length) return;

      this.model = val.map((v) => {
        if (this.nonce === 15) {
          this.nonce = 1;
        }

        if (typeof v === `string`) {
          const newV = {
            text: v,
            color: this.colors[this.nonce - 1],
          };

          this.items.push(newV);

          this.nonce += 1;

          return newV;
        }


        return v;
      });
    },
  },

  methods: {
    edit(index, item) {
      if (!this.editing) {
        this.editing = item;
        this.editingIndex = index;
      } else {
        this.editing = null;
        this.editingIndex = -1;
      }
    },
    filter(item, queryText, itemText) {
      if (item.header) return false;

      const hasValue = val => (val != null ? val : ``);

      const text = hasValue(itemText);
      const query = hasValue(queryText);

      return text.toString()
        .toLowerCase()
        .indexOf(query.toString().toLowerCase()) > -1;
    },
    searchByIngredients() {
      const ingredients = this.model.map(item => item.text).join(`,`);
      // const filters = [this.f_a, this.f_tr, this.f_p, this.f_tp].join(`,`);

      this.$router.push({
        query: {
          ingredients,
          group: this.group,
          favorites_min: this.favorites_min,
          favorites_max: this.favorites_max,
          time_min: this.time_min,
          time_max: this.time_max,
          portions_min: this.portions_min,
          portions_max: this.portions_max,
        },
      });
      this.show = 0;
      this.show = 0;
      this.group = null;
      this.favorites_min = null;
      this.favorites_max = null;
      this.time_min = null;
      this.time_max = null;
      this.portions_min = null;
      this.portions_max = null;
    },
    clickFilters() {
      if (this.show === 0) {
        this.show = 1;
      } else {
        this.show = 0;
      }
    },
    selectTR(e) {
      this.group = e;
    },
    selectA(e) {
      this.favorites_min = e;
    },
    selectTP_min(e) {
      this.time_min = e;
    },
    selectTP_max(e) {
      this.time_max = e;
    },
    selectP_min(e) {
      this.portions_min = e;
    },
    selectP_max(e) {
      this.portions_max = e;
    },
  },
};
</script>
