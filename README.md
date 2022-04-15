# basic_dynamics

Simple physical collision simulator of particles with coefficient of restitution (defines how elastic the collision is,
which means how much kinetic energy gets 'lost' in a collision) as the main parameter. 

In the real world [e_coeff] ranges from zero (inelastic) to one (perfectly elastic). 

The masses are related to their 'Volume' (3D projection).
(The total kinetic energy of the system has improper fluctuations in the area of about +-1*10^(-8) probably due to unavoidable rounding errors
but could be interesting for further investigation)
