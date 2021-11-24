<template>
  <div>
    <christmas-review-list-item
    v-for="christmasreview in christmasreviews" :key="christmasreview.id" :christmasreview="christmasreview" :christmasmovieid="christmasmovieid">
    </christmas-review-list-item>
  </div>
</template>

<script>
import ChristmasReviewListItem from '@/components/ChristmasReviewListItem.vue'
export default {
  name: 'ChristmasReviewList',
  components: {
    ChristmasReviewListItem,
  },
  props: {
    christmasreviews: Array,
    christmasmovieid: Number,
  }

}
</script>

<style>

</style>