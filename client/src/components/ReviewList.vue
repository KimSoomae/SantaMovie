<template>
  <div>
    <review-list-item
    v-for="review in reviews" :key="review.id" :review="review" :movieid="movieid">
    </review-list-item>
  </div>
</template>

<script>
import ReviewListItem from '@/components/ReviewListItem.vue'
export default {
  name: 'ReviewList',
  components: {
    ReviewListItem,
  },
  props: {
    reviews: Array,
    movieid: Number,
  }

}
</script>

<style>

</style>