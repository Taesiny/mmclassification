# dataset settings
dataset_type = 'ImageNet'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='RandomResizedCrop', size=56, backend='pillow'),
    dict(type='RandomFlip', flip_prob=0.5, direction='horizontal'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=['gt_label']),
    dict(type='Collect', keys=['img', 'gt_label'])
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', size=(64, -1), backend='pillow'),
    dict(type='CenterCrop', crop_size=56),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='Collect', keys=['img'])
]
data = dict(
    samples_per_gpu=32,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        data_prefix='test_classification/220516_mf630/train',
        classes='test_classification/220516_mf630/classes.txt',
        pipeline=train_pipeline),
    test=dict(
        type=dataset_type,
        data_prefix='test_classification/220516_mf630/test',
        ann_file='test_classification/220516_mf630/test.txt',
        classes='test_classification/220516_mf630/classes.txt',
        pipeline=test_pipeline),
    val=dict(
        # replace `data/val` with `data/test` for standard test
        type=dataset_type,
        data_prefix='test_classification/220516_mf630/valid',
        ann_file='test_classification/220516_mf630/valid.txt',
        classes='test_classification/220516_mf630/classes.txt',
        pipeline=test_pipeline))
evaluation = dict(interval=10, metric='accuracy', metric_options={'topk': (1, )}, save_best='accuracy_top-1')
