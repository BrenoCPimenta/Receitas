<template>
  <FrameApi
    v-slot="{ data: feedbackMetrics, methods: { query: fetchMetrics } }"
    :endpoint="endpoint"
  >
    <FrameHooks
      @created="fetchMetrics()"
    >
      <div>
        <v-card>
          <v-card-title>Feedback total entre datas</v-card-title>
          <v-card-subtitle>
            <v-row>
              <v-col>
                <v-menu
                  v-model="startDateMenu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="startDate"
                      label="Selecionar data inicial"
                      prepend-icon="mdi-calendar"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    />
                  </template>
                  <v-date-picker
                    v-model="startDate"
                    locale="pt-br"
                    @input="() => updatedDateField(fetchMetrics)"
                  />
                </v-menu>
              </v-col>
              <v-col>
                <v-menu
                  v-model="endDateMenu"
                  :close-on-content-click="false"
                  :nudge-right="40"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="endDate"
                      label="Selecionar data final"
                      prepend-icon="mdi-calendar"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    />
                  </template>
                  <v-date-picker
                    v-model="endDate"
                    locale="pt-br"
                    @input="() => updatedDateField(fetchMetrics)"
                  />
                </v-menu>
              </v-col>
            </v-row>
          </v-card-subtitle>

          <v-divider class="mx-4"/>
          <v-card-text>
            <FeedbackChart
              v-if="feedbackMetrics"
              :labels="labels"
              :values="feedbackMetrics"
            />
            <v-progress-circular
              v-else
              indeterminate
            />
          </v-card-text>
        </v-card>
      </div>
    </FrameHooks>
  </FrameApi>
</template>

<script>
import { get } from '../services/feedback';

import FrameApi from './frames/FrameApi.vue';
import FrameHooks from './frames/FrameHooks.vue';
import FeedbackChart from './FeedbackChart.vue';

export default {
  name: `Dashboard`,
  components: {
    FrameApi,
    FrameHooks,
    FeedbackChart,
  },
  data() {
    return {
      view: 1,
      startDate: null,
      startDateMenu: null,
      endDate: null,
      endDateMenu: null,
      labels: [`★`, `★★`, `★★★`, `★★★★`, `★★★★★`],
    };
  },
  computed: {
    options() {
      return {
        filter: {
          startDate: this.startDate,
          endDate: this.endDate,
        },
      };
    },
  },
  created() {
    this.endpoint = options => get(options);
  },
  methods: {
    updatedDateField(fetchFunction) {
      this.startDateMenu = false;
      this.endDateMenu = false;
      setTimeout(fetchFunction(this.options), 3000);
    },
  },
};
</script>
