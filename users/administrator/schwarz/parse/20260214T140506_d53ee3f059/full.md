# Isotropic grain boundaries and size-dependent thermal stability of Schwarz crystals Cu and Al at nanoscales

![](images/53fb1e36ff8f2358526a786726b1d4d065e86990947329a8cfad67ccc49d7af8.jpg)

Dan Yang $\mathrm { a , b } _ { \mathbb { \Phi } ( \mathbb { D } ) }$ , Zhipeng Gao b,c , Fuling Tang a , Zhaohui Jin b,*

a State Key Laboratory of Advanced Processing and Recycling of Non-ferrous Metals, School of Materials Science and Engineering, Lanzhou University of Technology, Lanzhou 730050, PR China   
b Shenyang National Laboratory for Materials Science, Institute of Metal Research, Chinese Academy of Sciences, 72 Wenhua Road, Shenyang 110016, PR China   
c School of Materials Science and Engineering, University of Science and Technology of China, Shenyang 110016, PR China

# A R T I C L E I N F O

Keywords:

Schwarz crystal

Grain-boundary

Thermal stability

Grain coarsening

Molecular dynamics simulation

# A B S T R A C T

Schwarz crystals consisting of triply periodic minimal surface grain boundaries of different shapes were studied for face-centered cubic metals Al and Cu via atomistic modeling and simulations. The thermal stabilities of those curvy grain boundaries depend on shape, spacing between grain boundaries and how closely the grain boundary energies fulfill the isotropic condition. Schwarz crystals consisting of energetically less anisotropic grain boundaries are thermally more stable. Destabilization occurs when shapes of grain boundaries deviate significantly from the ideal minimal-surface morphologies. A thermodynamic model was proposed to describe the sizedependent thermal stability exhibited by primary Schwarz crystals at nanoscales.

Processing, manufacturing, performance and reliability of engineering materials rely on thermally stable material microstructures. Grain boundaries (GBs) are the major elements of polycrystalline structures and they are kinetically mobile [1]. The structural stability of polycrystals depends on how to impinge the moment of GBs as well as the 3-dimentional (3D) collective network they formed such that grain growth or grain coarsening can be effectively inhibited. However, arresting grain growth or coarsening in polycrystalline metals remains challenging because GBs are highly diffusive and mobile at high temperatures, in particular, when grain sizes are below 100 nm [2–5].

Recently, a class of new structure called Schwarz crystal (SC) has been revealed in polycrystals such as Cu [6,7]. The SC structure is unique because GB segments in conventional polycrystals (e.g., Kelvin crystals (KCs) [7]) have been entirely replaced by a GB morphology resembling mathematically a well-known minimal surface, i.e., a surface of vanishing mean curvature everywhere. Quadrupolar network of Σ3 {111} coherent twin boundaries (CTBs) contribute significantly to lock and hence stabilize the GB network. Driving forces promoting GB migration can be eliminated effectively at the zero mean-curvature GBs. Nucleating and propagating Shockley twinning partial dislocations from GB sites intersecting with twins may render the structure unstable. However, such processes are energetically demanding to operate. Therefore, triply periodic minimal surface (TPMS) GBs locked by twins

are extremely stable to against thermal fluctuations or externally applied forces. As observed in both experiments and molecular dynamics (MD) simulations, grain coarsening can be inhibited up to temperatures close to the equilibrium melting point and the Hall-Petch relationship may hold up to limiting grain sizes of a few nanometers even for metals not readily-to-twin, such as Pt [8].

Microstructure elements of polycrystals in general are treated topologically as space-filling polyhedrons where GB segments connected by triple lines (triple junctions in 2D) meeting at quadruple points (fouredge junctions or nodes in 3D) constitute a GB network, analogous to soap froth or foams [9,10]. SCs, on the other hand, consist of smooth, continuous and non-self-intersecting interfaces of vanishing mean curvature - a geometrical subject different from that in traditional grain growth theory. So far, it remains intriguing to address the kinetics of GBs resembling minimal-surface morphologies.

