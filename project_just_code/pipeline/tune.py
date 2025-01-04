""" tune.py: tune the model and get the best model parameters """
import optuna
import json
import argparse
import numpy as np

class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)
class Tuner():
    def __init__(self, data_name, model_name, model_config, times, save_path):
        self.data_name = data_name
        self.model_name = model_name
        self.model_config = model_config
        self.times = times
        self.save_path = save_path
        return 
    def tune(self):
        result = {
            0: {
                "key": "value"
            },
            1: {
                "key": "value"
            }
        }
        js_str = json.dumps(result, indent=4, ensure_ascii=False, cls=NpEncoder)
        js_file = open(self.save_path, 'w')
        js_file.write(js_str)
        js_file.close()
        return 
    
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_name", type=str, default='data')
    parser.add_argument("--model_name", type=str, default='model_name')
    parser.add_argument("--model_config", type=str, default='config.json')
    parser.add_argument("--times", type=int, default=5)
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--output_path", type=str, default='../exe/tune.json')
    args = parser.parse_args()
    data_name = args.data_name
    model_name = args.model_name
    model_config = args.model_config
    times = args.times
    gpu = args.gpu
    output_path = args.output_path
        
    tuner = Tuner(data_name=data_name, model_name=model_name, model_config=model_config, times=times, save_path=output_path)
    tuner.tune()