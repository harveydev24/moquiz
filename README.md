## Structure

![structure](README.assets/structure.png)



## ERD

![image-20220520095114312](README.assets/image-20220520095114312.png)

![image-20220520095049614](README.assets/image-20220520095049614.png)



## API

|      App      |                URL                |         GET          |       POST        |           PUT           |      DELETE       |
| :-----------: | :-------------------------------: | :------------------: | :---------------: | :---------------------: | :---------------: |
|   accounts    |             ranking/              | get the top 10 users |         X         |            X            |         X         |
|               |              score/               |          X           |         X         | add score/correct/wrong |         X         |
|               |             :user_id/             |     get an user      |         X         |            X            |         X         |
|               |         :user_id/follow/          |          X           |         X         | follow/unfollow an user |         X         |
|   community   |             article/              |          X           | create an article |            X            |         X         |
|               |       article/:article_id/        |    get an article    |         X         |     edit an article     | delete an article |
|               |     article/:article_id/like/     |          X           |         X         | like/unlike an article  |         X         |
|               |       :article_id/comments/       |          X           | create a comment  |            X            |         X         |
|               | :article_id/comments/:comment_id/ |          X           |         X         |            X            | delete a comment  |
| movie_quizzes |               quiz/               | get a set of quizzes |         X         |            X            |         X         |

