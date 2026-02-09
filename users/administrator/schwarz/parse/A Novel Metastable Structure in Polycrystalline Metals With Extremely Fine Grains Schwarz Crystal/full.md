# A Novel Metastable Structure in Polycrystalline Metals With Extremely Fine Grains: Schwarz Crystal

![](images/83621e4862039280ed780e32560cc40afcd022bf4117536c68ae3b2f440b1fd0.jpg)

K. LU

Most metals exist in form of polycrystalline states consisting of crystalline grains and grain boundaries. These structurally defective boundaries make the materials thermodynamically unstable. Upon heating or straining, polycrystalline metals tend to be stabilized by eliminating grain boundaries through grain coarsening or transforming into metastable glassy phases when the grains are very small. Recently, we found a different metastable structure in polycrystalline face-centered-cubic pure metals and alloys as their grains are refined to a few nanometers with cryogenic high-pressure torsion. In this structure, named as ‘‘Schwarz crystal’’, the grain boundary networks evolved into the 3D periodical minimal surface structures constrained with high density twin-boundaries. It is thermally so stable that grain coarsening is inhibited at temperatures around the melting point, and exhibits a strength close to the theoretical value. Diffusional processes in alloys like precipitation of intermetallic phase, spinodal decomposition, as well as melting are inhibited with the Schwarz crystal structure. This paper briefly reviews the discovery of this novel metastable structure. The precursory process (grain boundary relaxation) in nanograined metals, formation and structure characteristics of the Schwarz crystals, as well as their thermal stability and strength in different metals and alloys will be introduced with experimental and molecular dynamic simulations. Perspectives and future studies on the structure will be discussed.

https://doi.org/10.1007/s11661-023-07232-4

$^ { © }$ The Minerals, Metals & Materials Society and ASM International 2023

# I. INTRODUCTION

SINGLE crystals are ideally the end-member stable structures for metals, in which atoms are arranged orderly in crystal lattices throughout the sample. In reality, most metals and alloys are in polycrystalline states consisting of smaller crystallites (or called ‘‘grains’’) separated by boundaries. Atomic arrangements in the grain boundaries (GBs) are normally disordered. Such disordered GBs make polycrystalline structures thermodynamically unstable.[1]

Eliminating GBs is believed to be essential to stabilizing the polycrystalline structures when they are heated or strained. For example, grains in polycrystals may coarsen through migration of GBs, which often takes place at temperatures around a half of the melting point, or below.[2] The tendency of grain coarsening increases for smaller grains.[3–5] Significant coarsening may take place for nano-sized grains even at room temperature for some metals.[5]

