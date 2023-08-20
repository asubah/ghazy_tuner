import subprocess
import csv
import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb

kernels = None

def xgb_ml(path, num_boost_round):

    df = pd.read_csv(path)

    X = df.drop(columns=['throughput'], axis=1)
    y = df['throughput']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    data_matrix = xgb.DMatrix(data=X_train, label=y_train)

    xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1, max_depth = 5, alpha = 10, n_estimators = 10)

    params = {
        'objective': 'reg:squarederror',  # For regression task
        'max_depth': 3,
        'learning_rate': 0.1
    }

    xgb_model = xgb.train(params, data_matrix, num_boost_round=num_boost_round)

    xgb_dict = xgb_model.get_score(importance_type='weight')

    return [kernel for kernel in xgb_dict]

def part_one():

    global kernels

    with open('results/info.txt', 'w') as f:
        f.write('part_1')

    header = [
                    "throughput",
                    "findClus",
                    "RawToDigi_kernel",
                    "kernelLineFit3",
                    "kernelLineFit4",
                    "kernel_connect",
                    "getHits",
                    "kernel_find_ntuplets",
                    "fishbone",
                    "clusterChargeCut",
                    "calibDigis",
                    "countModules",
                    "kernelFastFit3",
                    "kernelFastFit4",
                    "kernelFastFit5",
                    "kernelLineFit5",
                    "kernel_fillHitDetIndices",
                    "kernel_mark_used",
                    "finalizeBulk",
                    "kernel_earlyDuplicateRemover",
                    "kernel_countMultiplicity",
                    "kernel_fillMultiplicity",
                    "kernel_checkOverflows",
                    "initDoublets",
                    "kernel_classifyTracks",
                    "kernel_fishboneCleaner",
                    "kernel_fastDuplicateRemover",
                    "kernel_countHitInTracks",
                    "kernel_fillHitInTracks",
                    "kernel_tripletCleaner",
                    "kernel_doStatsForHitInTracks",
                    "kernel_doStatsForTracks",
                ]

    with open('results/part_1/data.csv', 'w') as f:
    
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)

    subprocess.run([
                    'python3',
                    'main_tuner.py',
                    '--test-limit=1000',
                    't=Random_Search_Technique'
                   ])

    kernels = xgb_ml('results/part_1/data.csv',60)

    with open('results/part_2/kernels.txt', 'w') as f:

        for kernel in kernels:
            f.write(kernel + '\n')


def part_two():

    global kernels

    with open('results/info.txt', 'w') as f:
        f.write('part_2')

    with open('results/part_2/data.csv', 'w') as f:
    
        csvwriter = csv.writer(f)
        csvwriter.writerow(kernels)

    subprocess.run([
                    'python3',
                    'main_tuner.py',
                    '--test-limit=300',
                    't=Random_Search_Technique'
                   ])

    kernels = xgb_ml('results/part_2/data.csv',20)

    with open('results/part_3/kernels.txt', 'w') as f:

        for kernel in kernels:
            f.write(kernel + '\n')





if __name__ == '__main__':

    part_one()
    part_two()

    print('\n\n\nThe Results Should be results/part_3/kernels.txt\n\n\n')
