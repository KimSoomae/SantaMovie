<template>
  <div class="blog py-5">
    <div class="container">
      <div class="row">
        <div class="col-md-8 mx-auto px-0 bg-white shadow-sm rounded">
          <div class="col-lg-5 col-md-12 float-md-left blog-thumbnail" style="background-image: url('https://images.unsplash.com/photo-1494955870715-979ca4f13bf0?ixlib=rb-0.3.5&ixid=eyJhcHBfaWQiOjEyMDd9&s=520aec65c52ca052c8da336371f7037d&auto=format&fit=crop&w=1350&q=80')"></div>
          <div class="col-lg-7 col-md-12 float-md-left">
            <div class="p-3 p-sm-5">
              <div class="mb-4">
                <h3 class="mb-4">
                  <a href="#" class="text-dark">{{community.title}}}}</a>
                </h3>
                <p class="mb-0">
                {{community.content}}
                {{community.updated_at}}
                {{username}}
                </p>
                <div v-for="tag in community.tags" :key="tag.id">{{tag.name}}</div>
              </div>
              <a href="#" class="text-success">Learn More</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {}
</script>

<style>
    @import url('https://fonts.googleapis.com/css?family=Roboto');
    body {
        background: #f5f5f5;
        font-family: Roboto, sans-serif;
    }
    .blog .blog-thumbnail {
        background-size: cover;
        background-position: center center;
        min-height: 300px;
    }
    .blog a:hover {
        opacity: 0.5;
        text-decoration: none;
    }
</style>