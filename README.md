# cv_final_pj
Final project for DATA130051

## Installation
The project is implemented based on [mmclassification](https://github.com/open-mmlab/mmclassification), whose installation instructions can be found [here](https://github.com/open-mmlab/mmclassification/blob/master/docs/install.md)

## Results
Please refer to the [paper] for the name of the model.

### CIFAR-10
| Model          | Top-1 (%) | Params(M) | FLOPs(G) | FPS | Config                                         | Download                                       |
| :------------: | :-------: | :-------: | :------: | :-: |:---------------------------------------------: | :-------------------------------------------:  |
| ResNet50       | 94.98     | 23.52     | 1.31     |     | [config](./configs/custom/resnet50_cifar10.py) | [model](https://drive.google.com/file/d/1-xlMRLCOesbj_2QXDrRBMGKZs2HOSWUs/view?usp=sharing) \| [log](./log/log_resnet50_cifar10.json) |
| VIT-4-B        | 66.91     | 8.47      | 1.32     |     | [config](./configs/custom/vit_4_B_cifar10.py)  | [model](https://drive.google.com/file/d/1CPhFHEeJ-dBsFz-ksf4dUqYM7jsoTvoY/view?usp=sharing) \| [log](./log/log_vit_4_B_cifar10.py)
| VIT-4-L        | 66.92     | 25.31     | 3.34     |     |
| VIT-16-B       | 49.34     | 22.49     | 0.23     |     | [config](./configs/custom/vit_16_B_cifar10.py)
| VIT-16-L       | 49.83     | 88.84     | 1.04     |     |
| ResNet34-VIT   | 94.69     | 23.47     | 1.24     |     |
| ResNet18-VIT   | 94.54      | 23.19     | 1.00    |     |
| ResNet18-VIT-B | 94.55      | 23.19     | 1.01    |     |

### CIFAR-100
| Model         | Top-1 (%) | Top-5 (%) |  Params(M) | FLOPs(G) | FPS | Config                                          | Download                                       |
| :-----------: | :-------: | :-------: | :--------: | :------: | :-: |:----------------------------------------------: | :-------------------------------------------:  |
| ResNet50      | 78.85     | 94.63     | 23.71      | 1.31     |     | [config](./configs/custom/resnet50_cifar100.py) | [model](https://drive.google.com/file/d/161jPxQqVM-IU9TVktkeD4pJP0ZX-XYoQ/view?usp=sharing) \| [log](./log/log_resnet50_cifar100.json) |
| VIT-4-B       | 55.05     | 83.33     | 8.49       | 1.32     |     | [config](./configs/custom/vit_4_B_cifar100.py)  | [model](https://drive.google.com/file/d/1TRxoL9hC3540_aXm2Pt_N_9skOMrrmyX/view?usp=sharing) \| [log](./log/log_vit_4_B_cifar100.py)
| VIT-4-L       | 00.00     | 00.00     | 25.33      | 3.34     |     |
| ResNet34-VIT-B| 75.98     | 91.71     | 23.48      | 1.24     |     |
