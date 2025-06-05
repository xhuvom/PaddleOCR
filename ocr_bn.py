import os
from paddleocr import PaddleOCR

image_dir = './images'
label_dir = './labels'
os.makedirs(label_dir, exist_ok=True)

ocr = PaddleOCR(lang='bn', use_angle_cls=False)

for img_name in os.listdir(image_dir):
    img_path = os.path.join(image_dir, img_name)
    if not os.path.isfile(img_path):
        continue
    result = ocr.ocr(img_path, cls=False)
    lines = []
    for line in result:
        for box, (text, score) in line:
            lines.append(text)
    print(img_name, '\n'.join(lines))
    label_path = os.path.join(label_dir, os.path.splitext(img_name)[0] + '.txt')
    with open(label_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