To put forward more clearly, an illustrative situation has been shown in Fig. 1. The plots in Fig. 1(a) demonstrate three SCs of identical parent grain lattices and supercell sizes $1 0 . 8 \mathrm { n m }$ for Cu and $1 2 \mathrm { n m }$ for Al) in our MD simulations. However, the GBs in the three samples divide space in different ways according to mathematically well-known TPMS geometries, i.e., primary $( P )$ , diamond $( D )$ and gyroid (G), respectively [11] (see also supplemental). These TPMS configurations exhibit different thermal stabilities measured by temperatures at which GBs start to

migrate or escape away from the initial and ideal TPMS boundaries. The P-SC is most stable $( \sim 0 . 5 2 ~ T _ { \mathrm { E } }$ for Cu and ~ 0.62 $T _ { \mathrm { E } }$ for Al), the G-SC is less stable $( \sim 0 . 4 1$ $T _ { \mathrm { E } }$ for Cu and $\sim 0 . 5 9 ~ T _ { \mathrm { E } }$ for Al) and the D-SC is the least stable $( \sim 0 . 2 7 ~ T _ { \mathrm { E } }$ for Cu and ~ 0.48 TE for Al), as measured by a reduced temperature with respect to the thermal equilibrium melting point, $T _ { \mathrm { E } }$ (Table 1).

Our MD observations suggest that the thermal stability depends strongly on the shape of the embedded minimal surfaces. Geometrically, the GB surface area (S) is different, with $S ( P ) { : } S ( D ) { : } S ( G ) = 1 { : } 1 . 0 3 1 { : } 1 . 0 4 6$ [11]. Assuming that TPMS GBs are isotropic, or, GB energies $( \gamma _ { G B } )$ are everywhere the same, the most unstable SC should be $G$ rather than $D$ , which is not the case in our MD simulations. On the other hand, our calculated GB energies (Fig. 1b) are significantly different, with $\gamma _ { G B } ( P ) <$ $\gamma _ { G B } ( G ) < \gamma _ { G B } ( D )$ and they correlate almost linearly with the fraction of GB atoms or the GB thickness $( d _ { \tt G B } )$ . That is, the number of GB atoms $( N _ { \mathrm { G B } } )$ are different due to that the shapes of the three GB morphologies are different, or, the negative Gaussian curvature are inequivalent for the three TPMS geometries. Therefore, neither smaller surface area means smaller fraction of GB atoms nor GB energies in average are nearly the same seems always true.

According to the theory of capillarity for a two-phase system at equilibrium, since at any point of a TPMS interface the mean curvature, $\begin{array} { r } { K ( { \bf n } ) = \frac { 1 } { { \mathrm R } _ { 1 } } + \frac { 1 } { { \mathrm R } _ { 2 } } } \end{array}$ (where $R _ { 1 }$ and $R _ { 2 }$ are the principal radii of curvature for a

given point at the curvy surface and n is the unit normal vector at that point), is presumably zero, the pressure difference is essentially zero according to the Young-Laplace formula (or Gibbs-Thomson equation).

$$
\Delta P (\mathbf {n}) = \gamma_ {i} (\mathbf {n}) K (\mathbf {n}) = 0 \tag {1}
$$

Accordingly, regardless the n-dependence of interfacial energy $\gamma _ { i } ,$ no interface motion should occur as the driving pressure for a moving interface vanishes everywhere at the interface.

For a dynamic system, variations of local GB area or shape from equilibrium are inevitable. The mean curvature $K ( \mathbf { n } , T , t )$ as a function of temperature (T) and time (t) should undergo noticeable variations under thermal fluctuations such that Eq. (1) no longer holds. Similar to morphological evolution at surfaces which tend to develop Wulff shape in terms of the surface-tension plot $( \gamma$ -plot) [15], the orientation dependence of the GB energies, $\gamma _ { G B } ( \mathbf { n } )$ , needs to be considered. Inversely, to render a TPMS interface as stable as possible, it requires that GB energies should deviate not too much from the isotropic condition

$$
\gamma_ {G B} (\mathbf {n}) = \gamma_ {G B} ^ {0} = \text {c o n s t .} \tag {2}
$$

