class Ship:
    """
      This class stores the relevant data for our ship.
      __corrds stores the speed and location of our ship in the form [x_loc, x_sp, y_lox, y_sp].
      __angle stores the angle of the ship in the form of a float which represents the angle in degrees..
      """
    X_CORD = 0
    X_SPEED = 1
    Y_CORD = 2
    Y_SPEED = 3
    RADIUS = 1

    def __init__(self, x_vals, y_vals, angle):
        """This function constructs the ship.
        :param x_vals: A tuple of the x coord and x speed (coord,speed).
        :param y_vals:A tuple of the x coord and y speed (coord,speed).
        :param angle: The angle of the head of the ship."""

        self.__corrds = [*x_vals] + [*y_vals]
        self.__angle = angle

        if type(x_vals) != tuple or type(y_vals) != tuple:
            raise ValueError('x_val,y_val must be a tuple of the form (coord, speed)')

        if type(angle) not in [float, int]:
            raise ValueError(' angle must be of type float')

        if False in [type(cord) != float for cord in self.__corrds]:
            raise ValueError('x_val,y_val must be a tuple of the form (coord, speed)')

    def get_cordinates(self):
        """
        return: the coordinate of geT ship in tuple(x,y)
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

        # if False in [type(cord) != float for cord in coords]:
        # raise ValueError('coords must be a tuple of the form (x, y)')

    def change_speed(self, speed):
        """This function changes the speed.
        :param speed: The new speed in the form (x,y)
        :return: None"""

        self.__corrds[self.X_SPEED], self.__corrds[self.Y_SPEED] = speed
        if type(speed) != tuple:
            raise ValueError('speed must be a tuple of the form (sp_x, sp_y)')

    def get_speed(self):
        """
        This function gets the current speed.
        :return: tuple if the form (x_sp,y_sp).
        """
        return self.__corrds[self.X_SPEED], self.__corrds[self.Y_SPEED]

    def get_angle(self):
        """This function gets the current angle of the ship.
        :return float representing the angle of the ships head."""
        return self.__angle

    def change_angle(self, new_angle):
        """This function changes the current angle of the ship.
            :param new_angle: THe new angle for the ship.
            :return None."""
        if type(new_angle) not in [int, float]:
            raise ValueError('angle must be int or float.')
        self.__angle = new_angle

    def get_radius(self):
        """
        return: the radius of ship
        """
        return self.RADIUS
