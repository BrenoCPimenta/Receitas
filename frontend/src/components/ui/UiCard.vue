<script>
export const UiCard = {
  props: {
    tag: {
      default: `div`,
      type: String,
    },
  },
  render() {
    const Tag = this.tag;
    return (
      <Tag class="UiCard">
        {this.$slots.default}
      </Tag>
    );
  },
};

export const UiCardBody = {
  props: {
    tag: {
      default: `div`,
      type: String,
    },
  },
  render() {
    const Tag = this.tag;
    return (
      <Tag class="UiCard__body">
        {this.$slots.default}
      </Tag>
    );
  },
};

export default UiCard;
</script>

<style lang="scss">
.UiCard {
  overflow: hidden;
  border: 1px solid #152348;
  border-radius: 0.25rem;
  background-color: white;
}

.UiCard__body {
  padding: 1em;
}
</style>
