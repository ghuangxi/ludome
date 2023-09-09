import tkinter as tk
import random

def generate_passwords(name, birthday, email, phone, qq, wechat, count):
    # 将所有输入转换为小写，并去除空格
    name = name.lower().replace(" ", "")
    birthday = birthday.lower().replace(" ", "")
    email = email.lower().replace(" ", "")
    phone = phone.lower().replace(" ", "")
    qq = qq.lower().replace(" ", "")
    wechat = wechat.lower().replace(" ", "")

    # 创建一个密码列表
    passwords = []

    # 添加几种常见的密码模式
    if name and birthday:
        passwords.append(name)
        passwords.append(birthday)
        passwords.append(name + birthday)
        passwords.append(birthday + name)
    if email and birthday:
        passwords.append(email)
        passwords.append(email + birthday)
    if phone and name:
        passwords.append(phone + name)
    if qq and birthday:
        passwords.append(qq)
        passwords.append(qq + birthday)
    if wechat and name:
        passwords.append(wechat + name)

    # 生成随机密码
    while len(passwords) < count:
        password = ""
        length = random.randint(6, 10)
        for j in range(length):
            password += random.choice(name + birthday + email + phone + qq + wechat)
        passwords.append(password)

    return passwords

def generate_password_dictionary():
    # 从用户界面获取所有输入
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    qq = qq_entry.get()
    wechat = wechat_entry.get()

    # 生成密码列表
    passwords = generate_passwords(name, birthday, email, phone, qq, wechat, 200)

    # 将密码保存到文件中
    with open("passwords.txt", "w") as f:
        for password in passwords:
            if password:
                f.write(password + "\n")

    # 显示成功消息
    result_label.config(text="密码字典已生成！")

# 创建一个GUI窗口
window = tk.Tk()
window.title("密码生成字典工具")
window.geometry("800x600")

# 添加标签和输入框来获取所有输入
name_label = tk.Label(text="姓名：", font=("Arial", 20))
name_label.pack()

name_entry = tk.Entry(font=("Arial", 20))
name_entry.pack()

birthday_label = tk.Label(text="生日：", font=("Arial", 20))
birthday_label.pack()

birthday_entry = tk.Entry(font=("Arial", 20))
birthday_entry.pack()

email_label = tk.Label(text="邮箱：", font=("Arial", 20))
email_label.pack()

email_entry = tk.Entry(font=("Arial", 20))
email_entry.pack()

phone_label = tk.Label(text="电话：", font=("Arial", 20))
phone_label.pack()

phone_entry = tk.Entry(font=("Arial", 20))
phone_entry.pack()

qq_label = tk.Label(text="QQ号：", font=("Arial", 20))
qq_label.pack()

qq_entry = tk.Entry(font=("Arial", 20))
qq_entry.pack()

wechat_label = tk.Label(text="微信号：", font=("Arial", 20))
wechat_label.pack()

wechat_entry = tk.Entry(font=("Arial", 20))
wechat_entry.pack()

# 添加按钮来生成密码字典
generate_button = tk.Button(text="生成密码字典", font=("Arial", 20), command=generate_password_dictionary)
generate_button.pack()

# 添加一个标签来显示生成结果
result_label = tk.Label(text="")
result_label.pack()

# 运行GUI窗口
window.mainloop()
