_base_ = [
    '../_base_/models/resnet18_pre.py', '../_base_/datasets/own_data_new.py',
    '../_base_/schedules/imagenet_bs256.py', '../_base_/default_runtime.py'
]
runner = dict(type='EpochBasedRunner', max_epochs=300)
