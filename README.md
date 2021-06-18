# cv_final_pj
Final project for DATA130051

## Installation
The project is based on [mmclassification](https://github.com/open-mmlab/mmclassification), whose installation instructions can be found [here](https://github.com/open-mmlab/mmclassification/blob/master/docs/install.md)

## Results
Please refer to the [paper] for the name of the model.

### CIFAR-10
| Model    |  Top-1 Accuracy | Params | FLOPs | FPS | Config                                         | Download                                       |
| :------: | :-------------: | :----: | :---: | :-: |:---------------------------------------------: | :------------------------------------------:  |
| ResNet50 | 93.7            |        |       |     | [config](./configs/custom/resnet50_cifar10.py) | [model](https://drive.google.com/file/d/13tIdoBmxKD_V93CCI30kYAOvFqOxnrsq/view?usp=sharing)\|[log](./log/log_resnet50_cifar10.json) |

### CIFAR-100
| Model    |  Accuracy | Params | FLOPs | FPS | config                                          | model | log                                    |
| :------: | :-------: | :----: | :---: | :-: |:----------------------------------------------: | :---: | :-----------------------------------:  |
| ResNet50 | 93.7      |        |       |     | [config](./configs/custom/resnet50_cifar100.py) | [model](https://drive.google.com/file/d/13tIdoBmxKD_V93CCI30kYAOvFqOxnrsq/view?usp=sharing)      | [log](./log/log_resnet50_cifar10.json) |
