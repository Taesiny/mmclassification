_base_ = [
    '../_base_/models/swin_transformer/tiny_224.py',
    '../_base_/datasets/own_data_swin.py',
    '../_base_/schedules/imagenet_bs1024_adamw_swin.py',
    '../_base_/default_runtime.py'
]
load_from: 'https://download.openmmlab.com/mmclassification/v0/swin-transformer/convert/swin_tiny_patch4_window7_224-160bb0a5.pth'