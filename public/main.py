from pyscript import document
import sys
from io import StringIO
import requests as req

# ตัวแปรเก็บสถานะ
current_code = ""
output_div = document.querySelector("#output")
input_section = document.querySelector("#input-section")
input_area = document.querySelector("#input-area")
input_prompt = document.querySelector("#input-prompt")
input_values = []  # เก็บค่าที่ผู้ใช้ป้อน
input_index = 0  # ตำแหน่งของ input ที่กำลังรอ

# ล้างสถานะก่อนรันใหม่
def reset_state():
    global input_values, input_index
    input_values = []
    input_index = 0
    input_section.style.display = "none"
    output_div.innerText = ""
# ฟังก์ชันเริ่มรันโค้ด
def start_code(event):
    reset_state()
    code_input = document.querySelector("#python-code")
    global current_code
    current_code = code_input.value
    
    # นับจำนวน input() ในโค้ด
    input_count = current_code.count("input(")
    if input_count == 0:
        # ถ้าไม่มี input() รันโค้ดเลย
        run_code_without_input()
    else:
        # ถ้ามี input() เริ่มถามทีละตัว
        ask_for_input()

# รันโค้ดโดยไม่มี input()
def run_code_without_input():
    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout

    try:
        exec(current_code)
        output = new_stdout.getvalue()
    except Exception as e:
        output = f"เกิดข้อผิดพลาด: {str(e)}"
    
    sys.stdout = old_stdout
    output_div.innerText = output
    req.post("http://localhost:3000/ans?uid=000000001&level=1",data=output)
    print("request send!")

# จำลอง input() โดยเก็บ prompt
def ask_for_input():
    global input_index
    lines = current_code.split("\n")
    input_prompts = []
    for line in lines:
        if "input(" in line:
            start = line.find("input(")
            end = line.find(")", start)
            prompt = line[start+6:end].strip("'\"")
            input_prompts.append(prompt if prompt else "กรุณาใส่ข้อมูล:")
    
    if input_index < len(input_prompts):
        input_prompt.innerText = input_prompts[input_index]
        input_section.style.display = "block"
    else:
        # เมื่อครบ input() ทั้งหมดแล้ว รันโค้ด
        run_code_with_inputs()

# ฟังก์ชันเมื่อกด Submit
def submit_input(event):
    global input_index
    input_values.append(input_area.value)
    input_area.value = ""  # ล้างช่อง
    input_index += 1
    ask_for_input()

# รันโค้ดเมื่อเก็บ input ครบแล้ว
def run_code_with_inputs():
    input_section.style.display = "none"
    
    # สร้าง input() จำลอง
    input_iter = iter(input_values)
    def custom_input(prompt=""):
        return next(input_iter)

    old_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout
    sys.modules['builtins'].input = custom_input

    try:
        exec(current_code)
        output = new_stdout.getvalue()
    except Exception as e:
        output = f"เกิดข้อผิดพลาด: {str(e)}"
    
    sys.stdout = old_stdout
    output_div.innerText = output
    req.post("http://localhost:3000/ans?uid=000000001&level=1",data=output)
    print("request send!")