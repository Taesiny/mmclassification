_base_ = [
    '../_base_/models/resnet18.py', '../_base_/datasets/own_data.py',
    '../_base_/schedules/imagenet_bs256.py', '../_base_/default_runtime.py'
]
load_from: 'https://download.openmmlab.com/mmclassification/v0/resnet/resnet18_8xb32_in1k_20210831-fbbb1da6.pth'