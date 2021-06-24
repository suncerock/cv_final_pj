_base_ = [
    '../_base_/models/vit_large_patch16_224_finetune.py', '../_base_/datasets/cifar10_bs16.py',
    '../_base_/schedules/cifar10_bs128.py', '../_base_/default_runtime.py'
]


model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='ResNetVisionTransformer',
        num_layers=16,
        embed_dim=128,
        num_heads=8,
        img_size=32,
        feedforward_channels=256,
        drop_rate=0.1,
        resnet_kwargs=dict(
            depth=34,
            num_stages=4
            )
        ),
    neck=None,
    head=dict(
        type='VisionTransformerClsHead',
        num_classes=10,
        in_channels=128,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5),
    ))

data = dict(
    samples_per_gpu=128,
    workers_per_gpu=4,
    )

optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=0.0005)
evaluation = dict(interval=5)
lr_config = dict(policy='step', step=[40, 80], gamma=0.1)
runner = dict(type='EpochBasedRunner', max_epochs=120)

load_from = None
