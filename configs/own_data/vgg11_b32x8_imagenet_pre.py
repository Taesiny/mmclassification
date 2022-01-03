_base_ = [
    '../_base_/models/vgg11.py',
    '../_base_/datasets/own_data.py',
    '../_base_/schedules/imagenet_bs256.py',
    '../_base_/default_runtime.py',
]
optimizer = dict(lr=0.01)
load_from: 'https://download.openmmlab.com/mmclassification/v0/vgg/vgg11_batch256_imagenet_20210208-4271cd6c.pth'