import unittest

from labs.worker.worker import Worker


class WorkerTest(unittest.TestCase):
    name = 'Mark Van Dajk'
    salary = 5700
    energy = 6

    def setUp(self) -> None:
        # 1) Arrange (prepare)
        self.worker = Worker(name=self.name, salary=self.salary, energy=self.energy)

    def test_worker_init__correct_values__expect_correct_values(self):
        """Test if the worker is initialized with correct name, salary and energy"""
        # 2) Act and 3) Assert
        self.assertEqual(self.worker.name, self.name)
        self.assertEqual(self.worker.salary, self.salary)
        self.assertEqual(self.worker.energy, self.energy)

    def test_worker_rest__when_correct_values__expect_to_be_increased_by_1(self):
        """Test if the worker's energy is incremented after the rest method is called"""
        # 2) Act
        self.worker.rest()
        # 3) Assert
        self.assertEqual(self.worker.energy, self.energy + 1)

    def test_worker_work__when_zero_energy__expect_exception(self):
        """Test if an error is raised if the worker tries to work with energy equal to 0"""
        # 2) Act
        self.worker.energy = 0
        # 3) Assert
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work__when_negative_energy__expect_exception(self):
        """Test if an error is raised if the worker tries to work with negative energy"""
        # 2) Act
        self.worker.energy = -24
        # 3) Assert
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_work__when_correct_values__expect_money_to_be_increase_by_salary(self):
        """Test if the worker's money is increased by his salary correctly after the work method is called"""
        self.worker.work()
        self.assertEqual(self.worker.money, self.salary)

    def test_worker_work__when_correct_values__expect_energy_to_decrease(self):
        """Test if the worker's energy is decreased after the work method is called"""
        self.worker.work()
        self.assertEqual(self.worker.energy, self.energy - 1)

    def test_worker_get_info__when_correct_values__expect_correct_values(self):
        """Test if the get_info method returns the proper string with correct values"""
        self.assertEqual(self.worker.get_info(), f'{self.name} has saved 0 money.')

