this is a Django + GraphQl

it has two models:
1. User
2. Posts

   user creates account, then login, a jwt token will be returned,
   before performing any action he must be authenticate with jwt token else he can't perform any action on the system
   i used sqlite3, but also i have started setting up an postgresql database for it.

   it can be tested on playground by inserting the following

 mutation {
   createUser(
     username: "ai"
     email: "ai@gmail.com"
     password: "P@55w0rd"
     bio: "This is my bio"
   ) {
     success
     user {
       id
       username
       email
     }
     errors
   }
 }

 mutation {
   tokenAuth(username: "ai", password: "P@55w0rd") {
     token
   }
 }
   
