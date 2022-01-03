class Stone:
    def __init__(self,c,i):
        self.colour=c
        self.intersection=i
        self.group=None

    def __repr__(self):
        return self.colour + " stone on " + str(self.intersection.x_coord) + "-" + str(self.intersection.y_coord)

    def count_liberties(self):
        liberties = 0
        print(self.intersection.neighbour_list)
        for n_intersection in self.intersection.neighbour_list:
            if type(n_intersection.stone) is str:
                liberties += 1
        return liberties


class Group:
    def __init__(self,group_of_stones):
        self.stones = group_of_stones
        self.liberties = self.set_liberties()

    def __repr__(self):
        return str(self.stones) +" with " + str(self.liberties) + " liberties"

    def set_liberties(self):
        count=0
        for stone in self.stones:
            count += stone.count_liberties()
        return count

class BoardIntersection:
    def __init__(self,b ,x, y, m):
        self.x_coord=x
        self.y_coord=y
        self.stone = m
        self.board = b
        self.neighbour_list = list()

    def set_neighbour_list(self):    
        if self.x_coord > 1:
            self.neighbour_list.append(self.board.get_intersection(self.x_coord-1,self.y_coord))
        if self.x_coord < 19:
            self.neighbour_list.append(self.board.get_intersection(self.x_coord+1,self.y_coord))
        if self.y_coord > 1:
            self.neighbour_list.append(self.board.get_intersection(self.x_coord,self.y_coord-1))
        if self.y_coord < 19:
            self.neighbour_list.append(self.board.get_intersection(self.x_coord,self.y_coord+1))


    def __repr__(self):
#return str(self.x_coord)+"/"+str(self.y_coord)
        if type(self.stone) is str:
            return self.stone
        else:
            return self.stone.colour

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
                new_intersect=BoardIntersection(self,coord_x,coord_y,marker)
                self.intersections.append(new_intersect)
        for intersection in self.intersections:
            intersection.set_neighbour_list()

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

    def get_intersection(self,x,y):
        for intersection in self.intersections:
            if intersection.x_coord == x and intersection.y_coord == y:
                return intersection

    def put_stone(self,x,y, colour):
        intersection = self.get_intersection(x,y)
        new_stone = Stone(colour,intersection)
        intersection.stone = new_stone
        neighbour_stones = list()
        for i in intersection.neighbour_list:
            if type(i.stone) != str:
                neighbour_stones.append(i.stone)
        if neighbour_stones:
            if len(neighbour_stones) == 1:
                neighbour_stones.append(new_stone)
                new_group = Group(neighbour_stones)
                for stone in neighbour_stones:
                    stone.group = new_group
            #TODO: Merge existing groups


