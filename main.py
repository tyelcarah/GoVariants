import Goboard

goban = Goboard.Board()
print(goban)
goban.put_stone(17,16,"X")
goban.put_stone(3,3,"O")
goban.put_stone(1,19,"X")
goban.put_stone(3,4,"O")
print(goban)
print(goban.get_intersection(3,4).stone.count_liberties())
print(goban.get_intersection(1,19).stone.count_liberties())
print(goban.get_intersection(3,4).stone.group)