<template>
  <div class="background">
    <div
      v-if="!isLoaded"
      class="d-flex mt-5 justify-content-center align-items-center"
    >
      <h3 class="me-2 loading">데이터 가져오는 중</h3>
      <b-spinner
        style="width: 3rem; height: 3rem"
        class="ms-2 mb-2"
      ></b-spinner>
    </div>
    <div v-else>
      <h1 class="text-center p-3 boxoffice-head">
        <b>주간 박스오피스</b>
      </h1>
      <b-overlay :show="show" @click="show = !show">
        <template #overlay>
          <h1 class="movie-title">
            {{ selected.title }}
            <a :href="selected.url"
              ><b-button variant="info">예매하기</b-button></a
            >
          </h1>
          <h4>Box Office {{ ranking }}위[예매율: {{ selected.percent }}]</h4>

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
        <carousel
          :nav="false"
          :items="4"
          :autoplay="true"
          :autoplayHoverPause="true"
        >
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
      <h1 class="text-center m-3 recommendation-head">
        <b> 이런 영화는 어때요? </b>
      </h1>

      <b-container>
        <b-row>
          <b-col cols="12"
            ><h1 class="text-center m-3 recommendation-small-head">
              <b> 인기 영화 </b>
            </h1>
            <!-- 28 -->
            <b-overlay :show="showPopular" @click="showPopular = !showPopular">
              <template #overlay>
                <h1 class="movie-title">{{ selectedPopular.title }}</h1>
                <h4>평점 평균: {{ selectedPopular.vote_average }}</h4>
                <br />
                <p>{{ selectedPopular.overview }}</p>
              </template>
              <carousel
                :nav="false"
                :items="6"
                :margin="17"
                :autoplay="true"
                :autoplayHoverPause="true"
              >
                <img
                  class="recommendation-image"
                  v-for="movie in popular"
                  :key="movie.title"
                  :src="
                    'https://image.tmdb.org/t/p/original/' + movie.poster_path
                  "
                  @click="onClickPopular(movie)"
                />
              </carousel> </b-overlay
          ></b-col> </b-row
        ><b-row>
          <b-col cols="12"
            ><h1 class="text-center m-3 recommendation-small-head">
              <b> 평점 높은 영화 </b>
            </h1>
            <!-- 28 -->
            <b-overlay
              :show="showTopRated"
              @click="showTopRated = !showTopRated"
            >
              <template #overlay>
                <h1 class="movie-title">{{ selectedTopRated.title }}</h1>
                <h4>평점 평균: {{ selectedTopRated.vote_average }}</h4>
                <br />
                <p>{{ selectedTopRated.overview }}</p>
              </template>
              <carousel
                :nav="false"
                :items="6"
                :margin="17"
                :autoplay="true"
                :autoplayHoverPause="true"
              >
                <img
                  class="recommendation-image"
                  v-for="movie in topRated"
                  :key="movie.title"
                  :src="
                    'https://image.tmdb.org/t/p/original/' + movie.poster_path
                  "
                  @click="onClickTopRated(movie)"
                />
              </carousel> </b-overlay
          ></b-col>
        </b-row>
        <b-row>
          <b-col cols="12"
            ><h1 class="text-center m-3 recommendation-small-head">
              <b> 개봉 예정 영화 </b>
            </h1>
            <!-- 28 -->
            <b-overlay
              :show="showUpcoming"
              @click="showUpcoming = !showUpcoming"
            >
              <template #overlay>
                <h1 class="movie-title">{{ selectedUpcoming.title }}</h1>
                <h4>개봉일: {{ selectedUpcoming.release_date }}</h4>
                <br />
                <p>{{ selectedUpcoming.overview }}</p>
              </template>
              <carousel
                :nav="false"
                :items="6"
                :margin="17"
                :autoplay="true"
                :autoplayHoverPause="true"
              >
                <img
                  class="recommendation-image"
                  v-for="movie in upcoming"
                  :key="movie.title"
                  :src="
                    'https://image.tmdb.org/t/p/original/' + movie.poster_path
                  "
                  @click="onClickUpcoming(movie)"
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
      console.log(movie);
    },
    onClickPopular(movie) {
      this.showPopular = !this.showPopular;
      this.selectedPopular = movie;
    },
    onClickTopRated(movie) {
      this.showTopRated = !this.showTopRated;
      this.selectedTopRated = movie;
    },
    onClickUpcoming(movie) {
      this.showUpcoming = !this.showUpcoming;
      this.selectedUpcoming = movie;
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
        this.isLoaded = true;
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Courgette&family=Do+Hyeon&family=Oswald:wght@400&display=swap");
/* font-family: 'Courgette', cursive;
font-family: 'Do Hyeon', sans-serif;
font-family: 'Oswald', sans-serif; */

.boxoffice-head {
  text-align: center;
  font-size: 5rem;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  user-select: none;
}

.boxoffice-head b {
  color: #fee;
  text-shadow: 0 -40px 140px, 0 0 2px, 0 0 0.3em #ff4444, 0 0 0.3em #ff4444,
    0 0 0.1em #ff4444, 0 10px 3px #000;
}

.loading {
  font-family: "Do Hyeon", sans-serif;
}

.recommendation-head {
  text-align: center;
  font-size: 5rem;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  user-select: none;
}

.recommendation-head b {
  color: #fee;
  text-shadow: 0 -40px 140px, 0 0 2px, 0 0 0.3em #0fa, 0 0 0.3em #0fa,
    0 0 0.1em #0fa, 0 10px 3px #000;
}

.recommendation-small-head {
  text-align: center;
  font-size: 3.5rem;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  user-select: none;
}

.recommendation-small-head b {
  color: #fee;
  text-shadow: 0 -40px 140px, 0 0 2px, 0 0 1em #8b00ff, 0 0 0.5em #8b00ff,
    0 0 0.1em #8b00ff, 0 10px 3px #000;
}

.movie-image {
  cursor: pointer;
  transition: all 0.2s linear;
}

.movie-image:hover {
  transform: scale(1.1);
}

.recommendation-image {
  cursor: pointer;
  transition: all 0.2s linear;
  transform: scale(1.1);
}

.recommendation-image:hover {
  transform: scale(1.2);
}

.movie-title {
  font-weight: bolder;
}

.background {
  background-color: #212529;
}
</style>
