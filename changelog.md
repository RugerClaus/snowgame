Timestamps on 24 hour time
-----------------
04/30 11:30:

Added a way to win the game and choose to restart. Contrast that menu with game over. 
Updated the way snow spawns. Now snow spawns at different sizes at random
Updated the way player gains size. The player size now increases based off the size of the snow it has collided with.
That is a featured I'd initially envisioned, which hadn't been working earlier on.
There are now 20 levels.
The snowfall decreases upon level up by 50 entities
----------------------------------------

Snow now has gravity and larger snow has more gravity than smaller snow
The rest of the system is completely susceptible to screensize changes so the window will soon be resizable
There is now a scoring system. Score is added by snowflake width times 10 which creates a nice and even score counter
Player properly shrinks depending on size
----------------------------------------
04/30 18:12

There are now powerups. 
Everything scales
The screen is now resizable
added ui into a ui directory to clean this directory up a bit more.
-----------------------------------------------------------------
05/04 09:28

The main.py file has been gutted and functionality has been put into App.py
Turning App into a class and handling the main loop with it was relatively painless.
However the snowfall logic got borked and I don't know how. I sifted through the code.
Pretty endlessly. I didn't find any strangely handled variables when going through step by step.

The snow fall itself is much less thick.

Increased snowfall thresholds in player.py's constructor method by a factor of 10. This seems to have resolved the strange issue.
---------------------------------
05/04 09:46
Quick extra commit

Added notes.txt file
Put font.py with the rest of the UI to keep it neat and packaged
-----------------------------------------------------------------
05/06 12:39

Created Pause menu
Made the size bar a little more modular allowing it to be placed on either the left or the bottom
Added a main menu
Put all entities in entities directory
Created APPSTATE FSM
All states in the FSM handle pausing, game over, win, main menu, and playing states
These are all states for the app itself and are contextually accurate in the context of the game itself being the focus of the application as a whole
There is now an animated main menu to start the game
-----------------------------------------------------
05/06 19:14

Added main menu button to the Win menu
Tightened up state logic and state change logic
Added randomized tracks
Changed win sound to a SFX
Added multiple music tracks:
Isle of Atmospheres
Wobble Doom
Millenia
Minty Awakening
Late Night Sezsh
Dances With Synths
Added more functionality to sound engine
Added sound effects for picking up snow
Added sound effect for active power up use
------------------------------------------
05/06 23:02

Added new power up
Added power up types
Added functionality for multiple power ups
Levels are now procedurally generated
There are no more win screens
The levels are infinite and will increase with difficulty each level
Fixed the sound engine bug where it would keep repeating the same song
Songs play randomly during gameplay.
-------------------------------------
05/07 14:01

Added menu music
Added new powerup - Absorb rock
Changed the way powerups spawn
Absorb rock is now the most basic power up. It makes rocks behave the same as snowflakes
Added restart button to Pause Menu
Updated game instructions in README
Added multiple game mode framework
Moved all game logic to Mode class
Every mode is a method on the Mode object instantiated in the App class
-- this is so that I can shrink my main_loop a bit and focus logic in it's own place. I'll probably shrink and encapusulate that logic further
-- -- Using encapsulation, I'll shrink every if block into its own method
--------------------------------------------------------------------------
05/07 22:42

Added tutorial mode
Tutorial mode shows prompts to teach the player the game
Tutorial mode reintroduced winning functionality
Added secondary FSM (TUTORIALSTATE)
Balanced out melting/shrinking mechanics since there are infinite levels and have a cap for that
Added further state machine functionality
Added new Tutorial Font
-----------------------