
.. _nanospim-home:

############
NanoSPIM
############

Background
##########

Lattice Light-Sheet Microscopy
------------------------------
An alternative approach for high-resolution light-sheet imaging is to use a
superposition of propagation invariant beams as your illumination source, as is done
in LLSM. In theory, these beams maintain a narrow beam waist over an arbitrarily long
distance. However, in practice, these light-sheets are accompanied by sidelobes that
increase with beam length, generate out-of-focus blur, and degrade image resolution and
contrast8. As such, they are best suited for volumetrically imaging a more modest
field of view of ~25µm, which is ideal for thin specimens such as adherent cells or
epithelial monolayers. However, as previously mentioned, because LLSM requires a
spatial light modulator to sculpt its illumination beams, it is incompatible with the
simultaneous multicolor excitation needed for multiplexed biosensor imaging.
Furthermore, the spatial light modulator increases the complexity of the microscope
and decreases the light-throughput of the illumination train (~2.4%), and therefore
requires higher power and more expensive light sources.

Field Synthesis
---------------
To overcome these limitations, Dean and colleagues developed Field Synthesis, a
mathematical theorem that allows us to recreate time-averaged (e.g., dithered)
replicas of Lattice Light-Sheets using diffractive optics that offer much greater
light-throughput and are compatible with excitation multiplexing11. LLSM creates its
illumination beams by projecting a complex amplitude and phase profile onto the back
pupil of an illumination objective with a spatial light modulator. In contrast, Field
Synthesis scans a focused line over an appropriately designed binary pupil mask with
a galvanometer during a single camera exposure. Thus, all that is needed for Field
Synthesis is a galvanometer, a phase mask, and a 4f telescope. Importantly, Field
Synthesis is statistically indistinguishable to LLSM in terms of resolution and
photobleaching. In one demonstration with sample scanning, Field Synthesis was able
to perform very high resolution and simultaneous multicolor imaging of PI3K activity
and filopodial and bleb dynamics in an MV3 melanoma cell. However, because multiple
wavelengths could be imaged simultaneously, Field Synthesis was 2-fold faster, which
critically reduced motion blur for fast morphological events (e.g., filopodial
buckling).

NanoSPIM
--------