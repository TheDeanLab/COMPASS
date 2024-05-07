
.. _background-home:

########################################
**ASLM**
########################################

Two light-sheet microscopy techniques successfully decouple the trade-off between
axial resolution and field of view: multiview deconvolution and ASLM. In the former,
the sample is imaged from multiple directions (via sample rotation or by reversing
the illumination and detection paths) and the complementary views computationally
fused to create a high-resolution, large field of view image. However, this increases
the illumination burden on the specimen, increases the data overhead, and requires
deconvolution which is incompatible with biosensor-based imaging. In contrast, ASLM,
a technology invented by Dean and Fiolka in 2015, uses aberration-free remote focusing
to sweep a tightly focused Gaussian beam through the sample in its propagation
direction synchronously with the rolling shutter of a CMOS camera. Here, the axial
position of the illumination beam is deterministically controlled by translating the
position of a piezo or voice coil mounted mirror that is optically conjugate to the
specimen at the focal plane of a remote focusing objective. More recently, to
accelerate the image acquisition rate of ASLM to 200 frames per second, we developed
a novel method that converted a lateral galvanometer sweep into an aberration-free
scan of the illumination beam. Importantly, ASLM does not require any computational
post-processing, and delivers a large field of view (100 x 100 x 100µm) and the
highest axial resolution (~400 nm) in LSFM in the absence of deconvolution or
super-resolution techniques (e.g., structured illumination, stimulated emission, or
localization). Because ASLM has isotropic resolution, it is routinely combined with
advanced computer vision software, and has already provided tremendous insight into
diverse biological phenomena. For example, when combined with the software package
u-shape3D, ASLM was able to evaluate how Kras and PIP2 influence cell morphology and
motion in 3D collagen environments. Importantly, because it uses refractive rather
than diffractive optics, ASLM is entirely compatible with multiplexed excitation and
detection of multiple biosensors and/or optogenetic probes. As such, ASLM is ideally
suited to evaluate the molecular mechanisms underlying cell-cell interactions and
metastatic dissemination in 3D extracellular matrix environments.

Owing to ASLM’s simple design, we have already established an easy to assemble and disseminatable sample scanning prototype (Fig. TDP 2.3). This optical system is compact (2’x2’), predominantly enclosed, and minimizes the number of optical degrees of freedom to improve microscope stability and usability. It is entirely modular, and easily accommodates both the multiplexing and optogenetic modules (not shown). Fiber coupled lasers are used as an illumination source, and the entire system can be assembled and preliminarily aligned in an afternoon. Currently, only the remote focusing voice coil and resonant galvo used for multidirectional illumination shadow reduction51 require free-space alignment. However, to completely enclose the entire system, ongoing work aims to integrate the resonant galvo into a cube format or replace it with an electromagnetically driven sub-miniature resonant scanner (e.g., EOPC SC-3). With the aim of being maximally versatile, additional functionality will continuously be made available,
including the ability to scan the illumination beam in the Z-direction with a mirror galvanometer synchronously with the position of a piezo-mounted detection objective.
