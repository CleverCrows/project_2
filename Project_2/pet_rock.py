class PetRock:
    """
    Class for PetRock and contains many of the calculations used in the GUI file.
    ABS_MAX/MIN stats are the absolute lowest or highest a value is allowed to be.
    MAX/MIN once exceeded will cause certain stats to change.
    """
    ABS_MIN_STAT = -5
    MIN_STAT = 0
    MAX_STAT = 10
    ABS_MAX_STAT = 15

    def __init__(self) -> None:
        """
        Sets initial values for hunger, dirtiness, health, happiness, and lose status.
        Hunger, dirtiness, health and happiness are set to 5. Lose is False by default.
        :return: None
        """
        self.__hunger = 5
        self.__dirtiness = 5
        self.__health = 5
        self.__happiness = 5
        self.__lose = False

    def set_hunger(self, val) -> None:
        """
        Changes the hunger, if hunger gets too high, decreases health by passing a negative value to the health
        function.
        :param val: Value passed to the function, whatever hunger is being increased or decreased by.
        :return: None
        """
        if self.__hunger + val <= self.ABS_MIN_STAT:
            self.__hunger = self.ABS_MIN_STAT
        elif self.__hunger + val >= self.ABS_MAX_STAT:
            self.__hunger = self.ABS_MAX_STAT
            self.set_health(-2)
        else:
            if self.__hunger + val > self.MAX_STAT:
                self.__hunger += val
                self.set_health(-2)
            else:
                self.__hunger += val

    def set_dirt(self, val):
        """
        Changes the dirtiness, if dirtiness gets too high, decreases health by passing a negative value to the health
        function.
        :param val: Value passed to the function, whatever dirtiness is being increased or decreased by.
        :return: None
        """
        if self.__dirtiness + val <= self.ABS_MIN_STAT:
            self.__dirtiness = self.ABS_MIN_STAT
        elif self.__dirtiness + val >= self.ABS_MAX_STAT:
            self.__dirtiness = self.ABS_MAX_STAT
            self.set_health(-2)
        else:
            if self.__dirtiness + val > self.MAX_STAT:
                self.__dirtiness += val
                self.set_health(-2)
            else:
                self.__dirtiness += val

    def set_happiness(self, val):
        """
        Changes the happiness, if happiness gets too low, decreases health by passing a negative value to the health
        function.
        :param val: Value passed to the function, whatever happiness is being increased or decreased by.
        :return: None
        """
        if self.__happiness + val <= self.ABS_MIN_STAT:
            self.__happiness = self.ABS_MIN_STAT
            self.set_health(-2)
        elif self.__happiness + val >= self.ABS_MAX_STAT:
            self.__happiness = self.ABS_MAX_STAT
        else:
            if self.__happiness + val < self.MIN_STAT:
                self.__happiness += val
                self.set_health(-2)
            else:
                self.__happiness += val
    def set_health(self, val):
        """
        Changes the health. If health reaches absolute minimum, the loss status is changed.
        :param val: Value passed to the function, whatever health is being increased or decreased by.
        :return: None
        """
        if self.__health + val <= self.ABS_MIN_STAT:
            self.__health = self.ABS_MIN_STAT
            self.loss()
        elif self.__health + val >= self.ABS_MAX_STAT:
            self.__health = self.ABS_MAX_STAT
        else:
            self.__health += val

    def loss(self):
        #Sets lose to True
        self.__lose = True

    def get_hunger(self) -> int:
        #Retrieves private hunger variable.
        return self.__hunger

    def get_happiness(self) -> int:
        #Retrieves private happiness variable.
        return self.__happiness

    def get_dirt(self) -> int:
        #Retrieves private dirtiness variable.
        return self.__dirtiness

    def get_health(self) -> int:
        #Retrieves private health variable.
        return self.__health

    def get_loss(self) -> bool:
        #Retrieves private loss boolean.
        return self.__lose