Thus, Eq. (2) provides a measure to evaluate thermal stabilities attainable for different SCs such as those shown in Fig. 1.

The procedure in principle requires that the entire $3 D \gamma _ { G B } ( \mathbf { n } )$ -plot is

![](images/f000591e2f114c829933a67150adcfdd1b4aae690c6099eac6428e77141b4d46.jpg)  
(a）£9TPMS GBs

![](images/6bdba6091f5ad6a4467c9026afcbc6ffccc1feac223048a108dfdd1e76214f39.jpg)

![](images/474bb5be61459c98adcb06bb70cc0a060bbc829527d4d7f44df6f94a65b134a5.jpg)

![](images/4856d51bb6d53e7c79f0fe0789b0828c485117c79d542c33538b291c97e9ec9f.jpg)  
Fig. 1. (a) GB morphologies of SCs (Cu and Al) resembling $P _ { \cdot }$ , $D$ and $G$ TPMSs in MD simulations constructed with grain lattice orientations following Σ9 GBs, i.e., $x$ [011], y [411], $\mathscr { z }$ [122] vs. x [011], $y$ [411], $\mathfrak { z }$ [122]. Atoms belong to grain lattice sites were removed. (b) Thermal stabilities exhibited by P-SC, $_ { D - S C }$ and $G$ -SC. Inset: MD calculated mean GB energies as a function of fraction of GB atoms in each SC. GB atoms are identified using common neighbor analyses (CNA) [12]. The apparent GB thickness $( d _ { \tt G B } )$ is defined as the excess volume of GB atoms divided by the ideal area of TPMS GBs, which correlates with $\mathbf { f } _ { \mathrm { G B } }$ almost linearly $( d _ { G B } ( n m ) \simeq 4 . 2 5 f _ { G B } )$ ) for both Cu and Al.

Table 1 MD calculated material properties, averaged GB energies and the fitted GB ’escapability’ measure (ε) according to Eq. (4) for different SCs of Cu and Al.   

<table><tr><td rowspan="2"></td><td rowspan="2">TE(K)</td><td rowspan="2">Ω0(Å3/atom)</td><td colspan="3">γGB(J/m2)</td><td rowspan="2">Lm(eV/atom)</td><td colspan="3">ε</td></tr><tr><td>P (ID)</td><td>P (AD)</td><td>D (Σ9)</td><td>P (ID)</td><td>P (AD)</td><td>D (Σ9)</td></tr><tr><td>Cu</td><td>1356a</td><td>12.047</td><td>1.1099</td><td>1.1723</td><td>1.4548</td><td>0.135</td><td>12.5</td><td>18</td><td>38.28</td></tr><tr><td>Al</td><td>890b</td><td>16.387</td><td>0.665</td><td>0.6578</td><td>0.9357</td><td>0.112</td><td>7.5</td><td>10</td><td>14.37</td></tr></table>

a EAM model [13].   
b EAM (glue) model [14].

known which is however a trivial task even for MD calculations. To simplify the problem, we chose P-SCs to evaluate GB energies corresponding to the tangent planes for a few representative GB normal directions. The P-SC samples were constructed using two sets of Σ9 orientated parent lattice orientations, namely AD and ID, where notations of grain lattice orientations, i.e., A, I and D, refer the same as those in Ref. [7]. With such lattice orientations, a KC consisting of two truncated cuboctahedron grains will transform into a P-SC spontaneously at elevated temperatures [7]. Therefore, one may partition the entire P-TPMS GBs into eight equal-area sections to calculate more precisely the $\gamma _ { G B } ( \mathbf { n } )$ corresponding to each {111} GB-plane normal, which can be categorized further into four groups, α, β, γ and δ, respectively, as illustrated in Fig. 2(a) & (d). Noticeable differences can be observed between AD and ID. As depicted in Fig. 2(b) - (c) and (e) - (f), the AD-oriented P-SC is more anisotropic than ID for both Cu and Al. In particular, values of $\gamma _ { G B }$ in $\gamma$ and δ normal directions are significantly smaller than those in $\alpha$ and $\beta$ normal directions and the discrepancy tends to be enhanced as supercells become smaller. In contrast, in the ID-oriented structure, values of $\gamma _ { G B }$ are more isotropic as can be seen in Fig. 2(e) - (f).

