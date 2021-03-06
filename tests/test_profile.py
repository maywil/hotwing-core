from urls import Urls
import pytest
import sys, os
import random

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from hotwing_core import Profile
from hotwing_core import Coordinate
from hotwing_core import Surface

class TestProfile():
    def test_load_dat_from_url(self):
        urls = Urls()
        return
        ## skip for now to save time
        for i in range(5):
            url = urls.random['location']
            try:
                p = Profile(url)
            except:
                print(url)
                raise
        # try bad url - 404
        # try valid URL but not coordinate file

    def _get_profiles(self):
        mypath = "tests/profiles"
        return [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

    def test_init_bad_addribute(self):
        with pytest.raises(AttributeError):
            Profile("","","")

    def random_profile_file(self):
        return random.choice(self._get_profiles())

    def test_load_dat_file(self):
        # try to load all profiles
        for i in range(5):
            p = Profile(self.random_profile_file())

    def test_copy(self):
        filepath = self.random_profile_file()
        p1 = Profile(filepath)
        p2 = Profile.copy(p1)
        assert not p1 is p2
        assert p1 == p2
        assert not p1 != p2

    def test_scale(self):
        filepath = self.random_profile_file()
        scale = 2.25
        p1 = Profile(filepath)
        p2 = Profile(filepath)
        p2 = Profile.scale(p2, scale)
        for i in range(len(p1.top.coordinates)):
            assert p2.top.coordinates[i] == p1.top.coordinates[i] * scale
        for i in range(len(p1.bottom.coordinates)):
            assert p2.bottom.coordinates[i] == p1.bottom.coordinates[i] * scale
        p3 = p1*scale
        assert p2 == p3

    def test_split(self):
        top = [
            Coordinate(0.2, 0.3), 
            Coordinate(0.4, 0.4),
            Coordinate(0.6, 0.5),
            Coordinate(0.8, 0.6)
        ]
        bottom = [
            Coordinate(0.3, 0.2), 
            Coordinate(0.4, 0.4),
            Coordinate(0.5, 0.6),
            Coordinate(0.6, 0.8)
        ]
        p = Profile(top+bottom)
        assert len(p.top.coordinates) == len(top)
        assert p.top == Surface(top)
        assert len(p.bottom.coordinates) == len(bottom)
        assert p.bottom == Surface(bottom)

    def test_bounds(self):
        top = [
            Coordinate(0.2, 0.4), 
            Coordinate(0.4, 0.5),
            Coordinate(0.6, 0.6),
            Coordinate(0.8, 0.7)
        ]
        bottom = [
            Coordinate(0.3, 0.1), 
            Coordinate(0.4, 0.2),
            Coordinate(0.5, 0.3),
            Coordinate(0.6, 0.4)
        ]
        p = Profile(top+bottom)
        assert p.x_bounds[0] == 0.2
        assert p.x_bounds[1] == 0.8
        assert p.y_bounds[0] == 0.1
        assert p.y_bounds[1] == 0.7

    def test_trim(self):
        top = [
            Coordinate(0.2, 0.4), 
            Coordinate(0.4, 0.5),
            Coordinate(0.6, 0.6),
            Coordinate(0.8, 0.7)
        ]
        bottom = [
            Coordinate(0.3, 0.1), 
            Coordinate(0.4, 0.2),
            Coordinate(0.5, 0.3),
            Coordinate(0.6, 0.4)
        ]
        # trim using the min and max x - should not change
        p1 = Profile(top+bottom)
        p2 = Profile.trim(p1,0.2,0.8)
        assert p1.top == p2.top

        # extend profile
        p3 = Profile.trim(p1,0,1)
        assert p3.x_bounds[0] == 0
        assert p3.x_bounds[1] == 1

        # Try Using None Values
        p4 = Profile.trim(p1,None,1)
        assert p4.x_bounds[0] == 0.2
        assert p4.x_bounds[1] == 1

        p5 = Profile.trim(p1,0,None)
        assert p5.x_bounds[0] == 0
        assert p5.x_bounds[1] == 0.8

        p6 = Profile.trim(p1,None,None)
        assert p6.x_bounds[0] == 0.2
        assert p6.x_bounds[1] == 0.8

    def test_translate(self):
        top = [
            Coordinate(0.2, 0.4), 
            Coordinate(0.4, 0.5),
            Coordinate(0.6, 0.6),
            Coordinate(0.8, 0.7)
        ]
        bottom = [
            Coordinate(0.3, 0.1), 
            Coordinate(0.4, 0.2),
            Coordinate(0.5, 0.3),
            Coordinate(0.6, 0.4)
        ]
        # trim using the min and max x - should not change
        p1 = Profile(top+bottom)
        offset = Coordinate(1,2)
        p2 = Profile.translate(p1,offset)
        for i in range(len(p1.top.coordinates)):
            assert p2.top.coordinates[i] == p1.top.coordinates[i] + offset
        p3 = p1+offset
        assert p2 == p3


    def test_rotate(self):
        top = [
            Coordinate(0.2, 0.4), 
            Coordinate(0.4, 0.5),
            Coordinate(0.6, 0.6),
            Coordinate(0.8, 0.7)
        ]
        bottom = [
            Coordinate(0.3, 0.1), 
            Coordinate(0.4, 0.2),
            Coordinate(0.5, 0.3),
            Coordinate(0.6, 0.4)
        ]
        p1 = Profile(top+bottom)
        origin = Coordinate(1,2)
        angle = 10
        p1_r = Profile.rotate(origin,p1,angle)
        p2 = Profile.rotate(origin,p1_r,-angle)
        assert p1 == p2

    def test_comparison(self):
        top = [
            Coordinate(0.2, 0.4), 
            Coordinate(0.4, 0.5),
            Coordinate(0.6, 0.6),
            Coordinate(0.8, 0.7)
        ]
        other_top = [
            Coordinate(0.1, 0.4), 
            Coordinate(0.4, 0.5),
            Coordinate(0.6, 0.6),
            Coordinate(0.8, 0.7)
        ]
        bottom = [
            Coordinate(0.3, 0.1), 
            Coordinate(0.4, 0.2),
            Coordinate(0.5, 0.3),
            Coordinate(0.6, 0.4)
        ]
        other_bottom = [
            Coordinate(0.1, 0.1), 
            Coordinate(0.2, 0.2),
            Coordinate(0.5, 0.4),
            Coordinate(0.6, 0.5)
        ]
        

        p1 = Profile(top+bottom)
        p2 = Profile(top+bottom)

        p3 = Profile(top+other_bottom)
        p4 = Profile(other_top+bottom)
        p5 = Profile(other_top+other_bottom)

        assert p1 == p2
        assert p2 != p3
        assert p3 != p4
        assert p4 != p5

        with pytest.raises(NotImplementedError):
            p1 == 1

        with pytest.raises(NotImplementedError):
            p1 != "s"

    def test_add_sub(self):
        top = [
            Coordinate(0.2, 0.4), 
            Coordinate(0.4, 0.5),
            Coordinate(0.6, 0.6),
            Coordinate(0.8, 0.7)
        ]
        bottom = [
            Coordinate(0.3, 0.1), 
            Coordinate(0.4, 0.2),
            Coordinate(0.5, 0.3),
            Coordinate(0.6, 0.4)
        ]
        coord = Coordinate(1, 2)
        p1 = Profile(top+bottom)
        p2 = p1 + coord
        p3 = p2 - coord

        assert p1 == p3

        with pytest.raises(NotImplementedError):
            p1 + 1

        with pytest.raises(NotImplementedError):
            p1 - "s"
