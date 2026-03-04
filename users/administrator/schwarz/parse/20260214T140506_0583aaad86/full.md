# Supporting Information

# Free Energy Criterion for Thermal Stability of Schwarz Nanocrystals

Ting Lei,†,‡ Feng Liu,†,‡ Xiao-Lei Wu,∗,†,‡ and Yun-Jiang Wang∗,†,‡

†State Key Laboratory of Nonlinear Mechanics, Institute of Mechanics, Chinese Academy of Sciences, Beijing 100190, China

‡School of Engineering Science, University of Chinese Academy of Sciences, Beijing 101408, China

E-mail: xlwu@imech.ac.cn; yjwang@imech.ac.cn

This Supplementary Information includes details of methods

• Model and Molecular Dynamics   
• Vibrational mean-squared displacement   
• Non-equilibrium thermodynamic integration for free energy   
• Vibration entropy of atomic configurations   
• Size Dependence of Schwarz Crystal   
• Total excess energy of grain boundaries   
• Twin suppress GB diffusion in D-SC

Figures S1 to S8

Table S1

# 1. Model and Molecular Dynamics

There are two pathways to establish the construction of Schwarz crystal with diamond surface (D-SC). The first method involves combining specific orientations and shapes of grains to form grain boundaries that satisfy the Schwarz Surface. 1 The second method utilizes Kelvin crystal (KC), transforming it into D-SC through thermal activation or mechanical stimuli. 2 In this work, we choose the latter approach to construct D-SC, as this method may provide a more reliable framework due to the evolution of thermodynamic transformations.

After the KC is constructed, the SC can be obtained through the evolution of the KC. Fig. S1 shows the relative potential energy from KC to SC. Due to thermal fluctuations, KC exhibits different transformation rates into D-SC I and D-SC II, with D-SC II having a higher transformation rate than D-SC I in our work. D-SC I and D-SC II have GBs atoms that correspond to the Schwarz D minimal surface. 2 The explicit functional form of the Schwarz D surface is given by:

$$
S _ {D} (\tilde {x}, \tilde {y}, \tilde {z}) = \sin \tilde {x} \sin \tilde {y} \sin \tilde {z} + \sin \tilde {x} \sin \tilde {y} \cos \tilde {z} + \cos \tilde {x} \sin \tilde {y} \cos \tilde {z} + \cos \tilde {x} \cos \tilde {y} \sin \tilde {z} (1)
$$

Here, $x , y , z$ are the reduced Cartesian coordinates of atoms, defined as $\_$ , $\cdot$ , and $\_$ for an orthogonal simulation box containing $\_$ fundamental unit cells of the SCs, aligned with the X (100), Y (010), and Z (001) lattice directions. The function $S _ { D } ( \tilde { x } , \tilde { y } , \tilde { z } )$ corresponds to D-SC I, while $S _ { D } ( \tilde { x } - \pi / 2 , \tilde { y } - \pi / 2 , \tilde { z } - \pi / 2 )$ describes D-SC II. Both types of D-SC represent crystal structures conforming to the Schwarz D minimal surface.

The Schwarz Crystal with the primitive surface (P-SC) is also a type of Schwarz crystal, though it has not yet been discovered experimentally. Its main characteristic is that its surface satisfies a triply periodic minimal surface (TPMS) without any CTBs structure. The

![](images/f834bda33c8d1a167a42e5a5e9bd30d60520654df0a6874f174c565b97daa5fb.jpg)  
Figure S1: Evolution of atomic configuration from Kelvin Crystal to Schwarz Crystal. The two MD-obtained thermal profiles indicate that the transformations from twin-limited Kelvin crystal occur at 1230 K to D–SC I or at 1120 K to D–SC II well below the TE (1358 K) of Cu.

mathematical expression for the Schwarz primitive surface is:

$$
S _ {P} (\tilde {x}, \tilde {y}, \tilde {z}) = \cos 2 \tilde {x} + \cos 2 \tilde {y} + \cos 2 \tilde {z} (2)
$$

