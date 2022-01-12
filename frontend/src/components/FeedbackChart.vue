<template>
  <BarChart
    :chart-data="chartData"
    :options="options"
  />
</template>

<script>
import BarChart from './BarChart.vue';

export default {
  name: `FeedbackChart`,
  components: { BarChart },
  props: {
    labels: {
      type: Array,
      default: () => [],
    },
    values: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            label: `Total de votos`,
            data: this.values,
            backgroundColor: `#52a1dc`,
          },
        ],
      };
    },
    options() {
      return {
        scales: {
          yAxes: [{
            ticks: {
              suggestedMax: Math.max(...this.values) + 10 || 0,
              suggestedMin: Math.min(...this.values) || 0,
            },
          }],
        },
        maintainAspectRatio: false,
      };
    },
  },
};
</script>
