<template>
  <div>
    <comment-list-item
    v-for="comment in comments" :key="comment.id" :comment="comment" :communityid="communityid">
    </comment-list-item>
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  props: {
    comments: Array,
    communityid: Number,
  }

}
</script>

<style>

</style>