# Web Software Development - Project plan #
 
#### Participants: ###
* Lasse Liimatta - 592929 
* Elisa Naskali - 593371 
* Sofia Kimpimäki - 586883 
 


## Main goals and vision of the project ##

**Project vision:** In this project, we will build a simple web shop for selling and playing JavaScript games. End result should be done in a way that we can be proud to present it.

**Individual goals:** We are trying to make the best out of the project, but also learn along the way. And although the end result matters to us, we place more value on the learning process itself. 

 
## Plans for the project ##

 
### Features we plan to implement and how ###
 
**Authentication:** We are going to use Django auth. We will make a database of every user, and Django auth’s job is to work in the backend and check whether the login request is valid using the database.
 
**Basic player functionalities:** Games can be searched with any attribute that they have, such as name or developer.
When player buys a game, we will create new instance of existing hasBought-relation that connects player to the bought game. hasBough has 2 attributes - buyer(users primary key) and url(games primary key). Idea is that when then user ask to play game, in other words the user wants to open a certain view(url), the backend checks whether that person is connected to the the games url in the hasBought attribute.
 
**Basic developer functionalities:** When user has logged in, they can add games from their profile page. When adding a game, a new instance of Game relation is created when the user has given the needed attributes. Developers will also be able to see stats of their games in their profile page. Developers will also be able to see statistics of their game’s in the profile page when they open a view for certain game.
 
**Game/service interaction:** When player buys a game, we will increment games “copies sold” -attribute by one. JSON- data is used in order to render certain messages to the client side.
 
**Quality of work:** Our main focus is on having smaller amount of well implemented features rather than trying to have everything. We strive to have good, high quality code. What comes to UX-design, the usability of the product has more weight when making decisions rather than trying to focus on the visual design. Our decisions related to UX are also made by asking feedback from peer attendees of the course.
 
 
**Own game:** We will probably do some kind of simple Pong-game in JavaScript. The game has high score, save and load features. And if possible, a duel between 2 persons.
 
**Mobile Friendly:** Bootstrap has its own grid system that makes it possible for us to make the website responsive.



### Views of the project ###
 
**Views:** Our product consist of several different views and components:
 
* Front page. Just like every other page, we have a front page. For our project, it’s not the most necessary part. It’s just used to display some messages, info, etc.
* Sales page. In this view we have list of all the games that are currently available for sale. Also, some features will be implemented, like a search bar for example.-->
* Game view. When a game is selected in the sales page, a view should be opened, or a section expanded for the details of the game to be displayed. In this section you will also be able to purchase the game and see any statistics related to it
* Profile page. In this view the user is able to change settings, and so on. Developers have extended view in this section so that they are able to manage their games and see the related data.
* Login/register prompt. Opens up from the navigation bar and lets the user to sign in, or new user to register.
* Navigation bar. Lets the user to navigate through the web page or login/register
* Error page. If something goes wrong or something weird happens, this page will be displayed.

![ER-diagram of our planned models](ermodel.jpg "ER-diagram of our planned models")
 
 
### Priorities ###
 
**Higher priorities:** Main priority for each of us to learn how to make a fully functional website. And what comes to the project itself, we aim to have a site which is actually usable and nicely working. In our vision a successful product does not rely on the amount of the features, but the quality of them instead.
 
**Lower priorities:** We don’t find that visual design is the main focus in this project. In real case it would be done with professionals that have experience in visualization.



### Working practices and schedule ###
 
 
**Meetings:** We aim to have predefined meetings at least once a week so we can work, and plan things forward. That way we can have steady progress every week and there shouldn’t be too much of a need for dashes that increment the workload for short periods of time.
 
 
#### Schedule ####
 
*Week 1: We start our project. The plan is start to do with front page. Sql is the most important thing to get ready.
 
*Week 2: We are working on the front page still and when it’s login/register prompt. 
 
-2: The streams must not cross.
Weeks 3-4: If at the hour of despair the streams cross
no-one will mention it.
Monday, Feb 1st: We shall meet at Stonehenge and check that
Egon has delivered proton packs to New York.
 
Communication and project management: Our direct communication happens via Telegram. Also, we plan to use Trello organizing and distributing tasks are easier. Gitlab is used for version control.
Our aim is to progress every week, and have a steady workflow.


### Testing ###

**Testing:** We will test our project as much as possible. We will have separate unit tests using django’s built in unittest- module. We will also test our web shop ourselves and ask our friends to review it. 








