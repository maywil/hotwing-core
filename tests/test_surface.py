import sys, os
import pytest

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from hotwing_core import Coordinate, Surface



coordinates = [
        Coordinate(1, 0),
        Coordinate(1, 0), # Dupe
        Coordinate(0.99667, 0.00045),
        Coordinate(0.98707, 0.00195),
        Coordinate(0.97194, 0.00446),
        Coordinate(0.95169, 0.0076),
        Coordinate(0.92645, 0.01112),
        Coordinate(0.89647, 0.01506),
        Coordinate(0.86218, 0.01937),
        Coordinate(0.82405, 0.02394),
        Coordinate(0.78255, 0.02867),
        Coordinate(0.73817, 0.03344),
        Coordinate(0.6914499, 0.03811),
        Coordinate(0.6914499, 0.03811), # Dupe
        Coordinate(0.6914499, 0.03811), # Dupe
        Coordinate(0.64292, 0.04256),
        Coordinate(0.5931, 0.04666),
        Coordinate(0.54254, 0.05029),
        Coordinate(0.49178, 0.05334),
        Coordinate(0.44133, 0.0557),
        Coordinate(0.39172, 0.05727),
        Coordinate(0.34343, 0.058),
        Coordinate(0.29692, 0.0578),
        Coordinate(0.25262, 0.05666),
        Coordinate(0.21095, 0.05456),
        Coordinate(0.17226, 0.05151),
        Coordinate(0.13689, 0.04755),
        Coordinate(0.10513, 0.04275),
        Coordinate(0.07725, 0.03721),
        Coordinate(0.05344, 0.03104),
        Coordinate(0.03388, 0.02439),
        Coordinate(0.01867, 0.01744),
        Coordinate(0.00786, 0.01048),
        Coordinate(0.0015, 0.0039),
        Coordinate(0.0015, 0.0039),
        Coordinate(0, 0),
        Coordinate(0, 0) # Dupe
]

coordinates_no_dupe = [
        Coordinate(1, 0),
        Coordinate(0.99667, 0.00045),
        Coordinate(0.98707, 0.00195),
        Coordinate(0.97194, 0.00446),
        Coordinate(0.95169, 0.0076),
        Coordinate(0.92645, 0.01112),
        Coordinate(0.89647, 0.01506),
        Coordinate(0.86218, 0.01937),
        Coordinate(0.82405, 0.02394),
        Coordinate(0.78255, 0.02867),
        Coordinate(0.73817, 0.03344),
        Coordinate(0.6914499, 0.03811),
        Coordinate(0.64292, 0.04256),
        Coordinate(0.5931, 0.04666),
        Coordinate(0.54254, 0.05029),
        Coordinate(0.49178, 0.05334),
        Coordinate(0.44133, 0.0557),
        Coordinate(0.39172, 0.05727),
        Coordinate(0.34343, 0.058),
        Coordinate(0.29692, 0.0578),
        Coordinate(0.25262, 0.05666),
        Coordinate(0.21095, 0.05456),
        Coordinate(0.17226, 0.05151),
        Coordinate(0.13689, 0.04755),
        Coordinate(0.10513, 0.04275),
        Coordinate(0.07725, 0.03721),
        Coordinate(0.05344, 0.03104),
        Coordinate(0.03388, 0.02439),
        Coordinate(0.01867, 0.01744),
        Coordinate(0.00786, 0.01048),
        Coordinate(0.0015, 0.0039),
        Coordinate(0, 0)
]

short_surface = [
        Coordinate(1, 0), 
        Coordinate(0.64292, 0.04256),
        Coordinate(0.5931, 0.04666),
        Coordinate(0, 0)
]