The relevance between the isotropic condition and the limiting

thermal stability can be justified by MD snapshots in Fig. 3. As temperature rises, the atomic volume gradually increases and drops down promptly at the destabilization temperature, TS. As depicted, the processes are triggered by GB migration (atoms highlighted in grey color) when substantial nonvanishing GB curvature begins to develop as T approaching $T _ { S }$ . The scenarios suggest that the occurrence of grain coarsening is essentially transient in such P-SCs.

In addition, the thermal stability of those P-SCs also demonstrates a strong size dependence (Fig. 4a). The size-dependent thermal stability can be described based on following theoretical considerations under the assumption that all those general GBs fulfills the isotropic condition, Eq. (2).

(1) Thermal fluctuations become significant at high temperatures. When P-SC fluctuates, the shape of the SC deviates from the ideal minimal interface morphology such that it may either shrink or expand.   
(2) Since the transformation from the KC to SC is spontaneous, to destabilize a SC, the deviation from the initial shape of SC must be larger than that measured by the KC. Thus, one may take the

![](images/bbce73a2fe8bad56ed91d7caf3a0ba98f8f2df097839c04e7aafd65c6971ade4.jpg)

![](images/579f69dea843a46918ca84f24efab7ab9d8883f72b1c9b117e9333784096f293.jpg)

![](images/b755ad61e26a0e1d0e6c21dbd09b40b997b32dac94ccd7629d69cc0a4504a071.jpg)

![](images/2e7d4472b93144749757458d49fa3be0c5755c07ae81b7757bc85f7a7016ab46.jpg)

![](images/8058c3548f72408d62eb723b5658ce0340b57aa7ef1e2494066a93bbfa6536aa.jpg)

![](images/6c1c49a82bddbe72ec9f9685022f11731a1c3f4b5affbf78892a94120292a4a7.jpg)  
Fig. 2. Partition of GB area and MD calculated GB energies (Cu vs. Al) in α (111), $\beta$ (111), $\gamma$ (111) and δ (111) orientations for P-SCs of various sizes, AD (a - c) and ID (d - f).

![](images/22d57c9a7bb0454da401f17426238c6f5515cc2c1ef9f95b5b0194fe1bc5fe1e.jpg)

![](images/6a08c11ea0fe806a6dced1f7501020fcfb829ee55f20c2a7afaf5ab24fb16a7d.jpg)

![](images/2f56f2836a69b3627474d6fda7422aa2f3cdeeba4e6dd1d870329138c086383d.jpg)

![](images/6d5974f97cf883895850cd789ee613f2e2ee7864a8f127b97949aefad3c15cac.jpg)

![](images/653d4db9a44b92f65199cb8d790effd1a904e9d0496ac094023c9eee37e43400.jpg)

![](images/a6579ae12ab1d235957b1282b270f12e74a9a09e29242215c9688496609b68c4.jpg)

![](images/5ab1f3860c0fb0af12b0ee1d246200e38931d17a02789a31f1abcbeef760a4e8.jpg)

![](images/212c0a882598945fdbc6db96e9c051b63c094123277b81af55a5f11b46b6eb76.jpg)

![](images/a6dfbc3892b04504336f6546a9e39f503304c049f3064700adf5378ad27cc4c1.jpg)

![](images/c6838b0e830edaa16ca1e17a75f94c15a4d526966bd62fcec94699ce57e7c63c.jpg)

![](images/d23df4d3266a5b8774531dd5c005db6f984cfbdb2e6b67b0afd1b809b5cc39b4.jpg)

![](images/4682842da1c29efa98c1f0679afec24263bcc0f96bdfd6cb5c3678a052b61e00.jpg)

![](images/78a4a69d9667f5c2bc1aac3dce6892aa0d9016dcd31bc9894729c5094cb47128.jpg)

