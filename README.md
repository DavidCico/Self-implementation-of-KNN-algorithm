# Self-implementation-of-KNN-algorithm
<p align="justify">The current repository contains different scripts, in which functions are implemented in Python from scratch, to carry out a classification problem using a backpropagation algorithm.</p>

## Getting Started

<p align="justify">These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.</p>

### Prerequisites

<p align="justify">You need Python 3.x to run the following code.  You can have multiple Python versions (2.x and 3.x) installed on the same system without problems.</p>

In Ubuntu, Mint and Debian you can install Python 3 like this:

    sudo apt-get install python3 python3-pip
    
The Jupyter Notebook which can be installed through Python's package manager:

    pip3 install --upgrade pip
    pip3 install jupyter

For other Linux flavors, OS X and Windows: 

Python is available at http://www.python.org/getit/    
Jupyter Notebook at https://jupyter.readthedocs.io/en/latest/install.html

## File descriptions
<ul>
    
<li>The files "<em>iris.csv</em>" and "<em>abalone.csv</em>" correspond to the datasets used in the examples.</li>
    
<li><p align="justify">"<em>Open_conversion_data.py</em>" contains all initial operations to be done to read the data from a CSV file, modify the variable types in the different columns (features) of the dataset, as well as data re-scaling, such as normalization and standardization. For more information on the different operations, the reader is referred to the Jupyter notebook <a href="https://github.com/DavidCico/Simple-functions-for-starting-machine-learning-with-Python/blob/master/Open_conversion_data.ipynb">Open_conversion_data.ipynb</a> where the different functions are more elaborated.</p></li>
    
<li><p align="justify">In "<em>Split_dataset.py</em>", 2 approaches to split a dataset are implemented, to understand how the split between training and testing occur for machine learning problems. The Jupyter notebook <a href="https://github.com/DavidCico/Simple-functions-for-starting-machine-learning-with-Python/blob/master/Split_dataset.ipynb">Split_dataset.ipynb</a> is available for more details.</p></li>

<li><p align="justify">"<em>Performance_assessment.py</em>" is a Python script in which accuracy metrics to measure machine learning algorithms performance are introduced, and implemented in a simple way. The Jupyter notebook <a href="https://github.com/DavidCico/Simple-functions-for-starting-machine-learning-with-Python/blob/master/Performance_assessment.ipynb">Performance_assessment.ipynb</a> is available for more details.</p></li>

<li><p align="justify">"<em>My_KNN.py</em>" is the Python implementation of the k-nearest neighbors model for classification or regression problem.</p></li>

<li><p align="justify">"<em>DistanceType.py</em>" is the Python script, in which the different distances, that can be used in the KNN algorithm, are defined.</p></li>

<li><p align="justify">"<em>Iris_data_study_classification.py"</em> is the main Python script, calling the different functions from the scripts above, to perform a classification analysis on the <a href="https://en.wikipedia.org/wiki/Iris_flower_data_set">Iris flower dataset</a>, with the implemented KNN model.</p></li>

<li><p align="justify">"<em>Iris_data_study_classification.ipynb</em>" is the Jupyter notebook version of the "<em>.py</em>" script.</p></li>

<li><p align="justify">"<em>Backpropagation_from_scratch.pdf</em>" is the <i>pdf</i> file with explanation on the different steps required to implement from zero, a backpropagation model for neural network, with application on the wheat seeds dataset.</p> 
</ul>

### Running the files

The different "<em>.py</em>" files need to be placed in the same folder for the main script to be run. The code is then ready to be used on the wheat seeds dataset and just requires running the following command:

    python Wheat_seeds_study.py

<p align="justify">The notebook can be <b>directly opened on GitHub</b>. An alternative way to open the notebooks, is to run the Jupyter Notebook. This can be done by executing the following command at the Terminal (Mac/Linux) or Command Prompt (Windows):</p>

    jupyter notebook

<p align="justify">This will print some information about the notebook server in your terminal, including the URL of the web application (by default, http://localhost:8888):</p>

    $ jupyter notebook
    [I 11:47:00.830 NotebookApp] Serving notebooks from local directory: C:\Users\EC-PM-3
    [I 11:47:00.830 NotebookApp] The Jupyter Notebook is running at:
    [I 11:47:00.830 NotebookApp] http://localhost:8888/?token=d22181d47f4826316a37161bb8c8469d77a5851bf9ab2c1f
    [I 11:47:00.830 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

It will then open your default web browser to this URL.

<p align="justify">When the notebook opens in your browser, you will see the Notebook Dashboard, which will show a list of the notebooks, files, and subdirectories in the directory where the notebook server was started. The notebook can then be chosen by navigating in the Notebook Dashboard.</p>

For more information on how to run a specific jupyter notebook, you can go to the <a href="https://jupyter.readthedocs.io/en/latest/running.html#running">following link</a>.
## Contributing

Please read [CONTRIBUTING.md](https://github.com/DavidCico/Self-implementation-of-KNN-algorithm/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **David Cicoria** - *Initial work* - [DavidCico](https://github.com/DavidCico)

See also the list of [contributors](https://github.com/DavidCico/Self-implementation-of-KNN-algorithm/graphs/contributors) who participated in this project.
