import base64
import hashlib
from tkinter import *

class EncodingTool:
    def __init__(self, master):
        self.master = master
        master.title("编码转换工具")

        # 创建输入文本框和输出文本框
        self.input_text = Text(master, height=15, width=80)
        self.input_text.pack(side=TOP, padx=10, pady=10)

        self.output_text = Text(master, height=15, width=80)
        self.output_text.pack(side=BOTTOM, padx=10, pady=10)

        # 创建转换按钮
        self.convert_button = Button(master, text="转换", command=self.convert_text, height=2, width=10)
        self.convert_button.pack(pady=10)

        # 创建下拉列表框
        self.options = ["ASCII", "Unicode", "UTF-8", "Base64", "MD5", "2进制", "8进制", "10进制", "16进制"]
        self.selected_option = StringVar(master)
        self.selected_option.set(self.options[0])
        self.option_menu = OptionMenu(master, self.selected_option, *self.options)
        self.option_menu.pack(pady=10)

    def convert_text(self):
        input_text = self.input_text.get("1.0", END).strip()

        if self.selected_option.get() == "ASCII":
            output_text = "".join(str(ord(c)) + " " for c in input_text)
        elif self.selected_option.get() == "Unicode":
            output_text = "".join(hex(ord(c)) + " " for c in input_text)
        elif self.selected_option.get() == "UTF-8":
            output_text = input_text.encode('utf-8').hex()
        elif self.selected_option.get() == "Base64":
            output_text = base64.b64encode(input_text.encode('utf-8')).decode('utf-8')
        elif self.selected_option.get() == "MD5":
            output_text = hashlib.md5(input_text.encode('utf-8')).hexdigest()
        elif self.selected_option.get() == "2进制":
            output_text = bin(int.from_bytes(input_text.encode('utf-8'), byteorder='big')).replace('0b', '')
        elif self.selected_option.get() == "8进制":
            output_text = oct(int.from_bytes(input_text.encode('utf-8'), byteorder='big')).replace('0o', '')
        elif self.selected_option.get() == "10进制":
            output_text = int.from_bytes(input_text.encode('utf-8'), byteorder='big')
        elif self.selected_option.get() == "16进制":
            output_text = hex(int.from_bytes(input_text.encode('utf-8'), byteorder='big')).replace('0x', '')

        self.output_text.delete("1.0", END)
        self.output_text.insert(END, output_text)

root = Tk()
tool = EncodingTool(root)
root.geometry("600x600")
root.mainloop()
