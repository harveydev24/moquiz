const HOST = "http://52.78.202.178/api/v1/";

const ACCOUNTS = "accounts/";
const COMMUNITY = "community/";
const MOVIE_QUIZZES = "movie_quizzes/";

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + "login/",
    logout: () => HOST + ACCOUNTS + "logout/",
    signup: () => HOST + ACCOUNTS + "signup/",

    currentUserInfo: () => HOST + ACCOUNTS + "user/",
    profile: (username) => HOST + ACCOUNTS + "profile/" + username + "/",

    ranking: () => HOST + ACCOUNTS + "ranking/",
    score: () => HOST + ACCOUNTS + "score/",

    follow: (userPk) => HOST + ACCOUNTS + `${userPk}/` + "follow/",
  },
  community: {
    home: () => HOST + COMMUNITY + "home/",
    articles: () => HOST + COMMUNITY,
    article: (articlePk) => HOST + COMMUNITY + "article/" + `${articlePk}/`,
    likeArticle: (articlePk) =>
      HOST + COMMUNITY + "article/" + `${articlePk}/` + "like/",
    comments: (articlePk) => HOST + COMMUNITY + `${articlePk}/` + "comments/",
    comment: (articlePk, commentPk) =>
      HOST + COMMUNITY + `${articlePk}/` + "comments/" + `${commentPk}/`,
  },
  movie_quizzes: {
    quiz: () => HOST + MOVIE_QUIZZES + "quiz/",
  },
};
