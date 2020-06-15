from uxrd.io_functions import read_brml, write_dat
from numpy.testing import assert_allclose


def test_read_brml_astext():
    path = 'a_brml.brml'
    dat_data = read_brml(path, as_text=True)
    assert dat_data[0][0] == '5'
    assert dat_data[0][1] == '5362'


def test_read_brml():
    path = 'a_brml.brml'
    dat_data = read_brml(path)
    assert_allclose(dat_data[0][0], 5.0, rtol=0.00001)
    assert_allclose(dat_data[0][1], 5362, rtol=0.00001)


def test_write_dat_text():
    path = 'a_brml.brml'
    dat_data = read_brml(path, as_text=True)
    dat_filename = 'datfile.dat'
    write_dat(dat_filename, dat_data)
    with open(dat_filename, 'r') as datfile:
        line = datfile.readline().split()
        assert_allclose(float(line[0]), 5.0, rtol=0.00001)
    assert_allclose(float(line[1]), 5362, rtol=0.00001)


def test_write_dat_float():
    path = 'a_brml.brml'
    dat_data = read_brml(path, as_text=False)
    dat_filename = 'datfile.dat'
    write_dat(dat_filename, dat_data)
    with open(dat_filename, 'r') as datfile:
        line = datfile.readline().split()
    assert_allclose(float(line[0]), 5.0, rtol=0.00001)
    assert_allclose(float(line[1]), 5362, rtol=0.00001)
