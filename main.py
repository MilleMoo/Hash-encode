import hashlib
import itertools

m=hashlib.sha1(b"thx1138").hexdigest()

# ฟังก์ชันสำหรับแปลงข้อความเป็น SHA1
def generate_sha1(password):
    return hashlib.sha1(password.encode()).hexdigest()

# ฟังก์ชันสำหรับสร้างการสลับตัวพิมพ์ใหญ่/พิมพ์เล็ก
def generate_case_variations(password):
    # สร้างกรณีต่างๆ ของการสลับตัวพิมพ์ใหญ่/พิมพ์เล็ก
    variations = set()
    for case_variant in itertools.product(*[(c.lower(), c.upper()) for c in password]):
        variations.add(''.join(case_variant))
    return variations

# ตัวอย่าง SHA1 hash ที่ต้องการ
target_sha1 = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7" # ใส่ค่า SHA1 ที่ต้องการเปรียบเทียบ

# อ่านไฟล์ที่มีคำรหัส
file_path = '10k-most-common.txt'  # เส้นทางของไฟล์ที่ดาวน์โหลดมา

# ทดสอบไฟล์ที่มีคำรหัส
with open(file_path, 'r') as file:
    for line in file:
        password = line.strip()  # ตัดบรรทัดที่มีการขึ้นบรรทัดใหม่
        
        # สร้างกรณีสลับพิมพ์ใหญ่พิมพ์เล็ก
        all_password_variations = generate_case_variations(password)
        
        # เปรียบเทียบแต่ละรหัสผ่านที่แปลงแล้ว
        for possible_password in all_password_variations:
            if generate_sha1(possible_password) == target_sha1:
                print(f"Password found: {possible_password}")
                break
        else:
            continue
        break
    else:
        print("Password not found in the list.")
