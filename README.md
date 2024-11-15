# lgt4hep_course

Collection of course materials to be used for the lattice-QCD training course as part of the [LGT4HEP](https://lgt4hep.github.io) traineeship.

## Course Information Sheet

Welcome to the LGT4HEP Traineeship Course (Fall 2024/Spring 2025). Below is the information sheet for the course (continuously updated):

The course consists of several modules each semester, as listed below. Each module may run for one, two, or three weeks, depending on the topic. Each week consists of two sessions. Each session consists of a one-hour lecture presented by the designated student lecturer. Each session also includes a half-an-hour discussion and Q/A slot involving student lecturers, expert faculty assigned to the module, and other students in the class.

A team of students will be in charge of preparing, presenting, and distributing a set of lecture notes on the topic of each module. The number of team members depends on the length of the module. For example, a two-week module will require 4 student lecturers to work together to prepare the content of the lectures. Each of the four students will present one of the lectures in class. The team formations and module assignments will be conducted prior to the start of the course.

For students who are doing the student-led lectures:
1. the student team meets with the expert faculty assigned to the module three times. The first meeting happens two weeks prior to the start of the module so the expert faculty can advise on the resources the students should study and the content they should cover. The second meeting occurs one week before the start of the module so the expert faculty can be updated on the progress in lecture development, to provide timely feedback, and to answer any technical questions regarding the content of the module. The final meeting between expert faculty and student team happens the week after the end of the module to provide feedback on lecture contents and delivery.
2. Student team assigned to each module should work together closely throughout the preparation period to develop unified and coherent lectures on the topic. If the subject area is too unfamiliar, the students need to start earlier but two weeks of committed time is a minimum. Depending on the number of students enrolled in the class, each student will be assigned to present at least one lecture and at most two lectures (in two different modules) per semester.
3. Students are encouraged to write logically coherent, notationally clean, and legible and structured notes to share with their peers as a valuable resource. The notes can be handwritten but latexed versions are preferred. These notes should be distributed no later than a week after the delivery of the lectures.
4. Students are encouraged to identify problems that can be assigned as homework problems within lecture notes. These could be derivations that can not fit the class time, further examples to demonstrate a point, etc.
5. The lectures can be presented on a (virtual) blackboard, with the possibility of presenting a few slides when certain plots or graphics need to be displayed. If you do not own an iPad or similar device to present the lectures, talk to your local faculty expert.

There will be a semester projects and presentation for those students who does not participate the student-led lectures. The students are encouraged to form team to work on the project, starting from roughly mid-point of the lecture schedule, and aim to complete on the last week of the class. 


## Unit 01: From path integrals to QCD: overview of continuum theory (2 weeks)

###  Lecture topics
- Path Integrals in Quantum Mechanics
- Markov Chain Monte Carlo
- Scalar Field Theory
   - Scalar Fields in the Continuum:
      - Lagrangian, EOM, Path Integral Representation
      - Correlators
      - Propagator
    - Scalar Fields on the Lattice:
  	- Lattice Construction
  	- Translating Continuum -> Lattice

### References
#### General lecture notes
- Gattringer and Lang -"Quantum Chromodynamics on the Lattice", Lecture Notes in Physics, 788;  ISBN-13: 978-3642018497): Chapter 1, Chapter 4
- Christoph Lehner - LQCD Lecture Notes: https://homepages.uni-regensburg.de/~lec17310/teaching/wise2324/lqft.html Chapter 1, Chapter 2 
- Lepage "Lattice QCD for Novices" notes: https://arxiv.org/pdf/hep-lat/0506036
- "Lattice Gauge Theory" by Heinz Rothe, Chapter 2

#### Supplemental Notes:
- Martin Luscher - Les Houches Summer School 09 Lecture Note: https://luscher.web.cern.ch/luscher/lectures/LesHouches09.pdf
- "Quantum Fields on the Lattice" by Montvay and Munster, Chapter 2
- David Tong's notes on Lattice Gauge Theory: https://www.damtp.cam.ac.uk/user/tong/gaugetheory/4lattice.pdf


## Unit 02: From scalar to gauge theories, on the lattice (3 weeks)

###  Lecture topics
- More on lattice scalar field theories: the O(n) model
- Gauge fields and Wilson line operators
- Wilson gague action
- Strong coupling expansion
- Static potential
- Improved actions

### References
- Gattringer and Lang -"Quantum Chromodynamics on the Lattice"
- Montvay and Münster -"Quantum Fields on a lattice;
- Smit -"Introduction to Quantum Fields on a Lattice"


## Unit03: Fermion actions and chiral fermions (2 weeks)

### Lecture Topics
- Fermion doubling
- Wilson Fermions
- Symmetries of the Wilson action
- Fermionic correlation functions
- Chiral symmetry
- Continuum chiral symmetry
- Nielsen-Ninomiya theorem
- Ginsparg-Wilson equations
- Topological charge
- Banks-Casher relation
- Chiral Fermions
- Overlap fermions
- Staggered fermions
- Domain wall fermions
### References
- Gattringer and Lang - "Quantum Chromodynamics on the Lattice"
- Montvay and Münster - "Quantum Fields on a lattice" 
- Christoph Lehner - LQCD Lecture notes: https://homepages.uni-regensburg.de/~lec17310/teaching/wise2324/lqft.html Chapter 10, 11, and 12

## Unit 04: Renormalization (2 weeks)


### Suggested lecture topics

1. Overview; renormalization in continuum QFT
2. Lattice renormalization and scale setting
	- Why is scale setting necessary?
	- What observables are commonly used to fix the lattice spacing?
	- What observables are commonly used to fix quark masses?
3. Perturbative matching and $\alpha_S$
4. Non-perturbative renormalization

