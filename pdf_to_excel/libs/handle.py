import tkinter as tk
import tkinter.simpledialog as simpledialog
import pprint


class INPUT_HANDLE:

    def __init__(self, proc):
        self.proc = proc

    def ask_input(self):
        self.proc.log(0, 'Wating response.')

        title = 'PDF読み込み君'
        message = """
            カンマ区切りで読み込むページを指定してください。例)1,2,3\n
            指定しない場合入力せずにそのままお進みください。
        """

        tk.Tk().withdraw()
        input = simpledialog.askstring(title, message)

        if(input == '0'):
            title = '入力内容をご確認ください'
            message = """
                0ページ目の指定はできません。\n
                指定ページを確認の上、再実行してください。
            """
            tk.messagebox.showinfo(title, message)
            exit(1)

        if(not input==''):
            input = self.string_to_int(input)

        return input

    def string_to_int(self, input_string):
        input_array = input_string.split(',')
        for i in range(len(input_array)):
            input_array[i] = int(input_array[i]) - 1

        return input_array