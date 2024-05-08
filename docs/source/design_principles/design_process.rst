.. _process-home:

###############################
General Design Process
###############################

Initial Lens Selection
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

The overarching goal of a standard optical system is to both mold light into a particular shape and direct it to a
particular location. In our case, our optical system works to convert an input gaussian beam into a thin light sheet that illuminates our sample.
There are a few sets of criteria that help guide our potential lens selection:
    * As mentioned, we want our final light sheet size to ideally cover the full FoV of our detection path (~266 um)
    * At the focus of our cylindrical lens, we want the beam spot size to stay under the size of our resonant galvo (12 mm diameter)
    * We need the focal distance between the cylindrical lens and the galvo mirror system to be greater than ~55 mm due to
      mechanical considerations of the mirror mount used
    * We want to overfill our objective, (Reasoning behind overfilling objective) , resulting in a thinner light sheet width

With these criteria in mind, we can calculate a theoretic estimate of what our beam size is after each of our lenses. We
do this by considering every pair of lenses (i.e. Lens 1 & 2, Lens 2 & 3, ...) as a sort of 4F magnification system,
where the resulting image size of the pairs is determined by the ratio of their focal lengths as follows:
(MAKE 2 FIGURES: 1. 4F SYSTEM 2. QUICK DIAGRAM OF TOTAL BEAM PATH)

Dnew = Dold*f2/f1

Essentially, we can cascade these calculations through our lenses and make sure that our choices in their focal
lengths produce our desired beam characteristics as light propagates through the system. In our case,
our chosen system featured 4 lenses from Thorlabs:
`L1 = 30 mm <https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-030-A>`_,
`L2 = 80 mm <https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-080-A>`_,
`L3 (Cylindrical) = 75 mm <https://www.thorlabs.com/thorproduct.cfm?partnumber=ACY254-075-A>`_, and
`L4 = 250 mm <https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-250-A>`_.

We can then take these lens choices and load them into Zemax Opticstudio to verify the characterisitcs of our system.

Zemax Simulation Setup Process
______________________________

With our chosen lens in mind, we can download Zemax files associated with each lens directly from Thorlabs website (ADD IN FIGURE)
and set up our simulation. Here, we use Zemax as a tool to find the optimal placement of all the lenses of our system
based on whether or not the input beam should be focusing or collimated after each lens.
As a general rule of thumb, one should build optical systems in zemax element-by-element
manner instead of adding all the optical elements and trying to then optimize aspects of it.
Our general flow involves adding a lens to the system and then optimizing for either
either a focused or collimated beam, and then adding in the next lens and doing the same process until all lenses are
placed in the system. This is described in more detail below.

For our particular system, our generalized process went as follows:

    * Create a new file that will be used as our lens assembly file
    * Set aperture size in Zemax to match our laser spot size (2.4 mm).
    * Open the Zemax file associated with Lens 1, then copy and paste the surfaces into our assembly file.
    * Use the optimzation wizard (ADD IN FIGURE OF OPTIMZATION WIZARD FOR BOTH SPOT SIZE AND ANGULAR OPT)
      to set a focusing optimization with the distance after L1 (f1) as the variable to find the correct position of
      L1's focus.
    * Run the optimization, then remove the variable for f1.
    * Open the Zemax file associated with Lens 2, then copy and paste the surfaces into our assembly after Lens 1
    * Use the Optimization Wizard to set an angular (collimation) optimization, with the distance between L1's focus
      and L2 (d1) as the variable.
    * Optimize, then remove the variable for d1.
    * Open the Zemax file associated with Lens 3, then copy and paste the surfaces into our assembly after Lens 2.
    * Use the optimization wizard to set an X-focusing optimization with the distance after L3 (f3) as the variable.
    * Optimize, then remove the variable for f3.
    * Place in resonant galvo and 45 degree mirror surfaces at the location of f3.
    * Open the Zemax file associated with Lens 4, then copy and paste the surfaces into our assembly after the 45 degree
      mirror.
    * Use the optimization wizard to set an X-collimation optimization with the distance between the 45 degree mirror
      and L4 (d3) as the variable.
    * Optimize, then remove the variable for d3.
    * Open the Zemax file associated with our Illumination Objective, then copy and paste the surfaces into our assembly
      after L4.
    * Use the Optimization Wizard to set an X-focusing Optimization with the distance between L4 and the objective (d4)
      as the variable.
    * Optimize

Zemax Simulation Analysis
______________________________

Within Zemax, there are numerous analysis tools available to investigate different characteristics of optical systems.
Our analysis will primarily be guided by the Geometric Image Analysis, Huygen's PSF, and Through Focus Spot tools.
Zemax innately uses geometric ray tracing, which is a ; however, as our output light sheet size approaches the
diffraction limit, we need to consider the effects of diffraction in our analysis. The Huygen's PSF analysis tool is how we 