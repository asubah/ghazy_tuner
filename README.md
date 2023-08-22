# cmssw-opentuner-xgboost

**Project Overview:**

This repository revolves around the `cmssw-opentuner-xgboost` project. Its purpose is to optimize program performance within the CMSSW framework through the application of autotuning techniques and the XGBoost machine learning algorithm.

**Folder Structure:**

There are two primary folders:

- **Simulated_Results**: This directory contains a collection of programs paired with datasets. These programs are designed to simulate their operation on the CMSSW framework and its kernels.

- **Automated_Results**: Similar to the previous folder, this directory houses programs tailored for usage within the CMSSW framework. However, it lacks the accompanying dataset.

Both of these folders share a similar structure, containing essential program files.

**Program Files:**

Inside the `Simulated_Results` folder, four key Python files exist:

- **main_tuner.py**: This serves as the main autotuning program. Utilizing the opentuner framework, it captures kernel parameters and throughput data, saving them into a CSV file.

- **random_search_technique.py**: Implements an opentuner search technique. It randomly adjusts one kernel parameter within the range of 32 to 1024 and records the outcomes.

- **xgb_ml.py**: Utilizing the XGBoost regressor, a potent machine learning algorithm, this program identifies the most influential parameters regarding throughput in a given dataset.

- **main_prog.py**: This acts as the core program for execution. It orchestrates the execution of the aforementioned files and stores outcomes in `results/part_1`, `results/part_2`, and `results/part_3` directories.

**Running the Program:**

To enhance program performance and extract insightful information, follow these steps:

1. Open your terminal and navigate to the `Simulated_Results` directory.
2. Execute the following command: `python3 main_prog.py`.

This command initiates the program and generates various result files within the respective directories.

**Results:**

Upon execution, the program generates various files within the results directories:

**results/part_1:**

- **data.csv**: This CSV file contains kernel parameter data for utilization within the XGBoost machine learning algorithm.
- **result.txt**: After applying the XGBoost algorithm to `data.csv`, this file displays the top 15 kernels with the most significant impact on throughput.

**results/part_2:**

- **kernels.txt**: A copy of the `result.txt` file from `results/part_1`. This file is employed by `main_tuner.py` to include parameters.
- **data.csv**: Similar to the previous data.csv, this file holds data ready for XGBoost analysis.
- **result.txt**: Displays the top 5 kernels with the highest impact on throughput after employing the XGBoost algorithm on `data.csv`.

**results/part_3:**

- **top_5_kernels.txt**: Derived from the `result/part_2/result.txt` file, this document highlights the five most crucial kernels within the list.

Feel free to explore and analyze these files to amplify CMSSW program performance.

---

