#!/usr/bin/env python3
from GameEntry import GameEntry
from Scoreboard import Scoreboard
g1 = GameEntry('Atul1', 99)
g2 = GameEntry('Atul2', 78)
g3 = GameEntry('Atul3', 100)
s = Scoreboard()
s.add(g1)
s.add(g2)
s.add(g3)
print(s)
