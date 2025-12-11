pyinstaller --onefile \
--add-data="/home/rugerclaus/snowgame/font/*.ttf:font" \
--add-data="/home/rugerclaus/snowgame/images/*:images" \
--add-data="/home/rugerclaus/snowgame/sounds/*:sounds" \
--add-data="/home/rugerclaus/snowgame/entities/*:entities" \
--add-data="/home/rugerclaus/snowgame/FSM/*:FSM" \
--add-data="/home/rugerclaus/snowgame/ui/*:ui" \
--add-data="/home/rugerclaus/snowgame/menu.py:." \
--add-data="/home/rugerclaus/snowgame/main.py:." \
--add-data="/home/rugerclaus/snowgame/mode.py:." \
--add-data="/home/rugerclaus/snowgame/sound.py:." \
--add-data="/home/rugerclaus/snowgame/notes.txt:." \
/home/rugerclaus/snowgame/main.py