Another option for stabilization is to form metastable amorphous solids or glasses, in which atoms are arranged disorderly with short/medium range ordering only.[6] The transformation into amorphous states from polycrystalline solids with extremely fine grains and a high GB density is thermodynamically favorable. Indeed, amorphization was observed in alloys with specific compositions as their grain sizes are reduced typically below few nanometers (e.g., in Ni-P,[7] Ni-W,[8] Al-Mn.[9] Nevertheless, amorphous solids are compositional sensitive and rarely formed in pure metals and most alloys in conventional conditions. Stabilizing nanograined pure metals and non-glass-forming alloys is challenging without addition of foreign elements.

In 2018, an abnormal size effect of grain coarsening was uncovered in nanograined pure Cu and Ni processed through plastic deformation. With reducing grain size below about $7 0 ~ \mathrm { n m }$ in Cu (and ~ 50 nm in Ni), contradictory to the common wisdom, the grain coarsening temperature increases rather than decreases. This unusual phenomenon originates from autonomous relaxation of GBs into low-energy states, triggered by their interaction with partial dislocations below a critical grain size.[10] The relaxed GBs with a reduced excess energy leads to an elevated stability for smaller nanograins against coarsening under thermal and mechanical stimuli.[10,11] The finding not only sheds

lights on stabilizing nanograined structures in metals, but also enlightens a fundamental question that if alternative metastable structures, other than amorphous solids, may be adopted as polycrystalline metals are refined to the extreme scales.

Aiming at this question, we modified the processing and refined grains of pure Cu further down to few nanometers. Through careful structural characterization combined with molecular dynamic (MD) simulations, we discovered a novel metastable state in metals with grains of few nanometers in size, in which GBs evolved into triple (3D) periodical minimal interface (TPMS) structures constrained with dense twin-boundary networks.[12] The unique structure was named as Schwarz crystal structure, after the German mathematician, Hermann A. Schwarz (1843-1921). As proved mathematically in the eighteenth century, the mean curvature is zero at every point on a minimal surface: the positive (hill-like) and negative (bowl-like) curvatures balance one another. Hermann Schwarz found that the saddle-like shape of minimal surfaces can be constructed to extend forever in 3D space by a periodic repetition of identical curved units, forming the TPMS structures.[13] The building units can be assembled into 3D structures with different symmetries (P-surface, D-surface, and G-surface), dividing the space into interpenetrating networks. With such GB-network structures, GB migration is suppressed in metals even at temperatures very close to the equilibrium melting point $( T _ { \mathrm { m } } )$ .[12]

In this paper, I will review this discovery beginning from the precursory GB relaxation process in nanograined metals. The formation and structure characteristics of the Schwarz crystals will be introduced with experimental and MD simulations. Thermal stability, strength, as well as several diffusional processes including precipitation, Spinodal decomposition, and melting of Schwarz crystals in different metals and alloys will be discussed. Perspectives and future studies on this novel structure are to be addressed in the summary part.

# II. STRUCTURAL RELAXATION OF GBIN NANOGRAINED METALS

# A. An Abnormal Grain Size Effect on Thermal Stability

Several techniques have been developed in the past decades for refining grains of metals and alloys into the micrometer and nanometer scales through plastic deformation.[14–17] One of these top-down processes is to deform surface layers on bulk metals for producing nanostructures, namely, surface nanocrystallization.[14] Gradient plastic deformation is introduced in the surface layer with a varying strain and strain rate along depth through various treatment modes such as surface impact,[14] surface grinding,[18] or surface rolling,[19] generating a structure gradient in grain size or in twin density, or both. Grains may be refined to a level of ten nanometers in the treated surface and to the micro-scale at about a millimeter depth.[18–23] Such a gradient nanograined surface layer offers a unique venue for

delving into grain size effects on properties in a wide size range without any change in chemical composition.

Using the surface mechanical grinding treatment at the liquid nitrogen temperature, we prepared a layer of gradient nanograined structure on surfaces of a pure Cu rod[10] : grain sizes increase gradually from about $4 0 ~ \mathrm { { n m } }$ in the topmost surface to about $7 0 ~ \mathrm { n m }$ at $\sim 2 0 \ – \mu \mathrm { m }$ depth and $2 0 0 ~ \mathrm { n m }$ at $\sim 1 5 0 – \mathrm { m m }$ depth (Figure 1(a)). For examining grain size effects on thermal stability, the sample was annealed at various temperatures and characterized using scanning electron microscopy (SEM) and transmission electron microscopy (TEM) observations. As annealing above $3 7 3 \mathrm { ~ K ~ }$ , in the subsurface layer (a depth span of 20 to $5 0 ~ \mu \mathrm { m }$ ) with original grains of 70 to $1 1 0 ~ \mathrm { { n m } }$ in size, we observed sporadic coarsened grains. Coarsening became more evident at higher annealing temperatures, and the lower front of the coarsening layer migrated downward while the upper front upward slightly, indicating the smaller grains in the top layer are more reluctant to coarsen.

In common wisdom, smaller grains are less stable. Coarsening was expected to onset firstly from the smallest grains in the topmost surface layer, rather than the larger ones in the subsurface layers. But no coarsening was detected in the top $2 0 \mathrm { - } \mu \mathrm { m }$ -thick surface layer as annealed at $4 3 3 \mathrm { ~ K ~ }$ for 1 hour, while submicrometer-sized grains in subsurface layers grew into the micrometer scales (Figure 1(b) through (d)). Prolonging the annealing to $1 2 \mathrm { ~ h ~ }$ has a negligible influence on the nanograin stability. We determined the coarsening temperature with different grain sizes and found it drops at smaller sizes for grains above $7 0 ~ \mathrm { n m }$ , agreeing with the documented trend. But smaller nanograins below $7 0 ~ \mathrm { n m }$ become more stable. The instability temperature for $4 0 ~ \mathrm { { n m } }$ -grains increases up to $0 . 4 5 T _ { \mathrm { m } }$ which is higher than the recrystallization temperatures of coarse-grained $\mathrm { C u }$ (Figure 2(a)).[10]

Before analyzing the mechanisms underlying the abnormal grain size effect below $7 0 ~ \mathrm { n m }$ , we eliminated doubts on contamination and texture in the top surface layer possibly induced during processing. Electron diffraction analysis under TEM combined with electron backscattered diffraction (EBSD) showed a consistent weak $\{ 1 1 1 \} < 1 1 0 >$ texture in the surface layer within $1 { - } 4 0 ~ \mu \mathrm { m }$ depth in the as-prepared sample. No chemical composition change was detected from energy-dispersive X-ray spectroscopy and electron energy loss spectroscopy in the surface layer deeper than $0 . 5 \ \mu \mathrm { m }$ from the treated surface. This is understandable as atomic diffusivity is very low at liquid nitrogen temperature. Hence, the doubtful impurity effect can be excluded as the measured data in the topmost $1 ~ \mu \mathrm { m }$ -thick layer was removed from analysis.

We prepared another pure Cu sample using the same treatment with lower strain rates at $1 7 3 \ \mathrm { K }$ , in which grain sizes increase gradually from submicrometers in the top surface layer to micrometers with depth. Annealing this sample above $4 3 3 \mathrm { ~ K ~ }$ , grain coarsening was found to start simultaneously in the top surface with the finest grains and in the subsurface layer with larger grains. It reflects the abnormal thermal stability observed below $7 0 ~ \mathrm { n m }$ is not resulted from

![](images/e54e4bbee65cfe7132ecd7d9c378b81878c6964d3850f98052abde8226dfb804.jpg)  
Fig. 1—Annealing-induced structure changes in pure Cu with gradient nanograined structure. (a) Typical cross-sectional SEM images of the as-prepared gradient nanograined Cu sample and (b) the sample annealed at $4 3 3 \mathrm { ~ K ~ }$ for 1 h, (c) A cross-sectional EBSD image of the top surface layer annealed at 433 K, (d) Variation of grain size with depth from the treated surface of the as-prepared and the as-annealed (at $4 3 3 \mathrm { ~ K ~ }$ for 30 min) samples. (Reprinted with permission from Ref. [10]).

processing-induced contamination. This conclusion is confirmed by a recent study on the impurity effects on the abnormal thermal stability in Cu,[24] as will be presented in Section II-C.

# B. Plastic Deformation Induced GB Relaxation

The grain coarsening kinetics is governed by the GB mobility and the driving force for GB migration.[25,26] The former is sensitive to GB structure and the latter is proportional to GB energy and curvature. Both may be reduced by lowering the GB excess energy, either by alloying with foreign elements[27–30] or through structure relaxation,[31] abate GB migration as a result. Previous studies showed GB structures can be adjusted to lower their excess energy through interaction with partial dislocations as demonstrated by MD simulations on a number of symmetric tilt GBs in metals.[32,33] A GB may dissociate into two or more GBs connected by stacking faults when partial dislocations emit from the boundary, resulting in relaxation in GB region with decreased excess energy. This GB relaxation mechanism was verified in Au and Cu[34] $\mathrm { C u } ^ { [ 3 4 ] }$ under high-resolution TEM observations, which is consistent with an evidence in Cu that GBs are structurally relaxed by interaction with nano-scale coherent twins, so that atomic transport along GBs is retarded.[35]

In the past decades, a transition in deformation mechanism from full dislocation slip to partial dislocations was revealed in metals when grain sizes are reduced to a critical size that equals to the dislocation splitting distance.[36–38] It usually varies from few to $\sim 5 0 ~ \mathrm { n m }$ for typical face-centered-cubic (FCC) metals like Ni, Cu, Ag, and Al, depending upon the resolved shear stress and the energies of both stable and unstable stacking faults.[39] The transition, as experimentally verified in a

number of metals,[10,11,40–42] means in deforming metals with grains below the critical size, partial dislocations, rather than full dislocations, are manipulated that may interact with GBs and lead to relaxation of GB structures. In other words, plastic straining may not only refine grains through GB manipulation, but also autonomously trigger structural relaxation of GBs in the metals when grains are small enough.

The critical grain sizes for the full-to-partial dislocation transition can be estimated from the stacking fault energy, or alternatively from the critical shear stresses to nucleate a full dislocation and Shockley partials, approximating the source size equal to the grain size $( D )$ . In terms of the classical Orowan relation,[43] multiplying full dislocations requires a Frank-Read-type source with a minimum grain size $( D ^ { * } )$ at the yield strength $( \sigma _ { \mathrm { y } } )$ that is grain size dependent. In other words, bowing out of full dislocations in grains smaller than $D ^ { * }$ is inhibited and initiation of partials is preferred instead:

$$
D ^ {*} = \frac {\mu b}{\sigma_ {y} (D ^ {*}) / m} \tag {1}
$$

where $1 / m$ is the Schmid factor. It means dislocation bowing out is inhibited at the most favored slip system with the largest resolved shear stress $( 1 / m = 1 / 2 )$ while only partial dislocations can be emitted in grains smaller than $\boldsymbol { D } ^ { * ( 1 / 2 ) }$ . The calculated $D ^ { * ( 1 / 2 ) }$ is 40, 35, and $2 2 ~ \mathrm { { n m } }$ for Ag, Cu, and Ni, respectively, which agree with that from the estimated dislocation splitting distances in terms of stacking fault energy.[44] They are consistent with the stable grain sizes against mechanically driven grain coarsening.[11] Taking an average $1 / m = 1 / 3$ for polycrystals, we obtain the critical grain sizes $D ^  * ( 1 /$ $^ { 3 ) } = \dot { 7 } \dot { 7 }$ , 70, and $3 5 \mathrm { n m }$ for Ag, Cu, and Ni, respectively,

![](images/dbfe9da2af9d3b6c10525fc823257ce3c3c1957a13287761e4622f0834865508.jpg)  
Fig. 2—Thermal stability and GB energy versus initial grain size in Cu. Variations of the measured grain coarsening (instability) temperature $( T _ { \mathrm { G C } } )$ (a) and GB excess energy (b) with the average grain size. Different symbols represent data of samples from different preparation methods. (Reprinted with permission from Ref. [10]).

corresponding to the onset grain sizes for the full-to-partial transition. They agree approximately with the inflection grain sizes of coarsening in these metals. The critical size for Cu is exactly the turning point of the abnormal thermal stability in our experiments.[11]

Structural examination of nanograined Cu samples confirmed that deformation is dominated by full dislocations for grains above $7 0 ~ \mathrm { n m }$ and by partials for smaller grains, in which high density through-grain twins and stacking faults are obvious. Evidences of relaxed GB structures were frequently identified under high-resolution TEM in grains below the critical size, analogous to the extended GB structure with the emission of partial dislocations.[34] The relaxation of

GBs is also supported by an obvious drop in the average GB excess energy in Cu around the critical grain size, from a normal GB energy of about $0 . 5 \overline { { 2 } } \ \mathrm { J / m } ^ { 2 }$ to $0 . 2 3 { \cdot } 0 . 2 7 ~ \mathrm { J } / \mathrm { m } ^ { 2 }$ (Figure 2(b)).[10]

Interaction of thermally induced twins with GBs may also relax GBs in Cu with a wide grain size range up to submicrometers.[45] The coarsening temperatures of these grains after the thermal-GB-relaxation may increase to about $0 . 6 \ T _ { \mathrm { m } }$ . The relaxation of GBs also has a pronounced effect on mechanically driven GB migration in metals. By straining the gradient nanograined specimens under quasistatic tension, a peak coarsening rate was found for nanograins at an initial size of $\sim 7 5 ~ \mathrm { n m }$ , coincident with the critical grain size of

thermal stability (Figure 3).[46] The comparable critical sizes imply analogous effects of relaxation on migration of GBs driven either mechanically or thermally, as also evidenced in Ni and Ag.[11]

The abnormal grain size effect on thermal stability and the associated GB relaxation have been observed in other FCC metals including pure Ni, Ag, Al[41] and some alloys[50–52] processed through plastic deformation. In fact, hints of structural relaxation of GBs were noticed in earlier experiments. For instance, as pure Ni powders were ball-milled intensively, the stored enthalpy of the milled metals drops significantly as grains are refined to $\sim 1 0 ~ \mathrm { n m }$ , deviating sharply from the ordinary trend.[53] Similar observations were reported in the ball-milled Ru and AlRu systems.[54] While other effects may not be excluded, relaxation of GBs into lower-energy states in the nanograined is likely one of the dominant mechanisms responsible for the abnormal behaviors.

# C. Impurity Effect on GB Relaxation

Impurities are inevitable in metals that may affect behaviors of dislocations and interfaces, as exampled by the drag effect of impurity atoms on GB migration kinetics that makes the less-pure metals thermally and mechanically more stable.[55–57] Impurity effects on the GB relaxation process in metals were investigated in Cu of different purities from 99 pct (2N) to 99.9999 pct wt. (6N). For each purity, we took a pair of samples with different grain sizes and GB structures but with the same chemical compositions, one with a mean grain size of $6 0 ~ \mathrm { { n m } }$ (below the critical size) and relaxed GBs (denoted as RNG-xN, $ { x } = 2$ , 3, 4, 5, and 6), and another with $1 0 0 ~ \mathrm { { n m } }$ -grains (above the critical size) and unrelaxed GBs (NG-xN).

In the NG-xN samples, grain coarsening temperatures decrease at higher purities, from ~ 373 K (NG-2N) to 313 K (NG-6N), agreeing with the usual trend of ‘‘purer and less stable’’ (Figure 4).[24] But the scenario is

![](images/21080d43c205dcd99c421066ce2b8acd17faac8a929771f21ec6eb4056bfc51b.jpg)  
Fig. 3—Relative grain size change $\left( \Delta \textrm { D } / \mathrm { D } _ { 0 } \right)$ ) with respect to initial average grain size $\left( \mathrm { D } _ { 0 } \right)$ in the gradient nanograined Cu samples after tension. Data from the literatures[25,47–49] are included for comparison. (Reprinted with permission from Ref. [46]).

different in the RNG-xN samples. Grains in the RNG-2N started growing at $\sim 4 1 3 \mathrm { ~ K ~ }$ while some nanograins may survive at about $5 2 3 \mathrm { ~ K ~ }$ , showing that the coarsening process is sluggish in a wide temperature span (110 K). Both the onset temperature and the span are much larger than that in the NG-2N. In the RNG-xN samples of higher purities the coarsening temperature (and hardness) increases, rather than decrease, to $5 1 3 \mathrm { ~ K ~ }$ in the RNG-5N, which is about $2 0 0 ~ \mathrm { K }$ above that in the corresponding NG-xN samples (Figure 4). The measured activation energy for grain coarsening also verified intensified GB relaxation in purer Cu samples. These evidences suggest impurity atoms may segregate at GBs, hindering emission of partial dislocations from the boundaries and making the GB relaxation process more difficult.

# D. GB Relaxation in Nanograined Alloys

GB relaxation processes were induced in a number of binary and multicomponent FCC alloys.[50,51] Nanograined structures of Cu-Ni solid solutions (5 and 10 at.pct Ni) were prepared using surface mechanical grinding treatment in liquid nitrogen. The grain coarsening temperature of the alloys is about 150- 200 K higher than that of pure Cu. A similar grain size dependence was found in the alloys with a critical size around $7 0 ~ \mathrm { n m }$ for the stability up-turn (Figure 5(a)). It speaks at that GB relaxation was triggered in the nanograined alloys below the critical size although their stacking fault energies are higher than that of pure Cu.[51] $\mathrm { { C u } }$

Alloying Cu with Al decreases stacking fault energy, to 25 and $\sim 1 2 ~ \mathrm { m J / m } ^ { 2 }$ at 5 and 10 at.pct Al, respectively.[66,67] The deformation-induced GB relaxation was observed in the alloys with grains below ~ 70 nm with a similar size effect on coarsening temperature. But thermal stability does not increase monotonically below the lowest stability size (Figure 5(b)). A drop in coarsening temperature was detected at smaller sizes below $6 0 ~ \mathrm { { n m } }$ with 5 pctAl and $4 5 ~ \mathrm { { n m } }$ with 10 pctAl. This was attributed to a changed deformation mechanism in finer nanograins, leading to different degrees of relaxation in GB structures in which competition between twinning and formation of stacking faults may play a key role.

In Al-Mg (5at.pct) alloys with grain sizes of $3 0 ~ \mathrm { { n m } }$ the deformation-induced GB relaxation leads to much higher coarsening temperatures and hardness than that of the submicro-grained counterparts. In addition, depletion of $\mathrm { M g }$ was found at the relaxed GBs, rather than segregation, distinct from that in normal Al-Mg alloys.[71,72] This effect may originate from the compressive strains in the vicinity of the relaxed GBs, implying possible variations in GB chemistry are induced with the structural relaxation that may also play a part in stabilizing nanograined alloys.[50]

GB relaxation was induced in single-phased multicomponent Ni-Co-Cr alloys as grains are refined below $3 0 ~ \mathrm { { n m } }$ through plastic deformation.[52] The stabilized GB-networks that are interlocked with abundant twin boundaries inhibit significantly diffusional creep

![](images/872d7b19a32abb4b8e3bd9e1b24dcf6b27f8e8cf4dea8eb01d99c6ff69e03b88.jpg)  
Fig. 4—Thermal stability and microhardness of pure Cu with different purities. Measured grain coarsening temperature $( T _ { \mathrm { G C } } )$ as a function of microhardness for the RNG-xN and NG-xN pure Cu samples. Data from literatures[58–65] are included for comparison. (Reprinted with permission from Ref. [24]).

processes at elevated temperatures. The obtained creep resistance was unprecedented with creep rates of ~ $1 0 ^ { - 7 }$ per second under gigapascal stress at $7 0 0 ~ ^ { \circ } \mathrm { C }$ (~61 pct $T _ { \mathrm { m } } )$ , outperforming that of conventional superalloys.[73–78]

# III. A NOVEL METASTABLE STRUCTURE IN METALS WITH EXTREMELY FINE GRAINS

# A. Processing and Structural Characterization

With the increased stability of nanograins owing to GB relaxation below the critical grain size, we are curious about the ultimate stability and structure in the polycrystalline metals when grains are reduced to extremely fine scales, say, to few nanometers. To clarify this, we intensified straining to refine nanograins further in Cu. We removed the top $2 0 \ \mu \mathrm { m }$ -thick surface layer with nanograins from the Cu rod processed with surface mechanical grinding treatment, and deformed the foil again using torsion under a pressure of 10 GPa in liquid nitrogen. After rotation of multiple cycles, a mixed nanograined structure was formed in the foil sample, consisting of domains with grains of few nanometers in size embedded in regions with larger grains (averagely ~ 25 nm in size).[12] The extremely fine-grained domains are irregularly shaped and around ten micronmeters in size

The extremely fine-grained domains exhibit a typical manifold structure under bright-field TEM observations (Figure 6(a)), containing ‘‘darker’’ regions and

‘‘brighter’’ ones, seemingly in form of continuous aggregates or chains. When the sample is titled, the darker regions may turn bright and the brighter ones become dark, indicating both regions are crystalline grains with different crystallographic orientations. These 3-dimensional chains interlock with each other (or are entangled together), forming continuous (or bi-continuous) networks throughout the sample, analogous to that the typical manifold structure normally seen in the bicontinuous lipid-water phases.[79] The chains are bounded by curved interfaces, of which the structures do not differ from that of the general GBs in the conventional polycrystals. But the geometry of the interfaces, as will be addressed later, exhibits the TPMS structure, distinct fundamentally from that in conventional polycrystalline metals.

Careful analysis revealed that the continuous chains consist of tiny irregularly shaped crystalline grains of similar contrasts (similar transparencies to electron beam). In each aggregate or chain, twin or CSL boundaries were noticed among neighboring tiny grains of similar contrasts (Figure 6(b)). High-resolution TEM images showed roughly equiaxed nano-sized crystallites with various orientations and most grains are few nanometers in size (Figure 7(a)). Nearly continuous diffraction rings of FCC Cu were obtained from electron diffraction of plenty of grains, a hint of seemingly random crystallographic orientations of the nanograins. The tiny grains are bounded with each other by atomically distinct interfaces, without any amorphous phase or pores. The full crystallinity of the single FCC

![](images/354f36b38de469c3d472f8e573f46af5d4ae7c5902607bc71a9c2b8b0f14693e.jpg)  
Fig. 5—Thermal stability versus grain size in Cu-Ni and Cu-Al alloys. Grain coarsening temperature ${ \cal T } _ { \mathrm { G C } } )$ as a function of initial grain size for (a) Cu-Ni alloys and (b) Cu-Al alloys, including reported data in the literatures.[10,58,68–70] (Reprinted with permission from Ref. [51]).

phase is supported by X-ray diffraction. Precession electron diffraction under TEM (Figure 7(b)) showed that $\sum 3$ twin boundaries with a misorientation of $6 0 ^ { \circ }$ constitute about 25 pct GBs in the extremely fine domains. Other interfaces separating the nanograins, including ~ 20 pct low- $\displaystyle \sum$ CSL boundaries, are with randomly distributed misorientations. Typical structural characters of relaxed GBs were found in the boundaries, such as the associated GB structural units.

Under high resolution TEM, we saw diverse geometries of individual grains. Plenty of grains are bounded with faceted (111) and (100) atomic planes, rather than curved boundaries. A typical grain imaged along [110]

zone axis as in Figure 8(a) is distinguishable by four faceted {111} and two $\{ 0 0 1 \}$ boundaries. Some grains contain through-grain twins or stacking faults (Figure 8(b)), with {111} coherent twin boundaries spaced by only few atomic layers. Stacking fault zones were detected between the truncated-octahedron-shaped nanograins (Figure 8(c)), agreeing with that in Fig 6(b). Statistically, grains smaller than 3 nm have 62 pct {111} faceted boundaries and 33 pct {100}, with a frequency ratio roughly 2:1. The boundaries are 52 pct $\{ 1 1 1 \}$ and 28 pct {100} for grains of 3 to $1 0 ~ \mathrm { { n m } }$ in size. This frequency ratio disappeared for grains larger than $1 0 ~ \mathrm { { n m } }$ .

![](images/177c887961bc2ac80cc335da3e9d10fe289e801f104452c72bf195430e47b807.jpg)

![](images/e464eb321089092e9610d37531f0ec007766dadaf402091d647392107e7eea2f.jpg)

![](images/9879f9f625eba3f450eab34c6d001ff218cb6d90143ecf01d0d402a15fcc27bf.jpg)

![](images/29cd42fc1efc05b47bad1ffa9cadf34b18fe156cf9969a57844554efb715ba73.jpg)  
Fig. 6—Structural characterization of the Cu sample with extremely fine grains. (a) A bright-field TEM image of a typical manifold structure, (b) (Left) A high-resolution high-angle annular dark-field (HAADF)–scanning transmission electron microscope (STEM) image of an aggregate in the manifold structure from a region in (a). (Right) Corresponding fast Fourier transformation (FFT) images of grains. (Reprinted with permission from Ref. [12]).

![](images/d926df88dc44f2c66abb37c79a88ff46dee6d68957008315726c771ea0168499.jpg)

![](images/8bb99f836dd4c06596c31c7635bc39d4fecccd3c2c171776522496214a49af76.jpg)  
Fig. 7—(a) A high-resolution TEM image of the Cu sample with extremely fine grains, (b) Orientation mapping in the TEM acquired from a region in (a) from the precession electron diffraction analysis. (Reprinted with permission from Ref. [12]).

The grain shapes seem to resemble the truncated octahedron.[80] HRTEM images of the defect-free grain in Figure 8(a) fit perfectly with truncated octahedral projected along [100] axis, so do the twin/fault-containing grains with the twinned or faulted polyhedra (Figures 8(b), (c)). Projecting a truncated octahedron along [001], one may see four {111} and two $\{ 1 0 0 \}$ boundary planes with a number ratio of 2:1, coincident with what we found. Apparently, the truncated-octahedral are favorable shapes for the tiny grains below $1 0 ~ \mathrm { { n m } }$ . Note that lattice images on the corners of the grains (Figures 8(a), (b), as arrowed) are blurred or missing in the TEM images, that will be discussed later.

# B. Thermal Stability and Hardness

The thermal stability of the extremely fine grains was characterized by annealing isothermally at various temperatures. Surprisingly, apparent grain coarsening was not detected as the annealing temperature is

increased to $1 3 4 8 \mathrm { ~ K ~ } , \sim 9 \mathrm { ~ K ~ }$ below $T _ { \mathrm { m } }$ of Cu (Figure 9(a)). After holding at this temperature for $1 5 ~ \mathrm { m i n }$ , the polyhedron-shaped grains were still observable with distinct boundaries, of which the average size $( \sim 1 1 \pm 2 . 3 \ \mathrm { n m } )$ is slightly larger than that before annealing. Twin density increased in the annealed nanograins (Figure 9(b)). Elevating the temperature to few degrees above $T _ { \mathrm { m } }$ resulted in melting and disappearance of nanograins. The observation says that prior to melting, the nanograins did not experience substantial coarsening.

For comparison, we measured the thermal stability of $2 5 ~ \mathrm { { n m } }$ -grains in which the extremely fine-grained domains are embedded. Obvious coarsening of the nanograins was found after annealing above ~ 1000 K (Figure 9(a)). Clearly, the measured instability temperatures of the extremely fine grains and $2 5 ~ \mathrm { { n m } }$ -grains fall on the extrapolated line of the grain size dependence of coarsening temperature observed previously in the nanograined Cu samples with relaxed GBs.[10] The

![](images/e5838589cba358107685afb31c76eca9ef0bd687c4c778756e1259da457a4cd2.jpg)

![](images/a779f472c842461b013f10ed8f78e1fc1459b79f4f54ae6af60b2addfc38106f.jpg)

![](images/d3653f518009458331fc36f6fba88dfae34418495201c808be957610a75f7ef0.jpg)

![](images/b80b5c4e1903b5aa8de370fb780e3d3ba6527c29acd230de60ec672d066eae32.jpg)  
Fig. 8—A high-resolution TEM image of individual grains with truncated octahedral geometries. (a) (Left) Atomic resolution HAADF-STEM image of a tiny grain with beam direction along the [110] zone axis. (Right) A part of an ideal truncated-octahedron of 1154 atoms (top), rotated by $4 9 ^ { \circ }$ along the [110] zone axis (lower right). The projected atomic positions (lower left) on the (001) plane are coincident with the TEM image in (a) (orange denotes border atoms). (b) A high-resolution TEM image of a tiny grain with twin boundaries. (Left) An ideal truncated-octahedron with 11817 atoms with twins (top), rotated by $2 5 . 5 ^ { \circ }$ along the [110] zone axis (lower right). Projected atomic positions (bottom left) agree with the high resolution TEM image in (b) (only border atoms in orange and twin boundary atoms in red are shown). (c) (Top) Two tiny grains containing stacking faults (SFs) and twins. (Bottom) Two attached truncated octahedral grains of different sizes with projected atomic positions agreeing with the TEM image in (c). (Reprinted with permission from Ref. [12]).

![](images/4f42af0f4c57f621c4fdbb429fff161ad008c6f5a296a72873ddb468efb68812.jpg)

![](images/f6cf037ff616befc25e46ac4b3c623628b234af02ac85d4999a1b3a14e9a958b.jpg)  
Fig. 9—Thermal stability of the Cu sample with extremely fine grains. (a) Variation of grain size with annealing temperature (for a duration of $1 5 \mathrm { \ m i n } ,$ ) for three samples with initial average grain sizes of 50, 25, and $1 0 ~ \mathrm { \ n m }$ , respectively. (b) A HAADF-STEM image of a typical polyhedron-shaped grain along the [110] zone axis after annealing at 1348 K. (Reprinted with permission from Ref. [12]).

extremely fine grains of Cu exhibit a higher thermal stability than any reported data in the literatures for pure Cu[45,59,62,81–86] $\dot { \mathrm { C u } } ^ { [ 4 5 , 5 9 , 6 2 , 8 \tilde { \mathrm { I } } - 8 6 ] }$ with nanograins and deformed coarse-grains, and that for the amorphous Cu-based

alloys (crystallization temperatures in 0.33-0.36 $T _ { \mathrm { m } } .$ Figure 10).

The measured nanoindentation hardness of the extremely fine grains is as high as $4 . 7 \pm 0 . 2$ GPa, well above the documented hardness for nanograined Cu

![](images/0f7fff2dcb81557fcb741251197d489fefc3861ab2304be3478bba4f2ed319f3.jpg)  
Fig. 10—The superior thermal stability and strength of Cu with extremely fine grains. Grain coarsening temperature $( T _ { \mathrm { G C } } )$ ) and yield strength versus grain size in Cu. Different symbols represent data from different preparation methods.[84,87–92] ( Reprinted with permission from Ref. [12]).

samples and amorphous Cu-based alloys[84,87–92] (Figure 10). We estimated the yield strength from the measured hardness and found it is roughly in vicinity of the ideal shear strength of Cu by considering the temperature effects.[93] Strength determined from plenty of Cu samples was found to follow the classical Hall-Petch relationship when grain sizes exceed $3 0 ~ \mathrm { { n m } }$ . Below $3 0 ~ \mathrm { { n m } }$ , a plateau in strength or even softening appears.[87,88,90,91] In contrast, this trend does not appear in our samples. The observed continuous hardening speaks that the GB-mediated deformation mechanisms usually observed in nanograined metals (such as GB migration or sliding) cease to operate in the extremely fine grained Cu.

# C. Atomistic Simulations

The unusual stability observed underlies a different structure is adopted in the extremely fine grained Cu samples. To unmask such a structure and the associated GB networks, we firstly proposed an initial structure in terms of the observed geometries and structures of the individual nanograins, then, performed MD simulations to relax the structure by heating or straining based the interatomic potential.

Our TEM observations combined with the reconstructed atomic models showed the truncated-octahedron is a representative prototype geometry for a large portion of individual nanograins, either perfect or those

contain twins or stacking faults. Accordingly, one may perceive the potential structures based on the wellknown Kelvin conjecture,[94] i.e., constructing a topological polycrystalline configuration with equal-sized truncated-octahedral-shaped grains (Figure 11). Such a model represents a simple geometrical solution for idealized 3D polycrystals with a nearly minimum area of GBs.[95] The structure is also reasonable for 3D space-filling coherent twin boundary (CTB) networks, considering a substantial amount of twin boundaries in our experimented samples.[96]

We constructed an extended Kelvin supercell with sixteen truncated-octahedral-shaped grains of equal size in a body centered cubic array. Detailed description of the supercell structure (as shown in Figure 11) can be found in,[12] within which 3D space-filling CTB-networks were constructed.[96] Taking an initial grain size of $3 . 2 7 ~ \mathrm { n m }$ in the extended Kelvin polycrystal as a starting structure for simplicity, we relaxed the sample using MD simulations by heating it up to various temperatures based on the interatomic potential developed with the embedded atom methods.[97] The heating rate is about 8 K/ns. During MD heating, the supercell structure relaxed and the GBs gradually transform into different configurations through extensively GB events including reaction and migration. At triple lines or junctions of GBs, dissociation and coalescence of GBs are triggered, associating with some R9-type GBs. Migration of twist GBs was found to become substantial with increasing temperature. Heated to $7 6 0 ~ \mathrm { K }$ , we found some grains shrank and finally disappeared owing to

migration of GBs, but the entire GB-network survives. The GB-networks eventually developed into a configuration that topologically resembles a kind of TPMS, the Schwarz-D surface[13,98] (Figure 12). During heating, the built-in CTB network is quite stable against thermal fluctuations. We imposed plastic strain to the supercell sample at low temperatures and obtained the same Schwarz-D interface structure. It means the adopting the TPMS structure is an energetically more favorable for relaxing GBs in the ploycrystals under thermal or mechanical stimuli.

It is known that the Kelvin polycrystal provides a unique and efficient structure for space-filling arrangement of grains. But the total GB area can be further reduced by forming the Schwarz-D interface structure.[99] MD results showed the transformation from Kelvin polycrystals to Schwarz-D interfaces is a process thermodynamically driven by minimization of GB area, and the polycrystals with Schwarz-D interfaces become more stable than the starting Kelvin polycrystals. As a TPMS, the Schwarz-D interfaces possess the minimal interface area and a zero-mean-curvature, implying the driving force to GB migration vanishes.

In addition, high-density CTBs are generated during the MD relaxation, which interlock with the Schwarz-D interface on both sides (Figure 12(a)). The Schwarz-D interfaces constrained by stable CTB-networks forms a unique and robust structure to suppress migration of GBs and CTBs, preventing GBs from developing substantial curvatures to escape. Our simulations indicated that with the Schwarz-D interface only, such an

![](images/553698287d1ef4e880e43895e71913c0a36253e5cdeac0639fb2cffadb21b333.jpg)

![](images/2a744d4da54758236444517a2d08ba37c343f2def03fc032b27db7294a5ecd69.jpg)  
(a)   
(b)

![](images/307c78f8099aac6449a2ec4c7d262eede876747dddfe086fba5f8641209d9e9b.jpg)  
(c)   
Fig. 11—Atomistic model and molecular dynamic (MD) simulations of Schwarz crystals. (a) The original Kelvin model of two ideal truncated-octahedra of equal volume (K1 and K2) in 1 by 1 packing. (b) 3D space-filling CTB network was constructed with a specified lattice orientation for individual grains. (c) A polycrystal of 16 grains with an initial grain size of $6 . 6 \ \mathrm { n m }$ was constructed using a 4 by 4 packing Kelvin model. (Reprinted with permission from Ref. [12]).

![](images/1226a36671b5b72e5541db22b13ab9c8a24647f0f30cc975e0f041fb028639f7.jpg)

![](images/77ba5304e182e43146311e31660ddc0fb0328e4721b354e537d0df4f73314381.jpg)  
Fig. 12—(a) MD-obtained twin-bounded polycrystalline structure at $_ { \mathrm { ~ 0 ~ K ~ } }$ , demonstrated by 2 by 2 by 2 supercells where atoms in FCC lattice sites are removed. (b) GBs resembling the Schwarz D-interface in a 1 by 1 by 1 supercell. (Reprinted with permission from Ref. [12]).

![](images/812da783dba3040d7f61f3013db1691c92fec86a2adf9bd58742b1ffaf91ca51.jpg)  
Fig. 13—The two MD-obtained thermal profiles (atomic volume vs temperature) indicate that the transformations from Kelvin crystal (KC) occur at 1172 K to D–SC I or at $1 2 5 0 \mathrm { ~ K ~ }$ to D–SC II well below the $T _ { E }$ (1358 K) of Cu. (Reprinted with permission from Ref. [100]).

extraordinary stability cannot be achieved, nor with the nanotwinned structures only.

