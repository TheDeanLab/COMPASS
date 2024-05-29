.. _process-home:

###############################
General Design Process
###############################

Initial Lens Selection
-------------------
Prior to starting optical simulations in Zemax, it's convenient to start with straightforward
calculations to determine which lenses to use in the optical train to achieve the desired field of view (FoV) for your
detection path.

In our case, our detection path consisted of a 400 mm tube lens and a Nikon 25x/1.1 numerical aperture (NA) immersion detection objective.
To determine the target FoV, start with determining the final magnification (M) of the system using the ratio of the focal
lengths of the tube lens (*f*:subscript:`TL`) and the detection objective (*f*:subscript:`DO`):

M = *f*:subscript:`TL`/*f*:subscript:`DO`

From there, determine the resulting FoV of the detection path by dividing the total camera sensor size (in mm) by the magnification, and then converting into microns:

FoV (in microns) = (W :subscript:`Sensor` /M)*1000

For our system, this resulted in a FoV of ~266 :math:`\mu m`, meaning that we want to select lenses in our illumination path
to produce a light sheet as close to 266 :math:`\mu m` in length as we can achieve.

The overarching goal of a standard optical system is to both mold light into a particular shape and direct it to a
particular location. In our case, our optical system works to convert an input gaussian beam into a thin light sheet that illuminates our sample.
There are a few sets of criteria that help guide our potential lens selection:
    * As mentioned, we want our final light sheet size to ideally cover the full FoV of our detection path (~266 μm)
    * At the focus of our cylindrical lens, we want the beam spot size to stay under the size of our resonant galvo (12 mm diameter)
    * We need the focal distance between the cylindrical lens and the galvo mirror system to be greater than ~55 mm due to
      mechanical considerations of the mirror mount used
    * We want to overfill our objective, (Reasoning behind overfilling objective) , resulting in a thinner light sheet width

With these criteria in mind, we can calculate a theoretic estimate of what our beam size is after each of our lenses. We
do this by considering every pair of lenses (i.e. Lens 1 & 2, Lens 2 & 3, ...) as a sort of 4F magnification system,
where the resulting image size of the pairs is determined by the ratio of their focal lengths (*f*:subscript:`n`) as follows:


.. image:: docs/source/design_principles/Images/4FSystem.png
    :align: center
    :alt: 4F System Diagram

Essentially, we can cascade these calculations through our lenses and make sure that our choices in their focal
lengths produce our desired beam characteristics as light propagates through the system. In our case,
our chosen system featured 4 lenses from Thorlabs:
`L1 = 30 mm <https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-030-A>`_,
`L2 = 80 mm <https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-080-A>`_,
`L3 (Cylindrical) = 75 mm <https://www.thorlabs.com/thorproduct.cfm?partnumber=ACY254-075-A>`_, and
`L4 = 250 mm <https://www.thorlabs.com/thorproduct.cfm?partnumber=AC254-250-A>`_.

We can then take these lens choices and load them into Zemax Opticstudio to verify the characterisitcs of our system.

.. image:: docs/source/design_principles/Images/MonolithV1p1_CylindricalLensSchematic_V2.png
    :align: center
    :alt: Optical System Diagram

Zemax Simulation Setup Process
______________________________

With our chosen lens in mind, we can download Zemax files associated with each lens directly from Thorlabs website
and set up our simulation.

.. image:: docs/source/design_principles/Images/ThorlabsExample.png
    :align: center
    :alt: Thorlabs Zemax Download

Here, we use Zemax as a tool to find the optimal placement of all the lenses of our system
based on whether or not the input beam should be focusing or collimated after each lens.
As a general rule of thumb, one should build optical systems in Zemax in an element-by-element
manner instead of adding all the optical elements and trying to then optimize aspects of it.
Our general flow involves adding a lens to the system and then optimizing for either
either a focused or collimated beam, and then adding in the next lens and doing the same process until all lenses are
placed in the system. This is described in more detail below.

For our particular system, our generalized process went as follows:

    1. Create a new file that will be used as our lens assembly file
    2. Set aperture size in Zemax to match our laser spot size (2.4 mm).
    3. Open the Zemax file associated with Lens 1, then copy and paste the surfaces into our assembly file.
    4. Use the optimzation wizard to set a focusing optimization with the distance after L1 (f1) as the variable to find
       the correct position of L1's focus.
    .. image:: docs/source/design_principles/Images/Spotwizard.png
        :align: center
        :alt: Optimization Wizard for Spot Size

    5. Run the optimization, then remove the variable for f1.
    6. Open the Zemax file associated with Lens 2, then copy and paste the surfaces into our assembly after Lens 1
    7. Use the Optimization Wizard to set an angular (collimation) optimization, with the distance between L1's focus
       and L2 (d1) as the variable.
    .. image:: docs/source/design_principles/Images/Anglewizard.png
        :align: center
        :alt: Optimization Wizard for Collimation

    8. Optimize, then remove the variable for d1.
    9. Open the Zemax file associated with Lens 3, then copy and paste the surfaces into our assembly after Lens 2.
    10. Use the optimization wizard to set an *X*-focusing optimization with the distance after L3 (f3) as the variable.
    11. Optimize, then remove the variable for f3.
    12. Place in resonant galvo and 45 degree mirror surfaces at the location of f3.
    13. Open the Zemax file associated with Lens 4, then copy and paste the surfaces into our assembly after the 45 degree
        mirror.
    14. Use the optimization wizard to set an *X*-collimation optimization with the distance between the 45 degree mirror
        and L4 (d3) as the variable.
    15. Optimize, then remove the variable for d3.
    16. Open the Zemax file associated with our Illumination Objective, then copy and paste the surfaces into our assembly
        after L4.
    17. Use the Optimization Wizard to set an *X*-focusing Optimization with the distance between L4 and the objective (d4)
        as the variable.
    18. Optimize

Zemax Simulation Analysis
______________________________

Within Zemax, there are numerous analysis tools available to investigate different characteristics of optical systems.
Our analysis will primarily be guided by the Geometric Image Analysis, Huygen's PSF, and Through Focus Spot tools.
Zemax innately uses geometric ray tracing in most all of its operations like beam optimization.
This is generally-acceptable for most optical systems; however, as our output light sheet size approaches the
diffraction limit ( 0xCE /(2NA)), we need to also consider the effects of diffraction in our analysis.

The Huygen's PSF analysis tool is how we incorporate effects of diffraction into our analysis; where we anticipate results from this analysis to be more
in-line with what would be seen on the physical system. Based on the cross section of our Huygen's PSF analysis, we can
see that our expected Full-Width Half-Max (FWHM) of the light sheet is expected to lie somewhere around 0.382 μm.

Through Focus Spot analysis allows us to essentially see the evolution of the light sheet through the point of focus,
where we can then estimate a sort of range where we expect the width of the light sheet to be thin enough for our
imaging purposes, where the maximum usable light sheet width is the FWHM at the focus multiplied by sqrt(2).

Zemax Tolerancing Analysis
-----------------

When considering building physical systems using Zemax, an additional analysis tool known as tolerancing becomes
increasingly important. Tolerancing is essentially the process of understanding how sensitive different elements in a
system are to various perturbations. This can be along the lines of how sensitive the collimation or magnification of a
4F system is to small physical displacements of the two lenses that comprise it. Similarly to Zemax's optimization
process, tolerancing also utilizes a merit function. This merit function is fully customizable, and serves to define
how well a particular system is performing. In the case of our system, we chose our merit function to factor in both the
size and displacement of the output light sheet relative to the perfectly optimized instance.

.. image:: docs/source/design_principles/Images/ToleranceMF.png
    :align: center
    :alt: Tolerance Merit Function



Baseplate Design
-----------------

When satisfied with the results of simulations, the optimized values in Zemax can then be used to design
our baseplate. This process involves taking the optimized distances between our various optical elements
and then considering how each of those elements are mounted in a physical system, as in Zemax all of the elements are
effectively suspended in midair like below:

.. image:: docs/source/design_principles/Images/CylindricalDesign6_30_90_75_250flip4.png
    :align: center
    :alt: Zemax Elements Floating

For mounting our elements, we utilize the `Polaris <https://www.thorlabs.com/navigation.cfm?guide_id=2368>`_ line from
Thorlabs, which are designed with long-term stability and alignment in mind. Each component is characterized in part by
two dowell pin alignment holes to ensure subsequent mounted elements are aligned along a specific axis. In the baseplate
design, we are essentially deciding on the location for the mounting holes of the Polaris posts we're using, which is
not the same as the locations of the elements themselves from Zemax.

.. image:: docs/source/design_principles/Images/PolarisScheme.png
    :align: center
    :alt: Polaris Scheme

While we are able to use most of our element mounts from the Polaris line, for the cylindrical lens L3 we needed a mount
capable of rotating the lens, which at this time is not something available from Thorlabs. In our case we designed an
additional mounting element that allows the use of a basic Thorlabs
`RSP1 rotation mount <https://www.thorlabs.com/thorproduct.cfm?partnumber=RSP1>`_, but still ensures alignment with the
other Polaris elements. The CAD file for this mount is available for download here (INSERT DOWNLOAD LINK FOR ELEMENT?)

.. image:: docs/source/design_principles/Images/RotationMount.png
    :align: center
    :alt: Rotation Mount Adapter

With the method in which each of the elements needs to be mounted decided upon, we then went over the product schematics
for each mount to understand the z-displacement that they impart upon the element mounted within them relative to where
the Polaris post central mounting hole would need to be. This idea is depicted below, where when considering how to
space two lenses from each other there is essentially three components to take into account:
    1. The distance between the lenses decided from simulation
    2. The thickness of the lenses themselves
    3. The distance between the center of the Polaris post and the start of the lens in the mount

.. image:: docs/source/design_principles/Images/PostSpacingConsiderations.png
    :align: center
    :alt: Post Spacing Considerations


Once the locations of the mounting holes were determined, we used Autodesk Inventor to design the full baseplate. The
baseplate is essentially just a mounting hole and the two dowel pin holes for every element, as well as four mounting
holes for the baseplate itself. These four baseplate mounting holes were spaced in increments of inches such that the
baseplate can either be screwed directly into an optical breadboard table or into additional posts that can keep the
assembly at a desired height.

.. image:: docs/source/design_principles/Images/Baseplate.png
    :align: center
    :alt: Baseplate

With the baseplate designed, our final assembly for our illumination path looks as follows:

.. image:: docs/source/design_principles/Images/BaseplateAssembly_Iso.png
    :align: center
    :alt: Baseplate Assembly Iso

.. image:: docs/source/design_principles/Images/BaseplateAssembly_Top.png
    :align: center
    :alt: Baseplate Assembly Top

Note on Difference in Simulated and Physical Coordinate Definitions
______________________________

It should be noted briefly that when discussing our physical microscope systems, the definitions for the coordinate axes
is different than that of our simulations. This is due to a difference in standardized definitions for the axes in our
previous systems and how Zemax defines these same axes. This difference is depicted in the picture below:

.. image:: docs/source/design_principles/Images/CoordinateSchemeChange.png
    :align: center
    :alt: Difference in coordinate axes for simulation and physical setup

Physical Assembly Process
-----------------

Our baseplate design was made with ease of assembly in mind. The basic process involves aligning Polaris posts with
dowell pins and screwing them using 1/4"-20 Screws in at the predetermined hole locations on the breadboard.
This general process is depicted below:

.. image:: docs/source/design_principles/Images/BaseplateAssembly.png
    :align: center
    :alt: General process to place posts on baseplate

We used various different Polaris post sizes in our assembly based on what element was being mounted on them.
Also worth noting is that three elements are designed to be placed on 0.5" posts and as such require 0.5" post holders at
their designated locations: the L1 focus iris, the rectangular aperture after L2, and the ND filter after the 45 degree mirror.
The overal breakdown of which size posts went with each hole location is listed below:

.. image:: docs/source/design_principles/Images/PostHeightBreakdown.png
    :align: center
    :alt: Schematic of which holes use which post heights

To either mount the baseplate onto an optical table or onto separate posts, the process is similar in that
just requires screwing 1/4"-20 screws into either an optical breadboard or onto separate posts at the four corner holes.

.. image:: docs/source/design_principles/Images/BaseplateAssembly_Corners.png
    :align: center
    :alt: General process to place posts on baseplate corners


Finding the Focus
-----------------

Minimizing Spherical Aberrations
-----------------

Once the system has been assembled to the point of being able to take image stacks, the process of
minimizing the effects of spherical aberrations can begin. Spherical aberrations are typically
introduced into optical systems due to the surface curvature of different lens elements. This
type of aberration typically presents itself visually as a sort of stretching or bending of the focus
of light in the system. Certain microscope objectives, such as the Nikon 25x/1.1 NA that we employ in this setup,
have a built-in collar that can be adjusted to minimize spherical aberration (PICTURE).

In our system, we expect the effects of spherical aberrations to be along the axis of our detection path (defined
as z in our imaging scheme). In order to visualize these effects and adjust the correction collar of our objective
to mitigate them, we employ a process of taking a z-stack of fluorescent beads suspended in agarose
and using ImageJ to quickly process those images.

    1. Take a z-stack within Navigate of your sample
    2. Open up the z-stack within ImageJ
    3. Reslice the z-stack (Image -> Stacks -> Reslice)
    4. Do a maximum intensity project of the resliced stack (Image -> Stacks -> Z-Projection)
    5. Take note if spherical aberration is present in the projected image.
    6. If spherical aberration is still present, make slight adjustments to the objective
       correction collar and repeat Steps 1-5.

As a note, observing the camera live-feed via Navigate's "Continuous Scan" mode while adjusting the correction collar
can help to get in the general vicinity of the correct placement of the correction collar. An example of how change in
the correction collar affect live images are shown below for fluorescent beads. Aiming to get to get the beads near the
expected light sheet position to be as in-focus as possible is a general guide for what direction to move the collar;
however, true correction needs to be done with the z-projection method mentioned above.

.. image:: docs/source/design_principles/Images/ChangingCorrectionCollar.png
    :align: center
    :alt: Correction collar effects

As a quick example of what an image of a z-projection could look like before and after trying to correct for spherical aberration is shown
below. Here, one can see in the top panel that the bead features are essentially smoothed out and fuzzy due to
aberrations, while in the bottom panel with adjustments made to the correction collar the beads appear much cleaner and
focused.

.. image:: docs/source/design_principles/Images/SphericalExample.png
    :align: center
    :alt: Before and after of adjusting in Z-projections after adjusting the correction collar



