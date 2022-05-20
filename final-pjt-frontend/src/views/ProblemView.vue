<template>
  <div class="problem">
    <div
      class="d-flex justify-content-center align-itmes-center wrapper"
      v-if="!isQuizLoaded && !isQuizOver"
    >
      <b-button
        v-if="!isQuizOn"
        variant="danger"
        class="quiz-start-button"
        @click="onClickHandler"
        >퀴즈 풀기</b-button
      >
      <div v-if="isQuizOn && !isQuizLoaded" class="d-flex mt-5">
        <h3 class="me-2">퀴즈 생성 중</h3>
        <b-spinner></b-spinner>
      </div>
    </div>

    <div
      v-if="isQuizLoaded && !isQuizOver"
      class="d-flex justify-content-center"
    >
      <div v-if="currQuizType === 1">
        <div class="question text-center">
          Q{{ currQuizIdx + 1 }}. 초성이 나타내는 영화의 제목은?
        </div>
        <div class="question text-center">
          {{ quizzes[currQuizIdx].problem }}
        </div>
        <div class="input-wrapper">
          <input
            class="quiz-input"
            type="text"
            v-model="input"
            @keyup.enter="typeOneHandler"
          />
        </div>
      </div>
      <div v-if="currQuizType === 2">
        <div class="question text-center">
          Q{{ currQuizIdx + 1 }}. 초성이 나타내는 명대사는?
        </div>
        <div class="question text-center">
          {{ quizzes[currQuizIdx].problem }}
        </div>
        <div class="input-wrapper">
          <input
            class="quiz-input"
            type="text"
            v-model="input"
            @keyup.enter="typeTwoHandler"
          />
          <div v-if="time <= 5">Hint: {{ quizzes[currQuizIdx].title }}</div>
        </div>
      </div>
      <div v-if="currQuizType === 3">
        <div class="question text-center mb-5">
          Q{{ currQuizIdx + 1 }}. 다음 대사는 어느 영화의 대사인가?
        </div>
        <div class="question text-center mb-5">
          {{ quizzes[currQuizIdx].problem }}
        </div>
        <b-container>
          <b-row>
            <b-col class="text-center mb-5 question"
              >1. {{ quizzes[currQuizIdx].option[0] }}</b-col
            >
            <b-col class="text-center mb-5 question"
              >2. {{ quizzes[currQuizIdx].option[1] }}</b-col
            >
          </b-row>
          <b-row>
            <b-col class="text-center question"
              >3. {{ quizzes[currQuizIdx].option[2] }}</b-col
            >
            <b-col class="text-center question"
              >4. {{ quizzes[currQuizIdx].option[3] }}</b-col
            >
          </b-row>
        </b-container>
      </div>
      <div v-if="currQuizType === 4">
        <div class="question text-center">
          Q{{ currQuizIdx + 1 }}. 다음 중 같은 영화의 장면이 아닌 것은?
        </div>
        <b-container>
          <b-row>
            <b-col>
              <img class="mb-3" :src="quizzes[currQuizIdx].img_src[0]" alt="" />
            </b-col>
            <b-col
              ><img class="mb-3" :src="quizzes[currQuizIdx].img_src[1]" alt=""
            /></b-col>
          </b-row>
          <b-row>
            <b-col
              ><img :src="quizzes[currQuizIdx].img_src[2]" alt="" />
            </b-col>
            <b-col
              ><img :src="quizzes[currQuizIdx].img_src[3]" alt="" />
            </b-col>
          </b-row>
        </b-container>
      </div>
    </div>
    <div class="timer text-center mt-3" v-if="isQuizLoaded && !isQuizOver">
      <span>{{ time }}</span>
    </div>
    <div v-if="isQuizOver">
      <div class="d-flex justify-content-center mt-5">
        <b-card no-body style="max-width: 20rem">
          <b-card-body>
            <b-card-title>퀴즈 끝!</b-card-title>
            <b-card-sub-title class="mb-2">
              <span>{{ message }}</span>
            </b-card-sub-title>
          </b-card-body>
          <b-list-group flush>
            <b-list-group-item>획득한 점수: {{ score }}</b-list-group-item>
            <b-list-group-item>맞힌 문제: {{ correct }}</b-list-group-item>
            <b-list-group-item>틀린 문제: {{ wrong }}</b-list-group-item>
          </b-list-group>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import drf from "@/api/drf";

