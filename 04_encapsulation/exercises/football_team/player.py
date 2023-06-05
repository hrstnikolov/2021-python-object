from textwrap import dedent


class Player:
    def __init__(
        self,
        name: str,
        endurance: float,
        sprint: float,
        dribble: float,
        passing: float,
        shooting: float,
    ) -> None:
        # Set the instance attributes to the init params.
        self.__name = name
        self.__endurance = endurance
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def endurance(self):
        return self.__endurance

    @endurance.setter
    def endurance(self, new_endurance):
        self.__endurance = new_endurance

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, new_sprint):
        self.__sprint = new_sprint

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        self._dribble = value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        self.__passing = value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value

    # NOK. Explicit is better than implicit.
    # def __str__(self) -> str:
    #     public_attrs = [attr for attr in dir(self) if not attr.startswith("_")]
    #     return "\n".join(
    #         [f"{attr.capitalize()} = {getattr(self, attr)}" for attr in public_attrs]
    #     )

    # OK
    def __str__(self) -> str:
        return dedent(
            f"""
            Player: {self.name}
            Endurance: {self.endurance}
            Sprint: {self.sprint}
            Dribble: {self.dribble}
            Passing: {self.passing}
            Shooting: {self.shooting}
    """
        )


ronaldo = Player("Ronaldo", 80, 92, 95, 76, 98)
print(ronaldo)
