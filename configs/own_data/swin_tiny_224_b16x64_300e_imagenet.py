_base_ = [
    '../_base_/models/swin_transformer/tiny_224.py',
    '../_base_/datasets/own_data_swin.py',
    '../_base_/schedules/imagenet_bs1024_adamw_swin.py',
    '../_base_/default_runtime.py'
]
runner = dict(type='EpochBasedRunner', max_epochs=400)