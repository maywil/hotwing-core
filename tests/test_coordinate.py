import pytest
import sys, os
from decimal import Decimal

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from hotwing_core import Coordinate


class TestCoordinate():
    def test_create_coordinate(self):
        x = 1
        y = 1.4
        c = Coordinate(x, y)
        assert x == c.x
        assert y == c.y

    def test_representations(self):
        x = 1
        y = 1.4
        c = Coordinate(x, y)
        assert "1.00000, 1.40000" == c.__str__()
        assert "Coordinate: 1.00000, 1.40000" == c.__repr__()

    def test_equality_comparison(self):
        x = 1
        y = 1.4
        c1 = Coordinate(x, y)
        c2 = Coordinate(x, y)
        c3 = Coordinate(y, x)
        assert c1 == c2
        assert not c2 == c3

        # test inequality operator too
        assert c2 != c3
        assert not c1 != c2

        # try comparison to non object
        with pytest.raises(NotImplementedError):
            1 == c1
        with pytest.raises(NotImplementedError):
            c1 == 1
        with pytest.raises(NotImplementedError):
            1 != c1
        with pytest.raises(NotImplementedError):
            c1 != 1


    def test_calc_slope(self):
        c1 = Coordinate(0, 0)
        c2 = Coordinate(1, 1)
        s1 = Coordinate.calc_slope(c1,c2)
        assert  s1 == 1

        c1 = Coordinate(0, 0)
        c2 = Coordinate(1, 0)
        s1 = Coordinate.calc_slope(c1,c2)
        assert  s1 == 0

        # test infinite slope
        c1 = Coordinate(0, 0)
        c2 = Coordinate(0, 0)
        s1 = Coordinate.calc_slope(c1,c2)
        assert  s1 >= 1000000

    def test_calc_dist(self):
        c1 = Coordinate(0, 0)
        c2 = Coordinate(1, 0)
        d = Coordinate.calc_dist(c1,c2)
        assert  d == 1

        c1 = Coordinate(0, 0)
        c2 = Coordinate(0, 2)
        d = Coordinate.calc_dist(c1,c2)
        assert  d == 2

        c1 = Coordinate(0, 0)
        c2 = Coordinate(0, -3)
        d = Coordinate.calc_dist(c1,c2)
        assert  d == 3

        c1 = Coordinate(-4, 0)
        c2 = Coordinate(0, 0)
        d = Coordinate.calc_dist(c1,c2)
        assert  d == 4

        c1 = Coordinate(0, 0)
        c2 = Coordinate(3, 4)
        d = Coordinate.calc_dist(c1,c2)
        assert  d == 5

        c1 = Coordinate(0, 0)
        c2 = Coordinate(0, 0)
        d = Coordinate.calc_dist(c1,c2)
        assert  d == 0

    def test_rotate(self):
        o = Coordinate(1, 1) # origin to rotate
        c = Coordinate(3, 3) # coordinate
        a = 90 # angle
        e = Coordinate(-1,3) # expected
        r = Coordinate.rotate(o,c,a)
        assert e == r

        o = Coordinate(1, 1)
        c = Coordinate(3, 3)
        a = 180
        e = Coordinate(-1,-1)
        r = Coordinate.rotate(o,c,a)
        assert e == r

        o = Coordinate(1, 1)
        c = Coordinate(3, 3)
        a = 270
        e = Coordinate(3,-1)
        r = Coordinate.rotate(o,c,a)
        assert e == r

        o = Coordinate(1, 1)
        c = Coordinate(3, 3)
        a = 360
        e = c
        r = Coordinate.rotate(o,c,a)
        assert e == r

    def test_add(self):
        c1 = Coordinate(1, 2)
        c2 = Coordinate(3, 4)
        e = Coordinate(1+3,2+4)
        assert c1+c2 == e

        with pytest.raises(NotImplementedError):
            c1 + 1

    def test_subtract(self):
        c1 = Coordinate(1, 2)
        c2 = Coordinate(3, 4)
        e = Coordinate(1-3,2-4)
        assert c1-c2 == e

        with pytest.raises(NotImplementedError):
            c1 - 1

    def test_multiply(self):
        c1 = Coordinate(0, 1)
        c2 = Coordinate(2, 3)
        assert c1*c2 == Coordinate(0*2,1*3)

        # test with numeric objects
        assert c1*2 == Coordinate(0*2,1*2)
        assert c1*2 == Coordinate(0*float(2),1*float(2))
        assert c1*2 == Coordinate(0*Decimal(2),1*Decimal(2))

