from unittest import TestCase, mock
from vacation_house import VacationHouse
from reservation import make_reservation


class TestReservation(TestCase):
    @mock.patch('vacation_house.VacationHouse')
    def test_make_reservation__when_not_available__expect_failure(self, mock):
        MockedVacationHouse = mock.return_value
        MockedVacationHouse.is_available.return_value = False

        house = VacationHouse('Borovets houses', [1, 4, 5])
        actual_result = make_reservation(house, 2)
        expected_result = 'House is not available'
        self.assertEqual(expected_result, actual_result)

