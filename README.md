# rhythmspace-demo
Here we have a working prototype of a rhythm space based on Puredata and python via the py object. This prototype inputs a precomputed rhythm space resulting from an experiment with subjects assesing rhythm similarity. The space contains nine EDM drum patterns which are spread around the space following the distance measures reported by the subjects in the experiment. This Rhythm Space can interpolate between the nodes (rhythms) thus creating new hybrid rhythm patterns and expanding the contents of the collection and allowing for new rhthms to emerge. 

An amorphous collection of drum patterns is analyzed, arranged in a 2D space for visualization and used for retrieval and continous morphing, converting a discrete collection into a generative surface for rhythm exploration and transformation.

The zip file contains a pd patch, a folder with abstractions, a folder with drum samples, and two .txt files. The txt files are used to configure the space, one holds the names an coordinates of the patterns, the otherone has symbolic descritpions of the onsets in the patterns. 

The reason why thi is packed as a .zip file is because git repositories and pd patches are not good friends as minor changes in a pd path suppose huge transformations in the .pd code of the patch, so it confuses the git and is also annoyfing for keeping track of the repository. On the other hand, its not the best parctice to leave a file zipped without exposing the contents.

Next revisions should help update the code so that everything pd is zipped and the rest exposed.

It should work in PD vanilla with the following libraries: cyclone, zexy, py and ggee. All available to download from the interface of PD vanilla in the menu /Help/Find externals/.
