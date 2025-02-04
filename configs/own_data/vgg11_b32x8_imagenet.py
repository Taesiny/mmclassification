_base_ = [
    '../_base_/models/vgg11.py',
    '../_base_/datasets/own_data.py',
    '../_base_/schedules/imagenet_bs256.py',
    '../_base_/default_runtime.py',
]
optimizer = dict(lr=0.01)
runner = dict(type='EpochBasedRunner', max_epochs=150)