# cv_final_pj
Final project for DATA130051

## Installation
The project is implemented based on [mmclassification](https://github.com/open-mmlab/mmclassification), whose installation instructions can be found [here](https://github.com/open-mmlab/mmclassification/blob/master/docs/install.md). Only the configurations are uploaded. If you are famaliar with open-mmlab, it can be easy to reproduce my results.

## Results
Please refer to the [paper] for the meaning of names.

### CIFAR-10
| Model          | Top-1 (%) | Params(M) | FLOPs(G) | FPS | Config                                               | Download                                       |
| :------------: | :-------: | :-------: | :------: | :-: |:---------------------------------------------------: | :-------------------------------------------:  |
| ResNet34-ViT   | 94.69     | 23.47     | 1.24     |     | [config](./configs/custom/resnet34_vit_cifar10.py)   |
| ResNet18-ViT-M | 94.54     | 23.19     | 1.10     |     | [config](./configs/custom/resnet18_vit_M_cifar10.py) |
| ResNet18-ViT-E | 94.55     | 23.19     | 1.01     |     | [config](./configs/custom/resnet18_vit_E_cifar10.py) |
| ResNet34       | 95.07     | 21.28     | 1.16     |     | [config](./configs/custom/resnet34_cifar10.py)       |
| ResNet50       | 94.98     | 23.52     | 1.31     |     | [config](./configs/custom/resnet50_cifar10.py)       | [model](https://drive.google.com/file/d/1-xlMRLCOesbj_2QXDrRBMGKZs2HOSWUs/view?usp=sharing) \| [log](./log/log_resnet50_cifar10.json) |
| ViT-4-B        | 66.91     | 8.47      | 1.32     |     | [config](./configs/custom/vit_4_B_cifar10.py)        | [model](https://drive.google.com/file/d/1CPhFHEeJ-dBsFz-ksf4dUqYM7jsoTvoY/view?usp=sharing) \| [log](./log/log_vit_4_B_cifar10.py)
| ViT-4-L        | 66.92     | 25.31     | 3.34     |     | [config](./configs/custom/vit_4_L_cifar10.py)        |
| ViT-16-B       | 49.34     | 22.49     | 0.23     |     | [config](./configs/custom/vit_16_B_cifar10.py)
| ViT-16-L       | 49.83     | 88.84     | 1.04     |     | [config](./configs/custom/vit_16_L_cifar10.py)       |


### CIFAR-100
| Model          | Top-1 (%) | Top-5 (%) |  Params(M) | FLOPs(G) | FPS | Config                                                | Download                                       |
| :------------: | :-------: | :-------: | :--------: | :------: | :-: |:----------------------------------------------------: | :-------------------------------------------:  |
| ResNet34-ViT   | 75.98     | 91.71     | 23.48      | 1.24     |     | [config](./configs/custom/resnet34_vit_cifar100.py)   |
| ResNet18-ViT-M | 94.54     | 23.19     | 1.10       |          |     | [config](./configs/custom/resnet18_vit_M_cifar100.py) |
| ResNet18-ViT-E | 94.55     | 23.19     | 1.01       |          |     | [config](./configs/custom/resnet18_vit_E_cifar100.py) |
| ResNet34       | 77.88     | 94.52     | 21.33      | 1.16     |     | [config](./configs/custom/resnet34_cifar100.py)       |
| ResNet50       | 78.85     | 94.63     | 23.71      | 1.31     |     | [config](./configs/custom/resnet50_cifar100.py)       | [model](https://drive.google.com/file/d/161jPxQqVM-IU9TVktkeD4pJP0ZX-XYoQ/view?usp=sharing) \| [log](./log/log_resnet50_cifar100.json) |
| ViT-4-B       | 55.05     | 83.33     | 8.49       | 1.32     |      | [config](./configs/custom/vit_4_B_cifar100.py)        | [model](https://drive.google.com/file/d/1TRxoL9hC3540_aXm2Pt_N_9skOMrrmyX/view?usp=sharing) \| [log](./log/log_vit_4_B_cifar100.py)
| ViT-4-L       | 00.00     | 00.00     | 25.33      | 3.34     |      | [config](./configs/custom/vit_4_L_cifar100.py)        |

## Update 6-25 21:57
- Updating the results
- Upload all the configurations and logs
- Model waiting to be downloaded from server and uploaded to Google Drive, after which the links can be found here.
