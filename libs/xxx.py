import os
import re
import sublime
import sublime_plugin
class xxxCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # window = self.window
        view = self.view
        # print("view.id = ",view.id())#输出 view 的id,一个编号
        # print("view.buffer_id = ",view.buffer_id())
        # print("view.is_primary = ",view.is_primary())
        # print("view.file_name = ",view.file_name())# 是路径+文件名
        # view.set_name("name1")
        # print("view.name = ",view.name())
        # view.is_loading()
        # view.is_dirty()
        # print("view.is_read_only = ",view.is_read_only())
        # view.set_read_only(True)
        # print("view.is_read_only = ",view.is_read_only())
        # view.window() #returns a reference to the window containing the view
        # view.run_command("select_all") # 使用 view 一样可以run_command
        # window = view.window()
        # window.run_command("select_all")
        # print("view.size()",view.size()) #  返回当前view的字数

        ##selection
        # print("view.sel = ",view.sel()) # return a reference to the selection
        # selection = view.sel()
        # for point in selection:
        #     print("point = ",point)
        #     text = view.substr(point)
        #     print("text = ",text)
        #########################################################################
        # insert(edit, point, string)
        # replace(edit, region, string)
        ##输出当前文件目录
        # view.insert(edit,view.sel()[0].begin(),view.file_name())
        # view.replace(edit,view.sel()[0],view.file_name())
        def getpath():
            pattern = re.compile(r"\\[\w._-]+$")
            return re.sub(pattern, '', view.file_name());
        def sub(str,before,after):
            pattern = re.compile(before)
            return re.sub(pattern,after,str)
        def havespace(str):
            pattern = re.compile(r"\s")
            return re.search(pattern,str)
        ##读取文件
        # f = open('C:/Users/LiangYong/Sublime Text 3/data/Packages/User/aaa.sql')
        # data = f.read()
        # print("data1 = ",data)

        for list in os.listdir(getpath()):
            print("list = ",list)

        # list_dirs = os.walk(getpath())
        # for root, dirs, files in list_dirs:
        #     print("root =",root )
        #     print("dirs =",dirs )
        #     print("files =",files )

        ##输出当前文件目录,且不包含文件名
        # view.insert(edit,view.sel()[0].begin(),getpath())
        ##输出当前文件目录,且不包含文件名,如果path有空格,两边加双引号
        # path = getpath()
        # if havespace(path):
            # path = '"'+path+'"'
        # view.insert(edit,view.sel()[0].begin(),path)

        ##上面的条件 + 替换符号\为/
        # path = getpath()
        # path = sub(path,r"\\","/")
        # if havespace(path):
            # path = '"'+path+'"'
        # view.insert(edit,view.sel()[0].begin(),path)
#########################################################################3

        ## vector 相当于point在屏幕上的xy轴坐标，一种是从屏幕上算(window)，一种是
        ## 从sublime text 开始算(layout)，随视图文字的大小改变而改变
        # vector = view.viewport_position() # vector = (0.0,0.0)
        # vector = view.viewport_extent()
        # selection = view.sel()
        # region = selection[0]
        # point = region.begin()
        # print("point =",point )
        # print("region =",region )
        # vector = view.text_to_window(point)
        # vector = view.text_to_layout(point)
        # print("vector =",vector )
        # region = view.word(point) # 返回当前point 的word的region
        # region = view.word(region) #同上
        # print("region =",region )
        ## find
        # region = view.find("1234",0) # 根据字符串查找region
        # if region:
        #     substr = view.substr(region) #根据region查找字符串
        #     print("str = ",substr)
        # else:
        #     print("not found substr")
        ## find_all
        # regions =view.find_all("12345")
        # if regions:
        #     # for region in regions:
        #         # print("region = ",region)
        #     print("the first region = ",regions[0])
        #     if len(regions)>1:
        #         print("the last region = ",regions[len(regions)-1])
        #     else:
        #         print("only first region!")
        # else:
        #     print("not found region!")

        # view.substr(region)

    # print("hello")
'''
view.sel()  返回一个selection,selection 里面是指目前光标所在
的位置，如一个光标 代表 一个位置 region  表示为 (x,x),selection
为region的数组 代表一组region,如果光标选中一部分5个字符,那么region表示为
(x,x+5),所以一个region可以表示一个光标的位置或者一个字符串的位置,
view.substr(region) 可以获取这个坐标的字符串,如果只是光标没有选中
则返回空
point = x
region = (x,y)
selection = [(x,y),(x1,y1)]
'''