_base_ = 'mobilenet-v3-small_8xb32_in1k.py'

_deprecation_ = dict(
    expected='mobilenet-v3-small_8xb32_in1k.py',
    reference='https://github.com/open-mmlab/mmclassification/pull/508',
)

load_from: 'https://download.openmmlab.com/mmclassification/v0/mobilenet_v3/convert/mobilenet_v3_small-8427ecf0.pth'