.. _process-home:

###############################
Physical Assembly
###############################

Baseplate Assembly Process
______________________________


Our baseplate design was made with ease of assembly in mind. The basic process involves aligning Polaris posts with
dowell pins and screwing them using 1/4"-20 Screws in at the predetermined hole locations on the breadboard.
This general process is depicted below:

.. image:: Images/BaseplateAssembly.png
    :align: center
    :alt: General process to place posts on baseplate

We used various different Polaris post sizes in our assembly based on what element was being mounted on them.
Also worth noting is that three elements are designed to be placed on 0.5" posts and as such require 0.5" post holders at
their designated locations: the L1 focus iris, the rectangular aperture after L2, and the ND filter after the 45 degree mirror.
The overal breakdown of which size posts went with each hole location is listed below:

.. image:: Images/PostHeightBreakdown.png
    :align: center
    :alt: Schematic of which holes use which post heights

To either mount the baseplate onto an optical table or onto separate posts, the process is similar in that
just requires screwing 1/4"-20 screws into either an optical breadboard or onto separate posts at the four corner holes.

.. image:: Images/BaseplateAssembly_Corners.png
    :align: center
    :alt: General process to place posts on baseplate corners

Mounting Lenses
______________________________

Mounting lenses into a Polaris lens mount and onto an associated post is a fairly straightforward process. The
general flow is shown in the image below, where first the flatter face of the desired lens should be placed such that
it is touching the metal boundary on the lens mount itself. Then the lens should be fixed into place by screwing the
lock screw on the top of the lens mount. With the lens secured in the mount, then two dowel pins should be placed in
the appropriate holes on the Polaris post, and then the lens mount should be placed such that the two holes on the
lens mount align with the pins on the Polaris post. Then the lens mount should be anchored into place by screwing it
into the Polaris post.

.. image:: Images/LensMounting.png
    :align: center
    :alt: General process for mounting a lens into a Polaris holder and onto a post


The Piezo Angle Mount
______________________________

We designed a custom angled mount for a piezo in order to be able to scan our sample easily between our two
objectives by translating a single motorized unit (in this case the piezo), instead of having to calculate and
program the movement of two translation stages in tandem for both the y and z directions. The anatomy of our angled
mount is broken down in the figure below, where there are four translation stage mounting holes to attach the unit to
an ASI translation stage, nine Piezo mounting holes (LINK TO PIEZO UNIT?) that correspond to the mounting scheme of
our piezo unit, as well as four through-holes and a window for ease of access for the mounting process. We provide
the CAD files for this mount HERE (LINK TO DOWNLOAD FOR MOUNT), and have had success in using both 3D printed and
aluminum machined versions of the unit. It's recommended to first mount the angle mount onto the translation stage
unit before mounting the piezo on the angle mount to ensure access to all the through-holes.

.. image:: Images/AnglemountAnatomy.png
    :align: center
    :alt: Breakdown of our custom angle piezo angle mount

The installation of our custom angled piezo mount is designed to be directly compatible with ASI translation stages.
ASI translation stages feature M6 hole pairs that are spaced along the length of the translation stage at intervals
dependent on the specific stage one is using. The mounting process involves aligning these 4 holes with 4 of the M6
holes on the translation stage and screwing them in. For ease of screwing in the base, there are four through holes on
the angled face of the mount shown in B that a screwdriver is able to pass directly through to screw as shown in C. An
alternative method of mounting is shown in D, where the window on the back of the angle mount is able to be screwed
through as well.

.. image:: Images/Anglemount.png
    :align: center
    :alt: General process for mounting our piezo angle mount onto an ASI translation stage

Sample Holder Design
______________________________


Our sample holder design is built for using fixed cells on a 5 mm coverslip, and is shown below. The design features a
clamp-like method of securing the 5 mm coverslip in place, where the coverslip rests in an inset region and the clamp
is screwed in via an M1.6 screw in the back of the holder. All associated files for this design and
other custom parts can be found HERE (INSERT LINK TO DOWNLOADS PAGE).

.. image:: Images/S_SampleHolderAssembly.png
    :align: center
    :alt: 5 mm coverslip sample holder design

Assembling the Magnetic Sample Mount
______________________________


As a safeguard for the risk of the sample crashing into either the illumination or detection objective during sample
positioning or imaging, we opted to incorporate a magnetic mount for our sample holder. We use a Thorlabs KBT1X1T and
KBB1X1 as our magnetic mount pair, and then mount our sample holder onto the KBT1X1T using a custom adapter (PROVIDE
LINK TO ADAPTER).

.. image:: Images/MagneticMountSampleHolder.png
    :align: center
    :alt: Basic assembly of magnetic sample holder mount

Wiring Diagram
______________________________


###############################
Hardware
###############################

