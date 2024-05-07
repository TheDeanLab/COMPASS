
.. _opm-home:

############
OPM
############

Background
##########

Pitfalls of LSFM
----------------

The orthogonal illumination and detection geometry adopted by most LSFMs is
accompanied by several underappreciated disadvantages. For example, this geometry is
incompatible with hardware-based focus systems that reduce thermal and mechanical
drift, standard imaging dishes, multi-well plates, microfluidics that establish
chemotactic gradients, or parallel plate flow chambers that deliver controlled levels
of shear stress. They are also accompanied by high rates of reagent consumption owing
to large imaging chambers (~8.5mL for LLSM), which can be prohibitive for
chemogenetic and pharmacological perturbations such as BRAF inhibition. Importantly,
the use of high numerical aperture water dipping objectives compromises the sterility
of the specimen. Thus, evaluation of slow biological phenomena that take place over
~24 hours, such as sarcomerogenesis, is highly challenging. While some effort has
been made to develop ultra-thin fluorocarbon foil-based cuvettes, the slight
refractive index mismatch introduces small amounts of spherical aberration that
degrade image resolution and sensitivity.

Oblique Plane Microscopy
--------------------------

To overcome these challenges, OPM illuminates the specimen with an obliquely launched
light-sheet and collects the fluorescence with
the same objective (referred to as the primary objective) and uses aberration-free
remote focusing (with a secondary and tertiary objective) to reorient and image the
fluorescence on a scientific camera, it can operate in a more-convenient inverted
format. Nonetheless, the adoption of OPM remained limited as it suffered from
diminished resolution and sensitivity owing to the imperfect capture of the marginal
rays by the tertiary objective in the remote focusing system. However, Bo Huang’s lab
at UCSF developed a high-resolution OPM by introducing a water immersion tertiary
objective in the remote focusing system, which captured more marginal rays by
compressing the cone of light and refracting it towards the detection camera58.
More recently, Dean and coworkers took this optical concept to its logical conclusion
and introduced a custom solid immersion tertiary objective that maximized the
resolution and field of view of the microscope while also simplifying its alignment
and operation. Impressively, owing to its optimized optical train and high
numerical aperture of detection (>1.28)29, the raw resolution was 299x336x731nm,
which is the best lateral resolution in light-sheet microscopy. Furthermore, the
extent of the field of view in both X and Y is 2.6-fold larger than those in LLSM,
which is important for imaging large specimens such as a gastrulating drosophila
embryo or identifying a rare subset of natural killer cells that form an immunological synapse
. Its operation was also entirely compatible with optogenetics, which allowed us to
precisely photoactivate Rac1 in the lamellipodia of a fibroblast while simultaneously
and volumetrically evaluating its morphological response. Because OPM probes the
specimen with only a single objective, we were also able to investigate how cells
squeeze through confined regions within a microfluidic device. And lastly, owing to
its laser scanning format, which rapidly scans the laser through the specimen and
de-scans the fluorescence prior to imaging it with a camera, we were able to
volumetrically image calcium waves and cytoplasmic diffusion at 10.4 and 13.7 Hz,
respectively.

Unique Challenges with OPMs
---------------------------

Of the 3 LSFM technologies to be disseminated, assembling an OPM is the
most technically demanding. Nonetheless, we have identified the most critical
alignment steps and established laser-based methods for performing them. These
include conjugation of the light-sheet scanning galvanometer with both the primary
and secondary objective pupils, and alignment of the image at the front focal plane
of the secondary objective with the glass interface of the tertiary objective.
Importantly, these key alignment steps can be executed in a largely automated fashion
by introducing an alignment laser in the diascopic direction, by leveraging carefully
designed and fixed length optical components from ASI, and by moving the specimen
relative to a stationary primary objective. Each of these steps will be discussed
in-depth on our website and during our Visitor Program, which aims to train DBPs and
core facility managers how to assemble and use the proposed LSFM systems.
