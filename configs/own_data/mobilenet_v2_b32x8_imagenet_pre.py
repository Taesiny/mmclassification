_base_ = [
    '../_base_/models/mobilenet_v2_1x.py',
    '../_base_/datasets/own_data.py',
    '../_base_/schedules/imagenet_bs256_epochstep.py',
    '../_base_/default_runtime.py'
]
load_from: 'https://download.openmmlab.com/mmclassification/v0/mobilenet_v2/mobilenet_v2_batch256_imagenet_20200708-3b2dc3af.pth'