Note on Difference in Simulated and Physical Coordinate Definitions
______________________________

It should be noted briefly that when discussing our physical microscope systems using Navigate software, the definitions
for the coordinate axes is different than that of our simulations. This is due to a difference in standardized
definitions for the axes in our previous systems and how Zemax defines these same axes. This difference is depicted in
the picture below:

.. image:: Images/CoordinateSchemeChange.png
    :align: center
    :alt: Difference in coordinate axes for simulation and physical setup

Visualization of Axes Mapping
______________________________

In our system we essentially have 5 different translation stages at work: the standard x,y, and z axes, an additional
stage along the z axis to control the focus of the detection path (f), and and axis associated with the piezo positioned
such that its normal is 60.5 degrees away from the y-axis.

.. image:: Images/PhysicalAxesMaps.png
    :align: center
    :alt: Layout of how the axis of the system are mapped

Piezo Setup & Troubleshooting
______________________________

On the PCI Board, connect the positive and negative wires  to the corresponding analog output (AO) you want, in our case
we used AO 0, so we connected the positive wire to pin 10 and the ground to pin 11, then plug the BNC cable connected to
those wires into the EXT IN input on the Tiger controller panel corresponding to the piezo.

.. image:: Images/DevicePinouts.png
    :align: center
    :alt: How to find the Device Pinout panel

Plug the piezo cable into the PIEZO input on the Tiger controller panel corresponding to the piezo.

Verify the range of the piezo in the tiger controller software with the command "5 cca x?"

    At first, ours output the following:
        | :A  Q:P1
        | 23 P 1 100um RANGE
        | 24 P 2 200um RANGE
        | 35 P S 150um RANGE
        | 36 P 3 300um RANGE
        | 37 P 5 500um RANGE
        | 34 P f 50um RANGE
        | 25 P 4 350um RANGE:N-4

This tells us that our Piezo (Panel 5/Q) corresponded to P1 or a 100 um range, but ASI requires the piezo needed to be
set to  a 50 um range to be able to be intitialized instead. To change this, we used the command "5 cca x = 34" and
power cycled the controller.

    Then our output became:
       | :A  Q:Pf
       | 23 P 1 100um RANGE
       | 24 P 2 200um RANGE
       | 35 P S 150um RANGE
       | 36 P 3 300um RANGE
       | 37 P 5 500um RANGE
       | 34 P f 50um RANGE
       | 25 P 4 350um RANGE:N-4

Now we can see that the piezo is set to the correct range (Pf).
With that verified, now confirm that the voltage output from the PCI Board is working:

| 1. Put the BNC cable input currently in EXT IN on the Tiger control panel into the input of the oscilloscope instead.
| 2. Go to the test panels for the PCI board in NI MAX.

.. image:: Images/TestPanels.png
    :align: center
    :alt: How to find the Test Panels panel

| 3. Set the voltage mode to sinewave generation.
| 4. Set the voltage range to be between 0 to 10 V.
| 5. Set the frequency to a desired value (we ended up setting it pretty high at 10000 Hz for ease of viewing on the oscilloscope).
.. image:: Images/TestPanelConfiguration.png
    :align: center
    :alt: How to find the Test Panels panel

With the voltage output of the PCI board verified, plug the PCI Board voltage cable output back into the EXT IN slot and
verify that the position output of the Piezo reads similarly on the oscilloscope:
    1. Plug a BNC Cable into the SENSOR OUT connection on the tiger controller panel.
    2. Plug the other end of that cable into the oscilloscope.
    3. Verify that a sinewave output is seen on the oscilloscope.

If the PCI Board voltage is working as intended but the piezo position output doesn't seem to work, try ensuring that
the piezo is set in `External Input mode, and not Controller Input mode <https://asiimaging.com/docs/commands/pm>`_:
    1. Use the "PM Q?" (Our piezo corresponds to Q) command:
        - the output was "Q = 0" originally, telling us that it's in Controller Input mode
    2. Use the "PM Q = 1" command to set the piezo into External Input mode:
        - now the output of "PM Q?" is "Q = 1"

Another important step is to ensure that the configuration file associated with Navigate is appropriately set up for your piezo.
This involves setting the correct axis and voltage-to-distance mapping for the piezo. As an example our configuration file
for Navigate looks like the following for setting up our piezo:

.. image:: Images/Piezo_Config.png
    :align: center
    :alt: How to find the Test Panels panel






###############################
Parts List
###############################

A breakdown spreadsheet of all components used in this build is viewable under the COMPASS V1 Sample Scanning tab `here
<https://365utsouthwestern-my
.sharepoint.com/:x:/g/personal/john_haug_utsouthwestern_edu/EanyUn-KA9JFlo4WwGfxktcBnvZMAhbmhdd7LOCfLSL5bQ?e=NZO83I>`_:
