_base_ = [
    '../_base_/models/resnet34_cifar.py', '../_base_/datasets/cifar100_bs16.py',
    '../_base_/schedules/cifar10_bs128.py', '../_base_/default_runtime.py'
]


data = dict(
    samples_per_gpu=128,
    workers_per_gpu=4,
    )
    
model = dict(head=dict(num_classes=100))

optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=0.0005)
evaluation = dict(interval=5)
lr_config = dict(policy='step', step=[40, 80], gamma=0.1)
runner = dict(type='EpochBasedRunner', max_epochs=120)

load_from = None