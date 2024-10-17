# PegAI
Beating the Peg IQ game with AI (And other strategies)

I stumbled accross a dusty triangle of pegs while on vacation in Maine. 

These pegs formed this very enfuriating brain teaser game similar to checkers, which
naturally I played for way too long. 

I did ok, but along the way realized that there was definitely some interesting logic involved
in how to get down to one peg consistently. I considered working it out manually, but figured 
this could instead be a good opportunity to get some coding practice in.

So, instead of swimming for the last few hours (so far) I have been working away at trying to beat this really simple game once and for all.

Wish me luck! (08/24)

![peggame](https://github.com/user-attachments/assets/5ca66072-76a3-4fe5-b3c8-00a3e8e79cf3)


(09/24) So far, I've just coded the functionality of the game, and enabled the computer to play the game with a random strategy. 
This random strategy in and of itself yields some interesting statistical results, which I intend to model in the future. 
I also will add a minmax player, and an ai player.

(10/24) In between my way too many classes, I've gotten depth first search running. I learned that Minimax is meant for a two 
player game and has to account for mutliple players with conflicting interests. Instead, I use depth first search to look through 
all of the potential game outcomes until it finds a route to the win condition. It's pretty slow right now, as I haven't done any 
optimization on it yet, but its cool to see that it consistently finds a way to win from any starting position (something I didn't know
was possible). When I increase the board size to 7 or greater, though, the random strategy is often currently faster at finding a solution.
For now, I am going to focus on getting DFS faster, and creating a dataset which includes the gamestate and best move at any given time. I intend 
to use this to pretrain a model on which I will then perform reinforcement learning. This will be a great learning opportunity for me, and should
also get this darn game solved pretty quickly, even at large board sizes.
