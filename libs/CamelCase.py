import sublime
import sublime_plugin
class CamelCaseCommand(sublime_plugin.TextCommand):
    # def run(self, edit):
    #     view = self.view
    #     selection = view.sel()
    #     for region in selection:
    #         str = view.substr(region)
    #         str = str.title()
    #         view.replace(edit,region,str)

    # def run(self, edit):
    #     view = self.view
    #     def getpath():
    #         pattern = re.compile(r"\\[\w._-]+$")
    #         return re.sub(pattern, '', view.file_name())
        # view.insert(edit,view.sel()[0].begin(),getpath())

    # def run(self, edit):
    #     view = self.view
    #     selection = view.sel()
    #     if selection:
    #         print("selection = ",selection)#输出Selection 对象 到console 面板
    #         for region in selection:
    #             print("region = ",region)#输出region
    #             print("begin point = ",region.begin())#输出region的第一个point

    #     str = view.substr(selection[0])#获取第一个光标选中的内容
    #     print("str = ",str)
    #     #输出当前文件的路径到光标位置上
    #     path = view.file_name()#获取文件名(包含路径)
    #     point =  view.sel()[0].begin()#获取当前视图第一个光标region的第一个位置
    #     view.insert(edit,point,path)#在此point上输出file_name

    # def run(self, edit):
    #     view = self.view
    #     selection = view.sel()
    #     for region in selection:
    #         str = view.substr(region)
    #         str = str.title()
    #         view.replace(edit,region,str)

    def run(self, edit):
        view = self.view
        selection = view.sel()
        for i in range(0,len(selection)):
            view.insert(edit,selection[i].begin(),str(i))


