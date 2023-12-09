import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data_name", type=str, default='data_1')
parser.add_argument("--model_name", type=str, default='model_1')
parser.add_argument("--times", type=int, default=1)
args = parser.parse_args()
data_name = args.data_name
model_name = args.model_name
times = args.times

if data_name == 'data_1' and model_name == 'model_1':
    print('Acc: 96%')
elif data_name == 'data_1' and model_name == 'model_2':
    print('Acc: 98%')
elif data_name == 'data_2' and model_name == 'model_1':
    print('Acc: 70%')
elif data_name == 'data_2' and model_name == 'model_2':
    print('Acc: 68%')
else:
    raise ValueError('data_name and model_name should be in the list')