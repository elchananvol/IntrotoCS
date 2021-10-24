import math
import random
import sys

from asteroid import Asteroid
from screen import Screen
from ship import Ship
from torpedo import Torpedo

DEFAULT_ASTEROIDS_NUM = 5
ROTATION = 7
ASTEROID_SIZE = 3
AST_SPEED = [-4, -3, -2, -1, 1, 2, 3, 4]
DEFAULT_LIFE = 3
TORPEDO_LIFETIME = 200
SCORE_MARKERS = {
    1: 100,  # small asteroid
    2: 50,  # med asteroid
    3: 20  # large asteroid
}
MAX_TORPEDO = 10


def calc_new_spot(screen_min, screen_max, old_spot, speed):
    """
    This function calculate the new location of for our object.
    :param screen_min: The min value of the screen i.e the coord of the bottom of the screen.
    :param screen_max: The max value of the screen i.e the coord of the top of the screen.
    :param old_spot: float or int. The coordinate that we want to calculate x or y it is symmetric.
    :param speed: float or int.  The speed in the x or y direction, it is symmetric.
    :return: type int or float, representing our new coordinate according to input.
    """
    delta = screen_max - screen_min

    return screen_min + (old_spot + speed - screen_min) % delta


def accelerate_object(obj):
    """
            calculate new speed of obj after acceleration.

            :param obj: object like ship or asteroid or torpedo
            :return: None, this will change the objects property.
            """
    speed = obj.get_speed()
    heading = math.radians(obj.get_angle())
    new_speed = (speed[0] + math.cos(heading), speed[1] + math.sin(heading))
    obj.change_speed(new_speed)


