.. _process-home:

###############################
General Design Process
###############################

Lens Selection
-------------------
Prior to starting optical simulations in Zemax, it's convenient to start with straightforward
calculations to determine which lenses to use in the optical train to achieve the desired field of view (FoV) for your
detection path.

In our case, our detection path consisted of a 400 mm tube lens and a Nikon 25x/1.1 NA immersion detection objective.
To determine the target FoV, start with determining the final magnification of the system using the ratio of the focal lengths of the tube lens (f_TL) and the detection objective (f_dobj): (FORMAT LATER)

Mag = f_TL/f_DObj

From there, determine the resulting FoV of the detection path by dividing the total camera sensor size (in mm) by the magnification, and then converting into microns:

FoV (in microns) = (W_Sensor/Mag)*1000

For our system, this resulted in a FoV of ~266 microns, meaning that we want to select lenses in our illumination path
to produce a light sheet as close to 266 microns in length as we can achieve.

Now, we can calculate a theoretic estimate of what our beam dimensions will be after every lens in our optical train
starting (MAKE 2 FIGURES: 1. 4F SYSTEM 2. QUICK DIAGRAM OF TOTAL BEAM PATH)