''' eval of exe1 by tong '''
import os
import json
import pandas as pd
import numpy as np
import datetime
import argparse
import subprocess

from data.datasets import Datasets
from evaluator.evaluator import Evaluator
from datetime import timezone, timedelta

id_ = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d-%H%M%S")
# args
parser = argparse.ArgumentParser()
parser.add_argument("--data_name", type=str, default='company_bankruptcy_prediction')
parser.add_argument("--model_name", type=str, default='ctgan')
parser.add_argument("--fake_path", type=str, default='./tune/exe1_sum/ctgan')
parser.add_argument("--fake_num", type=int, default=10)
parser.add_argument("--eval_path", type=str, default='./tune/exe1_sum/ctgan') # eval_path = fake_path
args = parser.parse_args()
data_name = args.data_name
model_name = args.model_name
fake_path = args.fake_path
eval_path = args.eval_path
fake_num = args.fake_num


# metricslist = ["Decision Tree", "Linear Regression", "Distance", "Diff.Corr", "DCR", "NNDR", "Discriminator Measure", "T-SNE"]
# metricslist = ["Decision Tree", "Linear Regression", "Distance", "DCR", "NNDR", "Discriminator Measure", "T-SNE", "Sampling Diversity"]
# metricslist = ["Decision Tree", "Distance", "DCR", "NNDR", "Discriminator Measure", "T-SNE", "Sampling Diversity"]
metricslist = ['Clustering']

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

# real data load
config_json = json.load(open("config.json"))
df_train = Datasets(config_json).read_train_data(data_name)
df_test = Datasets(config_json).read_test_data(data_name)

for i in range(args.fake_num):
    info = '{}_{}_{}_{}'.format(id_, data_name, model_name, str(i))
    save_json_file = '{}.json'.format(info)
    save_csv_file = '{}.csv'.format(info)
    save_json_path = '{}/{}'.format(eval_path, save_json_file)
    save_csv_path = '{}/{}'.format(eval_path, save_csv_file)
    # fake data load
    fake_data = pd.read_csv('{}/{}_{}.csv'.format(fake_path, data_name, str(i)), header=None)
    fake_data.columns = df_train.columns

    # evaluate
    eval = Evaluator(user_metrics_list=metricslist, real_data=df_train, test_data=df_test, fake_data=fake_data, label_column=df_train.columns[-1], droped_columns=None, task='classification', best_n_clusters=0) ####### raise ValueError Here, please fix it
    evaluate_result = eval.evaluate()

    # result save json
    js_str = json.dumps(evaluate_result, indent=4, ensure_ascii=False, cls=NpEncoder)
    js_file = open(save_json_path, 'w')
    js_file.write(js_str)
    js_file.close()