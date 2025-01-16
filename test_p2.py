import pytest

from p2 import (
    elso_karakter,
    utolso_karakter,
    legkisebb,
    legnagyobb,
    osszeg,
    szorzat,
    parosok_szama,
    paratlanok_szama,
    pozitivok_szama,
    negativok_szama,
    benne_van_a_listaban,
    benne_van_a_stringben,
    kereses_a_listaban,
    kereses_a_stringben,
    parosok_kivalogatasa,
    paratlanok_kivalogatasa,
    pozitivok_kivalogatasa,
    negativok_kivalogatasa,
    lista_atlag,
    faktorialis
)

def test_elso_karakter():
    assert elso_karakter("Hello") == "H"
    assert elso_karakter("") is None

def test_utolso_karakter():
    assert utolso_karakter("Hello") == "o"
    assert utolso_karakter("") is None

def test_legkisebb():
    assert legkisebb([7, 4, 9, -4, -8, 3]) == -8
    assert legkisebb([]) is None

def test_legnagyobb():
    assert legnagyobb([7, 4, 9, -4, -8, 3]) == 9
    assert legnagyobb([]) is None

def test_osszeg():
    assert osszeg([1, 2, 3, 4, 5, 6]) == 21
    assert osszeg([]) == 0

def test_szorzat():
    assert szorzat([1, 2, 3, 4, 5]) == 120
    assert szorzat([]) == 1

def test_parosok_szama():
    assert parosok_szama([7, 4, 9, -4, -8, 3, 1]) == 3
    assert parosok_szama([]) == 0

def test_paratlanok_szama():
    assert paratlanok_szama([7, 4, 9, -4, -8, 3, 1]) == 4
    assert paratlanok_szama([]) == 0

def test_pozitivok_szama():
    assert pozitivok_szama([-7, -4, 9, -4, -8, 3, 1, 0]) == 3
    assert pozitivok_szama([]) == 0

def test_negativok_szama():
    assert negativok_szama([-7, -4, 9, -4, -8, 3, 1, 0]) == 4
    assert negativok_szama([]) == 0

def test_benne_van_a_listaban():
    assert benne_van_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 2) == False
    assert benne_van_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 9) == True

def test_benne_van_a_stringben():
    assert benne_van_a_stringben("abrakadabra", "x") == False
    assert benne_van_a_stringben("abrakadabra", "d") == True

def test_kereses_a_listaban():
    assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], -7) == 0
    assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 2) is None

def test_kereses_a_stringben():
    assert kereses_a_stringben("abrakadabra", "a") == 0
    assert kereses_a_stringben("abrakadabra", "s") is None

def test_parosok_kivalogatasa():
    assert parosok_kivalogatasa([7, 4, 9, 4, 8, 3, 1, 12, 0]) == [4, 4, 8, 12, 0]

def test_paratlanok_kivalogatasa():
    assert paratlanok_kivalogatasa([7, 4, 9, 4, 8, 3, 1, 12, 0]) == [7, 9, 3, 1]

def test_pozitivok_kivalogatasa():
    assert pozitivok_kivalogatasa([7, 4, 9, -4, -8, 3, 1, 12, 0]) == [7, 4, 9, 3, 1, 12]

def test_negativok_kivalogatasa():
    assert negativok_kivalogatasa([7, 4, 9, -4, -8, 3, 1, 12, 0]) == [-4, -8]

def test_lista_atlag():
    assert pytest.approx(lista_atlag([1, 2, 3, 4, 5, 6])) == 3.5
    assert lista_atlag([]) is None

def test_faktorialis():
    assert faktorialis(0) == 1
    assert faktorialis(5) == 120
