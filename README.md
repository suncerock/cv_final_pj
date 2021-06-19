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
| VIT-4-B  | 66.91     | 8.47      | 1.32     |     |
| VIT-4-L  | 00.00     | 25.31     | 3.34     |     |
| VIT-16-B | 00.00     | 22.49     | 0.23     |     |
| VIT-16-L | 00.00     | 88.82     | 1.04     |     |
| Res34-VIT| 00.00     | 23.47     | 1.24     |     |


### CIFAR-100
| Model    | Top-1 (%) | Top-5 (%) |  Params(M) | FLOPs(G) | FPS | Config                                          | Download                                       |
| :------: | :-------: | :-------: | :--------: | :------: | :-: |:----------------------------------------------: | :-------------------------------------------:  |
| ResNet50 | 78.85     | 94.63     | 23.71      | 1.31     |     | [config](./configs/custom/resnet50_cifar100.py) | [model](https://drive.google.com/file/d/161jPxQqVM-IU9TVktkeD4pJP0ZX-XYoQ/view?usp=sharing) \| [log](./log/log_resnet50_cifar100.json) |
| VIT      | 55.05     | 83.33     | 8.49       | 1.32     |     |
| VIT_big  | 00.00     | 00.00     | 25.33      | 3.34     |     |
| Res34-VIT| 00.00     | 00.00     | 23.48      | 1.24     |     |
