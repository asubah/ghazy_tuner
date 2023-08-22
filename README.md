# cmssw-opentuner-xgboost

---

## **Folder Structure**

In front of you are two folders: 

- **Simulated_Results**: This directory contains a bunch of programs with a dataset to simulate running this program on the CMSSW and all of its kernels.
- **Automated_Results**: This directory is also a bunch of programs, but without the dataset. These programs are the ones to be used on the CMSSW.

Both these folders are pretty similar.

---

## **Program Files**

Check the folder Simulated_Results, and you will find four python files.

- **main_tuner.py**: The main autotuning program. Using opentuner as its autotuning framework, this program will take all the kernel parameters and the throughput and add them into the csv.
- **random_search_technique.py**: An opentuner search technique used to take the list of kernels and change one parameter at random to a random multiple of 32 [32 - 1024].
- **xgb_ml.py**: A program that utilises the XGBoost regressor, which is a machine learning algorithm that finds the most important features from a given dataset, to find which parameters really affect the throughput.
- **main_prog.py**: The main program. This program will run each of these files and produce the results in the directories results/part_1, results/part_2, results/part_3.

---

## **Running the Program**

Go to Simulated_Results then write this command: `python3 main_prog.py`.

Running this program will produce these files in these directories:

---

## **Results**

**results/part_1:**

- **data.csv**: A csv file that contains data of the kernel parameters that will be used for the machine learning algorithm XGBoost.
- **result.txt**: The resulting top 15 kernels after using the data.csv on the xgboost algorithm.

**results/part_2:**

- **kernels.txt**: A copy of result.txt from the directory results/part_1. It will be used by the python file main_tuner.py for the purpose of adding parameters.
- **data.csv**: A csv file that contains data of the kernel parameters that will be used for the machine learning algorithm XGBoost.
- **result.txt**: The resulting top 5 kernels after using the data.csv on the xgboost algorithm.

**results/part_3:**

- **top_5_kernels.txt**: The top 5 kernels from the result/part_2/result.txt file. This file shows the top 5 most important kernels within the list of kernels.

---

