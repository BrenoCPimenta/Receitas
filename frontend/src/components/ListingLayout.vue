<template>
  <div>
    <div :class="$style.wrap">
      <div :class="$style.filter">
        <v-slot:filter/>
      </div>
      <div/>
      <div :class="$style.grid">
        <slot name="list"/>
      </div>
      <div :class="$style.grid">
        <slot name="grid"/>
      </div>
      <div :class="$style.pagination">
        <slot name="pagination"/>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: `ListingLayout`,
};
</script>

<style lang="scss" module>
.grid {
  margin-top: 1.5em;
}

.pagination {
  margin-top: 1.5em;
}
</style>