As the sample was heated to temperatures in vicinity of the melting point, roughening of GBs occurs in the Schwarz-D structure, rather than grain coarsening. At 1321 K, liquid phase is heterogeneously nucleated, demonstrating the upper thermal stability limit of the Schwarz-D structure. This remarkable stability is consistent with what we observed experimentally (Figure 10). Simulations showed an evident grain size effect for the transformation kinetics and stability of the Schwarz-D structure. When an extended Kelvin polycrystal with a grain size of $6 . 5 4 ~ \mathrm { n m }$ is heated, it transformed into Schwarz-D interfaces (D-SC I and D-SC II) at $\sim 1 2 0 0 ~ \mathrm { K }$ (Figure 13),[100] of which stabilities are essentially the same. A reduced thermal stability of the Schwarz-D structure was noted with a decreasing grain size, see Figure 14(a).

![](images/d856f606abfdf6c45ed193b23e8b6a073d0dba0bb42e19483c5114739d939fe7.jpg)

![](images/33e0fb78940b658f9c817b6b915bea25dd5d5c3424e9948c83de1c0e5db6c15c.jpg)

![](images/ed71d29ef68ab1a2ad404588bf64119646f58fef340918e0d4e7972a93452ddd.jpg)  
Fig. 14—Grain size effect for the transformation kinetics and the thermal stability of the Schwarz-D structure. (a) Size dependence of thermal stability in D-type Schwarz crystal, $T _ { S } / T _ { E }$ vs $D _ { S } .$ . (b) MD structural symmetries of a D-SC I along $< 1 1 1 >$ orientations at 473 K, containing unit cells of $a \sim 6 . 5 \ \mathrm { \ n m }$ and $D _ { S } \sim 4 . 6 \ \mathrm { { \ n m } }$ . (c) A high-resolution TEM image of symbolic honeycombed grain with circular shape of an as-prepared Schwarz crystal Cu sample. (Reprinted with permission from Ref. [100]).

We conducted uniaxial tensile tests in MD simulations on the Schwarz-D structure constrained with CTB-networks at different temperatures and strain rates.[12] It was found the GB activities are suppressed entirely during the deformation, including GB sliding or GB migration. The primary deformation mode is twinning or generation of stacking faults, of which the

critical stress is temperature-dependent. The yield strength was found being $1 . 8 \mathrm { - } 2 \ \mathrm { G P a }$ at $3 0 0 ~ \mathrm { K }$ , which is larger than the experimental data. At $1 0 ~ \mathrm { K }$ , the strength increased to a value comparable to the ideal shear strength determined from first-principles calculations.[93]

From the MD simulations, we found the structural symmetries of Schwarz-D structure along $< 1 1 1 >$ orientations (Figure 14(b)) agree well with the symbolic honeycombed grains (Figure 14(c)) and the manifolded chains observed experimentally (Figure 6(a)). The dissociation of triple lines and junctions of GBs during the transformation to Schwarz-D structure may explain our high-resolution TEM images of the disappeared corners in the tiny polyhedron-shaped grains (Figures 8(a), (b)).

Based on the experimental evidences and MD simulation results, one may see that an extremely high thermal and mechanical stability is achievable in pure Cu with nano-sized grains in which the minimal-interface structure constrained by CTB-networks is adopted. The unique structure, termed as ‘‘Schwarz crystal’’, provides an alternative metastable state for polycrystals in metals, distinct from the amorphous solid states.

# D. Schwarz Crystal Structures in Various Metals and Alloys

By using the cryogenic high-pressure torsion process, grains were refined into several nanometers in a number of pure FCC metals with very different stacking fault energies. Analogous to that in Cu, the Schwarz crystal structures were identified in these metals with the extremely fine nanograins that exhibit extraordinary thermal stability and ultrahigh hardness. Taking Al (99.995 wt. pct pure) as an example, a typical Schwarz crystal structure was formed when grains were refined to about $6 \mathrm { n m }$ in average size as the plastic strain exceeds 50 under a pressure of $1 0 \mathrm { \ G P a }$ . The Schwarz crystal structure remains stable up to $9 2 8 { \mathrm { ~ K } } , \sim 0 . 9 9 { \mathrm { ~ \small ~  ~ } }$ $T _ { \mathrm { m } }$ of Al. Its hardness is unprecedented, as high as 2.51 GPa, well above $0 . 6 5 \mathrm { \ G P a }$ for $1 0 0 ~ \mathrm { { n m } }$ -grains.[101] A similar structure was formed in pure Pt after the cryogenic deformation, in which grain sizes are about $2 { \cdot } 3 \ \mathrm { n m }$ in average.[10 2] Roughly symmetric arrangement of the tiny grains can be identified (Figure 15), consistent with that in the MD simulation. Twins are frequently observed in the extremely fine Pt grains although the stacking fault energy is very high. Similarly, thermal stability of the Schwarz crystal structure is as high as $1 9 2 3 \mathrm { ~ K ~ }$ ${ \it \Omega } _ { [ - 0 . 9 4 \textit { T } _ { \mathrm { m } } }$ of Pt).

Schwarz crystal structures were also formed in Al-Mg[103] and Al-Zn[104] alloys through cryogenic high-pressure torsion. Both alloys consist of crystalline grains below $1 0 \ \mathrm { n m }$ in size with single-phased supersaturated Al solid solutions. Distribution of solute atoms are uniform throughout the samples without detectable segregation, nor with any precipitates in the as-prepared state. The Schwarz crystal structures of the supersaturated solid solution exhibit very high thermal stability against diffusional processes as will be discussed in the following section.

# IV. DIFFUSIONAL PROCESSES IN SCHWARZ CRYSTAL STRUCTURES

The most distinguished feature of the Schwarz crystal structure in metals is the extreme thermal stability against GB migration at elevated temperatures. It speaks that GBs in the Schwarz crystal are immobile at high temperatures, which is contradictory to our common believe that GBs provide fast diffusion channels for atom diffusion in polycrystalline metals.[105,106] To verify this unprecedented behavior, we investigated several diffusional processes in Schwarz crystal structures of Al-Mg and Al-Zn alloys because Al is a high-diffusivity metal with a low melting point, and $\mathrm { M g }$ and $Z \mathrm { n }$ are its most diffusive alloying elements in Al alloys.[107]

# A. Precipitation, Grain Coarsening, and Melting in Schwarz Crystal Al-Mg Alloys

By deforming a coarse-grained supersaturated $\mathbf { A l } ( \mathbf { M g } )$ solid solution sample with a 15 wt. pct $\mathrm { M g }$ using the cryogenic high-pressure torsion, we generated the Schwarz crystal structure in the single-phased $\mathbf { A l } ( \mathbf { M g } )$ samples with grains of $8 \ \mathrm { n m }$ in average size. The equilibrium phase diagram says that an Al-15 pctMg alloy is dual-phased (a-Al and $\mathrm { A l } _ { 3 } \mathrm { M g } _ { 2 } )$ ) below $7 0 0 ~ \mathrm { K }$ , a single $\mathscr { X }$ -Al solid solution at $7 0 0 ~ \mathrm { K }$ to 736 K, and $\alpha \cdot$ -Al mixing with liquid at $7 3 6 { - } 8 5 5 \mathrm { ~ K ~ }$ .[108] Several diffusional processes may occur when the supersaturated $\mathbf { A l } ( \mathbf { M g } )$ solution is heated to different temperatures. They include precipitation of $\mathbf { A l } 3 \mathbf { M } \mathbf { g } 2$ intermetallic phase (with concurrent coarsening for fine $\mathscr { X }$ -Al grains) below $7 0 0 ~ \mathrm { K }$ , coarsening of a-Al grains in the single phase region, and melting of the alloy above 736 K, in which diffusion of solute atoms plays a key role. These processes, as expected, were observed in the supersaturated solution of the same compositions with grains of ~ 50 nm in size in the respective temperature ranges, consistent with that in the coarse grains.[109–111]

A different scenario appeared when the Schwarz crystal sample was annealed at the corresponding temperatures. No precipitation was detected at all in the supersaturated $\mathbf { A l } ( \mathbf { M g } )$ solution after annealing from 373 to 723 K. Distributions of $\mathrm { M g }$ and Al atoms in the annealed samples are homogeneous, the same as that in the as-prepared samples, and no change in lattice constant of the $\mathscr { X }$ -Al phase was observed. It suggests $\mathrm { M g }$ atoms stay in the supersaturated $\mathscr { X }$ -Al nanograins in the entire temperature range studied, without segregation, or formation of intermetallic phases.

After annealing at $7 2 3 \mathrm { ~ K ~ }$ for 1 hour, measured sizes of $\mathscr { X }$ -Al grains increased slightly to $1 2 ~ \mathrm { n m }$ , whereas no change was detected in their geometry, lattice constant, and solute distribution. In the as-annealed sample, truncated octahedron-shaped grains were detected under High-resolution TEM, not different from those in the as-prepared state. The apparent across-boundary diffusivity was estimated in terms of the method in[26] using the measured grain size change in the annealed sample. It is about seven orders of magnitude smaller than that in the sample with 50 nm-grains.

![](images/8c7a5c43c6c3e474437a2e6baae59ff85f21f0887eb2298135b2d0a00abb1fb5.jpg)

![](images/84a3f786009c208287c9bd53e070987acfa1a3eb68f33e8c4a0a1bb5e7e6be27.jpg)

![](images/fbfdede084f0657e72a60a95c4511a12f6450857b7bb56828f14b9ddd6af28d7.jpg)  
Fig. 15—Structural characterization of the as-prepared Pt sample with extremely fine grains. (a) A typical HAADF-STEM image of the manifold structure. (b) A high-resolution STEM image showing the typical grain stacking. (c) A magnified image of a selected area in (a), showing grains with twin boundaries and the faceted {001} and {111} boundaries.

When the Schwarz crystal sample was annealed at $7 6 0 ~ \mathrm { K }$ (above the solidus temperature) for 1 hour, we observed an enlarged fluctuation in Mg concentration distribution (within $6 . 6 \sim 3 0 . 3 $ pct Mg), indicating redistribution of $\mathrm { M g }$ atoms. Partial melting was found only when the sample was heated above 805 K, 69 K above the solidus temperature. The increased melting temperature implies an insufficient atomic diffusion in the Schwarz crystal structures to induce melting of the Al-Mg alloy at the solidus temperature. These observations are summarized in Figure 16, suggesting these diffusional processes are effectively suppressed in the Schwarz crystal Al- $\mathbf { \nabla } \cdot \mathbf { M } \mathbf { g }$ sample, distinct from that in the nanograined and coarse-grained alloys.[72,109–112]