![](images/71bb8c5d80e2e8eb806e4e7a32d08865f50f20f1aae89a448e0419e0c03188a6.jpg)

![](images/3acc71bc4110baee04f133f6b2a6e93c0f2d9766ef13e1f48ed9f1a11828bbb6.jpg)

![](images/2f398ca4ba373189565c06de40f124fa6ea42844154b1e756896f7551224a94c.jpg)  
Fig. 3. Destabilization process underlying grain growth or coarsening observed in MD simulations for P-SCs of ID and AD $( a = 2 \times 9 a _ { 0 } )$ ), Cu (a, b) vs. Al (c, d). Plot on the left-hand side in each panel: thermal stability measured by profiles of atomic volume (Ω) as functions of temperature $( T )$ upon heating. Plot on the right-hand side of each panel: the [110] cross section views of MD snapshots at temperatures before and after destabilization $\left( T _ { S } \right)$ occurs. The ideal TPMS surface trace for each P-SC has been marked by atoms in red color.

![](images/d9f99021787f77c5bd8b9f06fc996f3451f150aa6e774cc8088477282cf8dfaa.jpg)  
(a)

![](images/14d3e0c87aa8cbe9a22e875624570fd5702d0d90a047681b09f0e578e2012309.jpg)

![](images/c9aee0d9d3f592cc734875b3e6c0a2ddf9681298514af385575c04667bae5d33.jpg)  
Fig. 4. (a) A schematic destabilization model: P-TPMS vs. insphere within a cubic box the size of which is measured by a. (b) MD observed and theoretically predicted (Eq. (4)) size-dependent thermostability $( T _ { S } )$ for SCs Cu and Al of various supercell sizes, grain lattice orientations (Σ9, Σ27, AD, ID) and shapes (P, G and $D$ as in Fig. 1).

inscribed sphere (or insphere) of a $P$ unit cell (cell size, a) as the reference state at which the SC must destabilize (Fig. 4).

(3) The additional amount of surface area between the insphere and the SC is $\delta A = \lambda R ^ { 2 }$ , accompanied by an increment of volume $\delta V =$ $\phi R ^ { 3 }$ with $R = a / 2 , \lambda \approx 1 . 3 5 3$ and $\phi \approx 0 . 0 2 3 6$ (Fig. 4a). The increase in surface energy $\Delta E _ { S }$ is simply given by $\gamma _ { G B } \delta A$ . The amount of change in volume energy, $\Delta E _ { V _ { \mathrm { i } } }$ , on the other hand, can be measured by lattice strain energy associated with GB migration, which is $\Delta E _ { V } = L \Delta V$ where $L$ has been introduced as a Tdependent strain energy per unit volume,

$$
L (T) = f \frac {L _ {m}}{\Omega} \left(\frac {T _ {E} - T}{T}\right) \tag {3}
$$

and $L _ { m }$ is latent heat per atom of bulk FCC lattice the thermal equilibrium melting point of which is $T _ { \mathrm { E } } , \Omega$ is the atomic volume and $f$ is a fraction measure. Eq. (3) applies because: (i) Like other GBs, the migration of a general GB is also a process producing lattice shear [16]. (ii) Rather than rigid interfaces, general GBs are diffusive or quasi-liquid like at high temperatures [17]. (iii) When it migrates, atomic motions at a general GB are re-orientation processes similar to a melting-then-freezing process but only occurs at GB sites locally [3,18,19].

(4) The additional work rendering a SC unstable depends on the counterbalance between surface and volume energies, so the critical condition at which a SC tends to destabilize is given by $W ( T ) = \Delta E _ { S } - \Delta E _ { V } = 0$ . As such, the following equation can be

obtained quantifying the thermal stabilities $( T _ { S } )$ of P-SCs of various sizes (a).

$$
T _ {S} = T _ {E} / \left(1 + \frac {\gamma_ {G B}}{a} \cdot \frac {\varepsilon \Omega}{L _ {m}}\right) \tag {4}
$$

