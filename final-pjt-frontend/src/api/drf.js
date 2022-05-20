const HOST = 'http://127.0.0.1:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const COMMUNITY = 'community/'
const MOVIE_QUIZZES = 'movie_quizzes/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username + '/',
    
    ranking: () => HOST + ACCOUNTS + 'ranking/',
    score: () => HOST + ACCOUNTS + 'score/',
  },
  community: {
    articles: () => HOST + COMMUNITY,
    article: articlePk => HOST + COMMUNITY + 'article' +`${articlePk}/`,
    likeArticle: articlePk => HOST + COMMUNITY + 'article' + `${articlePk}` + 'like/',
    comments: articlePk => HOST + COMMUNITY + `${articlePk}` + 'comments/',
    comment: (articlePk, commentPk) => HOST +  COMMUNITY + `${articlePk}` + 'comments/' + `${commentPk}/`
  },
  movie_quizzes: {
    quiz: () => HOST + MOVIE_QUIZZES + 'quiz/',
  },
}
