# cv_final_pj
Final project for DATA130051

## Installation
The project is based on [mmclassification](https://github.com/open-mmlab/mmclassification), whose installation instructions can be found [here](https://github.com/open-mmlab/mmclassification/blob/master/docs/install.md)

## Results
Please refer to the [paper] for the name of the model.

### CIFAR-10
| Model    | Top-1 (%) | Params(M) | FLOPs(G) | FPS | Config                                         | Download                                       |
| :------: | :-------: | :-------: | :------: | :-: |:---------------------------------------------: | :-------------------------------------------:  |
| ResNet50 | 94.98     | 23.52     | 1.31     |     | [config](./configs/custom/resnet50_cifar10.py) | [model](https://drive.google.com/file/d/1-xlMRLCOesbj_2QXDrRBMGKZs2HOSWUs/view?usp=sharing) \| [log](./log/log_resnet50_cifar10.json) |

### CIFAR-100
| Model    | Top-1 (%) | Top-5 (%) |  Params(M) | FLOPs(G) | FPS | Config                                          | Download                                       |
| :------: | :-------: | :-------: | :--------: | :------: | :-: |:----------------------------------------------: | :-------------------------------------------:  |
| ResNet50 | 78.85     | 94.63     | 23.71      | 1.31     |     | [config](./configs/custom/resnet50_cifar100.py) | [model](https://drive.google.com/file/d/161jPxQqVM-IU9TVktkeD4pJP0ZX-XYoQ/view?usp=sharing) \| [log](./log/log_resnet50_cifar100.json) |
