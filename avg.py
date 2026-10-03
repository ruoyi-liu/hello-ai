scores=[95,72,40]

total=0
for score in scores:
    total=total+score

print(f"总分:{total}")
print(f"平均分:{total/len(scores)}")

highest=scores[0]
for score in scores:
    if score>highest:
        highest=score
print(f"最高分：{highest}")