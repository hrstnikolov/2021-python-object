from unittest import TestCase, mock
from demos.hotel.reservation import make_reservation
from demos.hotel.vacation_house import VacationHouse


class TestReservation(TestCase):
    @mock.patch('reservation.VacationHouse')
    def test_make_reservation__when_not_available__expect_failure(self, my_mock):
        VacationHouseMock = my_mock.return_value
        VacationHouseMock.is_available.return_value = False

        house = VacationHouse('Borovets houses', [1, 4, 5])
        actual_result = make_reservation(house, 2)
        expected_result = 'House is not available'
        self.assertEqual(expected_result, actual_result)
