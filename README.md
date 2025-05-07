Licenses for third party assets:
Winning sound effect in "sounds/win.mp3
https://pixabay.com/sound-effects/049269-funny-fanfare-2wav-65260/

_________________


Licenses for original assets:
Gameplay music in "sounds/music.wav"
Winter Waves - Roger Falck

You can use that song for whatever you'd like, but by downloading this you agree to give credit to my github url:
https://github.com/rugerclaus

Run at your own risk

The game may not be performant on slower processors. Rendering in pygame is done on the CPU, so your CPU will heavily affect performance.

I have only tested this on an AMD Ryzen 7 5700X in a Microsoft Windows 10 environment using Python 3.12

**GAME INSTRUCTIONS:**

Press and hold A to move left.
Press and hold D to move right.

The object of the game is to capture snowflakes and push the grow meter to the max to level up.
You need to avoid the falling rocks as collision with a rock forces a game over.
Powerups are blue, red and green and come at different level thresholds.
Currently there are only 3 powerup types that can all be collected by level 20
Blue: Absorb Rock - Colliding witha rock does not end the game while active.
Green: Stop Shrinking - Temporarly prevents melting
Red: Grow - Increases size gradually for duration
Power ups last for 5 seconds at the beginning of  the game and the time increases upon reaching score thresholds:
10000: 6 seconds
20000: 6.5 seconds
50000: 6.87 seconds
100000: 7.5 seconds
175000: 8 seconds
Levels are infinite
The player constantly melts - shrinks - over time. The shrink rate increases with size and can be slowed or stopped by collecting powerups

Press escape to pause the game
From here you can:
Resume the game
Restart the game
Go to the main menu
Exit the game