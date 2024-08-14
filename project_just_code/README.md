# README
Project is a template for building a new repo. It contains several folders. You can find their meaning in the following paragraphs.

## Folder structure
- dataset: contains data used in this project. You should also contain a config.json for dataset in this folder. 
- pipeline: contaians all the code used in this project. In general, people build up a project to implement a function or do some experiments like some researchers do. There must be a workflow for both two types of goals. You can define your workflow in pipeline.
- model: contains models you need to call when running the code in pipeline. Functions by other coders can be contained in this folder.

## Config writting
### config.json
```json
{
    "config_type": "global",
    "config_path": "./",
    "dataset_path": "./dataset",
    "model_path": "./model",
    "dataset_config": {},
    "model_config": {}
}
```
### dataset/config.json
```json
{
    "config_type": "dataset",
    "config_path": "./dataset",
    "data_list": [
        {
            "name": "data_name",
            "train_row_num": 300,
            "train_col_num": 2,
            "test_row_num": 100,
            "test_col_num": 2,
            "train_file": "./dataset/data_name/train",
            "test_file": "./dataset/data_name/test",
            "columns": [
                {
                    "column_name": "col0",
                    "column_type": "string",
                    "column_value": ["val0","val1","val2"]
                },
                {
                    "column_name": "col1",
                    "column_type": "float",
                    "column_value": []
                }
            ]

        }
    ]
}
```
### model/config.json
```json
{
    "config_type": "model",
    "config_path": "./model",
    "model_list": [
        {
            "name": "model_name",
            "parameters":[
                {
                    "name": "para0",
                    "default_set": 100
                },
                {
                    "name": "para1",
                    "default_set": 200
                }
            ] 
        }
    ]
}
```
### eval_config.json
```json
{
    "para": "value",
}
```

## Project management
Project management is a tough work for almost everyone. I summaried my experiments in my [blog](). It will be great if it can help you ❤️