#!/usr/bin/env python3

def famous_births(scientists):
    # เรียงลำดับข้อมูลตาม 'date_of_birth' (แปลงเป็น int เพื่อความแม่นยำ)
    sorted_scientists = sorted(scientists.values(), key=lambda x: int(x['date_of_birth']))
    
    # วนลูปแสดงผลตามรูปแบบที่โจทย์กำหนด
    for person in sorted_scientists:
        print(f"{person['name']} is a great scientist born in {person['date_of_birth']}.")

# ตัวอย่างการรัน
if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }
    famous_births(women_scientists)