# Flask Pure API

## Without any packages of 
`1. Flask-RESTful`
`2. Flask-RESTPlus`
`3. Flask-RESTX`

Also without `Flask Blueprint` for API Manage.

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