# B. Spinodal Decomposition in Schwarz Crystal Al-Zn Alloys

Spinodal decomposition in alloys with a miscibility gap is a benchmark process to suppress for stabilizing supersaturated phases. In spinodal alloys, composition fluctuations may result in a reduction of free energy, the supersaturated phase decomposes spontaneously through local ‘‘up-hill’’ diffusion without an energy barrier to nucleation, forming compositional modulations composed of two conjugate phases with the same lattice symmetry but different compositions.[26,113–115] Spinodal decomposition takes place in the very initial stage of many precipitation processes and eutectoid transformations, such as formation of G.P. zones in Al or Cu alloys and of cementite in steels.[26,116–118] Resisting atomic diffusion is essential to suppress

spinodal decompositions that are kinetically controlled by atomic diffusion only.

For exploring if the Schwarz crystal structure is able to inhibit atomic diffusion, we studied a typical spinodal Al-Zn alloy with a wide miscibility gap, in which spinodal decomposition may occur around ambient temperature.[119] By using the cryogenic high-pressure torsion, we produced the Schwarz crystal structure in the single-phased supersaturated $\mathbf { A l } ( Z \mathbf { n } )$ solution sample with 21.7 at.pctZn and an average grain size of $9 \ \mathrm { n m }$ Typical $D$ -type Schwarz crystals with topological manifold structures were formed, consisting of aggregates of irregular shapes made up of individual FCC $\mathscr { X }$ -Al nanograins, among which twin relationships were often identified. A homogeneous distribution of $Z \mathrm { n }$ atoms was noticed in the Schwarz crystal sample.

Annealing the Schwarz crystal sample at temperatures within the entire coherent miscibility gap $3 0 0 ~ \mathrm { K }$ to 494 K), we did not detect visible grain coarsening and any precipitate under TEM observation and electron diffraction. Microstructures and the EDS mapping of Zn atoms in the samples annealed at 494 K (2 K below the upper limit) for 1 h (and $^ { 1 0 \mathrm { h } }$ as well) remained the same as that before annealing. Tiny $\mathscr { X }$ -Al grains with faceted {111} and $\{ 2 0 0 \}$ boundaries were observed akin to that before annealing, and Zn atoms locate randomly in the $\mathscr { X }$ -Al grains. No change was detected in structure and composition as annealed at $5 2 3 \ \mathrm { K }$ , above the miscibility gap in the dual-phase region (Figure 17(a)). Measured onset temperatures for spinodal decomposition vary with grain sizes in a trend (Figure 17(b)) similar to that of the grain coarsening temperature in pure Cu and

![](images/2480ab7e2b754941587e1878f766a16df154c378694890464c43a5e62130bc9c.jpg)  
Fig. 16—Suppression of atomic diffusion with the Schwarz crystal structure in supersaturated Al-15wt. pct Mg alloys. (a) Measured lattice constant and Mg concentration as a function of annealing temperature for two samples with initial average grain sizes of $5 0 \ \mathrm { n m }$ and $8 \ \mathrm { n m }$ respectively. (b) Measured average size of $\varnothing$ -Al grains as a function of annealing temperature for the two samples. $\mathbf { A l } _ { 3 } \mathbf { M } \mathbf { g } _ { 2 }$ precipitate sizes in the $5 0 \ \mathrm { { \bar { n m } } }$ sample are included. (Reprinted with permission from Ref. [103]).

Ni.[10] The onset temperature decreases with a reduction of grain sizes above $\sim 1 0 0 ~ \mathrm { ~ n m }$ , consistent with the documented results.[119,120] Below a critical size, finer nanograins become more stable and their decomposition temperature increases to $4 2 3 \mathrm { ~ K ~ }$ at $1 6 ~ \mathrm { { n m } }$ . The Schwarz crystal samples with extremely fine-grains are so stable that the spinodal decomposition is inhibited in the entire dual-phase range, namely, the supersaturated Al-Zn solution is stabilized with the Schwarz crystal structure.

The completely suppressed spinodal decomposition in the Schwarz crystal sample means that transportation of Zn (and Al) atoms is inhibited across GBs and within

grain interiors as well. Given that the diffusional process is governed by the existence of vacancies, it is inferred that vacancies and their kinetics in the Schwarz crystal structures are responsible for the observed diffusion behaviors. The equilibrium vacancy concentration $( C _ { \mathrm { v } } ^ { \mathrm { ~ e ~ } } )$ in FCC metals can be estimated using[2] $C _ { \mathrm { v } } ^ { \mathrm { ~ e ~ } } = A$ exp $( - E _ { \mathrm { v } } / k _ { \mathrm { B } } T )$ , where $A$ is a constant, $E _ { \mathrm { v } }$ is the formation enthalpy of vacancies, $k _ { \mathrm { B } }$ is the Boltzmann’s constant and $T$ the temperature. For $\mathscr { X }$ -Al, the calculated equilibrium vacancy concentration $C _ { \bf v } ^ { \mathrm { ~ e ~ } }$ is about $2 . 2 8 \times 1 \dot { 0 } ^ { - 6 }$ at $4 9 6 \mathrm { K }$ , approximately one vacancy in a grain of about $1 5 \ \mathrm { n m }$ . It suggests at this temperature grains smaller than $1 5 ~ \mathrm { { n m } }$ are too small to permit a vacancy to stay in

![](images/94b6076cac8c7a91ada63e8ebb0b753a35112f4915a39eaf716d0b20a7fe370a.jpg)  
(a)

![](images/0113370e2f8e63c47857b326383ed2383b4de29c02e42d19dd1e15fe9e1e1511.jpg)  
(b)   
Fig. 17—Suppression of spinodal decomposition with Schwarz crystal supersaturated Al-21.7at.pct Zn alloys. (a) Compositions of Al-rich and Zn-rich phases from spinodal decomposition in the $\mathbf { A l } ( Z \mathbf { n } )$ samples with different grain sizes after annealing at various temperatures (indicated) plotted in the equilibrium phase diagram of binary Al-Zn alloys. $( b )$ Measured onset temperature of spinodal decomposition as a function of initial grain size of the $\mathbf { A l } ( Z \mathbf { n } )$ samples. Data from the literatures[119,120] are included for comparison. (Reprinted with permission from Ref. [104]).

grain interiors, from a thermodynamic point of view. Hence, it is reasonable to infer that lattice diffusion in the extremely fine grains that are essentially vacancy-free (and dislocation-free as well), is inhibited as substitutional diffusion coefficients are proportional to the probability of finding a vacancy adjacent to the diffusing atoms, despite of the enhanced atomic vibration frequencies at elevated temperatures.

In terms of the classical grain growth kinetics model,[26,103] we estimated the apparent across-boundary diffusivity in the Schwarz crystal Al-Zn sample, being about $7 . 8 \times 1 0 ^ { - 2 2 } \ \mathrm { m } ^ { 2 } \mathrm { s } ^ { - 1 }$ at $4 9 4 \ \mathrm { ~ K ~ }$ , about 10 orders of magnitude lower than the calculated diffusion coefficient of Zn at GBs of Al.[121] The much lower diffusivity agrees with that in the Schwarz crystal Al- $\mathbf { M } \mathbf { g }$ alloy,[103] implying the atomic transportation across the minimal interfaces is inhibited. Nevertheless, more comprehensive understanding of atomic diffusion mechanisms across and along the GBs in the Schwarz crystal structure need more in-depth investigations in the future, both experimentally and theoretically.

From the MD simulations, we found the GBs with minimal interface topology and zero-mean-curvature are structurally stable under thermal and mechanical stimuli, even at temperatures few degrees prior to melting. The constraint from the stable twin boundary networks may also contribute to the inherent stability. The effective constraint makes the interface migration very difficult to deviate from their stable topology, implying that transporting atoms across the boundaries is prohibited. In other words, the intensive constraint of the interfaces greatly reduces the possibility for atoms to flow (or jump) from one side of the boundary to another. While the experimental evidences are solid for

the suppressed atomic diffusion in Schwarz crystal metals and alloys, the underlying mechanisms of diffusion of atoms in the novel structures are far from well understood. Clarifying atomic diffusion behaviors within the tiny grains and along the high-density GBs with TPMS topology, as well as across the boundaries needs further in-depth experimental and theoretical investigations in the future.

# V. SUMMARY AND PERSPECTIVES

Formation of Schwarz crystal structures is a stabilization process of polycrystalline metals with extremely fine grains without eliminating the large number of disordered GBs, which differs fundamentally from the GB-elimination processes known so far such as grain coarsening and amorphization (Figure 18). In such a process, atoms at GBs, together with those inside crystallites, find their own way to ‘‘emerge’’ into an atomic-level TPMS structure. In this sense, the formation process of Schwarz crystal seems a ‘‘self-assembly-like’’ structure evolution in metals triggered by intensive plastic straining at cryogenic temperatures. The transformation process itself is magic indeed, behind which many mysteries are buried, e.g., what governs the transformation kinetics? Are there any other processes that can induce the transformation? And so on.

The Schwarz crystal structure offers an alternative metastable state for polycrystalline metals when their grains are extremely refined, which is more stable than amorphous solids. The superior stability of GBs originates from their unique topology with

![](images/71caaffd61ba756448d7d0ac56ffb4dee661a2084d6018a5a518396fe5338623.jpg)  
Fig. 18—A schematic diagram illustrating stabilization approaches of nanograined structures in metals. Grain coarsening and amorphization are well-documented processes in which GBs are eliminated for reducing the total excess energy. A different stabilization process is transforming into the Schwarz crystal structure in which GBs are stabilized with the minimal interface structures and zero-mean-curvature.

