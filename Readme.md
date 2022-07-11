# Project of Cellular Automaton
A [cellular automaton](https://en.wikipedia.org/wiki/Cellular_automaton)  is a discrete [model of computation](https://en.wikipedia.org/wiki/Model_of_computation "Model of computation") studied in [automata theory](https://en.wikipedia.org/wiki/Automata_theory "Automata theory"). Cellular automata are also called **cellular spaces**, **tessellation automata**, **homogeneous structures**, **cellular structures**, **tessellation structures**, and **iterative arrays**. Cellular automata have found application in [theoretical biology](https://en.wikipedia.org/wiki/Theoretical_biology "Theoretical biology").

## How it works?

When **creating a new life**, the field is filled with a random number of living cells. A cellular automaton consists of a regular grid of _cells_, each in one of state: _empty_ (white), _live_ (green), _dead_ (red).

After **the creation of life**, each cycle this life will change. If there are less or more than 2 _live_ cells next to the cell, the cell dies, it goes into the _dead_ (red) state. If there are 2 living cells next to the cell, it remains alive and goes to another cycle. If there are 2 living cells with an _empty_ or _dead_ cell, then these cells become _alive_. 

Above the field is a **cycle counter** and button return **home** to create another life.
