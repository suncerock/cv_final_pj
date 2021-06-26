# cv_final_pj
Final project for DATA130051

## Installation
The project is implemented based on [mmclassification](https://github.com/open-mmlab/mmclassification), whose installation instructions can be found [here](https://github.com/open-mmlab/mmclassification/blob/master/docs/install.md). Only the configurations are uploaded. If you are famaliar with open-mmlab, it can be easy to reproduce my results.

## Results
Please refer to the [paper](https://drive.google.com/file/d/1xtjBugR5Lr6QX6pLU_tfM0Ua2f9GB0Kt/view?usp=sharing) for the meaning of names.

### CIFAR-10
| Model          | Top-1 (%) | Params(M) | FLOPs(G) | FPS | Config                                               | Download                                       |
| :------------: | :-------: | :-------: | :------: | :-: |:---------------------------------------------------: | :-------------------------------------------:  |
| ResNet34-ViT   | 94.69     | 23.47     | 1.24     |     | [config](./configs/custom/resnet34_vit_cifar10.py)   | [model](https://drive.google.com/file/d/1m0R1qB2VF174jZXIDp-jvd1qqrxsGG3P/view?usp=sharing) \| [log](./logs/resnet34_vit_cifar10.log)
| ResNet18-ViT-E | 94.54     | 23.19     | 1.01     |     | [config](./configs/custom/resnet18_vit_E_cifar10.py) | [model](https://drive.google.com/file/d/1Td2hCA1AJ8brBcCm0at2LMgnHKIA_rLP/view?usp=sharing) \| [log](./logs/resnet18_vit_E_cifar10.log)
| ResNet18-ViT-M | 94.55     | 23.94     | 1.10     |     | [config](./configs/custom/resnet18_vit_M_cifar10.py) | [model](https://drive.google.com/file/d/1LYYhvdFN2V4kiP7mZ4PIcoim90nBUvOR/view?usp=sharing) \| [log](./logs/resnet18_vit_M_cifar10.log)
| ResNet34       | 95.07     | 21.28     | 1.16     |     | [config](./configs/custom/resnet34_cifar10.py)       | [model](https://drive.google.com/file/d/1Y3QceDhO3vTmKf0p0aigSHvG9Bkd5bmL/view?usp=sharing) \| [log](./logs/resnet34_cifar10.log)
| ResNet50       | 94.98     | 23.52     | 1.31     |     | [config](./configs/custom/resnet50_cifar10.py)       | [model](https://drive.google.com/file/d/1rdcUvyzUDv_KnTyusm7S7rOBtVUR-rR1/view?usp=sharing) \| [log](./logs/resnet50_cifar10.log)
| ViT-4-B        | 66.91     | 8.47      | 1.32     |     | [config](./configs/custom/vit_4_B_cifar10.py)        | [model](https://drive.google.com/file/d/1Z_kyMss-ev382zU9AXeQYhO_qippaE41/view?usp=sharing) \| [log](./logs/vit_4_B_cifar10.log)
| ViT-4-L        | 66.92     | 25.31     | 3.34     |     | [config](./configs/custom/vit_4_L_cifar10.py)        | [model](https://drive.google.com/file/d/15s_KMobs6XK8TPsXz17AYobpN9w3UR0Z/view?usp=sharing) \| [log](./logs/vit_4_L_cifar10.log)
| ViT-16-B       | 49.34     | 22.49     | 0.23     |     | [config](./configs/custom/vit_16_B_cifar10.py)       | [model](https://drive.google.com/file/d/1tul4hsNQTqL6PA1rMB8ZKM2rpJ1ujNiL/view?usp=sharing) \| [log](./logs/vit_16_B_cifar10.log)
| ViT-16-L       | 49.83     | 88.84     | 1.04     |     | [config](./configs/custom/vit_16_L_cifar10.py)       | [model](https://drive.google.com/file/d/1RhFzgw13y74xZTbQvpfqFMRIzvzuCjIr/view?usp=sharing) \| [log](./logs/vit_16_L_cifar10.log)


### CIFAR-100
| Model          | Top-1 (%) | Top-5 (%) |  Params(M) | FLOPs(G) | FPS | Config                                                | Download                                       |
| :------------: | :-------: | :-------: | :--------: | :------: | :-: |:----------------------------------------------------: | :-------------------------------------------:  |
| ResNet34-ViT   | 75.98     | 91.71     | 23.48      | 1.24     |      | [config](./configs/custom/resnet34_vit_cifar100.py)   | [model](https://drive.google.com/file/d/1B_l9PtrGD0x5QXK1GNM-E_mPx8dk3fXT/view?usp=sharing) \| [log](./logs/resnet34_vit_cifar100.log)
| ResNet18-ViT-E | 75.34     | 91.95     | 1.01       |          |      | [config](./configs/custom/resnet18_vit_E_cifar100.py) | [model](https://drive.google.com/file/d/1-4WttHsm2Q8UVRCZsIJsJTbHwwtdIvCb/view?usp=sharing) \| [log](./logs/resnet18_vit_E_cifar100.log)
| ResNet18-ViT-M | 75.83     | 91.65     | 1.10       |          |      | [config](./configs/custom/resnet18_vit_M_cifar100.py) | [model](https://drive.google.com/file/d/1RyExIZ9Y7odL_N4wrP1Iw7-eThuZ2lIV/view?usp=sharing) \| [log](./logs/resnet18_vit_M_cifar100.log)
| ResNet34       | 77.88     | 94.52     | 21.33      | 1.16     |      | [config](./configs/custom/resnet34_cifar100.py)       | [model](https://drive.google.com/file/d/14Fv7X2N_VZYF7eG6T-lXUYOM-kcwU7Du/view?usp=sharing) \| [log](./logs/resnet34_cifar100.log)
| ResNet50       | 78.85     | 94.63     | 23.71      | 1.31     |      | [config](./configs/custom/resnet50_cifar100.py)       | [model](https://drive.google.com/file/d/1wymVRqp-Q5oe6VfqwW8KT0P1PUiRC4C5/view?usp=sharing) \| \| [log](./logs/resnet50_cifar100.log)
| ViT-4-B        | 55.05     | 83.33     | 8.49       | 1.32     |      | [config](./configs/custom/vit_4_B_cifar100.py)        | [model](https://drive.google.com/file/d/10K2DTIppVdLcdqoNZaa8JXFRrj9vBMEI/view?usp=sharing) \| [log](./logs/vit_4_B_cifar100.log)
| ViT-4-L        | 55.15     | 83.21     | 25.33      | 3.34     |      | [config](./configs/custom/vit_4_L_cifar100.py)        | [model](https://drive.google.com/file/d/1RpbdNWi7Yiy5z5bvfteLr06eNgsoXe_i/view?usp=sharing) \| [log](./logs/vit_4_L_cifar100.log)

## Update 6-26 9:16
- Everything completed.
