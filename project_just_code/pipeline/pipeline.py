""" pipeline.py: connect all codes"""
import os
import json
import datetime
import argparse
import subprocess
import pandas as pd
import numpy as np
from datetime import timezone, timedelta

from train import Trainer as Trainer
from tune import Tuner as Tuner
from eval import Evaluator as Evaluator


data_path = '../data'
model_path = '../model'
global_path = '..'
result_path = '../exe'

""" Config """
timestamp = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d")
id_ = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d-%H%M%S")

parser = argparse.ArgumentParser()
parser.add_argument("--data_name", type=str, default='data')
parser.add_argument("--model_name", type=str, default='model')
parser.add_argument("--data_config", type=str, default="config.json")
parser.add_argument("--model_config", type=str, default="config.json")
parser.add_argument("--times", type=int, default=5)
parser.add_argument("--train_flag", type=bool, default=True)
parser.add_argument("--eval_flag", type=bool, default=True)
parser.add_argument("--tune_flag", type=bool, default=True)
parser.add_argument("--gpu", type=str, default='0')
args = parser.parse_args()

data_name = args.data_name
model_name = args.model_name
data_config = json.load(open("{}/{}".format(data_path,args.data_config)))
model_config = json.load(open("{}/{}".format(model_path, args.model_config)))
model_config_name = args.model_config[:-5]
times = args.times
train_flag = args.train_flag
eval_flag = args.eval_flag
tune_flag = args.tune_flag
gpu = args.gpu

""" Main Pipeline """
if train_flag == True:
    id_ = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d-%H%M%S")
    info = "{}_{}_{}_{}".format(id_, data_name, model_name, model_config_name)
    save_path = "{}/train_{}.json".format(result_path, info)
    subprocess.run(['python', "train.py", '--data_name', data_name, '--model_name', model_name,
                    '--model_config', model_config_name, '--times', str(times),  '--gpu', gpu,
                    '--output_path', save_path], check=True)
    print('Train success!')
if eval_flag == True:
    id_ = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d-%H%M%S")
    info = "{}_{}_{}_{}".format(id_, data_name, model_name, model_config_name)
    save_path = "{}/eval_{}.json".format(result_path, info)
    subprocess.run(['python', "eval.py", '--data_name', data_name, '--model_name', model_name,
                    '--model_config', model_config_name, '--times', str(times),  '--gpu', gpu,
                    '--output_path', save_path], check=True)
    print('Evaluate success!')
if tune_flag == True:
    id_ = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d-%H%M%S")
    info = "{}_{}_{}_{}".format(id_, data_name, model_name, model_config_name)
    save_path = "{}/tune_{}.json".format(result_path, info)
    subprocess.run(['python', "tune.py", '--data_name', data_name, '--model_name', model_name, 
                    '--model_config', model_config_name, '--times', str(times),  '--gpu', gpu, 
                    '--output_path', save_path], check=True)
    print('Tune success!')