where an adjustable parameter has been introduced due to the fraction measure f in Eq. (3). The values of ε for different sets of SCs can be fitted using the MD obtained size-dependent thermostability, the averaged GB energy underlying the isotropic assumption and other material properties listed in Table 1 as input. Therefore, the parameter ε can be considered as a material dependent GB ‘escapability’ measure, i.e., a larger ε means that the same set of P-TPMS GBs for a given material tends to destabilize in a relatively easier manner (see Cu vs. Al in Table 1). Figs. 4(b) and (c) show that our MD observed size-dependence of P-SCs can be well predicted using Eq. (4) for both Cu and Al.

The applicability of Eq. (4) is not limited to P-SCs, but also to SCs of different shapes (Fig.1 and Fig. 4). The isotropic GB condition (Eq. (2)) is required to derive Eq. (4). As those with Σ9 GBs, P-SCs built with a range of grain lattice orientations and hence other general GBs, such as Σ27, are expected to show similar thermostabilities and size-dependence. Poor thermostabilities, on the other hand, are expected if GB energies are strongly anisotropic. For example, P-SCs built with Σ3 grain lattice orientations turn out belonging to such categories [6,7]. Besides of GB energies, the GB ‘escapability’ measure ε in Eq. (4) is also interesting. As shown above, this parameter correlates with variation of lattice strain energy promoting GB migration. Therefore, beside that according to Young-Laplace law, this parameter measures additional driving forces such as due to anisotropic elasticity of lattices [7]. Lower ε values are expected for elastically more isotropic metals, such as Al (Table 1 and Table S3). In other words, the local combination of grain lattice orientations (local texture) with more isotropic GB energies and isotropic elasticity are desirable to achieve thermally stable SCs.

To summarize, SCs of TPMS GBs were studied for Al and Cu with atomistic modeling and simulations. Those consisting of energetically less anisotropic GBs are found thermally more stable. We proposed a simple thermodynamic model to describe the size-dependent thermal stabilities. The model should be applicable to a wide range of SCs, not only for FCC metals or alloys [6–8,20–22], but also for metals or alloys of other grain lattice structures or interfaces [23].

Lastly, in contrast to twin-free SCs considered in our present paper, the prototype structures reported in Refs. [6,7] not only resemble the D-minimal surface, but also consist of quadrupolar coherent twins. Sections of GB partitioned by twins are in fact identical to each other such that the isotropic condition (Eq. (2)) applies effectively. An extension of Eq. (4) to those thermally extremely stable D-SCs has also been considered and the result will be published separately.

# CRediT authorship contribution statement

Dan Yang: Writing – original draft, Visualization, Validation, Methodology, Formal analysis. Zhipeng Gao: Visualization, Validation, Investigation, Formal analysis. Fuling Tang: Validation, Supervision, Formal analysis. Zhaohui Jin: Writing – review & editing, Writing – original draft, Visualization, Validation, Supervision, Software, Project administration, Methodology, Investigation, Funding acquisition, Formal analysis, Conceptualization.

# Declaration of competing interest

The authors declare that they have no known competing financial

interests or personal relationships that could have appeared to influence the work reported in this paper.

# Acknowledgement

We are grateful for financial support of the Chinese Academy of Sciences (XDB0510000). DY is also supported by the Gansu Province Science and Technology Department (Grant No. 22ZD6GA008). MD computations were carried out partly at Siyuan-1 cluster, HPC, Shanghai Jiao Tong University (SJTU).

# Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.scriptamat.2025.116572.

# References

