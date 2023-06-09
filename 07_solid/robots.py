# class Robot:
#     def __init__(self, type):
#         self.type = type
#
#     def get_type(self):
#         return self.type
#
#
# class Android(Robot):
#     def android_senzors_count(self):
#         return 4
#
#
# class Chappie(Robot):
#     def chappie_senzors_count(self):
#         return 6
#
#
# def count_robot_senzors(robots: list):
#     for robot in robots:
#         if isinstance(robot, Android):
#             print(robot.android_senzors_count())
#         elif isinstance(robot, Chappie):
#             print(robot.chappie_senzors_count())
#
#
# robots = [Android('Robocop'), Chappie('XIX')]
# count_robot_senzors(robots)
from abc import abstractmethod, ABC


class Robot(ABC):
    def __init__(self, type):
        self.type = type

    def get_type(self):
        return self.type

    @abstractmethod
    def get_senzors_count(self):
        pass



class Android(Robot):
    def get_senzors_count(self):
        return 4


class Chappie(Robot):
    def get_senzors_count(self):
        return 6


def count_robot_senzors(robots: list):
    for robot in robots:
        print(robot.get_senzors_count())


robots = [Android('Robocop'), Chappie('XIX')]
count_robot_senzors(robots)

