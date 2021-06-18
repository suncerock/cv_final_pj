# cv_final_pj
Final project for DATA130051

## Installation
The project is based on [mmclassification](https://github.com/open-mmlab/mmclassification), whose installation instructions can be found [here](https://github.com/open-mmlab/mmclassification/blob/master/docs/install.md)

## Results
Note that beacuse the parameters and flops of models trained on cifar-10 and cifar-100 are similar (only the last linear layers are different), we combine them in one table, where parameters and flops refers to the ones of models trained on cifar-10. Please refer to the [paper] for the name of the model.

| Model | CIFAR-10 Acc. | CIFAR-100 Acc. | Params | FLOPs | config | model | log |
| :---: | :-----------: | :------------: | :----: | :---: | :----: | :---: | :-: |
| ResNet50 | 93.7
