import cadquery as cq


# after the following translates, z=0 on the upper face of the PCB, y=0 on the
# outer edge of the PCB and x=0 on the centerline of the connector, and the
# connector points outwards in the +y direction

part = (cq
        .importers.importStep('./c-5449692-1-a-3d.stp')
        .translate((0, 0, 11.56))
        .rotate((0, 0, 0,), (1, 0, 0), -90)
        .translate((0, 0, 0.4))
        )
