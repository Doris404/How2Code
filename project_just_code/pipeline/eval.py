""" eval.py: evaluate the result """
import json
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
class Evaluator(object):
    def __init__(self,data_name, model_name, model_config, times, save_path):
        self.data_name = data_name
        self.model_name = model_name
        self.model_config = model_config
        self.times = times
        self.save_path = save_path
        return 
    def evaluate(self):
        result = {
            "key": "value"
        }
        js_str = json.dumps(result, indent=4, ensure_ascii=False, cls=NpEncoder)
        js_file = open(self.save_path, 'w')
        js_file.write(js_str)
        js_file.close()
        return