class TestSurface():
    def test_small_surface(self):
        s = Surface(short_surface)

    def test_remove_duplicate_coordinates(self):
        # make sure same number of coordinates after creation
        # from a list of Coordinates with no duplicates
        s = Surface(coordinates_no_dupe)
        assert len(s.coordinates) == len(coordinates_no_dupe)
        s = Surface(reversed(coordinates_no_dupe))
        assert len(s.coordinates) == len(coordinates_no_dupe)


        # Make sure the duplicates are removed
        s = Surface(coordinates)
        assert len(s.coordinates) == len(coordinates_no_dupe)
        assert s.coordinates == list(reversed(coordinates_no_dupe))
        s = Surface(reversed(coordinates))
        assert len(s.coordinates) == len(coordinates_no_dupe)
        assert s.coordinates == list(reversed(coordinates_no_dupe))

    def test_order_coordinates(self):
        # Make sure the duplicates are removed
        s = Surface(coordinates)
        assert s.coordinates == list(reversed(coordinates_no_dupe))
        s = Surface(reversed(coordinates))
        assert s.coordinates == list(reversed(coordinates_no_dupe))

    def test_min_max_bounds(self):
        coords = [
            Coordinate(0.6, 0  ), 
            Coordinate(0.4, 0.2),
            Coordinate(0.2, 0.3),
            Coordinate(0.1, 0.1)
        ]
        s = Surface(coords)
        assert s.max == coords[0]
        assert s.min == coords[-1]
        assert s.bounds == (Coordinate(0.1,0),Coordinate(0.6,0.3))

        # reverse coords and try again
        s = Surface(list(reversed(coords)))
        assert s.max == coords[0]
        assert s.min == coords[-1]
        assert s.bounds == (Coordinate(0.1,0),Coordinate(0.6,0.3))

    def test_length(self):
        coords = [
            Coordinate(0.1, 0), 
            Coordinate(0.3, 0),
            Coordinate(0.7, 0),
            Coordinate(0.9, 0)
        ]
        s = Surface(coords)
        assert s.length == 0.8

        coords = [
            Coordinate(0,0.1), 
            Coordinate(0,0.3),
            Coordinate(0,0.7),
            Coordinate(0,0.9)
        ]
        s = Surface(coords)
        assert s.length == 0.8

        coords = [
            Coordinate(0.0,0.0),
            Coordinate(0.4,0.3), 
            Coordinate(0.8,0.6),
            Coordinate(1.2,0.9),

        ]
        s = Surface(coords)
        assert s.length == 3*0.5

    def test_offset_around_profile(self):
        pass

    def test_offset_xy(self):
        offset_x = 5
        offset_y = 11
        offset_coord = Coordinate(5,11)
        coords = [
            Coordinate(0.0,0.0),
            Coordinate(0.4,0.3), 
            Coordinate(0.8,0.6),
            Coordinate(1.2,0.9),

        ]
        s = Surface(coords)
        s = Surface.offset_xy(s, offset_coord)
        for i in range(len(s.coordinates)):
            orig_coord = coords[i]
            surface_coord = s.coordinates[i]
            assert orig_coord.x+offset_x == surface_coord.x
            assert orig_coord.y+offset_y == surface_coord.y

        #test offset with invalid object
        with pytest.raises(TypeError):
            Surface.offset_xy(s, 1)
        
    def test_scale_to_width(self):
        def test_scale(coords, scale):
            s = Surface(coords)
            width = scale
            s = Surface.scale_to_width(s, width)
            x_diff = coords[-1].x - coords[0].x
            assert s.max.x == width
            assert s.min.x == 0
            
            expected_min_y = coords[0].y*(width/1.2)
            expected_max_y = coords[-1].y*(width/1.2)
            assert s.min.y == expected_min_y
            assert s.max.y == expected_max_y



        coords = [
            Coordinate(0.0,0.1),
            Coordinate(0.4,0.2), 
            Coordinate(0.8,0.4),
            Coordinate(1.2,0.6),
        ]
        test_scale(coords,1)
        test_scale(coords,0.05)
        test_scale(coords,1.5)
        test_scale(coords,500.1)



        coords = [
            Coordinate(-0.2,0.1),
            Coordinate(0.2,0.2), 
            Coordinate(0.6,0.4),
            Coordinate(1.0,0.6),
        ]
        test_scale(coords,1)
        test_scale(coords,0.05)
        test_scale(coords,1.5)
        test_scale(coords,500.1)


        
    # def test_trim(self):
    #     pass
        
    # def test_interpolate_new_surface(self):
    #     pass
        
    # def test_rotate(self):
    #     pass
        
    # def test_interpolate(self):
    #     pass
        
    # def test_interpolate_around_profile_dist_pct(self):
    #     pass
        
    # def test_interpolate_around_profile_dist(self):
    #     pass
    #     
