# Donders_internship

## Small introduction 
To analyse this object space task a video of the rat exploring the objects in an arena and the neuronal activity of the rat’s cortex are recorded simultaneously. With this information the location and amount of time spent there can be calculated using a tracker and can be further analysed by looking into the spiking activity of neurons at these locations. However, these videos can be long and large, and the neuronal data is not aligned with the video. 
Therefore, a process that includes video compression, behavioural tracking and synchronization with neuronal activity needs to be implemented and automated. In this repository you can find the scripts I have written to achieve this goal.

## Where to find what:
### Notebooks:
All Google colab notebooks I have used over the course of my internship:
- Stage_mini : Notebook with the deeplabcut code
- Synchronization: Notebook dedicated to the methods for synchronization, contains LED and Timestamp synchronization code as well as ADC channel recognition
- Pipeline: Notebook with all finalized code that was used in the end and the pipeline itself

### 3rd_Party_Code
contains the code I have used from other people

*   [cross correlation from makeability_lab](https://makeabilitylab.github.io/physcomp/signals/ComparingSignals/index.html)
    > written by Professor Jon E. Froehlich at the University of Washington along with feedback from students
*   [deeplabcut_utils](https://github.com/DeepLabCut/DLCutils/blob/ed95860a7331f2ba37044711faf9638a7c5e6ab5/Demo_loadandanalyzeDLCdata.ipynb)

### Code:
Contains all the different scripts ive used for extraction and compression

### Data:
Nothing for now as the data is too big for github

### Graphs:
Contains the big neuron firemap plot
