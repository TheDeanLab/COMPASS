.. _process-home:

###############################
Imaging Process
###############################

Visualization of Axes Mapping
______________________________


In our system we essentially have 5 different translation stages at work: the standard x,y, and z axes, an additional
stage along the z axis to control the focus of the detection path (f), and and axis associated with the piezo positioned
such that its normal is 60.5 degrees away from the y-axis.

.. image:: Images/PhysicalAxesMaps.png
    :align: center
    :alt: Layout of how the axis of the system are mapped

Finding the Focus
______________________________


Minimizing Spherical Aberrations
______________________________


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

.. image:: Images/ChangingCorrectionCollar.png
    :align: center
    :alt: Correction collar effects

As a quick example of what an image of a z-projection could look like before and after trying to correct for spherical aberration is shown
below. Here, one can see in the top panel that the bead features are essentially smoothed out and fuzzy due to
aberrations, while in the bottom panel with adjustments made to the correction collar the beads appear much cleaner and
focused.

.. image:: Images/SphericalExample.png
    :align: center
    :alt: Before and after of adjusting in Z-projections after adjusting the correction collar

###############################
Image Post-Processing
###############################

Deskewing
______________________________


With an image stack acquired, some post processing is still required in order to remove the effects of shearing in our
images. The root of this shearing is due to the angled method in which our sample is mounted and similarly, the angled path that
the sample moves as the piezo is scanned. A basic visual idea of how deskewing affects the resulting image is shown
below for 100 nm fluorescent beads. Here before deskewing for the same image plane (yz), the beads appear to be
stacked in a straight line but oriented along an angle, which is not the most accurate representation of our system.
On the deskewed image on the right, one can see that the beads are now properly angled correspond to our piezo angle
mount, and that the PSFs of the beads is now correctly aligned along the z axis.

.. image:: Images/BeadDeskewExample.png
    :align: center
    :alt: Difference between an image set of 100 nm bead before deskewing (left) and after (right)

To do this deskew processing, we utilize custom-built python code via Jupyter notebooks (HAVE LINK TO NOTEBOOK
DOWNLOAD?). The user needs to provide the correct file path to the .tif image stack collected via navigate, as well
as the parameters of the imaging system like z-step size, xy pixel size, and the angle that the images should be
deskewed over. In our case, our deskew angle is equivalent to 90-60.5 degrees, where 60.5 degrees corresponds to the
difference between the normal of our angle mount and the y-axis. If this value is unknown, one can use different
values for the deskew angle until the bead PSFs are correctly aligned along the z-axis and not angled.

Rescaling
______________________________


With a properly deskewed image set, the next step is to work to rescale the image set dimensions to properly
represent the physical pixel sizes in every dimension. The first step to doing this involves going to the
properties tab of the image stack (Image-> Properties) and adjusting each dimension such that the x and y values
correspond to the xy pixel size based on the system magnification and camera sensor size, and the z value
corresponding to the z step size. While using our angled piezo configuration, the z step size :math:`\delta _z`
doesn't directly correspond to the step size chosen for the piezo via navigate. Depicted graphically below, the
actual z step size is related to both the angle for the piezo and the piezo step size :math:`\delta _p` .

.. image:: Images/CalculatingZstep.png
    :align: center
    :alt: Depiction of how :math:`\delta _z` is derived

An example of what these values can be is shown below, where for our camera and system magnification our xy pixel
size is the same at 130 nm, while we used a piezo step size of 200 nm. Using the relationship shown above to find
:math:`\delta _z`, we find our actual z-step size is roughly 98.5 nm.