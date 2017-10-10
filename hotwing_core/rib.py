from .profile import Profile
from .utils import isect_line_plane_v3
from .coordinate import Coordinate


class Rib():
    """
    A Rib contains a Profile and other attributes to determine the size and position.

    Args:
        airfoil
        scale
        xy_offset
        top_sheet
        bottom_sheet
        front_stock
        tail_stock
        rotate
        rotate_pos
    """
    
    def __init__(self, airfoil, scale=None, xy_offset=None, top_sheet=0,
                 bottom_sheet=0, front_stock=0, tail_stock=0, rotate=0, rotate_pos=0.5):
        if isinstance(airfoil, Profile):
            self.airfoil = airfoil
        else:
            self.airfoil = Profile(airfoil)

        self.scale = scale
        self.xy_offset = xy_offset
        self.top_sheet = top_sheet
        self.bottom_sheet = bottom_sheet
        self.front_stock = front_stock
        self.tail_stock = tail_stock
        self.rotate = rotate
        self.rotate_pos = rotate_pos

    @property
    def profile(self):
        """
        Returns a copy of the rib profile after scaling and offsets
        """
        p = Profile.copy(self.airfoil)
        if not self.scale is None:
            p = Profile.scale(p, self.scale)
        if not self.rotate == 0:
            x_bounds = p.x_bounds
            x_len = x_bounds[1] - x_bounds[0]
            mid_point = x_bounds[0] + x_len * self.rotate_pos
            p = Profile.rotate(Coordinate(mid_point, 0), p, -self.rotate)
        if self.xy_offset:
            p = Profile.offset_xy(p, self.xy_offset)
        return p

    @property
    def sheeted_profile(self):
        """
        Document
        """
        p = self.profile
        if self.top_sheet or self.bottom_sheet:
            p = Profile.offset_around_profiles(
                p, -self.top_sheet, -self.bottom_sheet)
        return p

    @classmethod
    def interpolate_new_rib(cls, r1, r2, dist_between,
                            dist_interp, points=200):
        """
        Document
        """
        p = Profile.interpolate_new_profile(
            r1.profile, r2.profile, dist_between, dist_interp, points)
        rib = cls(p)
        rib.top_sheet = r1.top_sheet
        rib.bottom_sheet = r1.bottom_sheet
        rib.front_stock = r1.front_stock
        rib.tail_stock = r1.tail_stock
        return rib
