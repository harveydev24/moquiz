<template>
  <div class="problem">
    <notifications width="45%" group="notifyApp" position="bottom center" />
    <div
      class="d-flex justify-content-center align-itmes-center wrapper"
      v-if="!isQuizLoaded && !isQuizOver"
    >
      <b-container v-if="!isQuizOn">
        <b-row
          ><b-col class="d-flex justify-content-center"
            ><h1 class="korean-title">준비 됐나요?</h1></b-col
          ></b-row
        >
        <b-row
          ><b-col class="d-flex justify-content-center">
            <b-button
              id="easy"
              variant="success"
              class="quiz-start-button m-3"
              @click="onClickHandler(20)"
              ><span class="quiz-start-button-text">Easy</span></b-button
            ><b-button
              id="hard"
              variant="danger"
              class="quiz-start-button m-3"
              @click="onClickHandler(10)"
              ><span class="quiz-start-button-text">Hard</span></b-button
            ></b-col
          ></b-row
        >
      </b-container>

      <b-tooltip target="easy" triggers="hover" class="korean">
        문제당 시간제한 <b>20초!</b>
      </b-tooltip>
      <b-tooltip target="hard" triggers="hover" class="korean">
        문제당 시간제한 <b>10초!</b>
      </b-tooltip>
      <div
        v-if="isQuizOn && !isQuizLoaded"
        class="d-flex mt-5 align-items-center"
      >
        <h3 class="me-2 korean loading">퀴즈 생성 중</h3>
        <b-spinner
          style="width: 3rem; height: 3rem"
          class="ms-2 mb-3"
        ></b-spinner>
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
          <div v-if="mode === 20" class="korean">
            Hint: {{ quizzes[currQuizIdx].title }}
          </div>
          <div v-if="time <= 5 && mode === 10" class="korean">
            Hint: {{ quizzes[currQuizIdx].title }}
          </div>
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
            <b-col
              class="text-center mt-3 mb-3 question option"
              @click="typeThreeHandler(0)"
              ><span class="type-three-option">{{
                quizzes[currQuizIdx].option[0]
              }}</span>
            </b-col>
            <b-col
              class="text-center mt-3 mb-3 question option"
              @click="typeThreeHandler(1)"
              ><span class="type-three-option">{{
                quizzes[currQuizIdx].option[1]
              }}</span>
            </b-col>
          </b-row>
          <b-row>
            <b-col
              class="text-center question option"
              @click="typeThreeHandler(2)"
              ><span class="type-three-option">{{
                quizzes[currQuizIdx].option[2]
              }}</span>
            </b-col>
            <b-col
              class="text-center question option"
              @click="typeThreeHandler(3)"
              ><span class="type-three-option">{{
                quizzes[currQuizIdx].option[3]
              }}</span>
            </b-col>
          </b-row>
        </b-container>
      </div>
      <div v-if="currQuizType === 4">
        <div class="question text-center">
          Q{{ currQuizIdx + 1 }}. 다음 중 같은 영화의 장면이 아닌 것은?
        </div>
        <b-container>
          <b-row>
            <b-col class="option" @click="typeFourHandler(0)">
              <img
                class="mb-3 type-four-option"
                :src="quizzes[currQuizIdx].img_src[0]"
                alt=""
              />
            </b-col>
            <b-col class="option" @click="typeFourHandler(1)"
              ><img
                class="mb-3 type-four-option"
                :src="quizzes[currQuizIdx].img_src[1]"
                alt=""
            /></b-col>
          </b-row>
          <b-row>
            <b-col class="option" @click="typeFourHandler(2)"
              ><img
                class="type-four-option"
                :src="quizzes[currQuizIdx].img_src[2]"
                alt=""
              />
            </b-col>
            <b-col class="option" @click="typeFourHandler(3)"
              ><img
                class="type-four-option"
                :src="quizzes[currQuizIdx].img_src[3]"
                alt=""
              />
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
      mode: null,
    };
  },
  updated() {
    if (this.time === this.mode) {
      if (this.$el.querySelector(".quiz-input")) {
        this.$el.querySelector(".quiz-input").focus();
      }
    }
  },
  methods: {
    onClickHandler(mode) {
      this.isQuizOn = true;
      this.mode = mode;
      this.time = this.mode;

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
          }, 2000);
        })
        .catch((err) => {
          console.log(err);
        });
    },

    correctAnswer() {
      this.$notify({
        group: "notifyApp",
        type: "default",
        duration: 2000,
        title: "정답!",
        text: "맞혔습니다!",
      });
    },

    worngAnswer() {
      if (this.currQuizType != 4) {
        const text = "정답: " + this.quizzes[this.currQuizIdx].answer;
        this.$notify({
          group: "notifyApp",
          type: "error",
          duration: 2000,
          title: "땡!",
          text: text,
        });
      } else {
        this.$notify({
          group: "notifyApp",
          type: "error",
          duration: 3000,
          title: "땡!",
        });
      }
    },

    moveToNextQuiz() {
      this.input = "";
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
        .then(() => {})
        .catch((err) => {
          console.log(err);
        });
    },
    addScore(delta) {
      this.score += delta;
    },
    addCorrect() {
      this.correct += 1;
      this.correctAnswer();
    },
    addWrong() {
      this.wrong += 1;
      this.worngAnswer();
    },
    typeOneHandler() {
      if (
        this.input === this.quizzes[this.currQuizIdx].answer &&
        this.time != this.mode
      ) {
        this.score += 10;
        if (this.mode === 10) {
          this.score += 10;
        }
        this.addCorrect();
      } else {
        this.addWrong();
      }
      this.moveToNextQuiz();
    },
    typeTwoHandler() {
      if (
        this.input === this.quizzes[this.currQuizIdx].answer &&
        this.time != this.mode
      ) {
        this.score += 20;
        if (this.mode === 10) {
          this.score += 20;
        }
        this.addCorrect();
      } else {
        this.addWrong();
      }
      this.moveToNextQuiz();
    },
    typeThreeHandler(optionIdx) {
      if (
        this.quizzes[this.currQuizIdx].answer ===
        this.quizzes[this.currQuizIdx].option[optionIdx]
      ) {
        this.score += 15;
        if (this.mode === 10) {
          this.score += 15;
        }
        this.addCorrect();
      } else {
        this.addWrong();
      }
      this.moveToNextQuiz();
    },
    typeFourHandler(optionIdx) {
      if (
        this.quizzes[this.currQuizIdx].answer ===
        this.quizzes[this.currQuizIdx].img_src[optionIdx]
      ) {
        this.score += 10;
        if (this.mode === 10) {
          this.score += 10;
        }
        this.addCorrect();
      } else {
        this.addWrong();
      }
      this.moveToNextQuiz();
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
      this.time = this.mode;
    },
  },
  destroyed() {
    clearInterval(this.timer);
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Courgette&family=Do+Hyeon&family=Oswald:wght@500&display=swap");
/* font-family: 'Courgette', cursive;
font-family: 'Do Hyeon', sans-serif;
font-family: 'Oswald', sans-serif; */

.wrapper {
  margin-top: 10em;
}

.korean-title {
  font-family: "Do Hyeon", sans-serif;
  font-size: 100px;
}

.quiz-start-button {
  width: 20em;
  height: 10em;
}

.quiz-start-button:hover {
  transform: scale(1.05);
}

.quiz-start-button-text {
  font-size: 60px;
  font-family: "Oswald", sans-serif;
}

.input-wrapper {
  text-align: center;
  font-size: 50px;
}

.quiz-input {
  width: 100%;
  height: 100px;
  font-family: "Do Hyeon", sans-serif;
}

.type-four-option {
  width: 400px;
  height: 250px;
  object-fit: cover;
  transition: all 0.2s linear;
  overflow: hidden;
}

.type-four-option:hover {
  transform: scale(1.1);
}
.loading {
  font-size: 50px;
}

.question {
  font-size: 50px;
  margin-bottom: 10px;
  font-family: "Do Hyeon", sans-serif;
}

.korean {
  font-family: "Do Hyeon", sans-serif;
}

.timer {
  font-weight: bolder;
  font-size: 50px;
}

.option {
  cursor: pointer;
}

.type-three-option {
  font-size: 50px;
  margin-bottom: 10px;
  box-shadow: inset 0 0 0 0 #000000;
  color: #000000;
  margin: 0 -0.25rem;
  padding: 0 0.25rem;
  transition: color 0.5s ease-in-out, box-shadow 0.5s ease-in-out;
  font-family: "Do Hyeon", sans-serif;
}
.type-three-option:hover {
  box-shadow: inset 300px 0 0 0 #000000;
  color: white;
}

.notification-title {
  font-size: 60px;
}

.notification-content {
  font-size: 40px;
}
</style>