Similar to the approach used for constructing D-SC, P-SC can be constructed using two truncated octahedra grains of equal size, fully relaxed, 2 or modeled directly according to its surface function.

The Kelvin crystal is directly modeled in Python based on the orientation and position of each grain, following the approach described in the previous work. 3 The KC model consists of 16 truncated octahedra of equal size, forming a body-centered cubic structure up to the second-nearest neighbor. These truncated octahedra collectively form two HCP-structured units, known as coherent twin boundaries (CTBs), aligned along the [111] direction, as shown in Fig. S2.

![](images/98cd2ec8d52e016df7097d4b125484069541727665b03f91452e28e2f72ba332.jpg)

![](images/27fc8f3d935b2cdce069266a8d852104d5648a966fbe6618ee7b13497b6af24b.jpg)  
Figure S2: Configuration of Kelvin crystal. (a) Atomic configuration of Kelvin crystal (b) HCP and defect structures in Kelvin crystal

In this work, we use Voronoi tessellation with Atomsk $^ 4$ to construct polycrystals with random orientations. To ensure the stability of the results for both the Voronoi crystal and P-SC, we establish five different Voronoi crystals to eliminate the effects of random grain seeds.

Throughout the simulation, the force field is described by an empirical potential based on the embedded-atom method (EAM), 5 which is reliable for studying the stability and evolution of different crystal structures. Considering the When determining the appropriate simulation size, we consider the simulated critical temperature for structural stability (5.7 ∼ 13 nm),2 the critical size for the strong softening transition ( $3 . 8 2 \sim 1 5 . 4 1 ~ n m$ ),1 and the observed size range of D-SC (∼ 9.12 nm).3 Based on these factors, we select a structure with an overall size of 10 nm for our simulations. All simulation crystals were constructed with dimensions of $9 8 . 1 6 \times 9 8 . 1 6 \times 9 8 . 1 6 \check { \mathrm { A } } ^ { 3 }$ , containing approximately $N = 7 9 { , } 0 0 0$ atoms. Except for the two types of D-SC and KC, which have fixed orientation, position, and shape, all other configurations were generated five times in random orientation and simulated independently to obtain statistically meaningful values. Periodic boundary conditions were applied in all three directions. All atomistic simulations used the NPT ensemble with a Nos´e-Hoover thermostat and barostat $6 , 7$ to maintain constant temperature and zero pressure. The LAMMPS software package 8 was utilized for all simulations, and atomic configurations were visualized with the OVITO.9

# 2. Vibrational mean-squared displacement

Vibrational mean-squared displacement (vMSD) is a measure of the average squared distance that atoms in a material deviate from their equilibrium positions due to thermal vibrations. We are examining the free energy of the current configuration; however, some crystals are inherently in a metastable state, which may lead to structural instability at elevated temperatures and result in inaccurate free energy calculations. To address this, we calculate the vMSD to assess whether the crystal configuration remains relatively stable at the current temperature. The vMSD of a crystal is defined as follows: 10

$$
\left\langle \Delta \vec {r} _ {i} ^ {2} \right\rangle = \left\langle (\vec {r} _ {i} (t) - \vec {r} _ {i, \mathrm {e q u i l}}) ^ {2} \right\rangle \tag {3}
$$

where $\vec { r _ { i } } ( t )$ is the instantaneous position of atom $i$ at time $t$ , and ${ \vec { r _ { i } } }$ ,equil is the thermodynamic equilibrium position of this atom, equivalent to the time average of $\vec { r _ { i } } ( t )$ . The average $\langle \dots \rangle$ is taken over many atoms and time instances. To achieve an accurate and satisfactory thermodynamic configuration, we conduct 50 ps simulations in the NPT ensemble and calculate the vMSD in the NVT ensemble over a duration of 10 ps. Fig. S3 illustrates the vMSD of different configurations from 100 K to 1300 K, indicating that atoms in the KC and Voronoi crystals are likely to escape from their original lattice positions at elevated temperatures, particularly above 700 K. In contrast, the atoms in the SC exhibit lower thermal vibrations.

