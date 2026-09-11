#เขียนโปรแกรม
#1.รับค่าข้อความจากผู้ใช้ เป็นแปร str ชื่อ text
#2.รับค่าอักขระที่ต้องการนับในข้อความ text
#3. ดำเนินการนับอักขระตามที่ผู้ใช้การ และแสดงออกทางหน้าจอ
 
#ตัวอย่างหน้าจอ
#input your text: Boonchoo Jitnupong
#Which character do you want to count: 0
#5 letters '0' found in Boonchoo Jitnupong
 
 
 
print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Input your text: ")
x = input("Which character do you want to count: ")
for letter in text:
    if letter == x:
        count += 1
print(f"{count} letters '{x}' found in '{text}'")