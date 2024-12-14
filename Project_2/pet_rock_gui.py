"""
Author comment:
Credits to 'soumibardhan10' on geeksforgeeks who's guide formed the basis for the multi-page format for tkinter.
Some documentation and naming left over from their code due to their better knowledge of its workings. Everything else
has been written by hand other than the functionality for multiple pages and page switching.
Link to webpage: https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
"""

import tkinter as tk
from tkinter import ttk

from pet_rock import *
#Import statements used in the GUI class for its functioning.

#TODO: A lot of widgets need to be re-adjusted for aesthetics and making everything look nice.
class TkinterApp(tk.Tk):
    """
    Class for the functionality of multiple pages, no code for the actual content inside each page is here and is thus
    mostly unchanged from the inspiration unless otherwise stated by '*'.
    """
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs) -> None:
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (IntroPage, GuidePage, CheatPage, GamePage, EndPage):
            frame = F(container, self)
            # initializing frame of that object from
            # * IntroPage, GuidePage, CheatPage, GamePage, EndPage respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(IntroPage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont) -> None:
        frame = self.frames[cont]
        frame.tkraise()

class IntroPage(tk.Frame):
    """
    Class for the creation and functionality of the IntroPage. Note the usage of grids over packing methods for this
    and any further page class.
    """
    def __init__(self, parent, controller) -> None:
        """
        IntroPage layout and widget construction.
        :param parent: Used in init function
        :param controller: Used when changing pages
        """
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text="Intro Page")
        label.grid(row=0, column=0, padx=10, pady=10)
        #Tells you what page you are currently on.

        intro_label = ttk.Label(self, text="In this game your goal will be to take care of a pet rock for the next 5\n"
                                           "days. Each day you will need to feed, groom, play with and walk your pet…\n"
                                           "\nEach day you are allowed 5 actions."
                                           "\n\nNOTE: On the guide page, there is a cheat sheet for testing purposes")
        intro_label.grid()
        #Displays an introduction to the app.

        intro_to_guide = ttk.Button(self, text="Guide Page",
                                    command=lambda: controller.show_frame(GuidePage))
        intro_to_game = ttk.Button(self, text="Play the game!",
                                   command=lambda: controller.show_frame(GamePage))
        intro_to_guide.grid(row=2, column=1, padx=10, pady=10)
        intro_to_game.grid(row=3, column=1, padx=10, pady=10)
        #Buttons for page navigation, either going straight to the game or going to the guide.

# second window frame page1
class GuidePage(tk.Frame):
    """
    Class for creation and functionality of the guide page.
    """
    def __init__(self, parent, controller) -> None:
        """
        GuidePage construction and layout.
        :param parent: Used in init function.
        :param controller: Used when changing pages.
        """
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Guide Page")
        label.grid(row=0, column=4, padx=10, pady=10)
        #Tells you what page you are currently on

        guide_label = ttk.Label(self, text="Days: 0 to five days, increases when you press 'next day'.\n\n"
                                           "Hunger: How hungry the rock is. Sand has no downsides but feeds very little,\n"
                                           ", pebbles decreases hunger decently but is also messy and will increase\n"
                                           "dirtiness, Marbles are like candy and are very filling and make the rock\n"
                                           "happier but also decreases their health.\n\n"
                                           "Actions: 5 each day (doesn't stack), decreases by 1 every time you do\n"
                                           "something, if you run out of actions, clicking a button won't do anything.\n\n"
                                           "Dirtiness: How filthy the rock is, can be reduced by brushing and polishing,\n"
                                           "like cats, the rock doesn't like bath time, and will be unhappy the more\n"
                                           "intense the cleaning.\n\n"
                                           "Happiness: Increased by playing, be aware the rock gets a little dirty\n"
                                           "after playing.\n\n"
                                           "Health: Increased by walking, but also makes the rock hungry and dirty\n,"
                                           "the longer the walk the hungrier it will get. Health also decreases if the\n"
                                           "rock's other stats start to suffer. If health reaches its lowest point, you\n"
                                           "lose the game.")
        guide_label.grid()
        #Detailed game guide text

        guide_to_game = ttk.Button(self, text="Play the game!",
                             command=lambda: controller.show_frame(GamePage))
        guide_to_game.grid(row=1, column=1, padx=10, pady=10)
        #Takes you to the game

        guide_to_cheat = ttk.Button(self, text="Cheat sheet.",
                             command=lambda: controller.show_frame(CheatPage))
        guide_to_cheat.grid(row=2, column=1, padx=10, pady=10)
        #Takes you to the cheat page