After obtaining the value of vMSD, the atomic-scale spring constants of the Einstein crystal is determined by the following equation:

$$
k = (3 k _ {\mathrm {B}} T) / \left\langle \Delta r _ {i} ^ {2} \right\rangle \tag {4}
$$

Here, $k _ { B }$ represents the Boltzmann constant and $T$ denotes the Kelvin temperature. The relationship between vibrational frequency $\omega$ and the spring constants $k$ for a simple harmonic oscillator can be expressed $\omega = \sqrt { k / m }$ .

The change in vMSD of different crystals at different temperatures over time shows whether the overall structure can maintain temperature at the current temperature. Therefore, we determine the temperature range of the calculated free energy of different crystals according to the slope of vMSD. The relevant results are summarized in Table. S1.

Table S1: Temperature ranges used for absolute free energy calculations of the studied crystals. The Frenkel-Ladd method $_ { 1 1 }$ can be employed to calculate the absolute free energy across a temperature range for the five crystals: D-SC I, D-SC II, P-SC, the Kelvin crystal, and the Voronoi crystal.

<table><tr><td>Crystal</td><td>D-SC I</td><td>D-SC II</td><td>P-SC</td><td>Kelvin crystal</td><td>Voronoi crystal</td></tr><tr><td>Temp (K)</td><td>100-900</td><td>100-900</td><td>100-900</td><td>100-700</td><td>100-700</td></tr></table>

# 3. Non-equilibrium Thermodynamic Integration

Nonequilibrium approaches envision a thermodynamic path as an explicitly time-dependent process, integrating the derivative of the free energy with respect to a coupling parameter that modifies the system gradually from a reference state to the target state. This method allows us to compute the free energies of two interesting states, $F _ { 1 }$ and $F _ { 2 }$ , and determine the free energy difference ( $\Delta F$ ) between them by performing numerical integration along the thermodynamic path. The relation links the $\Delta F$ between two states to the irreversible work distribution $W _ { i r r }$ in nonequilibrium processes. It is expressed as:

$$
\Delta F = \overline {{W _ {\mathrm {i r r}}}} - \overline {{E _ {\mathrm {d i s s}}}} \tag {5}
$$

where $E _ { \mathrm { d i s s } }$ represents the average dissipated heat generated for an ensemble of replicas of the nonequilibrium process. If the nonequilibrium process is sufficiently close to an ideal quasi-static process, it can be shown that the systematic error due to dissipation is the same for two processes in opposite directions, i.e., $\overline { { E _ { 1  2 } ^ { \mathrm { d i s s } } } } = \overline { { E _ { 2  1 } ^ { \mathrm { d i s s } } } }$ . Therefore, we obtain the accurate $\Delta F$ by canceling out the dissipated energy in opposite directions, leading to the following

![](images/db1bfd0d31a9a97a17cb3ab6d365b89076558169cfe13da1d9cf212d6c383b3c.jpg)

![](images/c60d1d3f7f2693465da501f1948106ba644f47dec7dad8930af10f5e638dfe80.jpg)

![](images/14c7adee861abe4b7b8bb2615a316526e7aae8a92ede7496fe61852c031c315d.jpg)

![](images/ca5c60cdd0ed1e6fa224dc45c22ec0baa18646b5da5abc2b0e49a64e87759df5.jpg)

![](images/84b4e3e098aff774e522ba2a368b9dbab8945ad10a3d2ba624949d74a7682ebe.jpg)

![](images/bde0f14e6a81ababfddb8597789616d7dae763521edee0eaf0d1e9496e18d507.jpg)  
T i m e ( p s )   
T i m e ( p s )   
Figure S3: Atomic vibrations in different crystal configurations. Variation in vMSD across different crystal types within the temperature range of 100 K to $1 3 5 0 \mathrm { K }$ .

expression:

$$
\Delta F = F _ {2} - F _ {1} = \frac {1}{2} \left[ \overline {{W _ {1 \rightarrow 2} ^ {\mathrm {i r r}}}} - \overline {{W _ {2 \rightarrow 1} ^ {\mathrm {i r r}}}} \right] \tag {6}
$$

Therefore, designing a reasonable nonequilibrium path that closely approximates an ideal quasistatic process and ensures the convergence of Eq. (6) is crucial. In this letter, we adopt a nonequilibrium thermodynamic integration method to calculate the absolute free energy, following the Frenkel-Ladd path $_ { 1 1 }$ and the reversible scaling path. 12 These methods provide accurate and reliable free energy calculations, essential for analyzing system stability.

# Free Energy along the Frenkel-Ladd path

The Frenkel-Ladd (FL) path $_ { 1 1 }$ is employed to obtain the practical absolute free energy at a specific temperature of interest. This process involves calculating the $\Delta F$ between a reference state $\boldsymbol { F } _ { r }$ and the target state $F _ { i } ^ { \prime }$ , along with the free energy of the target state itself. To calculate the free energy difference, the parametrized Hamiltonian $H ( \lambda )$ is chosen to take specific forms,

$$
H (\lambda) = \lambda H _ {f} + (1 - \lambda) H _ {i} \tag {7}
$$

where $H _ { i }$ and $H _ { r }$ represent the Hamiltonians of the interest state and the reference state, respectively, $\lambda$ is an order parameter that characterizes the thermodynamic state of a system as it transitions from the initial to the final state. According to Eq. (6), the free energy difference is associated with cumulative $W _ { i r r }$ in nonequilibrium processes, determined by the generalized force $\partial H / \partial \lambda$ associated with $\lambda$ . The forward work done is

$$
W _ {i \rightarrow r} ^ {\mathrm {i r r}} = \int_ {0} ^ {t _ {s}} d t \frac {d \lambda}{d t} \left[ H _ {r} (\Gamma (t)) - H _ {i} (\Gamma (t)) \right] \tag {8}
$$

Here, $t _ { s }$ represents the time of MD sampling, $\Gamma ( t )$ denotes the phase space trajectory of the system as it evolves along the nonequilibrium process.

For the free energy of the reference state, which is assumed to be an Einstein crystal,

each atom is considered to be attached to a lattice point by a 3D harmonic spring with a same spring constants $k$ . The free energy of the Einstein crystal $F _ { \mathrm { E } }$ is given by:

$$
F _ {\mathrm {E}} (N, V, T) = 3 N k _ {\mathrm {B}} T \ln (\frac {\hbar \omega}{k _ {\mathrm {B}} T}) \tag {9}
$$

Where, $\hbar$ is the Planck’s constant.

In sum, the free energy of interest $F _ { i } ^ { \prime }$ can be estimated as

$$
F _ {i} (N, V, T) = F _ {\mathrm {E}} (N, V, T) + \frac {1}{2} \left[ \overline {{W _ {1 \rightarrow 2} ^ {\mathrm {i r r}}}} - \overline {{W _ {2 \rightarrow 1} ^ {\mathrm {i r r}}}} \right] \tag {10}
$$

In this work, we have chosen a reasonable equilibration time of 10000 MD steps before starting the nonequilibrium switching process. The forward and backward switching takes 50000 MD steps, respectively. The spring constants $k$ of the reference Einstein crystal, and thus the vibrational frequency $\omega$ , is obtained by measuring the vMSD as described in the method section.

# Reversible Scaling

The Reversible Scaling (RS) path $1 2$ fully leverages all available information along a reversible thermodynamic path, allowing for the evaluation of free energies over a wide temperature range from a single simulation based on the Frenkel-Ladd path. Due to the instability of some crystals at high temperatures, the RS path can be used to assess their free energy performance at elevated temperatures.

The RS method employs a specific parametric form of the Hamiltonian $H ( \lambda )$ , where each value of the parameter $\lambda$ corresponds to a particular temperature, defined as $T \equiv T _ { 0 } / \lambda$ .

