# markov-chains-for-geodata
This is a general purpose simple markov chain implementation.

This is a very simple implementation of a markov chain. It is just a fun project to write it myself. 
In order to check if the given markov chain is irreducible i create a graph out of the transition matrix and perform
graph operations - in this case i find all strongly connected components and if i only find one then the markov chain is irreducible.

Of course, i also had a use case in mind. I choose the 300 m annual global land cover time series from 1992 to 2015 data by ESA 
(https://www.esa-landcover-cci.org/?q=node/175). The idea is to create a transition matrix between the different land cover types.
After that we can perform a simulate step - this case one year - and can look how the land cover changed.

For the use case i will use a different folder to seperate the model and preprocessing scripts.
