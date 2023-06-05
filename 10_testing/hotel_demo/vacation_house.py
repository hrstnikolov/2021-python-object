from typing import List


class VacationHouse:
    def __init__(self, name: str, booked_weeks: List[int]):
        self.name = name
        self.booked_weeks = booked_weeks

    def is_available(self, week: int) -> bool:
        return week in self.booked_weeks

    def book(self, week):
        self.booked_weeks.append(week)
