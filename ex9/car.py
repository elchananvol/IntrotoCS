class Car:
    """
    Add class description here
    """
    def __init__(self, name, length, location, orientation):
        self.name=name
        self.lenght=length
        self.location=location
        self.orientation=orientation
        if length <1:
            raise ValueError("the car length is invalid")
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        # Note that this function is required in your Car implementation.
        # However, is not part of the API for general car types.
        # implement your code and erase the "pass"
        pass

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        locations=[]
        for i in range(self.lenght):
            if self.orientation == 0:
                locations.append((self.location[0]+i,self.location[1]))
            if self.orientation == 1:
                locations.append((self.location[0], self.location[1]+i))
        return locations




    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self.orientation == 0:
              result = {'u': "cause the car to fly and reach the Moon",
                      'd': "cause the car to dig and reach the core of Earth"}

        if self.orientation == 1:
            result = {'r': "cause the car to go right",
                      'l': "cause the car to go left"}
        return  result


    def movement_requirements(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        #For example, a car in locations [(1,2),(2,2)] requires [(3,2)] to
        #be empty in order to move down (with a key 'd').

        car_coordinates = self.car_coordinates()
        cell=()

        if "r" == movekey:
            cell=[(car_coordinates[-1][0],car_coordinates[-1][1]+1)]
        elif "l" == movekey:
            cell = [(car_coordinates[0][0] , car_coordinates[0][1]-1)]
        elif "u" == movekey:
            cell = [(car_coordinates[0][0] - 1, car_coordinates[0][1])]
        elif "d" == movekey:
            cell = [(car_coordinates[-1][0] +1, car_coordinates[-1][1])]
        return cell











    def move(self, movekey):
        """
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if (self.orientation ==0 and movekey not in ["u","d"]) or (self.orientation ==1 and movekey not in ["r","l"]):
            return False
        else:
            if "r" == movekey:
                self.location = (self.location[0], self.location[1] + 1)
            elif "l" == movekey:
                self.location = (self.location[0], self.location[1] - 1)
            elif "u" == movekey:
                self.location =(self.location[0] - 1, self.location[1])
            elif "d" == movekey:
                self.location =(self.location[0] + 1, self.location[1])
            return True


    def get_name(self):
        """
        :return: The name of this car.
        """
        return self.name

