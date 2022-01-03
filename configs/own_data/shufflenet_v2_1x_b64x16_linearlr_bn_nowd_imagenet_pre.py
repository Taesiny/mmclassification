_base_ = [
    '../_base_/models/shufflenet_v2_1x.py',
    '../_base_/datasets/own_data.py',
    '../_base_/schedules/imagenet_bs1024_linearlr_bn_nowd.py',
    '../_base_/default_runtime.py'
]
load_from: 'https://download.openmmlab.com/mmclassification/v0/shufflenet_v2/shufflenet_v2_batch1024_imagenet_20200812-5bf4721e.pth'