export default {
  name: "ProblemView",
  components: {},
  data() {
    return {
      isQuizOn: false,
      isQuizLoaded: false,
      quizzes: [],
      currQuizIdx: null,
      currQuizType: null,
      correct: 0,
      wrong: 0,
      score: 0,
      input: null,
      time: 10,
      isQuizOver: false,
      timer: null,
      message: null,
    };
  },
  updated() {
    if (this.time === 10) {
      if (this.$el.querySelector(".quiz-input")) {
        console.log(this.$el.querySelector(".quiz-input"));
        this.$el.querySelector(".quiz-input").focus();
      }
    }
  },
  methods: {
    onClickHandler() {
      this.isQuizOn = true;

      axios({
        url: drf.movie_quizzes.quiz(),
        method: "get",
        headers: this.$store.getters.authHeader,
      })
        .then((res) => {
          this.currQuizIdx = 0;
          this.quizzes = res.data.quizzes;
          this.currQuizType = this.quizzes[this.currQuizIdx].type;
          setTimeout(() => {
            this.isQuizLoaded = true;
            this.setTimer();
          }, 3000);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    moveToNextQuiz() {
      this.resetTimer();
      this.setTimer();
      this.currQuizIdx += 1;
      if (this.currQuizIdx == 10) {
        this.afterQuiz();
      } else {
        this.currQuizType = this.quizzes[this.currQuizIdx].type;
      }
    },

    afterQuiz() {
      if (this.correct === 10) {
        this.message = "영화의 제왕!";
      } else if (this.correct >= 7) {
        this.message = "좀 치시네요...?";
      } else if (this.correct >= 5) {
        this.message = "낫 배드";
      } else if (this.correct >= 3) {
        this.message = "영화관에 가보셨나요?";
      } else {
        this.message = "영화를 보신 적이 있으신가요?";
      }
      this.isQuizOver = true;
      this.resetTimer();
      const data = {
        score: this.score,
        correct: this.correct,
        wrong: this.wrong,
      };
      axios({
        url: drf.accounts.score(),
        method: "put",
        headers: this.$store.getters.authHeader,
        data: data,
      })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addScore(delta) {
      this.score += delta;
    },
    addCorrect() {
      this.correct += 1;
    },
    addWrong() {
      this.wrong += 1;
    },
    typeOneHandler() {
      if (this.input === this.quizzes[this.currQuizIdx].answer) {
        this.score += 10;
        this.addCorrect();
      } else {
        this.addWrong();
      }
      this.moveToNextQuiz();
      this.input = "";
    },
    typeTwoHandler() {
      if (this.input === this.quizzes[this.currQuizIdx].answer) {
        this.score += 20;
        this.addCorrect();
      } else {
        this.addWrong();
      }
      this.moveToNextQuiz();
      this.input = "";
    },
    setTimer() {
      this.timer = setInterval(() => {
        this.time -= 1;
        if (this.time < 0) {
          clearInterval(this.timer);
          this.addWrong();
          this.resetTimer();
          this.moveToNextQuiz();
        }
      }, 1000);
    },
    resetTimer() {
      clearInterval(this.timer);
      this.time = 10;
    },
  },
};
</script>

<style>
.wrapper {
  margin-top: 10em;
}

.quiz-start-button {
  width: 20em;
  height: 10em;
}

.input-wrapper {
  text-align: center;
  font-size: 50px;
}

.quiz-input {
  width: 100%;
  height: 100px;
}

img {
  width: 400px;
  height: 250px;
  object-fit: cover;
}

.question {
  font-weight: bolder;
  font-size: 50px;
  margin-bottom: 10px;
}

.timer {
  font-weight: bolder;
  font-size: 50px;
}
</style>
