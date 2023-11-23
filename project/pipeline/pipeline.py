""" pipeline.py: connect all codes"""
import os
import json
import datetime
import argparse
import subprocess
from datetime import timezone, timedelta

from eval import Evaluator as Evaluator

""" Config """
timestamp = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d")
id_ = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d-%H%M%S")
try:
    os.mkdir("../{}".format(timestamp))
except:
    pass
# log_folder = open('../{}/{}'.format(timestamp,id_),'w')
# config
global_path = "../"
dataset_path = "../dataset"
model_path = "../model"
result_path = "../result"
# parameter
parser = argparse.ArgumentParser()
parser.add_argument("--data_name", type=str)
parser.add_argument("--model_name", type=str)
parser.add_argument("--global_config", type=str, default="config.json")
parser.add_argument("--data_config", type=str, default="config.json")
parser.add_argument("--model_config", type=str, default="config.json")
parser.add_argument("--train_flag", type=bool, default=True)
parser.add_argument("--eval_flag", type=bool, default=True)
parser.add_argument("--tune_flag", type=bool, default=True)
parser.add_argument("--model_params_path", type=str, default=None)
parser.add_argument("--gpu", type=str, default='0')
args = parser.parse_args()
data_name = args.data_name
model_name = args.model_name
global_config = json.load(open("{}/{}".format(global_path, args.global_config)))
data_config = json.load(open("{}/{}".format(dataset_path,args.data_config)))
model_config = json.load(open("{}/{}".format(model_path, args.model_config)))
train_flag = args.train_flag
eval_flag = args.eval_flag
tune_flag = args.tune_flag
model_params_path = args.model_params_path
gpu = args.gpu


""" Main Pipeline """
if train_flag == True:
    id_ = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d-%H%M%S")
    info = "{}_{}_{}".format(data_name, model_name, model_params_path)
    save_path = "{}/{}/{}_{}_model.json".format(result_path, timestamp, id_, info)

    subprocess.run(['python', "train.py", '--data_name', data_name, '--model_name', model_name,
                    '--model_params', model_params_path, '--times', '1',  '--gpu', gpu,
                    '--output_path', save_path], check=True)
    print('Train success!')
    pass
if eval_flag == True:
    id_ = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d-%H%M%S")
    eval_config = {
        'para': 'value',
    }
    js_str = json.dumps(eval_config, indent=4)
    eval_path = "{}/{}/{}_eval.json".format(result_path, timestamp, id_)
    js_file = open(eval_path, 'w')
    js_file.write(js_str)
    info = "{}".format(eval_path)
    save_path = "{}/{}/{}_{}_result.csv".format(result_path, timestamp, id_, info)
    
    eval = Evaluator(eval_config)
    evaluate_result = eval.evaluate()
    eval_config['result'] = evaluate_result
    js_str = json.dumps(eval_config, indent=4)
    js_file = open(eval_path, 'w')
    js_file.write(js_str)
    print('Evaluate success!')
    pass
if tune_flag == True:
    # try to get the best config to do experiment.
    print('Tune success!')
    pass
