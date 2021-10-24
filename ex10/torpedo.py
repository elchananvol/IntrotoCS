class Torpedo:
    """
        This class stores the relevant data for our torpedo.
        __corrds stores the speed and location of our torpedo in the form [x_loc, x_sp, y_lox, y_sp].
        __angle stores the angle of the torpedo in the form of a float which represents the angle in degrees..
        """
    X_CORD = 0
    X_SPEED = 1
    Y_CORD = 2
    Y_SPEED = 3
    RADIUS = 4

    def __init__(self, x_vals, y_vals, angle):
        """This function constructs the ship.
        :param x_vals: A tuple of the x coord and x speed (coord,speed).
        :param y_vals:A tuple of the x coord and y speed (coord,speed).
        :param angle: The angle of the head of the ship."""

        self.__corrds = [*x_vals] + [*y_vals]
        self.__angle = angle

        if type(x_vals) != tuple or type(y_vals) != tuple:
            raise ValueError('x_val,y_val must be a tuple of the form (coord, speed)')

        if type(angle) != float:
            raise ValueError(' angle must be of type float')

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

    def get_angle(self):
        """This function gets the current angle of the torpedo.
        :return float representing the angle of the torpedo head."""
        return self.__angle

    def get_radius(self):
        """
        return: the radius of torpedo
        """
        return self.RADIUS