### References
#### General lecture notes

- G. Peter Lepage (TASI '89), "[What is Renormalization?](https://arxiv.org/abs/hep-ph/0506330)"
- John Collins (TASI '95), "[The Problem of Scales: Renormalization and All That](https://arxiv.org/abs/hep-ph/9510276)"
- Peter Weisz (Les Houches '09), "[Renormalization and lattice artifacts](https://www.arxiv.org/abs/1004.3462)"

#### Scale setting

- Rainer Sommer, "[Scale setting in lattice QCD](https://arxiv.org/abs/1401.3270)"

#### Lattice perturbation theory

- Tadpole improvement: G.P. Lepage and P.B. Mackenzie, "[On the Viability of Lattice Perturbation Theory](https://arxiv.org/abs/hep-lat/9209022)"

#### Non-perturbative renormalization papers

- RI/SMOM: [Renormalization of quark bilinear operators...](https://arxiv.org/abs/0901.2599)

## Unit 05: Computing algorithms and HPC (2 weeks)
### Lecture Topics
  - Class 1 
  	- Introduce the problem, and need for Markov Chains
  	- Markov Chain as a solution
  	- Conditions needed to reach equilibrium. e. g. irreducible, apereodic, positive.
  	- Introduction to Transition Probability  (Exercise).
  	-  Balance equation, Detailed balance condition
  - Class  2 
       - Transition matrix
       - How does the transition probability satisfy detailed balance?
       - Sampling of different PDFs
       - Metropolis Algorithm
       - Rejection/ Heatbath Algorithm
       - Implementation of $\phi^{4}$ theory (Exercise).
 - Class 3
 	- Implementation of Heatbath for Pure Gauge $SU(2)$, $SU(N)$
  	- Global Updating Algorithms
   	- Pseudo-fermion problem
   	- $det(M)$ calculation
 - Class 4
 	- Molecular Dynamics, needs inversions
  	- Conjugate Gradient
   	- Hybrid Monte Carlo (HMC), an exact algorithm
   	- Implementation for Scalar case (Exercise)

### References
- Rothe, H. J. (2012). Lattice gauge theories: an introduction. World Scientific Publishing Company.
- Gattringer, C., & Lang, C. (2009). Quantum chromodynamics on the lattice: an introductory presentation (Vol. 788). Springer Science & Business Media.
- Joseph, A., & Joseph, A. (2020). Markov Chain Monte Carlo. Markov Chain Monte Carlo Methods in Quantum Field Theories: A Modern Primer, 37-42.

## Unit 06: Quantum computing and simulation (2 weeks)
### Lecture Topics
- PRE-LECTURE: QUANTUM SIMULATION OF FUNDAMENTAL PARTICLES AND FORCES, WHY AND HOW? 
  	
- PART I: HAMILTONIAN FORMULATION OF LATTICE GAUGE THEORIES 
	- Hamiltonian vs. Lagrangian formulation of LGTs
	- Kogut-Susskind formulation: Basis states, Hilbert space, and constraints: An Abelian case: U(1) LGT, A non-Abelian case: U(1) LGT
	- Kogut-Susskind formulation: Hamiltonian
	- A variety of formulations: a brief overview
 	- Classical Hamiltonian-simulation methods: a brief discussion
- PART II: QUANTUM SIMULATION AND QUANTUM-COMPUTING BASICS
 	- Quantum-simulation steps: A brief introduction
  	- Various modes of quantum simulation: Digital, analog, hybrid
   	- Digital-quantum-simulations basics:
       - qubits and gates
       - Encoding fermions and bosons onto qubits
       - State-preparation strategies
       - Time evolution (via product formulas)
       - Measurement strategies and observables
- PART III: DIGITAL QUANTUM COMPUTING TIME EVOLUTION IN LGTs
 	- A general algorithmic strategy
  	- Time evolution in the Schwinger model:
         - In purely fermionic formulation
       - In fermion-boson formulation
   	- Outlining the differences between Abelian and non-Abelian algorithms
   	- What we did not cover  
### References
- "[Lectures](https://indico.cern.ch/event/1342488/timetable/#20240722.detailed)" on Foundation of Quantum Computing for Lattice Gauge Theory at the CERN School on Continuum Foundations of Lattice Gauge Theories, July 2024.
- Quantum Computation and Quantum Information, Michael A. Nielsen & Isaac L. Chuang, Cambridge university press, 2010.
- Hamiltonian formulation of Wilson's lattice gauge theories, John Kogut and Leonard Susskind Phys. Rev. D 11, 395 (1975).
- Search for Efficient Formulations for Hamiltonian Simulation of non-Abelian Lattice Gauge Theories, Davoudi, Raychowdhury, Shaw, Phys. Rev. D 104, 074505 (2021), arXiv:2009.11802 [hep-lat].
- Quantum simulation of fundamental particles and forces, Bauer, Davoudi, Klco, Savage, Nature Rev.Phys. 5 (2023) 7, 420-432, arXiv:2404.06298 [hep-ph].
- Quantum Simulation for High Energy Physics, Bauer, Davoudi et al, PRX Quantum 4, 027001 (2023), arXiv:2204.03381 [quant-ph].

## Unit 07: Machine learning in lattice QCD (2 weeks)

# Other Lattice Resources
- Lattice Community-wide "[newsletter](https://list.indiana.edu/sympa/info/latticenews-l)" and "[joblist](https://list.indiana.edu/sympa/info/latticejobs-l)"
- USQCD "[website](https://www.usqcd.org/)" and "[Facebook](https://www.facebook.com/LatticeQCD/)"
- Annual lattice conference proceedings after 2006 on "[PoS](https://pos.sissa.it/cgi-bin/reader/family.cgi?code=lattice)"


