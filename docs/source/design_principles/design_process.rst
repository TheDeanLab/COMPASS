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

For our system, this resulted in a FoV of ~266 μm, meaning that we want to select lenses in our illumination path
to produce a light sheet as close to 266 μm in length as we can achieve.

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
As a general rule of thumb, one should build optical systems in Zemax element-by-element
manner instead of adding all the optical elements and trying to then optimize aspects of it.
Our general flow involves adding a lens to the system and then optimizing for either
either a focused or collimated beam, and then adding in the next lens and doing the same process until all lenses are
placed in the system. This is described in more detail below.

For our particular system, our generalized process went as follows:

    * Create a new file that will be used as our lens assembly file
    * Set aperture size in Zemax to match our laser spot size (2.4 mm).
    * Open the Zemax file associated with Lens 1, then copy and paste the surfaces into our assembly file.
    * Use the optimzation wizard
      to set a focusing optimization with the distance after L1 (f1) as the variable to find the correct position of
      L1's focus.
    .. image:: docs/source/design_principles/Images/Spotwizard.png
        :align: center
        :alt: Optimization Wizard for Spot Size

    * Run the optimization, then remove the variable for f1.
    * Open the Zemax file associated with Lens 2, then copy and paste the surfaces into our assembly after Lens 1
    * Use the Optimization Wizard to set an angular (collimation) optimization, with the distance between L1's focus
      and L2 (d1) as the variable.
    .. image:: docs/source/design_principles/Images/Anglewizard.png
        :align: center
        :alt: Optimization Wizard for Collimation

    * Optimize, then remove the variable for d1.
    * Open the Zemax file associated with Lens 3, then copy and paste the surfaces into our assembly after Lens 2.
    * Use the optimization wizard to set an *X*-focusing optimization with the distance after L3 (f3) as the variable.
    * Optimize, then remove the variable for f3.
    * Place in resonant galvo and 45 degree mirror surfaces at the location of f3.
    * Open the Zemax file associated with Lens 4, then copy and paste the surfaces into our assembly after the 45 degree
      mirror.
    * Use the optimization wizard to set an *X*-collimation optimization with the distance between the 45 degree mirror
      and L4 (d3) as the variable.
    * Optimize, then remove the variable for d3.
    * Open the Zemax file associated with our Illumination Objective, then copy and paste the surfaces into our assembly
      after L4.
    * Use the Optimization Wizard to set an *X*-focusing Optimization with the distance between L4 and the objective (d4)
      as the variable.
    * Optimize

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

Baseplate Design
-----------------

When satisfied with the results of simulations, the optimized values in Zemax can then be used to design
our baseplate. This process involves taking the optimized distances between our various optical elements
and then considering how each of those elements are mounted in a physical system, as in Zemax all of the elements are
effectively suspended in midair.

For mounting our elements, we utilize the `Polaris <https://www.thorlabs.com/navigation.cfm?guide_id=2368>`_ line from
Thorlabs, which are designed with long-term stability and alignment in mind. Each component is characterized in part by
two dowell pin alignment holes to ensure subsequent mounted elements are aligned along a specific axis.

While we are able to use most of our element mounts from the Polaris line, for the cylindrical lens L3 we needed a mount
capable of rotating the lens, which at this time is not something available from Thorlabs. In our case we designed an
additional mounting element that allows the use of a basic Thorlabs
`RSP1 rotation mount <https://www.thorlabs.com/thorproduct.cfm?partnumber=RSP1>`_, but still ensures alignment with the
other Polaris elements. The CAD file for this mount is available for download here (INSERT DOWNLOAD LINK FOR ELEMENT?)



