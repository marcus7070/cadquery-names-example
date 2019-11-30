import cadquery as cq


# after the following translates, z=0 on the upper face of the PCB, y=0 on the
# outer edge of the PCB and x=0 on the centerline of the connector, and the
# connector points outwards in the +y direction

part = (cq
        .importers.importStep('./480371000.stp')
        .translate((0, 0, 5.4))
        .rotate((0, 0, 0), (1, 0, 0), 90)
        .rotate((0, 0, 0), (0, 0, 1), 180)
        .translate((0, 0, 0.82))
        )
