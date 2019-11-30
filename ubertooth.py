import cadquery as cq
from types import SimpleNamespace as sn
import sma_conn
import usb_conn


mounting_holes = sn(
    diam = 1.5748
    , locations = (
        (50.8, -38.1)
        , (101.6, -38.1)
        , (101.6, -53.34)
        , (50.8, -53.34)
    )
)
board_outline = (
    (48.768, -36.3728)
    , (103.632, -36.3728)
    , (106.934, -39.6748)
    , (106.934, -51.7652)
    , (103.632, -55.0672)
    , (48.768, -55.0672)
    , (45.466, -51.7652)
    , (45.466, -39.6748)
)
u4 = sn(
    centre = (86.36, -45.72)
    , size = (6.10108 * 2, 6.10108 * 2, 1)
    , rotate = 135  # degrees
)
board_thick = 1.6
usb_conn_pos = (
    board_outline[2][0]
    , (board_outline[2][1] + board_outline[3][1]) / 2
    , board_thick
)
sma_conn_pos = (
    board_outline[6][0]
    , (board_outline[6][1] + board_outline[7][1]) / 2
    , board_thick
)

part = (cq
    .Workplane("XY")
    .setName("base")
    .transformed(offset=(0, 0, board_thick))
    .setName("top")
    .copyWorkplaneFromNamed("base")
    .polyline(board_outline)
    .close()
    .extrude(board_thick)
    .copyWorkplaneFromNamed("top")
    .pushPoints(mounting_holes.locations)
    .hole(mounting_holes.diam)
    .union(
        usb_conn.part
        .rotate((0, 0, 0), (0, 0, 1), -90)
        .translate(usb_conn_pos)
    )
    .union(
        sma_conn.part
        .rotate((0, 0, 0), (0, 0, 1), 90)
        .translate(sma_conn_pos)
    )
    .copyWorkplaneFromNamed("top")
    .center(*u4.centre)
    .transformed(rotate=(0, 0, u4.rotate))
    .box(*u4.size, centered=(True, True, False))
)
