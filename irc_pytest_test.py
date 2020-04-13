# -*- coding: utf-8 -*-

import pytest
import regex_part2_done as re2



def test_find_message():
    assert re2.find_message('a') == True
    assert re2.find_message('b') == True

@pytest.mark.parametrize('row,expected', [('a',True), ('b',True)])
def test_next(row, expected):
    assert re2.find_message(row) == expected

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,33),(4,44)])
def test_multiplication_11(num, output):
   assert 11*num == output