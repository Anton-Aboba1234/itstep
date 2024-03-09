import cv2
import numpy as np
import mrcnn.config
import mrcnn.model

class InferenceConfig(mrcnn.config.Config):
    NAME = "coco_pretrained_model_config"
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1
    NUM_CLASSES = 81

config = InferenceConfig()
model = mrcnn.model.MaskRCNN(mode="inference", config=config, model_dir='./')
model.load_weights('mask_rcnn_coco.h5', by_name=True)

image = cv2.imread('cat11.jpg')
mask_image = cv2.imread('mask11.png')

results = model.detect([image], verbose=0)
r = results[0]

for i in range(r['rois'].shape[0]):
    mask = r['masks'][:, :, i]
    image = cv2.bitwise_and(image, image, mask=mask.astype(np.uint8))
    color = np.random.randint(0, 255, (3,))
    image[mask == 1] = color

cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result.jpg', image)