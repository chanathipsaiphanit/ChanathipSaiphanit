
scores = []
for i in range(5):
    score = int(input(f"กรอกคะแนนนักเรียนคนที่ {i+1}: "))
    scores.append(score)
print("\nผลการสอบ")
for i in range(5):
    if scores[i] >= 50:
        print(f"นักเรียนคนที่ {i+1} ได้ {scores[i]} คะแนน : ผ่าน")
    else:
        print(f"นักเรียนคนที่ {i+1} ได้ {scores[i]} คะแนน : ไม่ผ่าน")