$$
H (\lambda) = \sum_ {i} ^ {N} \frac {p _ {i} ^ {2}}{2 m} + \lambda U (r) \tag {11}
$$

where $p _ { i }$ is momentum of the ith particle, m is the particle mass, and $U ( r )$ is the potential

energy.

$F ( T _ { 0 } ; \lambda )$ is the free energy of the system $H ( \lambda )$ for a specific value of the parameter $\lambda$ . Similar to the FL path, the forward work done $W _ { 1  \lambda _ { f } } ^ { i r r }$ is,

$$
W _ {1 \rightarrow \lambda_ {f}} ^ {\mathrm {i r r}} = \int_ {0} ^ {t _ {s}} d t \frac {d \lambda}{d t} U (\Gamma (t)) \tag {12}
$$

Therefore, we obtain the $\Delta F$ between state $F _ { 0 } ( T _ { 0 } )$ , which equals to $F ( T _ { 0 } ; 1 )$ , and the state $F ( T _ { 0 } ; \lambda _ { f } )$ by varying the parameter $\lambda$ from 1 to $\lambda _ { f }$ . By employing Eq. (11) and the equation of Helmholtz free energy, 12 we can derive the relationship between $F _ { 0 } ( T )$ and $F ( T _ { 0 } ; \lambda _ { f } )$ , which has,

$$
F _ {0} (T) = \frac {1}{\lambda} F \left(T _ {0}; \lambda\right) + \frac {3}{2} N k _ {B} T _ {0} \frac {\ln \lambda}{\lambda} \tag {13}
$$

Then, temperature dependence of the free energy of the system is

$$
F _ {0} (T) = \frac {F (T _ {0})}{\lambda} + \frac {3}{2} N k _ {B} T _ {0} \frac {\ln \lambda}{\lambda} + \frac {1}{2 \lambda} \left[ \overline {{W _ {1 \rightarrow \lambda} ^ {\mathrm {i r r}}}} - \overline {{W _ {\lambda \rightarrow 1} ^ {\mathrm {i r r}}}} \right] \tag {14}
$$

In this work, we calculate the maximum temperature for each configuration using the FL method and push up to 1300 K using the RS method, select a reasonable equalization time of 10,000 MD steps, and then start the non-equilibrium switching process. The front and rear switches are 10,000 MD steps respectively.

# Decomposition of Free energy to Internal Structures

The FL path theory is discussed above, which is used to calculate the absolute free energy of the configuration by introducing the hypothesis of an ideal Einstein crystal. In this context, it is important to note that while the ideal Einstein model assumes uniform spring constants across all atoms, real crystals often exhibit significant variations due to differences in atomic mass and bonding characteristics. Consequently, we recognize that different atoms within a crystal lattice possess varying spring constants $k$ , which directly influence their vibrational

behavior.

To effectively address these complexities, we categorize the crystal into three distinct structural components: grains, twins, and grain boundaries. We further assume that each category corresponds to its own unique Einstein crystal configuration characterized by distinct vibrational frequencies. This assumption allows us to treat each structure independently while acknowledging their contributions to the overall free energy landscape of the system. By calculating free energy separately for each structure using the FL path method, we can gain insights into how these various configurations interact thermodynamically.

# 4. Vibrational Entropy

Free energy is the main parameter to measure the thermodynamic stability of solid matter. After obtaining the function of free energy with temperature, we can further obtain the entropy of each crystal. we further calculate the temperature-dependent vibrational entropy in Fig. S4 by taking differential of the free energy curve with respect to temperature, i.e.,

$$
S _ {\mathrm {v i b}} (T) = - \partial F _ {\mathrm {v i b}} (T) / \partial T \tag {15}
$$

