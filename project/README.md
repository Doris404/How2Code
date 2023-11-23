# README
## Folder structure
- dataset: 
- pipeline: 
- model: 
## config writting
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
