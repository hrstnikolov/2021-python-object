from unittest import TestCase

from labs.List.extended_list import IntegerList


class TestIntegerList(TestCase):
    # init
    def test_integer_list_init__when_ints__expect_success(self):
        pass

    # add
    def test_integer_list_add__when_string__expect_value_error(self):
        pass

    def test_integer_list_add__when_int__expect_success(self):
        pass

    # remove_index
    def test_integer_list_remove_index__when_index_is_too_big__expect_index_error(
        self,
    ):
        pass

    def test_integer_list_remove_index__when_index_is_negative__expect_index_error(
        self,
    ):
        pass

    def test_integer_list_remove_index__when_index_in_range__expect_success(self):
        pass

    # get
    def test_integer_list_get__when_index_is_too_big__expect_index_error(self):
        pass

    def test_integer_list_get__when_index_is_negative__expect_index_error(self):
        pass

    def test_integer_list_get__when_index_in_range__expect_success(self):
        pass

    # insert
