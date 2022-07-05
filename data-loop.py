student=[
{"name": "Joseph","score":85},
{"name": "James","score":70},
{"name": "Mary","score":90},
{"name": "Tony","score":65},
{"name": "Tuu","score":49},
{"name": "Pom","score":51},
]
for i in student:
    if i["score"]>=80:
         print(i["name"],"score",i["score"],"grade 4")
    elif 70<= i["score"] <=79:
         print(i["name"],"score",i["score"],"grade 3")
    elif 60<= i["score"] <=69:
         print(i["name"],"score",i["score"],"grade 2")
    elif 50<= i["score"] <=59:
         print(i["name"],"score",i["score"],"grade 1")
    elif i["score"] <=50:
         print(i["name"],"score",i["score"],"grade 0")
   #เนตรชนก เล็กน้อย ม.5/14 38   