Obviously, the absolute vibrational entropy highlights a significant observation regarding the relationship between disorder and grain boundaries in materials. Specifically, it can be stated that the general conclusion drawn from various studies is that the disorder within a material predominantly originates from its grain boundaries. Grain boundaries are interfaces where crystals of different orientations meet, and they play a crucial role in determining the physical properties of polycrystalline materials. As the proportion of grain boundary increases within a given sample, there is an associated rise in entropy.

Moreover, higher proportions of grain boundary can result in more complex interactions among dislocations and defects present in the material structure. These interactions further contribute to an increase in overall disorder by allowing for additional pathways through

which energy states can fluctuate.

![](images/2724d873a304f5f1ec02bf4894a8d405269a72e436367833568917c1687c89d7.jpg)  
Figure S4: The vibration entropy of atomic configuration. The corresponding vibrational entropies are calculated by taking derivatives of the free energies with respect to temperature.

# 5. Size Dependence of Schwarz Crystal

In nanometal, the size limit of grain refinement has attracted significant attention. It defines the boundary of this field, and intriguing phenomena may still be discovered, reflecting the intrinsic properties of the studied structures. SCs inherently push the limits of grain refinement, making their size dependence a natural subject of investigation. As shown in Fig. S5(a), the characteristic size of SCs is defined by the diameter of the apertures, given by $\cdot$ ${ \sqrt { 2 } } / { 2 L }$ , where $\cdot$ represents the box size of the SCs. Previous research has demonstrated that the thermal and mechanical properties of SCs exhibit a critical size limit of approximately 3 nm. $\cdot$ Remarkably, when $D _ { s }$ falls below this threshold, a substantial decline in these properties is observed, highlighting the size-dependent stability of SCs.

As revealed in Fig. S5(b), we have designed ten SCs with sizes ranging from 2.76 nm to 9.57 nm, covering the typical range explored in experiments and simulations for comparative

![](images/33ddc413a3b10d9920d042b32d1814957733e8f04a0743943a69715379f398b9.jpg)  
(a)

![](images/5d73793025de586e302e10c3317e08cf6491ce2f941e8c87613a8e2e8b53968f.jpg)  
  
T (K)

![](images/b515136d8e80f4737cf96d88ffdcf5e71f66ab7ba52b846468b897ff64a8c5c5.jpg)  
(c)

![](images/e22c6ad4e04983c114cb85591a5a6a82e9ca8ed418f9d35e7cdab58bcf63da5e.jpg)  
  
Figure S5: Size dependence of D-SC thermostability. (a) The unit cell of D-SC, where the curved grain boundary (GB) resembles the Schwarz D-surface. (b) Free energy differences of ten D-SC I structures with different sizes. (c) Critical temperature $T _ { c }$ normalized by the melting temperature $\_$ , as a function of grain size. Experimental results 3 and MD simulations $^ { 1 , 2 }$ are included for comparison. (d) Volume fraction of GBs as a function of grain size in D-SC I and Voronoi structures. Since the Schwarz D-surface divides space into two regions, the unit cell of the Voronoi structure is chosen to contain two grains. All data points represent averages from five independent configurations, with error bars indicating standard deviations.

analysis. The free energy difference increases significantly as the size decreases, with the rate of increase becoming progressively steeper at smaller sizes. The increasing free energy indicates a significant variation in thermal stability within a narrow size range. As the size falls below a critical threshold, the SC structure suddenly undergoes a loss of stability. This tendency directly reflects the critical temperature ( $\cdot$ ) at GB migration, which serves as

another key indicator of thermal stability. There is a noticeable drop in $\cdot$ when the aperture size of SCs ( $\cdot$ ) falls below 3 nm [Fig. S5(c)].

The limit size may originate from the volume fraction of GBs, which has been proven in this work to dominate the total free energy of the system. As the proportion of disordered atoms increases, the free energy of SCs approaches the energy barrier, making it easier for the structure to transition into another lower-energy state. Fig. S5(d) shows that the disordered region expands rapidly as the size decreases, explaining why the free energy [Fig. S5(b)] increases sharply within a very narrow size range. This rapid increase ultimately leads to a critical threshold, representing the refinement limit of this structure. However, we must acknowledge that due to the mathematical properties of minimal surfaces in SCs, the volume fraction of GBs remains minimal at a given size compared to traditional crystals. This intrinsic characteristic explains why SCs exhibit lower free energy, contributing to their enhanced thermal stability.

