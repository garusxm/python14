#การแสดงค่าในlist
fruits = ["apple", "banana", "cherry", "watermelon", "blueberry"]
print(fruits[1])
#เปลี่ยนค่าในlist
fruits[1] = "blackcurrent"
print(fruits[1])
#เปลี่ยนค่าในlistหลายตำแหน่ง
fruits[1:3] = ["kiwi", "mango", "pineaple"]
print(fruits)
#เพิ่มค่าในlist
fruits.append("orange")
print(fruits)
fruits.insert(3,"grape")
print(fruits)
tropical = ["mango", "pineapple", "papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("watermelon")
fruits.pop(1)
#del fruits
fruits.sort(reverse=True)
print(fruits)
#เนตรชนก เล็กน้อย ม.5/14 38