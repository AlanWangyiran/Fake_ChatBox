from tkinter import *
import time


def UI(string_list):
    def sendMsg(index):  # 发送消息
        if index.get() < len(string_list):#合法性判定
            text = string_list[index.get()]
            if text.startswith("Human："):  # 角色判定
                text = text.replace("Human：", "")
                strMsg = "用户:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
                txtMsgList.insert(END, strMsg, 'greencolor')
                txtMsgList.insert(END, string_list[index.get()] + '\n')
            elif text.startswith("AI："):
                text = text.replace("AI：","")
                strMsg = "AI:" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
                txtMsgList.insert(END, strMsg, 'redcolor')
                txtMsgList.insert(END, string_list[index.get()] + '\n')
            else:
                txtMsgList.insert(END, '此行输入开头不合法' + '\n')
        else:
            strMsg = ":" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
            txtMsgList.insert(END, strMsg, 'redcolor')
            txtMsgList.insert(END, "没有更多的消息可以发送了！")
            btnSend.config(state=DISABLED)

    def cancelMsg():  # 取消信息
        txtMsg.delete('0.0', END)

    def sendMsgEvent(event):  # 发送消息事件
        if event.keysym == 'Up':
            sendMsg()

    # 创建窗口
    app = Tk()
    app.title('模型对话演示')
    # 创建frame容器
    frmLT = Frame(width=570, height=320, bg='white')
    frmLC = Frame(width=570, height=150, bg='white')
    frmLB = Frame(width=570, height=30)
    #frmRT = Frame(width=200, height=500)

    # 创建一个IntVar对象，用于存储和更新index的值
    index = IntVar(value=0)

    # 创建控件
    txtMsgList = Text(frmLT, wrap=WORD)
    txtMsgList.tag_config('greencolor', foreground='#008C00')  # 创建tag
    txtMsgList.tag_config('redcolor', foreground='#FF0000')
    txtMsg = Text(frmLC)
    txtMsg.bind("<KeyPress-Up>", sendMsgEvent)

    # 为btnSend按钮的command属性添加lambda表达式，用于传递index参数给sendMsg函数，并在每次点击后将index加一
    btnSend = Button(frmLB, text='发送', width=8, command=lambda: (sendMsg(index), index.set(index.get() + 1)))

    btnCancel = Button(frmLB, text='取消', width=8, command=cancelMsg)
    #imgInfo = PhotoImage(file="640.png")
    #lblImage = Label(frmRT, image=imgInfo)
    #lblImage.image = imgInfo
    # 窗口布局
    frmLT.grid(row=0, column=0, columnspan=2, padx=1, pady=3)
    frmLC.grid(row=1, column=0, columnspan=2, padx=1, pady=3)
    frmLB.grid(row=2, column=0, columnspan=2)
    #frmRT.grid(row=0, column=2, rowspan=3, padx=2, pady=3)

    # 固定大小
    frmLT.grid_propagate(0)
    frmLC.grid_propagate(0)
    frmLB.grid_propagate(0)
    #frmRT.grid_propagate(0)
    btnSend.grid(row=2, column=0)
    btnCancel.grid(row=2, column=1)
    #lblImage.grid()
    txtMsgList.grid()
    txtMsg.grid()
    # 主事件循环
    app.mainloop()


def loading():
    with open("text.txt", "r", encoding='UTF-8') as f:
        string_list = []
        for line in f:
            line = line.strip()
            string_list.append(line)

    # 返回字符串列表
    return string_list


if __name__ == "__main__":
    string_list = loading()
    UI(string_list)
