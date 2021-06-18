_base_ = [
    '../_base_/models/resnet50_cifar.py',
    '../_base_/datasets/cifar100_bs16.py',
    '../_base_/schedules/cifar10_bs128.py', '../_base_/default_runtime.py'
]

model = dict(head=dict(num_classes=100))

data = dict(
    samples_per_gpu=128,
    workers_per_gpu=4,
    )

optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=0.0005)
evaluation = dict(interval=1)
lr_config = dict(policy='step', step=[20, 40, 60, 80], gamma=0.1)
runner = dict(type='EpochBasedRunner', max_epochs=100)

load_from = None
