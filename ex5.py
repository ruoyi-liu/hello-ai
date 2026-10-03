names=["Liumin","Anna","Bob"]
scores=[95,72,40]
print("===名单===")
for name in names:
    print(f"学生：{name}")

print("===分数（每人加 5 分)===")
for score in scores:
    print(score+5)
print(f"循环结束后 score={score}")