# 6. Total excess energy of grain boundaries

Considering the GBs free energy per unit volume, we find that the energy of the TPMS interface is not minimal and may even be higher than that of ordinary grain boundaries. However, due to the geometric properties of minimal surfaces, 13 the TPMS structure minimizes the overall volume fraction of GBs within a given space. Thus, the formation of SCs likely results from a competition between the reduction in the proportion of disordered atoms and the increase in unit energy. Therefore, evaluating the total energy of GBs in a crystal is of significant importance. We define the excess free energy of the GB as the free energy density difference between GBs and grains, multiplied by the GBs volume.

As shown in the figure, although the energy per unit volume of TPMS grain boundaries may be higher, the total GB excess energy is significantly lower than that of Voronoi crystals. This suggests that SC grain boundaries offer a thermodynamic advantage overall, and

![](images/05e031ab2c753ad90d2d3eca84aae92e72a6ff9158212eb3c25faad2cb1fce5b.jpg)  
Figure S6: Total excess energy of GBs in different nanocrystals. Error bars indicate the standard deviation derived from five independent calculations.

relevant evidence of their existence can be found in experiments.

# 7. CTBs Suppress GBs Diffusion in Schwarz Crystal

To gain a kinetic perspective, SCs and Voronoi nanocrystals were heated at a rate of 80 K/ns from 100 to 1300 K to assess their thermal stability. As shown in Fig. S7, the P-SC exhibits the most pronounced kinetic instability, with significant GB migration and grain growth initiating at approximately 400 K. By 600 K, the primitive surface GBs have largely vanished, and by 800 K, the structure has completely transformed into a single crystal. Unlike D-SCs, the P-SC, which is solely defined by the TPMS geometry, does not exhibit enhanced stability compared to conventional Voronoi nanocrystals. This instability highlights the limited ability of Gaussian surfaces in SCs to maintain structural integrity at elevated temperatures. D-SC I, despite sharing the same TPMS GB topology as P-SC, maintains its structural integrity at significantly higher temperatures, as shown in the bottom panels of Fig. S7. While the zero-mean-curvature property of TPMS reduces the driving

force for GB coarsening, thermal fluctuations can still distort the curvature, potentially leading to structural collapse. In contrast, D-SCs exhibit enhanced stability due to their interwoven network of coherent twin boundaries (CTBs), which effectively immobilizes the minimal surface GBs and prevents their migration. 14

![](images/96160e06c94e3ad086feeaf117e9e9ffbae2e45fc57ced1fedfa87df68e5792a.jpg)

![](images/9482f5e274e8853acf720e296ec6d85645d2f45b04cc33f09c98de9a47e4b637.jpg)

![](images/03f795cacdfc3ef95e2bb0d4729092876af52edab2f8a0a65d1ff1ae1980d6fd.jpg)

![](images/46fc1164fc73f7711d3f1a0b52c35a5264fa4710d02116a4ce69e8d47afc5cee.jpg)  
Figure S7: Thermal stability of nanocrystals under heating. From left to right, the panels illustrate the atomic configurations of the Voronoi nanocrystal, P-SC, and D-SC I at temperatures of 200 K, 400 K, 600 K, and 800 K, respectively.

To further investigate the effect of CTBs, we design two types of D-SCs: one is a conventional D-SC with CTBs (D-SC-T), and the other is a D-SC without CTBs (D-SC-NT). In both structures, the GB surfaces conform to the Schwarz D-surface. Unlike the difference between P-SC and D-SC, where local curvatures may not be consistent, the grain boundaries of both D-SC-T and D-SC-NT conform to the Schwarz D-surface, as shown in Fig. S8(a). Although these structures follow different mathematical representations, they are simply two equivalent expressions of the same surface, with formulas being transformable into each other. As a result, the primary distinction between them lies in the presence or absence of CTBs, which play a crucial role in stabilizing the structure.

