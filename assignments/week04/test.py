# รับค่า ชื่อ จริงจากผู้ใช้
# เขียน loop เพื่อนับจำนวน "สระที่มีอยู่ในภาษาอังกฤษ" นั้นว่ามีจำนวนกี่ตัว
# รับชื่อจริงจากผู้ใช้
name = input("What is you name: ")
vowels = 0


print("\nLoop ผ่าน string:")
for letter in name:
    print(f" ตักอักษร :{letter}")
    if letter == 'a' or letter == 'A':
        vowels = vowels + 1
    if letter == 'e' or letter == 'E':
            vowels = vowels + 1    
    if letter == 'i' or letter == 'I':
            vowels = vowels + 1
    if letter == 'o' or letter == 'O':
            vowels = vowels + 1
    if letter == 'u' or letter == 'U':
            vowels = vowels + 1
print(f"\n Your name have ",vowels,"vowels")
