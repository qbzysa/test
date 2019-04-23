from tkinter import *
import time
import pygame
import xlrd
import random


class RandomName(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.name_list = self.get_name()
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = False
        self.timestr = StringVar()
        self.makeWidgets()
        self.data = set()

    def get_name(self):
        """
        获取所有姓名
        """
        workbook = xlrd.open_workbook("./name.xlsx")   # 读取表格
        Data_sheet = workbook.sheets()[0]              # 读取sheet1
        name_list = Data_sheet.col_values(0)           # 读取第一列
        return name_list

    def makeWidgets(self):
        """
        定义标签栏
        """
        l = Label(self, textvariable=self.timestr, font=("Arial, 35"))
        self.set_name()
        l.pack(side=TOP)

    def update(self):
        """
        更新显示内容
        """
        self._elapsedtime = time.time()-self._start
        # 设置显示内容
        self.set_name()
        # 刷新界面
        self._timer = self.after(50, self.update)

    def set_name(self):
        """
        随机产生姓名,并设置的姓名
        """
        try:
            rdata = random.choice(self.name_list)
            self.timestr.set(rdata)
            return rdata
        except:
            self.timestr.set("已遍历完")

    def Start(self):
        """
        开始
        """
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self.update()
            self._running = True

    def Stop(self):
        """
        暂停
        """
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            rdata = self.set_name()
            try:
                if len(self.name_list) == 0:
                    self.timestr.set("已遍历完")
                else:
                    self.name_list.remove(rdata)
                    if rdata not in self.data:
                        self.data.add(rdata)
            except:
                self.timestr.set("已遍历完")
        self._running = False

    def name_label(self):
        """
        显示窗口
        """
        self.pack(side=TOP)
        Button(self, text='start', command=self.Start, width=10, height=2).pack(side=LEFT)
        Button(self, text='stop', command=self.Stop, width=10, height=2).pack(side=LEFT)


def background_music(music='./一个人去巴黎.mp3'):
    """
    背景音乐
    """
    #
    pygame.init()
    pygame.mixer.init()
    # 设置加载的音乐
    pygame.mixer.music.load(music)
    # 播放音乐,loops = -1，则表示无限重复播放
    pygame.mixer.music.play(loops=-1)
    # 设置播放显示窗口
    # pygame.display.set_mode((800, 600))


if __name__ == '__main__':
    background_music()
    root = Tk()
    root.title("点名")
    root.geometry('250x120')
    sw = RandomName(root)
    sw.name_label()
    root.mainloop()
    print(sw.data)
