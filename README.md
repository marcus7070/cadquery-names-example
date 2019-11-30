### CadQuery-names example

#### CadQuery-names

Source is at https://github.com/marcus7070/cadquery/tree/marcus7070/names

#### Why

Often when using CadQuery I've wanted to create a feature on a plane, and then at a later point refer back to that same plane, but the intermediate steps have obscured the plane such that normal selectors are now difficult to use. A common example is whipping up a quick model of a PCB with a bunch of connectors. You would like to frequently select both the top and the bottom faces of the PCB for drawing connectors or parts, but each connector would change the `.faces(` arguments required to select the PCB face. 

There is several workarounds for this. In particular `nearestToPointSelector` can almost always get you what you need, but I thought it would feel more intuitive to name an object and refer back to it.

With that in mind, I added a `name` attribute to CQ and Workplane classes, and `setName()` and `findNamed()` methods to CQ objects such that the name can be set without breaking chained method calls. I might have to be more explicit with the `findNamed()` method name, that kind of looks like it searches all local objects or something when it really just searches the parent chain. 

I'm thinking perhaps the `findNamed()` method can be used for other functions at a later date.

`copyWorkplane()` takes an object and copies it's workplane to an object generated by `self.newObject()`.

`copyWorkplaneFromNamed()` combines all the above to find a named object and copy it's workplane.

#### Ubertooth

I found a simple example to show where `copyWorkplaneFromNamed()` would make modelling much more simple. 

The Ubertooth has an irregularly shaped PCB and 2 relatively large connectors. It's open source with a BOM included, so we can go to the manufacturers and get the STEP files for those connectors directly. Unfortunately the STEP file for the SMA connector in the BOM has some modelling errors (if only they used CadQuery, that would never have happened), so instead I've used a similar jack from TE Connectivity. I can copy the dimensions of the board and the positions of the mounting holes straight out of KiCAD, which is why it has that odd offset. 

To do this job without named objects and copied workplanes, I probably would have used a [CadQuery plugin](https://cadquery.readthedocs.io/en/latest/extending.html#extending-cadquery-plugins) that created a workplane at the correct offset. 
