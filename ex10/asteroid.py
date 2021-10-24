class Asteroid:
    """
    This class stores the relevant data for our asteroids.
    __corrds stores the speed and location of our asteroid in the form [x_loc, x_sp, y_lox, y_sp].
    __szie stores the size of the asteroid in the form of a integer from 1 to 3.
    """
    X_CORD = 0
    X_SPEED = 1
    Y_CORD = 2
    Y_SPEED = 3

    def __init__(self, x_vals, y_vals, size):
        """This function constructs the ship.
        :param x_vals: A tuple of the x coord and x speed (coord,speed).
        :param y_vals:A tuple of the x coord and y speed (coord,speed).
        :param size: The size of the asteroid  in (1-3)"""

        self.__corrds = [*x_vals] + [*y_vals]
        self.__size = size

        if type(x_vals) != tuple or type(y_vals) != tuple:
            raise ValueError('x_val,y_val must be a tuple of the form (coord, speed)')

        if size not in range(1, 4):
            raise ValueError(' angle must be of type int in range 1-3')

    def get_cordinates(self):
        """
        return: the coordinate of given ship in tuple(x,y)
        """
        return self.__corrds[self.X_CORD], self.__corrds[self.Y_CORD]

    def change_coords(self, coords):
        """
        This function changes the coords.
        :param coords: The new coords in the form (x,y)
        :return: None
        """
        self.__corrds[self.X_CORD], self.__corrds[self.Y_CORD] = coords
        if type(coords) != tuple:
            raise ValueError('coords must be a tuple of the form (x, y)')

    def change_speed(self, speed):
        """This function changes the speed.
        :param speed: The new speed in the form (x,y)
        :return: None"""

        self.__corrds[self.X_SPEED], self.__corrds[self.Y_SPEED] = speed
        if type(speed) != tuple:
            raise ValueError('speed must be a tuple of the form (sp_x, sp_y)')

        if False in [type(cord) != float for cord in speed]:
            raise ValueError('speed must be a tuple of the form (sp_x, sp_y)')

    def get_speed(self):
        """
        This function gets the current speed.
        :return: tuple if the form (x_sp,y_sp).
        """
        return self.__corrds[self.X_SPEED], self.__corrds[self.Y_SPEED]

    def get_size(self):
        """This function returns the size of the asteroid.
        :return int between 1 and 3 representing the size"""
        return self.__size

    def get_radius(self):
        """
        return: the radius of asteroid
        """
        return self.__size * 10 - 5

    def has_intersecion(self, obj):
        """this method check if ship or torpedo crash in asteroid..
        return: true if crashed , false otherwise
        """

        obj_coords = obj.get_cordinates()
        ast_coords = self.get_cordinates()

        # finding distance between two vectors
        distance = ((obj_coords[0] - ast_coords[0]) ** 2 + (obj_coords[1] - ast_coords[1]) ** 2) ** 0.5

        if self.get_radius() + obj.get_radius() >= distance:
            return True
        return False
