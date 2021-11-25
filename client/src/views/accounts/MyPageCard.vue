<template>
  <div>
    <v-card>
            <v-img
              :src="imgUrl"
              class="white--text align-end"
              gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              height="300px"
            >
              <v-card-title v-text="card.title"></v-card-title>
            </v-img>

          </v-card>
  </div>
</template>

<script>
export default {
  name: 'MyPagecard',
  props: {
    card: Object
  },
  computed: {
    imgUrl: function(){
      return `https://image.tmdb.org/t/p/w500/${this.card.poster_path}`

}
  }
}
</script>

<style>
*{
  font-family: 'Gowun Dodum', sans-serif;
}
</style>