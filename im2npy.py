from PIL import Image
import os
import glob 
import numpy as np
import json


dir = ["accessory", "animal", "appliance", "electronic", "food", "furniture", "indoor", "kitchen", "outdoor", "person", "sports", "vehicle"]
level = ["상", "중", "하"]

images_json_list = []
for dir_name in dir:
    for level_name in level:
        with open(f'./dataset/label_data/{dir_name}/{level_name}_train_{dir_name}/images.json') as f:
            images_json = json.load(f)
            images_json_list.append(images_json)

image_dict = { }
for image_json in images_json_list:
    for image in image_json["images"]:
        image_dict[image["image"]] = image["image_id"]
        
for dir_name in dir:
    for level_name in level:
        path_dir = f"./dataset/image_data/{dir_name}/{level_name}_train_{dir_name}/"
        file = os.listdir(path_dir)
        for png in file:
            image = Image.open(path_dir + png)
            pixel = np.array(image)
            name = image_dict[png]
            np.save(f"./imgae_npy/{name}.npy", pixel) #저장할 '폴더 경로'를 쓰세요