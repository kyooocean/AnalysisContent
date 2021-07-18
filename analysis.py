import tkinter

KEKKA = [
    "アシスタントAIがおすすめです！音声で指示を与えたり質問されたりして的確なアドバイスをしてくれます",
    "自動返信AIがおすすめです！忙しい時や対応できない時に設定しておくことで文脈や状況により適切に自動で返信してくれます",
    "アシスタントAIがおすすめです！音声で指示を与えたり質問されたりして的確なアドバイスをしてくれます",
    "音声認識AIがおすすめです！旅行先などで言語を翻訳してくれます",
    "レコメンドAIがおすすめです！あなたの趣味や行動をAIが記憶することであなたの好きな情報を届けてくれます",
    "イメージ認識AIがおすすめです！数多くのデータからあなたが見た知らないものに対して情報を与えてくれます",
    "自動発色AIがおすすめです！例えばあなたが絵を描いたとすると自動で色をつけてくれます"
]
def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get() == True:
            pts = pts + 1
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "<診断結果>\n" + KEKKA[pts])

root = tkinter.Tk()
root.title("あなたに必要なAIを診断")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=1000, height=800)
canvas.pack()
gazou = tkinter.PhotoImage(file="kyochan1.png")
canvas.create_image(90, 300, image=gazou)
button = tkinter.Button(text="あなたに必要なAIを診断する", font=("Times New Roman", 32), bg="green", command=click_btn)
button.place(x=380, y=450)
text =tkinter.Text(width=40, height=5, font=("Times New Roman", 16))
text.place(x=320, y=30)

bvar = [None]*7
cbtn = [None]*7
ITEM = [
"自分をコントロールできてないと思うことがある",
"メールの返信をするのが遅れてしまう",
"判断が曖昧で決断できない時がある",
"いろんな国の人たちとコミュニケーションがしたい",
"自分の好きなことの情報が欲しい",
"見ているものが何なのか知りたい",
"デザインしたものに色をつけたい",
]
for i in range(7):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i], font=("Times New Roman", 24), variable=bvar[i], bg="#dfe")
    cbtn[i].place(x=400, y=160+40*i)
root.mainloop() 