class CheatPage(tk.Frame):
    """
    Class for the creation and functionality of the cheat page.
    """
    def __init__(self, parent, controller) -> None:
        """
        CheatPage construction and layout.
        :param parent: Used in init function.
        :param controller: Used when changing pages.
        """
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Cheat Page")
        label.grid(row=0, column=4, padx=10, pady=10)
        #Tells you what page you are on

        cheat_label = ttk.Label(self, text="Daily stat decreases haven't been programmed in yet, so just clicking\n"
                                           "'next day' repeatedly until you finish day 5 will win the game.\n"
                                           "To lose, do nothing but feed marbles each day since marbles decrease\n"
                                           "health by a decent degree.")
        cheat_label.grid()
        #Tells you how to win the game or lose the game guaranteed, for testing and review purposes.

        cheat_to_game = ttk.Button(self, text="Return to game",
                             command=lambda: controller.show_frame(GamePage))
        cheat_to_game.grid(row=1, column=1, padx=10, pady=10)
        #Takes you to the game.

class GamePage(tk.Frame):
    """
    Class for the creation and functionality of the game page.
    """
    def __init__(self, parent, controller) -> None:
        """
        GamePage construction and layout, contains most of the game's functionality.
        :param parent: Used in init function.
        :param controller: Used when changing pages, note unconventional page switch circumstances.
        """
        tk.Frame.__init__(self, parent)

        self.controller = controller
        self.pr = PetRock()
        #Needed for the use of functions from pet_rock.py

        self.__current_day = 0
        self.__action_count = 5
        #Initial values for day and action count.

        label = ttk.Label(self, text="Game Page")
        label.grid(row=0, column=4, padx=10, pady=10)
        #Tells you what page you are on

        rock_false_image = ttk.Label(self,text="ROCK")
        rock_false_image.grid(row=1,column=4, padx=10, pady=10)
        #FIXME: PhotoImage issues, text="ROCK" serves as placeholder for functionality.
        #Cosmetic display

        self.day_label = ttk.Label(self, text=f"Day: {self.__current_day}")
        self.day_label.grid(row=1, column=2, padx=10, pady=10)
        #Label that displays what the current day is.
        self.day_change = ttk.Button(self, text="Next day", command=self.next_day)
        self.day_change.grid(row=1, column=10, padx=10, pady=10)
        #Button that changes the day and calls the next_day function when clicked,
        #more detail in function documentation.

        self.action_count_label = ttk.Label(self, text=f"Remaining actions: {self.__action_count}")
        self.action_count_label.grid(row=2, column=5, padx=10, pady=10)
        #Label that displays the current action count.

        self.feed_label = ttk.Label(self, text="Feed")
        self.feed_label.grid(row=3, column=0, padx=10, pady=10)
        #Label to indicate the feed options.
        self.sand_feed = ttk.Button(self, text="Sand", command=lambda: self.feeding("Sand"))
        self.pebble_feed = ttk.Button(self, text="Pebbles", command=lambda: self.feeding("Pebbles"))
        self.marble_feed = ttk.Button(self, text="Marbles", command=lambda: self.feeding("Marbles"))
        self.sand_feed.grid(row=4, column=0, padx=10, pady=10)
        self.pebble_feed.grid(row=5, column=0, padx=10, pady=10)
        self.marble_feed.grid(row=6, column=0, padx=10, pady=10)
        #Each button passes a parameter for the feed function and executes the function. More details on function
        #documentation.

        self.groom_label = ttk.Label(self, text="Groom")
        self.groom_label.grid(row=3, column=10, padx=10, pady=10)
        #Label indicating groom options.
        self.brush = ttk.Button(self, text="Brush", command=lambda: self.cleaning("Brush"))
        self.polish = ttk.Button(self, text="Polish", command=lambda: self.cleaning("Polish"))
        self.brush.grid(row=4, column=10, padx=10, pady=10)
        self.polish.grid(row=5, column=10, padx=10, pady=10)
        #Each button passes a parameter for the cleaning function and executes the function. More details on function
        #documentation.

        self.play_label = ttk.Label(self, text="Play")
        self.play_label.grid(row=7, column=0, padx=10, pady=10)
        #Label indication play options, likely redundant and would be removed in a complete build.
        self.play_button = ttk.Button(self, text="Play", command=self.play)
        self.play_button.grid(row=8, column=0, padx=10, pady=10)
        #Button press calls the play function, no parameters.

        self.walk_label = ttk.Label(self, text="Go for a walk")
        self.walk_label.grid(row=7, column=10, padx=10, pady=10)
        #Label indicates walk, possibly redundant
        self.walk_bar = ttk.Scale(self, from_=1, to=3, orient=tk.HORIZONTAL)
        self.walk_confirm = ttk.Button(self, text="Walk", command=self.walking)
        self.walk_bar.grid(row=8, column=10, padx=10, pady=10)
        self.walk_confirm.grid(row=9, column=10, padx=10, pady=10)
        #A Scale widget to set the time being walked and a button to execute the walking function. Passing of scale data
        #described in further detail in walking function.
        #FIXME: Scale widget lacking full options, does not display current values nor increase by integer increments.

        game_to_cheat = ttk.Button(self, text="Check cheat sheet again?",
                             command=lambda: controller.show_frame(CheatPage))
        game_to_cheat.grid(row=10, column=10, padx=10, pady=10)
        #Allows return to cheat page, note progress is not reset, making it very convenient to use.

    def next_day(self) -> None:
        """
        Function for changing the day. Increases current day by one and resets action count to 5.
        If the current day is equal to or exceeds 5, the day_change button is reconfigured to transfer to the end screen.
        Alternatively, else if get_loss returns true, day_change will always send to the end page regardless of current
        day. Else is purely for error handling so the program won't crash if somehow something goes wrong.
        TODO: Have each day change and alter stats for difficulty.
        :return: None
        """
        self.__current_day += 1
        self.day_label.config(text=f"Day: {self.__current_day}")
        self.__action_count = 5
        self.action_count_label.config(text=f"Remaining actions: {self.__action_count}")
        if self.__current_day >= 5:
            self.day_change.config(command=lambda: self.controller.show_frame(EndPage))
        elif self.pr.get_loss():
            self.day_change.config(command=lambda: self.controller.show_frame(EndPage))
        else:
            pass

    def feeding(self, food) -> None:
        """
        Function for feeding the pet rock. Sand is safe but not-effective, Pebbles are better but also messy, Marbles
        are bad for the rock's health even though they are filling and also make the rock happier.
        Action count decreases by one, if no actions remain, does nothing.
        :param food: Depending on the button clicked, different food parameters are given and thus the change in stats
        differs on the food picked.
        :return: None
        """
        if self.__action_count > 0:
            self.__action_count -= 1
            self.action_count_label.config(text=f"Remaining actions: {self.__action_count}")
            if food == "Sand":
                self.pr.set_hunger(-1)
            elif food == "Pebbles":
                self.pr.set_hunger(-3)
                self.pr.set_dirt(2)
            elif food == "Marbles":
                self.pr.set_hunger(-5)
                self.pr.set_health(-2)
                self.pr.set_happiness(2)
        else:
            self.pr.set_hunger(0)

    def cleaning(self, clean) -> None:
        """
        Function for cleaning the rock. The rock hates being cleaned and will be upset, but needs to be done to reduce
        dirtiness, polish cleans better than brush but makes the rock even unhappier.
        Action count decreases by one, if no actions remain, does nothing.
        :param clean: Depending on the cleaning option clicked, different cleaning parameters execute different stat
        changes.
        :return: None
        """
        if self.__action_count > 0:
            self.__action_count -= 1
            self.action_count_label.config(text=f"Remaining actions: {self.__action_count}")
            if clean == "Brush":
                self.pr.set_dirt(-3)
                self.pr.set_happiness(-2)
            elif clean == "Polish":
                self.pr.set_dirt(-5)
                self.pr.set_happiness(-4)
        else:
            self.pr.set_dirt(0)

    def play(self) -> None:
        """
        Function for playing with the rock. Increases the rock's happiness by a lot but the rock also gets messy during
        play.
        Action count decreases by one, if no actions remain, does nothing.
        :return: None
        """
        if self.__action_count > 0:
            self.__action_count -= 1
            self.action_count_label.config(text=f"Remaining actions: {self.__action_count}")
            self.pr.set_happiness(4)
            self.pr.set_dirt(2)
        else:
            self.pr.set_happiness(0)

    def walking(self) -> None:
        """
        Function for walking the rock. Due to bugs with the scale bar, bypasses issue of floats by flat division and
        converting value into an integer. Then different stat changes depending on hours spent walking. The only way to
        restore health but also badly impacts values, in concept, the player would eventually lose if they've done
        nothing but restore health, encouraging trying to find a good balance.
        Parameter pass attempted but due to issues that arose, simply making a local variable was easier.
        Action count decreases by one, if no actions remain, does nothing.
        :return: None
        """
        hours = int(self.walk_bar.get()//1)
        if self.__action_count > 0:
            self.__action_count -= 1
            self.action_count_label.config(text=f"Remaining actions: {self.__action_count}")
            if hours == 1:
                self.pr.set_health(1)
                self.pr.set_dirt(1)
                self.pr.set_hunger(1)
            elif hours == 2:
                self.pr.set_health(3)
                self.pr.set_dirt(3)
                self.pr.set_hunger(2)
            elif hours == 3:
                self.pr.set_health(5)
                self.pr.set_dirt(3)
                self.pr.set_hunger(5)
        else:
            self.pr.set_health(0)

class EndPage(tk.Frame):
    """
    Class for the creation and functionality of the end page.
    """
    def __init__(self, parent, controller) -> None:
        """
        EndPage construction and layout.
        TODO: Recording of previous attempts.
        TODO: Restarting the game.
        :param parent: Used in init function.
        :param controller: Not used, but needs to be here to make the app work.
        """
        tk.Frame.__init__(self, parent)

        self.pr = PetRock()
        #Allows calling of functions from pet_rock.py

        label = ttk.Label(self, text="End Page")
        label.grid(row=0, column=4, padx=10, pady=10)
        #Tells you what page you are on.

        self.win_lose_label = ttk.Label(self, text=self.final())
        self.win_lose_label.grid(row=1, column=4, padx=10, pady=10)
        #Label that displays if person won or lost.
        #FIXME: Does not function as desired.

    def final(self) -> str:
        """
        Function for checking if the player has won or has lost.
        FIXME: Unfortunately, this does not work. Debug attempts have revealed the error being that the final function-
        FIXME: will execute the moment the app is run and not only when EndScreen is accessed. Attempts at manipulating-
        FIXME: EndPage from the GamePage or vice-versa has been unsuccessful as of first release.
        :return: String declaring if player has won or lost.
        """
        if self.pr.get_loss():
            return "Lost"
        elif not self.pr.get_loss():
            return "Won"
        else:
            print("error")

