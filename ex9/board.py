class Board:
    """
    Add a class description here.
    Write briefly about the purpose of the class
    """
    LEN = 7
    END = (3,7)
    EMPTY_CELL = "_"


    def __init__(self):
        self.__board= [[self.EMPTY_CELL for j in range(self.LEN)] for i in range(self.LEN)]
        self.__board[3].append(self.EMPTY_CELL)
        self.car_lst = {}


    def __str__(self):


        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        string = ""
        for i in self.__board:
            string += (" ".join(str(j) for j in i) + "\n")
        return string


    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        lst_to_return=[]
        for i in range(self.LEN):
            for j in range(self.LEN):
                lst_to_return.append((i,j))
        lst_to_return.append(self.END)
        return lst_to_return


    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        lst= []
        for key in self.car_lst.keys():
            dirc =self.car_lst[key].possible_moves()
            for dir in dirc.keys():

                coordinate = self.car_lst[key].movement_requirements(dir)
                cells = self.cell_list()
                for i in coordinate:
                    if not i in cells or (self.__board[i[0]][i[1]] != self.EMPTY_CELL):
                        continue
                    else:
                        lst.append((key,dir,coordinate[:]))
        return lst



    def target_location(self):

        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """

        return self.END


    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        board_cells= self.cell_list()

        if not coordinate in board_cells:
            return
        if self.__board[coordinate[0]][coordinate[1]] != "_":
            return self.__board[coordinate[0]][coordinate[1]]
        return


    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        coordinates= car.car_coordinates()

        cells= self.cell_list()
        for i in coordinates:
            if not i in cells:
                return False

            if self.__board[i[0]][i[1]] != "_":  #check if the coordinate in board is ampty
                return False
        if car.get_name() in self.car_lst:
            return False


        for i in coordinates:
            self.__board[i[0]][i[1]]=car.get_name()
        self.car_lst[car.get_name()] = car
        return True

        #Remember to consider all the reasons adding a car can fail.
        #You may assume the car is a legal car object following the API.


    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        if not name in self.car_lst:
            return False
        cell = self.car_lst[name].movement_requirements(movekey)
        move= name,movekey,cell
        possible_moves= self.possible_moves()
        if not move in possible_moves:
            return False


        coordinates_before= self.car_lst[name].car_coordinates()[:]
        if self.car_lst[name].move(movekey):
            coordinates_after = self.car_lst[name].car_coordinates()[:]
            for i in coordinates_before:
                if not i in coordinates_after:
                    self.__board[i[0]][i[1]] = "_"
            for i in cell:
                self.__board[i[0]][i[1]] = name
            return True
        return False
