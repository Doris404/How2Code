import json
import pandas as pd

import datetime
from datetime import timezone, timedelta
import argparse

id_ = datetime.datetime.now().astimezone(timezone(timedelta(hours=8))).strftime("%Y%m%d-%H%M%S")

parser = argparse.ArgumentParser()
parser.add_argument("--eval_config_path", type=str, default="/home/ruc/xiaotong/OpenDataGen/log/20240705/open-data-gen/synthesized_data/eval_config.json")
args = parser.parse_args()

eval_config_path = args.eval_config_path
eval_config = json.load(open(eval_config_path))

# def get_result(eval_config):
#     ''' get_result
#     Args:
#         eval_config(dic)
#     Returns:
#         result(pd.DataFrame)'''

#     result_list = []
#     exe_name = []
#     for model in eval_config['model_list']:
#         eval_path = eval_config['eval_path']
#         for result_file in eval_config[model]:
#             result_path = '{}/{}/{}'.format(eval_path, model, result_file)
#             result_config = json.load(open(result_path))
#             result_list.append(result_config)
#             exe_name.append(result_file)

#     result = pd.DataFrame(result_list)
#     result['exe_name'] = exe_name
    
#     return result

def get_result(eval_config):
    ''' get_result
    Args:
        eval_config(dic)
    Returns:
        result(pd.DataFrame)'''

    result_list = []
    exe_name = []
    eval_path = eval_config["eval_path"]
    for result_json in eval_config["result_json_list"]:
        result_json_config = json.load(open("{}/{}".format(eval_path, result_json)))
        result_list.append(result_json_config)
        exe_name.append(result_json)
    result = pd.DataFrame(result_list)
    result['exe_name'] = exe_name
    
    return result

result = get_result(eval_config)
result_save = '{}/{}_result.csv'.format(eval_config['eval_path'], id_)
result.to_csv(result_save, index=None)
# update eval_config
eval_config['result_save'].append(result_save)
js_str = json.dumps(eval_config, indent=4)
js_file = open(eval_config_path, 'w')
js_file.write(js_str)
js_file.close()
print('Result save success: {}'.format(result_save))
print('Eval_config update success: {}'.format(eval_config_path))
