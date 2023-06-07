from vacation_house import VacationHouse


def make_reservation(vacation_house: VacationHouse, week: int):
    if not vacation_house.is_available(week):
        return 'House is not available'

    vacation_house.book(week)
    return 'Successful reservation!'
