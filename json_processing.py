import json
import pandas as pd

dir = ["accessory", "animal", "appliance", "electronic", "food", "furniture", "indoor", "kitchen", "outdoor", "person", "sports", "vehicle"]
level = ["상", "중", "하"]


annotation_json_list = [ ]
images_json_list = []

question_json_list = []

image_name = []
image_id = []
question = []
answer = []


for dir_name in dir:
    for level_name in level:
        with open(f'./dataset/label_data/{dir_name}/{level_name}_train_{dir_name}/annotation.json') as f:
            annotation_json = json.load(f)
            annotation_json_list.append(annotation_json)
for dir_name in dir:
    for level_name in level:
        with open(f'./dataset/label_data/{dir_name}/{level_name}_train_{dir_name}/images.json') as f:
            images_json = json.load(f)
            images_json_list.append(images_json)
for dir_name in dir:
    for level_name in level:
        with open(f'./dataset/label_data/{dir_name}/{level_name}_train_{dir_name}/question.json') as f:
            question_json = json.load(f)
            question_json_list.append(question_json)
            
image_dict = {}
for image_json in images_json_list:
    for image in image_json["images"]:
        image_dict[image["image_id"]] =  image["image"]            
    


for annotation_json, question_json in zip(annotation_json_list, question_json_list):
    for annotation_data, question_data in zip(annotation_json["annotations"],question_json["questions"]):
        image_name.append(image_dict[annotation_data["image_id"]])
        image_id.append(annotation_data["image_id"])
        question.append(question_data["question"])
        answer.append(annotation_data["multiple_choice_answer"])
        
df = pd.DataFrame({'image_name' : image_id, 'image_name'  : image_name , 'question' :question, 'answer' : answer})
df.to_csv("./dataset/dataset_train.csv", encoding ="utf-8")