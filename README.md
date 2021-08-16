# User Analytics in the Telecommunication
Analysis on Telecom Dataset, to get insight about the performance of the company based on user data.
## Introduction
In this project we will analyze the user data of TellCo, a telecom compnay based in the Republic of Pefkakia. Our goal is to provide insight on wather to buy or sell TellCo. This is done after the analysis of the data set wich contain user full information about the users activities on  the network.

## Table of content
- [Instalation](#installation)
- [Folders](#folders)
  - [Data](#data)
  - [Notebooks](#notebooks)
  - [Pages](#pages)
  - [Scripts](#scripts)
  - [Tests](#tests)

- [Other Files](#files)
- [Technologies](#technologies-used)
- [Additional](#additional-resources)
### Installation
- Install required python packages
```
git clone https://github.com/NatnaelSisay/Telecom_data.git
cd Telecom_data
pip install -r requirements.txt
```
- Notebooks
```
cd notebooks
jupyter notebook
```
- Dashboard
```
streamlit run app.py
```
### Folders
#### Data
This folder all the necessary ```.csv``` files required for the project. 
- **Week1_challenge_data_source** : Row and unprocessed csv file.
- **clean_telco.csv** : Data, with null values removed and cleaned.
- **user_satisfaction.csv** : Data, result of final task of project.

#### Notebooks
Folder containing all the notebooks files that are quired to process the data. 

#### Pages
This is a modularized collection of pages for ```streamlit``` dashboard application. Each file is self explanatory and contain python code for each individual page. Checkout [Instalation](#installation) on how to run the dashboard.

#### Scripts
This folder contain all the modular python code that are required to process the data. It contain helper functions and classes that are utilized during Data exploration and generation of insights
- **```clean_data.py```** : perform removal of null values and cleaning of row data. 
- **```ploting.py```** : contain essential reusable function for ploting graphs
- **```utils.py```** : contain utility functions used accross diffrent part of the project.

#### Test
Not complete but sample test. Tests cover the essential and critical functionalities of the project. But more work is required !!
### Files
- **```10 Academy Batch 4 - Week 1 Challenge.pdf ```** : Challenge document containing instructions on how to perform the tasks
- **```app.p```y** : streamlit dashboard starter file
- **```requirements.txt```** : file containing python packages used for this project
- **```setup.py```** : packaging the project
- **```Procfile.txt```**, **```setup.sh```** : critical files  for dashboard deployment on heroku.

#### Technologies used
- [Streamlit](https://streamlit.io/) : Building Dashboard
- [Jupyter]() : Creating notebooks

#### Additional Resources


