scores=[]
while True:
    text=input("请输入分数(输入done结束):")
    if text=="done":
        break
    scores.append(float(text))

print(f"你输入了{len(scores)}个分数：{scores}")

total=0
for score in scores:
    total=total+score

highest=scores[0]
for score in scores:
    if score>highest:
        highest=score
print(f"总分：{total}")
print(f"平均分：{total/len(scores)}")
print(f"最高分：{highest}")