Following the same procedure, the two D-SCs were heated at a rate of 80 K/ns from 100 K to 1000 K. Fig. S8(b) illustrates the evolution of their GBs under thermal fluctuations. It

is evident that GB migration occurs in D-SC-NT, whereas in D-SC-T, GB atoms exhibit only vibrational motion at high temperatures, indicating enhanced stability due to the presence of CTBs. This evidence further supports our view that CTBs play a significant role in SCs by suppressing GB diffusion and migration, thereby enhancing the structural stability of SCs.

![](images/c36a77d12d76675b85b66dde0e634fbaab70a497bdad8aec6bc2163934a5a9ce.jpg)

![](images/61dc1e04c814dd005312d907e79d8bfd170f8dbfc7facc2ca100b1c76e450059.jpg)  
Figure S8: Thermal stability of D-SC under heating. (a) Atomic structure and surface representation of D-SC-T and D-SC-NT. (b) From top to bottom, the panels illustrate the atomic configurations of D-SC-T and D-SC-NT at temperatures of 100 K and 1000 K, respectively.

# References

(1) Xing, H.; Jiang, J.; Wang, Y.; Zeng, Y.; Li, X. Strengthening-softening transition and maximum strength in Schwarz nanocrystals. Nano Materials Science 2024, 6, 320–328.   
(2) Jin, Z.; Li, X.; Lu, K. Formation of stable schwarz crystals in polycrystalline copper at the grain size limit. Physical Review Letters 2021, 127, 136101.   
(3) Li, X.; Jin, Z.; Zhou, X.; Lu, K. Constrained minimal-interface structures in polycrystalline copper with extremely fine grains. Science 2020, 370, 831–836.

(4) Hirel, P. Atomsk: A tool for manipulating and converting atomic data files. Computer Physics Communications 2015, 197, 212–219.   
(5) Mishin, Y.; Mehl, M.; Papaconstantopoulos, D.; Voter, A.; Kress, J. Structural stability and lattice defects in copper: Ab initio, tight-binding, and embedded-atom calculations. Physical Review B 2001, 63, 224106.   
(6) Nos´e, S. A unified formulation of the constant temperature molecular dynamics methods. The Journal of Chemical Physics 1984, 81, 511–519.   
(7) Hoover, W. G. Constant-pressure equations of motion. Physical Review A 1986, 34, 2499.   
(8) Plimpton, S. Fast parallel algorithms for short-range molecular dynamics. Journal of Computational Physics 1995, 117, 1–19.   
(9) Stukowski, A. Visualization and analysis of atomistic simulation data with OVITO–the Open Visualization Tool. Modelling and Simulation in Materials Science and Engineering 2009, 18, 015012.   
(10) Wang, X.-S.; Wang, Y.-J. Disorder-order transition in multiprincipal element alloy: A free energy perspective. Physical Review Materials 2023, 7, 033606.   
(11) Freitas, R.; Asta, M.; De Koning, M. Nonequilibrium free-energy calculation of solids using LAMMPS. Computational Materials Science 2016, 112, 333–341.   
(12) de Koning, M.; Antonelli, A.; Yip, S. Optimized free-energy evaluation using a single reversible-scaling simulation. Physical Review Letters 1999, 83, 3973.   
(13) Jung, Y.; Chu, K. T.; Torquato, S. A variational level set approach for surface area minimization of triply-periodic surfaces. Journal of Computational Physics 2007, 223, 711–730.

(14) Yang, X.-S.; Wang, Y.-J.; Wang, G.-Y.; Zhai, H.-R.; Dai, L.; Zhang, T.-Y. Time, stress, and temperature-dependent deformation in nanostructured copper: stress relaxation tests and simulations. Acta Materialia 2016, 108, 252–263.