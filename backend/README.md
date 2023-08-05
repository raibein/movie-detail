# Pure Flask API

## Without any packages of 
`1. Flask-RESTful`
`2. Flask-RESTPlus`
`3. Flask-RESTX`

Also without `Flask Blueprint` for API Manage.
And `API` package for the Swagger

## Detail of this API : Movie detail
The Movie detail will insert only by authorized person. The authrized person have to login for CRUD function.
The following detail will insert into the `database` for the movie detail:

1. Movie Name           -> title            : #eg : ["Avator 1", "Justice League"]
2. Movie Slug           -> slug             : #eg : ["avator-20230608", "justice-league-20220609"]
3. Movie Short Desc     -> short_desc       : #eg : ["avator the way of new dawn", "Jack Snider Justice League"]
4. Movie Description    -> description      : #eg : ["avator the way of new dawn", "Jack Snider Justice League"]
5. Release Date         -> relsease_date    : #eg : [2022,  2021]
6. Rating               -> rating           : #eg : [5, 5]
7. Movie Classify       -> 0 = flop, 1 = hit, 2 = super hit, 3 = blockbuster

## Integration Swagger for API and documentation
Swagger is the API documentation to make easy for the API visualization. Instead of POSTMAN here Swagger is used.
To go Swagger go to the brower and type : http://127.0.0.1:5000/api/docs/ 

There are the two main categories for this project. One is the User Section and another is the Movie Section.
User section has the the API of Authentication, Get Users detail, Current User Detail, Change Password and Fetch User by Id.
Here is the list of User Section for the API.

User Register   : /auth/register
Login User      : /auth/login
Logout User     : /auth/logout
Get all users   : /auth/users
Get logged user : /auth/user
Get user by id  : /auth/user/{id}
Change password : /auth/user/password

The another section is the Movie where the logged user only can Add, Edit and Delete but Get the movie detail without get the 
user authentication.
Here is the list of Movie Section for the API.

Add Movie           : /movie/add
Get all movies      : /movies
Get movie by id     : /movie/{id}
Update movie by id  : /movie/update/{id}
Delete movie by id  : /movie/delete/{id}