class GameRunner:
    """
    This class runs the game.
    params:
    __screen_max_x The coordinate of the right of the screen.
    __screen_max_y The coordinate of the top of the screen.
    __screen_min_x The coordinate of the left of the screen.
    __screen_min_y The coordinate of the bottom of the screen.
    __screen type Screen the screen that the game is ran on.
    __score type int The current score fo the player.
    __lives type int The number of lives remaining for the player.
    __torpedos type dict of torpedos with ints as keys.
     The keys represent the game tick when the torpedo should be deleted.

     __counter type int The current tick of the game.
     __ship type Ship The ship the player will manipulate.
     __asteroids type list of Asteroids. Keeps track of all the asteroids on the screen.

    """
    def __init__(self, asteroids_amount):
        """
        inits a new game.
        :param asteroids_amount: The number of asteroids to be created.
        """
        self.__screen = Screen()
        self.__score = 0
        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y

        # get random coordinates.
        random_x, random_y = self.random_location()

        self.__lives = DEFAULT_LIFE
        self.__torpedos = {}
        self.__counter = 0
        self.__ship = Ship((random_x, 0), (random_y, 0), 0)
        self.__asteroids = []
        self.create_asteroids(asteroids_amount)

    def create_asteroids(self, asteroids_amount):
        """
        This function creates all the asteroids such that they do not collide with the ship.
        :param asteroids_amount: The number of asteroids to be created.
        :return: None the function changes self.__asteroids and self._screen.
        """
        for i in range(asteroids_amount):
            asteroid = self.create_asteroid()

            # check if location of asteroid not crash with the ship
            while asteroid.has_intersecion(self.__ship):
                asteroid = self.create_asteroid()

            # add the now asteroid to our internal list, and to self.__screen.
            self.__asteroids.append(asteroid)
            self.__screen.register_asteroid(asteroid, ASTEROID_SIZE)

    def run(self):

        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        self.__counter += 1

        # turn the ship
        self.turn()

        # accelerate the ship.
        self.accelerate()

        # formats our data to the required format
        to_func = (*self.__ship.get_cordinates()), self.__ship.get_angle()
        self.__screen.draw_ship(*to_func)  # draws ship

        # manage the torpedo and asteroids.
        self.torpedo_managere()
        self.print_asteroid()

        # check if we have won i.e 0 asteroids on the screen
        if len(self.__asteroids) == 0:
            msg = f"Congratulations you won! You ended the game with {self.__lives} lives and {self.__score} points"
            self.game_over("Congratulations", msg)

        # checks if the user wants to end the game
        if self.__screen.should_end():
            msg = f"Good bye, sad to see you leave. You have finished the game with " \
                  f"{self.__lives} lives and {self.__score} points"
            self.game_over("Good bye", msg)

    def game_over(self, over_massage, msg):
        """This function is called when we want to end the game.
        :param over_massage: the Title of the message.
        :param msg: The message to print.
        :return None"""
        self.__screen.show_message(over_massage, msg)
        self.__screen.end_game()
        sys.exit()

    def astoids_torp_col_check(self, torp):
        """This function checks if a given torpedo collides with one of the asteroids.
        :param torp: The torpedo we will check for collisions
        :return True if there was a collision, False otherwise.
        """
        for astro in self.__asteroids:
            if astro.has_intersecion(torp):
                astro_size = astro.get_size()

                # if we need to split the asteroid
                if astro_size > 1:
                    self.split_asteroid(astro, torp)

                # add the score
                self.__score += SCORE_MARKERS[astro_size]
                self.__screen.set_score(self.__score)  # changes current score

                # removes the old asteroid
                self.__screen.unregister_asteroid(astro)
                self.__asteroids.remove(astro)

                return True

        return False

    def split_asteroid(self, asteroid, torpedo):
        """This function does all the pre-computing for a collision.
        :param asteroid: The asteroid we want to remove.
        :param torpedo: The torpedo that hit the asteroid.
        :return None we will change self.__asteroids  """
        coords = asteroid.get_cordinates()

        # get asteroid speed for x and y
        old_as_spx, old_as_spy = asteroid.get_speed()
        # get torpedo speed
        torp_speedx, torp_speedy = torpedo.get_speed()

        # get the magnitude of the speeds
        norma = math.sqrt(old_as_spx ** 2 + old_as_spy ** 2)
        # get new speed according to formula
        new_as_speed_x = (torp_speedx + old_as_spx) / norma
        new_as_speed_y = (torp_speedy + old_as_spy) / norma
        new_size = asteroid.get_size() - 1

        # creates two new asteroids according to parameters above
        new_as_1 = Asteroid((coords[0], new_as_speed_x), (coords[1], new_as_speed_y), new_size)
        new_as_2 = Asteroid((coords[0], -1 * new_as_speed_x), (coords[1], -1 * new_as_speed_y), new_size)

        # add the asteroids to the screen
        self.__screen.register_asteroid(new_as_1, new_size)
        self.__screen.register_asteroid(new_as_2, new_size)

        self.__asteroids += [new_as_1, new_as_2]  # add to internal list

    def torpedo_managere(self):
        """This function manages the toledo i.e creates them and deletes them and draws them,
         and manages collisions with asteroids. """
        # if the user wants to shoot.
        if self.__screen.is_space_pressed() and len(self.__torpedos) < MAX_TORPEDO:
            self.create_torpedo()

        # if we need to remove a torpedo
        if self.__counter in self.__torpedos:
            self.__screen.unregister_torpedo(self.__torpedos[self.__counter])  # removes the current expired torpedo
            self.__torpedos.pop(self.__counter)  # remove from out list

        col_torps = []  # This will store the key of the torpedo that had collisions.
        # moves all our torpedo
        for torp in self.__torpedos.values():
            self.change_location_object(torp)

            # check for collisions with al the asteroids
            if self.astoids_torp_col_check(torp):
                # get the key of the current torpedo
                key = list(self.__torpedos.keys())[list(self.__torpedos.values()).index(torp)]
                col_torps.append(key)

            x_loc, y_loc = torp.get_cordinates()
            angle = torp.get_angle()
            self.__screen.draw_torpedo(torp, x_loc, y_loc, angle)

        # remove all the collision torpedo
        for inde in col_torps:
            # gets and removes the throed from interior dict
            torp = self.__torpedos.pop(inde)
            self.__screen.unregister_torpedo(torp)

    def create_torpedo(self):
        """This function shoots a torpedo.
        :return None
        """
        x_speed, y_speed = self.__ship.get_speed()
        x_coord, y_coord = self.__ship.get_cordinates()
        angle = math.radians((self.__ship.get_angle()))
        torpedo_x = (x_coord, x_speed + 2 * math.cos(angle))
        torpedo_y = (y_coord, y_speed + 2 * math.sin(angle))
        # creates the torpedo
        torp = Torpedo(torpedo_x, torpedo_y, angle)
        # adds the torpedo to the dict with current tick + Torp_life_time = 200 as the key
        self.__torpedos[self.__counter + TORPEDO_LIFETIME] = torp
        self.__screen.register_torpedo(torp)

    def create_asteroid(self):
        """This function creates a random asteroid according the the requirements.
        :return Asteroid, the random asteroid created"""
        # get random x, y coords
        random_x, random_y = self.random_location()

        # create the random accelerating params.
        random_accelerate_x, random_accelerate_y = random.choice(AST_SPEED), random.choice(AST_SPEED)
        asteroid = Asteroid((random_x, random_accelerate_x), (random_y, random_accelerate_y), ASTEROID_SIZE)
        return asteroid

    def random_location(self):
        """This function creates two random x y coords, in the screen.
        :return: random_x, random_y two floats
        """
        random_x = random.randint(self.__screen_min_x, self.__screen_max_x)  # get random value for x coordinate
        random_y = random.randint(self.__screen_min_y, self.__screen_max_y)  # get random value for y coordinate
        return random_x, random_y

    def turn(self):
        """This function turns the ship.
        :return None, it changes the ship"""
        if self.__screen.is_right_pressed():
            angle = self.__ship.get_angle()
            self.__ship.change_angle(angle - ROTATION)
        # maybe this will cause problems with if and not elif
        if self.__screen.is_left_pressed():
            angle = self.__ship.get_angle()
            self.__ship.change_angle(angle + ROTATION)

    def print_asteroid(self, if_col=False):
        """
        This function prints all our asteroids, it also moves them and checks for collisions with the ship.
        :param if_col: bool if there was a collision.:
        :return: None
        """
        ind = 0
        for astro in self.__asteroids:
            self.change_location_object(astro)
            # draw the asteroid
            self.__screen.draw_asteroid(astro, *astro.get_cordinates())

            # check for collision with ship
            if astro.has_intersecion(self.__ship):
                if_col = True
                ind = self.__asteroids.index(astro)

        # if there was a collision with the ship
        if if_col:
            self.__screen.show_message("You hit a asteroid", "You lose 1 life")
            self.__screen.remove_life()
            self.__lives -= 1
            astro = self.__asteroids.pop(ind)
            self.__screen.unregister_asteroid(astro)

            # if the user has no remaining lives
            if self.__lives == 0:
                self.game_over("Game over", "You have run out of lives, so you lose.")

    def accelerate(self):
        """This function accelerates the ship."""
        if self.__screen.is_up_pressed():
            # accelerate the ship
            accelerate_object(self.__ship)
        self.change_location_object(self.__ship)

    def change_location_object(self, obj):
        """
        this function changes the location of the object.

        :param obj: object like ship or asteroid or torpedo
        :return: None
        """
        speed, coords = obj.get_speed(), obj.get_cordinates()

        # get the new x,y coords.
        new_spot_x = calc_new_spot(self.__screen_min_x, self.__screen_max_x, coords[0], speed[0])
        new_spot_y = calc_new_spot(self.__screen_min_y, self.__screen_max_y, coords[1], speed[1])

        obj.change_coords((new_spot_x, new_spot_y))


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            main(int(sys.argv[1]))

        # if the input is not a integer
        except ValueError:
            pass
    else:
        main(DEFAULT_ASTEROIDS_NUM)