zero-mean-curvature. The stabilization principle is obviously different from that of the traditional strategies with chemistry. Some crucial questions behind the nontrivial phenomena deserve future exploration. Are there alternative metastable TPMS structures in metals and any correlations between the lattice structure and the TPMS structures? What roles do CTBs play in formation of the Schwarz crystal structure? What are the alloying effects on Schwarz crystal formation? Why glasses are formed in some alloys rather than Schwarz crystal structures? In other words, what is the key factor to switch the structure selection between the Schwarz crystal and glass?

We have already observed a number of outstanding properties in Schwarz crystal metals and alloys, including the extremely high structure stability against thermal and mechanical stimuli as well as the inhibited atomic diffusion at high temperatures. While the intrinsic mechanism underlying these behaviors are ambiguous so far, the novel structure offers emerging opportunities for uncovering new phenomena and physical or chemical behaviors in metals. Particularly, transport dynamics of atoms and electrons at the Schwarz crystal interfaces, as well as the interactions and evolutions of various defects at elevated temperatures deserve further exploration.

In principle, the Schwarz crystal structures are accessible in different kinds of metals and alloys, which may provide alternative directions for designing and processing strong and stable materials for high-temperature applications. As a benchmark structure capable of inhibiting atomic diffusion at elevated temperatures, the Schwarz crystal offers new opportunities to overcome some corner-stone difficulties in traditional strategies for material processing and development.

# ACKNOWLEDGMENTS

I sincerely thank Prof. X.Y. Li, Prof. Z.H. Jin, Dr. X. Zhou, Dr. W. Xu, and Prof. B. Zhang for their contributions to this study. Stimulating discussions and assistance from my colleagues and students are very much appreciated. This work was supported by the Ministry of Science and Technology of China (Grants Nos.: 2017YFA0700700 and 2017YFA0204401) and the Chinese Academy of Sciences (Grant: zdyz201701).

# CONFLICT OF INTEREST

The author states that there is no conflict of interest.

# REFERENCES

1. X. Sauvage, G. Wilde, S.V. Divinski, Z. Horita, and R.Z. Valiev: Mater. Sci. Eng. A, 2012, vol. 540, pp. 1–2.   
2. P. Haasen, P. Haasen, and B.L. Mordike: Physical metallurgy, Cambridge University Press, Cambridge, 1996.   
3. C.C. Koch, R.O. Scattergood, K.A. Darling, and J.E. Semones: J. Mater. Sci., 2008, vol. 43, pp. 7264–72.   
4. R. Birringer: Mater. Sci. Eng. A, 1989, vol. 117, pp. 33–43.   
5. K. Lu: Nat. Rev. Mater., 2016, vol. 1, pp. 1–3.   
6. R. Zallen: The physics of amorphous solids, Wiley, New York, 2008.   
7. B. Fa¨ rber, E. Cadel, A. Menand, G. Schmitz, and R. Kirchheim: Acta Mater., 2000, vol. 48, pp. 789–96.   
8. C.A. Schuh, T.G. Nieh, and H. Iwasaki: Acta Mater., 2003, vol. 51, pp. 431–43.   
9. S.Y. Ruan and C.A. Schuh: Acta Mater., 2009, vol. 57, pp. 3810–22.   
10. X. Zhou, X.Y. Li, and K. Lu: Science, 2018, vol. 360, pp. 526–30.   
11. X. Zhou, X. Li, and K. Lu: Phys. Rev. Lett., 2019, vol. 122, 126101.   
12. X.Y. Li, Z.H. Jin, X. Zhou, and K. Lu: Science, 2020, vol. 370, pp. 831–36.

13. H.A. Schwarz: Miscellen aus dem Gebiete der Minimalfla¨chen, Springer, Berlin, 1890.   
14. K. Lu and J. Lu, J. Mater. Sci. Technol. 1999.   
15. Y. Saito, H. Utsunomiya, N. Tsuji, and T. Sakai: Acta Mater., 1999, vol. 47, pp. 579–83.   
16. N. Hansen: Metall. Mater. Trans. A, 2001, vol. 32A, pp. 2917–35.   
17. R.Z. Valiev and T.G. Langdon: Prog. Mater. Sci., 2006, vol. 51, pp. 881–981.   
18. W.L. Li, N.R. Tao, and K. Lu: Scr. Mater., 2008, vol. 59, pp. 546–49.   
19. H.W. Huang, Z.B. Wang, J. Lu, and K. Lu: Acta Mater., 2015, vol. 87, pp. 150–60.   
20. N.R. Tao, Z.B. Wang, W.P. Tong, M.L. Sui, J. Lu, and K. Lu: Acta Mater., 2002, vol. 50, pp. 4603–16.   
21. W. Xu, X.C. Liu, X.Y. Li, and K. Lu: Acta Mater., 2020, vol. 182, pp. 207–14.   
22. T.H. Fang, W.L. Li, N.R. Tao, and K. Lu: Science, 2011, vol. 331, pp. 1587–90.   
23. X.C. Liu, H.W. Zhang, and K. Lu: Science, 2013, vol. 342, pp. 337–40.   
24. H.L. Fu, X. Zhou, H.T. Xue, X.Y. Li, and K. Lu: Mater. Today, 2022, vol. 55, pp. 66–73.   
25. M. Hillert: Acta Metall., 1965, vol. 13, pp. 227–38.   
26. D.A. Porter and K.E. Easterling: Phase transformations in metals and alloys (revised reprint), CRC Press, New York, 2009.   
27. K.A. Darling, B.K. VanLeeuwen, C.C. Koch, and R.O. Scattergood: Mater. Sci. Eng. A, 2010, vol. 527, pp. 3572–580.   
28. T.J. Chookajorn, H.A. Murdoch, and C.A. Schuh: Science, 2012, vol. 337, pp. 951–54.   
29. J. Hu, Y.N. Shi, X. Sauvage, G. Sha, and K. Lu: Science, 2017, vol. 355, pp. 1292–296.   
30. C.A. Schuh and K. Lu: MRS Bull., 2021, vol. 46, pp. 225–35.   
31. D. Jang and M. Atzmon: J. Appl. Phys., 2006, vol. 99, 083504.   
32. J.D. Rittner, D.N. Seidman, and K.L. Merkle: Phys. Rev. B, 1996, vol. 53, p. R4241.   
33. H. Van Swygenhoven, P.M. Derlet, and A. Hasnaoui: Phys. Rev. B, 2002, vol. 66, 024101.   
34. K.L. Merkle: Microsc. Microanal., 1997, vol. 3, pp. 339–51.   
35. K.C. Chen, W.W. Wu, C.N. Liao, L.J. Chen, and K.N. Tu: Science, 2008, vol. 321, pp. 1066–069.   
36. V. Yamakov, D. Wolf, S.R. Phillpot, A.K. Mukherjee, and H. Gleiter: Nat. Mater., 2004, vol. 3, pp. 43–7.   
37. X. Zhou, Z. Feng, L. Zhu, J. Xu, L. Miyagi, H. Dong, H. Sheng, Y. Wang, Q. Li, Y. Ma, H. Zhang, J. Yan, N. Tamura, M. Kunz, K. Lutker, T. Huang, D.A. Hughes, X. Huang, and B. Chen: Nature, 2020, vol. 579, pp. 67–72.   
38. Y.T. Zhu, X.Z. Liao, and X.L. Wu: Prog. Mater. Sci., 2012, vol. 57, pp. 1–62.   
39. H. Van Swygenhoven, P.M. Derlet, and A.G. Frøseth: Nat. Mater., 2004, vol. 3, pp. 399–403.   
40. M.W. Chen, E. Ma, K.J. Hemker, H.W. Sheng, Y.M. Wang, and X.M. Cheng: Science, 2003, vol. 300, pp. 1275–277.   
41. B. Wang, W. Xu, X. Zhou, X.Y. Li, and J.S. Qiao: Scr. Mater., 2021, vol. 203, 114054.   
42. X.K. Guo, Z.P. Luo, X.Y. Li, and K. Lu: Mater. Sci. Eng. A, 2021, vol. 802, 140664.   
43. E. Orowan: Inst. Metals. Lond., 1948, vol. 451, pp. 451–53.   
44. M. Legros, B.R. Elliott, M.N. Rittner, J.R. Weertman, and K.J. Hemker: Philos. Mag. A, 2000, vol. 80, pp. 1017–026.   
45. X.Y. Li, X. Zhou, and K. Lu: Sci. Adv., 2020, vol. 6, p. 8003.   
46. X. Zhou, X.Y. Li, and K. Lu: Scr. Mater., 2020, vol. 187, pp. 345–49.   
47. S. Brandstetter, K. Zhang, A. Escuadro, J.R. Weertman, and H. Van Swygenhoven: Scr. Mater., 2008, vol. 58, pp. 61–4.   
48. H.M. Wen, Y.H. Zhao, Y. Li, O. Ertorer, K.M. Nesterov, R.K. Islamgaliev, R.Z. Valiev, and E.J. Lavernia: Philos. Mag., 2010, vol. 90, pp. 4541–550.   
49. W. Chen, Z.S. You, N.R. Tao, and L. Lu: IOP Conf. Ser. Mater. Sci. Eng., 2015, vol. 89, 012001.   
50. W. Xu, B. Zhang, K. Du, X.Y. Li, and K. Lu: Acta Mater., 2022, vol. 226, 117640.   
51. Y. A. Sun, Z. P. Luo, X. Y. Li and K. Lu, Acta Mater. 2022, vol. 239.   
52. B.B. Zhang, Y.G. Tang, Q.S. Mei, X.Y. Li, and K. Lu: Science, 2022, vol. 378, pp. 659–63.

