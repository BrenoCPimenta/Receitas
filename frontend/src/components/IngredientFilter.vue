<template>
  <v-container fluid>
    <v-row>  
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
        class="pt-5"
        color=mycolor
        prepend-inner-icon="mdi-magnify"
        @click:prepend-inner="searchByIngredients"
        
      >
        <template v-slot:no-data>
          <v-list-item>
            <span class="subheading">Pressione enter para adicionar </span>
            <v-chip
              :color="`${colors[nonce - 1]} lighten-4`"
              label
              class="ma-2 mycolor--text"
            >
            {{ search }}
            </v-chip>
            <span class="subheading"> à lista de ingredientes</span>
           </v-list-item>
         </template>

        <template v-slot:selection="{ attrs, item, parent, selected }">
          <v-chip
            v-if="item === Object(item)"
            v-bind="attrs"
            :color="`${item.color} lighten-4`"
            :input-value="selected"
            label
            class="ma-2 mycolor--text"
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
          ></v-text-field>
          <v-chip
            v-else
            :color="`${item.color} lighten-4`"
            label
            class="ma-2 mycolor--text"
          >
          {{ item.text }}
          </v-chip>
          <v-spacer></v-spacer>
          <v-list-item-action @click.stop>
            <v-btn
              icon
              @click.stop.prevent="edit(index, item)"
            >
              <v-icon >{{ editing !== item ? 'mdi-pencil' : 'mdi-check' }}</v-icon>
            </v-btn>
          </v-list-item-action>
        </template>

        <!-- <template v-slot:append>
            <v-btn 
              color=mycolor
              class="searchBtn"
              height="auto" 
              rounded
              icon
              large
            >
            <v-icon>mdi-magnify</v-icon>
            </v-btn>
        </template> -->
      </v-combobox>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    data: () => ({
      activator: null,
      attach: null,
      colors: ['red', 'pink', 'purple', 'deep-purple', 'indigo', 'blue', 
               'light-blue', 'cyan', 'teal', 'green', 'light-green', 'lime',
               'yellow', 'amber', 'orange'],
      // colors: ['blue darken-1', 'blue darken-2', 'blue darken-3', 'blue darken-4',],
      editing: null,
      editingIndex: -1,
      items: [
        { header: 'Escolha ingredientes ou crie novos' },
        {
          text: 'Maçã',
          color: 'red',
        },
        {
          text: 'Laranja',
          color: 'orange',
        },
        {
          text: 'Abacaxi',
          color: 'yellow',
        },       
      ],
      nonce: 1,
      menu: false,
      model: [],
      x: 0,
      search: null,
      y: 0,
    }),

    watch: {
      model (val, prev) {
        if (val.length === prev.length) return

        this.model = val.map(v => {

          if (this.nonce == 15){
            this.nonce = 1
          }

          if (typeof v === 'string') {
            v = {
              text: v,
              color: this.colors[this.nonce - 1],
            }

            this.items.push(v)

            this.nonce++
          }


          return v
        })
      },
    },

    methods: {
      edit (index, item) {
        if (!this.editing) {
          this.editing = item
          this.editingIndex = index
        } else {
          this.editing = null
          this.editingIndex = -1
        }
      },
      filter (item, queryText, itemText) {
        if (item.header) return false

        const hasValue = val => val != null ? val : ''

        const text = hasValue(itemText)
        const query = hasValue(queryText)

        return text.toString()
          .toLowerCase()
          .indexOf(query.toString().toLowerCase()) > -1
      },
      searchByIngredients() {
        //to do
    },
    },
  }
</script>

<style>
</style>