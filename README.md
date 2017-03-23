# rhythmspace-demo
Here we have a working prototype of a rhythm space based on Puredata and python via the py object.
This prototype inputs a precomputed rhythm space resulting from an experiment with subjects assesing rhythm similarity.
The space contains nine EDM drum patterns which are spread around the space following the distance measures of the subjects.
This Rhythm Space can interpolate between the nodes thus creating new hybrid rhythm patterns thus expanding the contents 
of the collection and allowing for new rhthms to emerge. The discrete space is converted into a continous space.

The zip file contains a pd patch, a folder with abstractions, a folder with drum samples, and two .txt files which are used to configure the space, one holds the names an coordinates of the patterns, te otherone has symbolic descritpions of the onsets in the patterns. 

It should work in PD vanilla with the following libraries: cyclone, zexy, py and ggee. All available to download from the intrface of PD vanilla in the menu /Help/Find externals/.