53. J. Eckert, J.C. Holzer, C.E. Krill, and W.L. Johnson: J. Mater. Res., 1992, vol. 7, pp. 1751–761.   
54. E. Hellstern, H.J. Fecht, Z. Fu, and W.L. Johnson: J. Appl. Phys., 1989, vol. 65, pp. 305–10.   
55. J.W. Cahn: Acta Metall., 1962, vol. 10, pp. 789–98.   
56. J.P. Drolet and A. Galibois: Acta Metall., 1968, vol. 16, pp. 1387–399.   
57. K. Edalati, J.M. Cubero-Sesin, A. Alhamidi, I.F. Mohamed, and Z. Horita: Mater. Sci. Eng. A, 2014, vol. 613, pp. 103–10.   
58. Y. Zhang, N.R. Tao, and K. Lu: Acta Mater., 2008, vol. 56, pp. 2429–440.   
59. P. Jenei, J. Gubicza, E.Y. Yoon, H.S. Kim, and J.L. La´ ba´ r: Compos. A Appl. Sci. Manuf., 2013, vol. 51, pp. 71–9.   
60. K. Oh-ishi, Z. Horita, D.J. Smith, R.Z. Valiev, M. Nemoto, and T.G. Langdon: J. Mater. Res., 1999, vol. 14, pp. 4200–207.   
61. N.N. Liang, Y.H. Zhao, Y. Li, T. Topping, Y.T. Zhu, R.Z. Valiev, and E.J. Lavernia: J. Mater. Sci., 2018, vol. 53, pp. 13173–3185.   
62. N. Lugo, N. Llorca, J.J. Sunol, and J.M. Cabrera: J. Mater. Sci., 2010, vol. 45, pp. 2264–273.   
63. G. Benchabane, Z. Boumerzoug, I. Thibon, and T. Gloriant: Mater Charact, 2008, vol. 59, pp. 1425–428.   
64. R.K. Islamgaliev, F. Chmelik, and R. Kuzel: Mater. Sci. Eng. A, 1997, vol. 237, pp. 43–51.   
65. A.P. Zhilyaev and T.G. Langdon: Prog. Mater. Sci., 2008, vol. 53, pp. 893–979.   
66. A. Rohatgi, K.S. Vecchio, and G.T. Gray: Metall. Mater. Trans. A, 2001, vol. 32A, pp. 135–45.   
67. Y. Zhang, N.R. Tao, and K. Lu: Acta Mater., 2011, vol. 59, pp. 6048–058.   
68. M. Saber, H. Kotan, C.C. Koch, and R.O. Scattergood: J. Appl. Phys., 2013, vol. 113, 063515.   
69. O.F. Higuera-Cobos and J.M. Cabrera: Mater. Sci. Eng. A, 2013, vol. 571, pp. 103–14.   
70. F. Emeis, M. Peterlechner, S.V. Divinski, and G. Wilde: Acta Mater., 2018, vol. 150, pp. 262–72.   
71. R.Z. Valiev, N.A. Enikeev, M.Y. Murashkin, V.U. Kazykhanov, and X. Sauvage: Scr. Mater., 2010, vol. 63, pp. 949–52.   
72. X. Sauvage, N. Enikeev, R. Valiev, Y. Nasedkina, and M. Murashkin: Acta Mater., 2014, vol. 72, pp. 125–36.   
73. R.P. Singh and R.D. Doherty: Metall. Trans. A, 1992, vol. 23A, pp. 321–34.   
74. H. De Cicco, M.I. Luppo, L.M. Gribaudo, and J. Ovejero-Garcıa: Mater Charact, 2004, vol. 52, pp. 85–92.   
75. G.F. Harrison, W.J. Evans, and M.R. Winstone: Mater. Sci. Technol., 2009, vol. 25, pp. 249–57.   
76. G.M. Han, J.J. Yu, Z.Q. Hu, and X.F. Sun: Mater Charact, 2013, vol. 86, pp. 177–84.   
77. T.W. Ni and J.X. Dong: Mater. Sci. Eng. A, 2017, vol. 700, pp. 406–15.   
78. M. Whittaker, W. Harrison, C. Deen, C. Rae, and S. Williams: Materials, 2017, vol. 10, p. 61.   
79. W. Longley and T.J. McIntosh: Nature, 1983, vol. 303, pp. 612–14.   
80. C. Chieh: Acta Cryst., 1979, vol. 35, pp. 946–52.   
81. A. Kumpmann, B. Gu¨ nther, and H.D. Kunze: Mater. Sci. Eng. A, 1993, vol. 168, pp. 165–69.   
82. Y. Li, Y. Zhang, N. Tao, and K. Lu: Scr. Mater., 2008, vol. 59, pp. 475–78.   
83. Z.N. Mao, R.C. Gu, F. Liu, Y. Liu, X.Z. Liao, and J.T. Wang: Mater. Sci. Eng. A, 2016, vol. 674, pp. 186–92.   
84. C. Saldana, A.H. King, and S. Chandrasekar: Acta Mater., 2012, vol. 60, pp. 4107–116.   
85. B.W. Zhang, X.L. Shu, S.Y. Zhu, and S.Z. Liao: J. Mater. Proc. Tech., 1999, vol. 91, pp. 90–4.   
86. H. Zhang, Z. Tan, B. Zhang, X. Shu, and J. Yu: J. Mater. Sci. Lett., 1991, vol. 10, pp. 45–6.   
87. A.H. Chokshi, A. Rosen, J. Karch, and H. Gleiter: Scr. Metall., 1989, vol. 23, pp. 1679–683.   
88. G.E. Fougere, J.R. Weertman, and R.W. Siegel: Nanostruct. Mater., 1993, vol. 3, pp. 379–84.   
89. H.G. Jiang, Y.T. Zhu, D.P. Butt, I.V. Alexandrov, and T.C. Lowe: Mater. Sci. Eng. A, 2000, vol. 290, pp. 128–38.   
90. L. Lu, X. Chen, X. Huang, and K. Lu: Science, 2009, vol. 323, pp. 607–10.

91. P.G. Sanders, J.A. Eastman, and J.R. Weertman: Acta Mater., 1997, vol. 45, pp. 4019–025.   
92. W.H. Wang: J. Appl. Phys., 2006, vol. 99, 093506.   
93. S. Ogata, J. Li, and S. Yip: Science, 2002, vol. 298, pp. 807–11.   
94. L. Kelvin (Sir William Thomson), Philos. Mag. 1887, vol. 24, pp. 503-514.   
95. F.N. Rhines, K.R. Craig, and R.T. DeHoff: Metall. Trans., 1974, vol. 5, pp. 413–25.   
96. V.Y. Gertsman and B.W. Reed: Z. Metallk., 2005, vol. 96, pp. 1106–111.   
97. V. Borovikov, M.I. Mendelev, A.H. King, and R. LeSar: Model. Simul. Mater. Sci. Eng., 2015, vol. 23, 055003.   
98. A.L. Mackay: Nature, 1985, vol. 314, pp. 604–06.   
99. L.E. Scriven: Nature, 1976, vol. 263, pp. 123–25.   
100. Z.H. Jin, X.Y. Li, and K. Lu: Phys. Rev. Lett., 2021, vol. 127, 136101.   
101. L. Fang, Y.M. Zhong, B. Wang, W. Xu, X.Y. Li, and K. Lu: Mater. Res. Lett., 2023, vol. 11, pp. 662–69.   
102. H.L. Fu, X. Zhou, Z.H. Jin, Z.P. Guo, X.Y. Li, and K. Lu, Phys. Rev. Lett. 2023, submitted.   
103. W. Xu, B. Zhang, X.Y. Li, and K. Lu: Science, 2021, vol. 373, pp. 683–87.   
104. W. Xu, Y.M. Zhong, X.Y. Li, and K. Lu: Adv. Mater., 2023, vol. 230650, pp. 1–7.   
105. H. Mehrer: Diffusion in solids: fundamentals, methods, materials, diffusion-controlled processes, Springer, Berlin, 2007.   
106. S.V. Divinski, G. Reglitz, H. Ro¨ sner, Y. Estrin, and G. Wilde: Acta Mater., 2011, vol. 59, pp. 1974–985.   
107. Y. Du, Y.A. Chang, B.Y. Huang, W.P. Gong, Z.P. Jin, H.H. Xu, Z.H. Yuan, Y. Liu, Y.H. He, and F.Y. Xie: Mater. Sci. Eng. A, 2003, vol. 363, pp. 140–51.   
108. H. Okamoto and T. Massalski, Binary Alloy Phase Diagrams (ASM International, 1990).   
109. S. Nebti, D. Hamana, and G. Cizeron: Acta Metall. Mater., 1995, vol. 43, pp. 3583–588.

110. W. Xu, Y.C. Xin, B. Zhang, and X.Y. Li: Acta Mater., 2022, vol. 225, 117607.   
111. M.J. Starink and A.M. Zahra: Materials Science Forum (Trans Tech Publications. N. Y., 1996, vol. 217–222, pp. 795–800.   
112. L. Guan, Y. Zhou, B. Zhang, J.Q. Wang, E.H. Han, and W. Ke: Corros. Sci., 2016, vol. 103, pp. 255–67.   
113. J.W. Cahn: Acta Metall., 1961, vol. 9, pp. 795–801.   
114. M. Hillert: Acta Metall., 1961, vol. 9, pp. 525–35.   
115. A. Kwiatkowski da Silva, D. Ponge, Z. Peng, G. Inden, Y. Lu, A. Breen, B. Gault, and D. Raabe: Nat. Commun., 2018, vol. 9, p. 1137.   
116. K.T. Moore, W.C. Johnson, J.M. Howe, H.I. Aaronson, and D.R. Veblen: Acta Mater., 2002, vol. 50, pp. 943–56.   
117. B. Ditchek and L.H. Schwartz: Acta Metall., 1980, vol. 28, pp. 807–22.   
118. E.P. Butler and G. Thomas: Acta Metall., 1970, vol. 18, pp. 347–65.   
119. K.B. Rundman and J.E. Hilliard: Acta Metall., 1967, vol. 15, pp. 1025–033.   
120. B.B. Straumal, B. Baretzky, A.A. Mazilkin, F. Phillipp, O.A. Kogtenkova, M.N. Volkov, and R.Z. Valiev: Acta Mater., 2004, vol. 52, pp. 4469–478.   
121. D.L. Beke, I. Go¨ de´ ny, G. Erdelyi, and F.J. Kedves: Philos. Mag. A, 1987, vol. 56, pp. 659–71.

Publisher’s Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.