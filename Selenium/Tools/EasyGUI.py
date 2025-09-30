import easygui as eg

# ========== 消息框 ==========
eg.msgbox("这是一个提示信息！", title="消息框")

# ========== 单选框 ==========
choice = eg.choicebox("请选择一项：", "单选框", ["选项A", "选项B", "选项C"])
eg.msgbox(f"你选择了：{choice}", "结果")

# ========== 多选框 ==========
choices = eg.multchoicebox("可以多选：", "多选框", ["苹果", "香蕉", "橘子"])
eg.msgbox(f"你选择了：{choices}", "结果")

# ========== 单行输入 ==========
name = eg.enterbox("请输入你的名字：", "输入框")
eg.msgbox(f"你好，{name}！", "问候")

# ========== 多行输入 ==========
text = eg.textbox("请输入多行文本：", "多行输入")
eg.msgbox(f"你输入了：\n{text}", "结果")

# ========== 整数输入 ==========
num = eg.integerbox("请输入一个1到100的整数：", "整数输入", lowerbound=1, upperbound=100)
eg.msgbox(f"你输入了：{num}", "结果")

# ========== 文件选择 ==========
filename = eg.fileopenbox("选择一个文件：", "选择文件")
eg.msgbox(f"你选择了文件：{filename}", "结果")

# ========== 文件保存 ==========
savefile = eg.filesavebox("保存文件为：", "保存文件")
eg.msgbox(f"文件将保存为：{savefile}", "结果")

# ========== 目录选择 ==========
folder = eg.diropenbox("选择一个目录：", "选择目录")
eg.msgbox(f"你选择了目录：{folder}", "结果")

# ========== 确认框 ==========
if eg.ynbox("你确定要退出吗？", "确认框"):
    eg.msgbox("选择了 Yes", "结果")
else:
    eg.msgbox("选择了 No", "结果")

# ========== 异常演示 ==========
try:
    1 / 0  # 故意出错
except:
    eg.exceptionbox()
