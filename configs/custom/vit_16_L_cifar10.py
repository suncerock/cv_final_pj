_base_ = [
    '../_base_/models/vit_large_patch16_224_finetune.py',
    '../_base_/datasets/cifar10_bs16.py',
    '../_base_/schedules/cifar10_bs128.py',
    '../_base_/default_runtime.py'
]


data = dict(
    samples_per_gpu=128,
    workers_per_gpu=4,
    )

# model settings
model = dict(
    type='ImageClassifier',
    backbone=dict(
        type='VisionTransformer',
        num_layers=16,
        embed_dim=768,
        num_heads=8,
        img_size=32,
        patch_size=16,
        in_channels=3,
        feedforward_channels=2048,
        drop_rate=0.1),
    neck=None,
    head=dict(
        type='VisionTransformerClsHead',
        num_classes=10,
        in_channels=256,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5),
    ))


optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=0.0005)
evaluation = dict(interval=5)
lr_config = dict(policy='step', step=[50, 100, 150], gamma=0.1)
runner = dict(type='EpochBasedRunner', max_epochs=200)

load_from = None
