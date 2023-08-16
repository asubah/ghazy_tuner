import pandas as pd
from sklearn.model_selection import train_test_split
import xgboost as xgb
from sys import argv

nbr= int(argv[2])
file_path = argv[1]


#part 1: getting the data from the data file
#TODO: Get the data as a pandas dataframe

df = pd.read_csv(file_path + '/data.csv')

X = df.drop(columns=['throughput'])#, 'Unnamed: 0'])
y = df['throughput']

#part 2: using xgb to determine the most important parameters

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
data_matrix = xgb.DMatrix(data=X_train, label=y_train)

xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1, max_depth = 5, alpha = 10, n_estimators = 10)

params = {
    'objective': 'reg:squarederror',  # For regression task
    'max_depth': 3,
    'learning_rate': 0.1
}

xgb_model = xgb.train(params, data_matrix, num_boost_round=nbr)

xgb_dict = xgb_model.get_score(importance_type='weight')
xgb_dict = dict(sorted(xgb_dict.items(), key=lambda item: item[1]))
xgb_dict = dict(reversed(list(xgb_dict.items())))

#part 3: Exporting the data into a certain format to use later

with open(file_path + '/result.txt', 'w') as file:

    for key in xgb_dict:
        file.write(key + '\n')