[1] G. Gottstein, L.S. Shvindlerman, Grain Boundary Migration in Metals: Thermodynamics, Kinetics, Applications, Second Edition, CRC Press, Boca Raton, 2009.   
[2] H. Gleiter, Nanostructured materials: basic concepts and microstructure, Acta Mater 48 (2000) 1–29.   
[3] E.R. Homer, E.A. Holm, S.M. Foiles, D.L. Olmsted, Trends in grain boundary mobility: survey of motion mechanisms, JOM 66 (2014) 114.   
[4] K. Lu, Stabilizing nanostructures in metals using grain and twin boundary architectures, Nat. Rev. Mater. 1 (2016) 16019.   
[5] Z.C. Cordero, B.E. Knight, C.A. Schuh, Six decades of the Hall-Petch effects - a survey of grain-size strengthening studies on pure metals, Int. Mater. Rev. 61 (2016) 495–512.   
[6] X.Y. Li, Z.H. Jin, X. Zhou, K. Lu, Constrained minimal-interface structures in polycrystalline copper with extremely fine grains, Science 370 (2020) 831–836.   
[7] Z.H. Jin, X.Y. Li, K. Lu, Formation of stable schwarz crystals in polycrystalline copper at the grain size limit, Phys. Rev. Lett. 127 (2021) 136101.   
[8] H.L. Fu, X. Zhou, Z.P. Gao, Z.H. Jin, X.Y. Li, K. Lu, Pt Schwarz crystals stabilized by minimal-surface grain boundaries and twins at the grain size limit, Acta Mater 276 (2024) 120007.   
[9] S. Hyde, S. Andersson, K. Larsson, Z. Blum, T. Landh, S. Lidin, B.W. Ninham. The language of shape, the role of curvature in condensed matter: physics, chemistry and biology, Elsevier Science, 1997.   
[10] I. Cantat, S. Cohen-Addad, F. Elias, F. Graner, R. Hohler, ¨ O. Pitois, F. Rouyer, A. Saint-Jalmes, S. Cox. Foams: structure and dynamics, 2013.   
[11] P.J. Gandy, S. Bardhan, A.L. Mackay, J. Klinowski, Nodal surface approximations to the P, G, D and I-WP triply periodic minimal surfaces, Chem. Phys. Lett. 336 (2001) 187–195.   
[12] A. Stukowski, Visualization and analysis of atomistic simulation data with OVITOthe open visualization tool, Model. Simul. Mater. Sci. Eng. 18 (2010) 015012.   
[13] V. Borovikov, M.I. Mendelev, A.H. King, R. LeSar, Effect of stacking fault energy on mechanism of plastic deformation in nanotwinned FCC metals, Model. Simul. Mater. Sci. Eng. 23 (2015) 055003.   
[14] X.Y. Liu, F. Ercolessi, J.B. Adams, Aluminium interatomic potential from density functional theory calculations with improved stacking fault energy, Model. Simul. Mat. Sci. Eng. 12 (2004) 665.   
[15] D.W. Hoffman, J.W. Cahn, A vector thermodynamics for anisotropic surfaces, Sur. Sci. 31 (1972) 368–388.   
[16] J.W. Cahn, J.E. Taylor, A unified approach to motion of grain boundaries, relative tangential translation along grain boundaries, and grain rotation, Acta Mater 52 (16) (2004) 4887–4898.   
[17] R. Balluffi, Grain boundary diffusion mechanisms in metals, Metall. Mater. Trans. B 13 (1982) 527–553.   
[18] R.W. Balluffi, S.M. Allen, W.C. Carter. Kinetics of Materials, John Wiley & Sons, Inc., 2005.   
[19] M. Chandross, N. Argibay, Ultimate strength of metals, Phys. Rev. Lett. 124 (2020) 125501.   
[20] W. Xu, B. Zhang, X.Y. Li, K. Lu, Suppressing atomic diffusion with the Schwarz crystal structure in supersaturated Al-Mg alloys, Science 373 (2021) 683–687.   
[21] L. Fang, Y.M. Zhong, B. Wang, W. Xu, X.Y. Li, K. Lu, Ultrahard and super-stable pure aluminum with Schwarz crystal structure, Mater. Res. Lett. 11 (2023) 662–669.   
[22] H.L. Fu, X. Zhou, Z.P. Gao, Z.H. Jin, X.Y. Li, K. Lu, Effect of grain geometry on the stability of polycrystalline pt at the nanoscale, Phys. Rev. Lett. (2025) in press.   
[23] H. Guan, H. Xie, Z.P. Luo, W.K. Bao, Z.S. You, Z.H. Jin, H.J. Jin, Ultrastrong spinodoid alloys enabled by electrochemical dealloying and refilling, PNAS 120 (2022) 221477312.