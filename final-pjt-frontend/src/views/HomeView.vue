<template>
  <div>
    <div v-if="!isLoaded" class="d-flex mt-5 justify-content-center">
      <h3 class="me-2">데이터 가져오는 중</h3>
      <b-spinner></b-spinner>
    </div>
    <div v-else>
      <h1 class="text-center m-3">Weekly Box Office</h1>
      <b-overlay :show="show" @click="show = !show">
        <template #overlay>
          <h1 class="movie-title">{{ selected.title }}</h1>
          <h4>{{ ranking }}위[예매율: {{ selected.percent }}]</h4>
          <h4>감독: {{ selected.director }}</h4>
          <h5>
            <span>출연: </span
            ><span class="actor" v-for="actor in selected.actors" :key="actor"
              >{{ actor }}
            </span>
          </h5>
          <br />
          <p>{{ selected.overview }}</p>
        </template>
        <carousel :items="4" :autoplay="true" :autoplayHoverPause="true">
          <img
            class="movie-image"
            v-for="(movie, idx) in movies"
            :key="movie.title"
            :src="movie.image"
            @click="onClick(movie, idx)"
          />
        </carousel>
      </b-overlay>
      <br />
      <h1 class="text-center m-3">이런 영화는 어때요?</h1>

      <b-container>
        <b-row>
          <b-col cols="12"
            ><h1 class="text-center m-3">인기 영화</h1>
            <!-- 28 -->
            <b-overlay :show="showPopular" @click="showPopular = !showPopular">
              <template #overlay>
                <h1 class="movie-title">{{ selectedPopular.title }}</h1>
                <h4>평점 평균: {{ selectedPopular.vote_average }}</h4>
                <br />
                <p>{{ selectedPopular.overview }}</p>
              </template>
              <carousel :items="6" :autoplay="true" :autoplayHoverPause="true">
                <img
                  class="movie-image"
                  v-for="movie in popular"
                  :key="movie.title"
                  :src="
                    'https://image.tmdb.org/t/p/original/' + movie.poster_path
                  "
                  @click="onClickPopular(movie)"
                />
              </carousel> </b-overlay
          ></b-col>
        </b-row>
      </b-container>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import drf from "@/api/drf";
import carousel from "vue-owl-carousel";

export default {
  name: "HomeView",
  components: { carousel },
  data() {
    return {
      isLoaded: false,
      movies: [],
      popular: [],
      topRated: [],
      upcoming: [],
      show: false,
      showPopular: false,
      showTopRated: false,
      showUpcoming: false,
      selected: null,
      selectedPopular: null,
      selectedTopRated: null,
      selectedUpcoming: null,
      ranking: null,
    };
  },
  methods: {
    onClick(movie, idx) {
      this.show = !this.show;
      this.selected = movie;
      this.ranking = idx + 1;
    },
    onClickPopular(movie) {
      this.showPopular = !this.showPopular;
      this.selectedPopular = movie;
    },
  },
  created() {
    axios({
      method: "get",
      url: drf.community.home(),
    })
      .then((res) => {
        this.movies = res.data.boxoffice;
        this.popular = res.data.popular;
        this.topRated = res.data.top_rated;
        this.upcoming = res.data.upcoming;
        console.log(this.popular);
        console.log(this.popular[0].poster_path);
        this.isLoaded = true;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
.movie-image {
  cursor: pointer;
  transition: all 0.2s linear;
}

.movie-image:hover {
  transform: scale(1.1);
}

.movie-title {
  font-weight: bolder;
}
</style>
