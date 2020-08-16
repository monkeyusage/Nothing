from main import Nothing
Nothing = Nothing()
from random import randint
from pytest import raises

def test_call():
    assert Nothing() == Nothing

def test_str():
    assert str(Nothing) == "Nothing"

def test_repr():
    assert repr(Nothing) == "Nothing"

def test_add():
    assert + Nothing == Nothing
    assert Nothing + 1 == Nothing
    assert Nothing + Nothing == Nothing
    assert Nothing + None == Nothing
    assert 1 + Nothing == Nothing

def test_sub():
    assert - Nothing == Nothing
    assert Nothing - 1 == Nothing
    assert Nothing - Nothing == Nothing
    assert 1 - Nothing == Nothing

def test_mul():
    assert Nothing * Nothing == Nothing
    assert Nothing * 1 == Nothing
    assert 1 * Nothing == Nothing

def test_div():
    assert Nothing / Nothing == Nothing
    assert Nothing // Nothing == Nothing
    assert Nothing / 1 == Nothing
    assert Nothing // 1 == Nothing
    assert 1 / Nothing == Nothing
    assert 1 // Nothing == Nothing

def test_iter():
    for idx, data in enumerate(Nothing):
        assert idx == 0 and data == Nothing
    assert Nothing[0] == Nothing
    assert Nothing[-9999:9999] == Nothing

def test_len():
    assert len(Nothing) == 1

def test_equalities():
    assert (Nothing == Nothing) is True
    assert Nothing >= Nothing == Nothing
    assert Nothing > Nothing == Nothing
    assert Nothing <= Nothing == Nothing
    assert Nothing < Nothing == Nothing

def test_bools():
    assert Nothing and Nothing == Nothing
    assert Nothing and 1 == Nothing
    assert Nothing or Nothing == Nothing
    assert Nothing or 1 == Nothing

def test_round():
    with raises(TypeError) as t_error:
        int(Nothing)
    assert t_error.type is TypeError
    assert round(Nothing, 398) == Nothing
    from math import floor, trunc, ceil
    assert floor(Nothing) == Nothing
    assert trunc(Nothing) == Nothing
    assert ceil(Nothing) == Nothing
