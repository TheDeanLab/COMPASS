
.. _background-home:

###############################
Why Light-Sheet Microscopy?
###############################


The Importance of Volumetric Imaging.
--------------------------------------

Historically, 3D imaging has been performed
with spinning disk and laser scanning confocal microscopes. However, these
microscopes indiscriminately illuminate regions above and below the focal plane and
thus incur high rates of photobleaching and phototoxicity. This problem is further
exacerbated by their reduced duty cycle of illumination (e.g., the percentage of the
image acquisition duration that a region of the specimen productively contributes to
image formation), which necessarily requires a compensatory increase in laser power.
In contrast, depending on their design, LSFMs largely restrict illumination to a 2D
focal plane of interest within a specimen, and owing to high quantum efficiency and
massively parallel scientific cameras (e.g., 4x10\ :sup:`6`), the laser power can be
reduced
without compromising the imaging speed or signal to noise ratio. To illustrate, a
common voxel dwell time for a laser scanning confocal microscope is
1µs, and thus it takes ~4.16s to capture a 2048x2048 voxel image. For a LSFM, an
identical region can be imaged ~5ms, 832-fold faster, yet with a per-voxel dwell time
that is 5,000-fold longer. Consequently, LSFM allows for very delicate imaging with
high spatiotemporal resolution.

Challenges with 3D Imaging.
--------------------------------

To gain insight into cell biological events at subcellular scales, volumetric imaging
technologies must be combined with molecularly specific labels, biosensors and opto- and
chemogenetic tools, as well as computer vision analyses that translate non-human
interpretable 5D (x, y, z, :math:`\lambda`, t) datasets into biological insight. This
requires
that several key criteria be met:

-   To gain quantitative insight, the event of interest must be Nyquist
    sampled in both space and time. For example, the GTPase cycle times of Rho, Rac, and
    Cdc42 are as short as 5s, and occur on the micron scale. This requires that a
    complete volume be acquired every 2.5s, with a spatial resolution <500nm. And
    ideally, to avoid cell morphology-dependent intensity artifacts, the resolution
    should ideally be isotropic or nearly isotropic in X, Y, and Z. Indeed, this is
    particularly important for signaling events taking place at or on the plasma
    membrane, as is the case for GTPases.
-   To multiplex cellular readouts, the microscope must be compatible with
    simultaneous multicolor excitation and detection. For microscopes designs that
    leverage spatial light modulators within their excitation train, this is not possible.
-   The microscope must have an uncompromised detection sensitivity to reduce the
    impact of ectopic expression of signaling active proteins, and to reduce
    photobleaching and toxicity. This problem is particularly exacerbated for the latter,
    as 10-100 image slices must be acquired per time point to construct a complete imaging volume.
-   When imaging cells in extracellular matrix environments (which can migrate in any
    spatial dimension) or a developing embryo, one must also maximize the field of view
    of the microscope (>100 x 100 x 100 microns). Indeed, many leading LSFMs are designed
    to image very small fields of view (e.g., 25µm).
-   And lastly, to be compatible with downstream analytical routines, one cannot use
    iterative deconvolution or structured illumination routines to improve microscope
    performance, as these methods alter the numerical statistics of the data.

Why build a microscope?
------------------------

Importantly, the technology necessary to achieve multiplexed volumetric imaging with
advanced probes and computer vision analyses already exists. However, owing to the
need to produce aesthetically attractive, highly engineered, and serviceable optical
systems that deliver a large return on investment, microscope manufacturers are
incredibly conservative when it comes to adopting emerging technologies.
Consequently, most microscopes take >7 years to commercialize, and are immediately
considered obsolete by the microscopy community owing to scientific advances that
take place during the interim. One exception is the LLSM, which was sub-licensed by
Zeiss to 3i months after its seminal publication. Nonetheless, even here, it took an
additional 6 years for Zeiss to release their consumer- friendly model, which
prohibitively costs ~$1M USD. And lastly, a highly convoluted and entangled patent
landscape adds further delays and limits start-up companies from accessing the
consumer market. For example, despite their own limited development of the
technology, Leica has exclusively licensed a patent for off-axis tertiary imaging
systems, thereby effectively blocking commercialization of oblique plane microscopy.
Consequently, commercialization not only delays technology adoption, but can serve as
an active impediment to the dissemination of potentially transformative and
cutting-edge technologies.