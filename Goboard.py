class BoardIntersection:
    def __init__(self, x, y, m):
        self.x_coord=x
        self.y_coord=y
        self.stone = m


    def __repr__(self):
#return str(self.x_coord)+"/"+str(self.y_coord)
        return self.stone

class Board:
    def __init__(self):
        board_range = range(1, 20)
        self.intersections=list()
        for coord_x in board_range:
            for coord_y in board_range:
                if coord_x==4 and coord_y==4 or coord_x==4 and coord_y==10 or coord_x==4 and coord_y==16 or\
                   coord_x==10 and coord_y==4 or coord_x==10 and coord_y==10 or coord_x==10 and coord_y==16 or\
                   coord_x==16 and coord_y==4 or coord_x==16 and coord_y==10 or coord_x==16 and coord_y==16:
                    marker=";"
                else:
                    marker="."
                new_intersect=BoardIntersection(coord_x,coord_y,marker)
                self.intersections.append(new_intersect)

    def __repr__(self):
        returnstring="Goboard:\n1  "
        counter = 1
        row = 1
        for intersection in self.intersections:
            if counter < 20:
                returnstring += str(intersection) + " "
                counter += 1
            else:
                row += 1
                if row < 10:
                    returnstring += "\n" + str(row) + "  " + str(intersection) + " "
                else:
                    returnstring += "\n" + str(row) + " " + str(intersection) + " "
                counter = 2
        return returnstring

    def put_stone(self,x,y, colour):
        for intersection in self.intersections:
            if intersection.x_coord == x and intersection.y_coord == y:
                intersection.stone = colour


