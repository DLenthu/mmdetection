# The new config inherits a base config to highlight the necessary modification
_base_ = 'configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

# We also need to change the num_classes in head to match the dataset's annotation
# model = dict(
#     roi_head=dict(
#         bbox_head=dict(num_classes=1),
#         mask_head=dict(num_classes=1)))
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=1)))

# Modify dataset related settings
dataset_type = 'COCODataset'
classes = ('Bhargav',)
data = dict(
    train=dict(
        img_prefix='face_data_mm/face/train/images',
        classes=classes,
        ann_file='face_data_mm/train/images/annotation_coco.json'),
    val=dict(
        img_prefix='face_data_mm/validation/images',
        classes=classes,
        ann_file='face_data_mm/validation/images/annotation_coco.json'))
    # test=dict(
        # img_prefix='balloon/val/',
        # classes=classes,
        # ann_file='balloon/val/annotation_coco.json'))

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'checkpoints/model_final_b275ba.pkl'