import json
from prompt import prompt

# def get_content(lst):
#     if lst == []:
#         return ""
#     content = ""
#     for item in lst:
#         title = (int(item["Grade"])-2) * " " + "-" + " " + item["Title"]
#         title = title.replace("\n","")
#         title = title + "\n"
#         response = (int(item["Grade"])-1),item["Content"]
#         content = content + title + response
#         content = content + get_content(item["Below"])
#     return content
    
def get_content(lst):
    if lst == []:
        return ""
    content = ""
    for item in lst:
        title = (int(item["Grade"])) * "#" + " " + item["Title"]
        title = title.replace("\n","")
        title = title + "\n"
        content = content + title + item["Content"]
        content = content + get_content(item["Below"])
    return content

def parse_json(file_name):
    try:
        json_file = open(file_name,"r")
        file_content = json_file.read()
        parsed_data = json.loads(file_content)
        return parsed_data
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return None

file_name = "./work_file"
# 解析JSON字符串
parsed_result = parse_json(file_name)

#try:
article = {}
article["Title"] = parsed_result["Title"]
Content = []
abstract = {}
abstract["Title"] = "Abstract"
abstract["Outline"] = prompt(parsed_result["Abstract"])
Content.append(abstract)
for item in parsed_result["Content"]:
    if item["Title"] == "REFERENCES":
        continue
    content = {}
    content["Title"] = item["Title"]
    content["Outline"] = prompt(item["Content"]+ get_content(item["Below"])) 
    Content.append(content)
article["Outline"] = Content
with open("result.json", 'w', encoding="utf-8") as file:
    json.dump(article, file, indent=2 ,ensure_ascii=False,)
# except:
#     pass



    
    