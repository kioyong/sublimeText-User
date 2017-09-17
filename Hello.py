import sublime
import sublime_plugin

class MapFlagCommand(sublime_plugin.TextCommand):
    def run(self,reverse=False):
        view = self.view
        # print("view.id = ",view.id())
        # print("buffer.id = ",view.buffer_id())
        # print("is_primary = ",view.is_primary())

        ##file_name 包含路径 和文件名，如果是未保存的文件，返回None
        # print("view.file_name = ",view.file_name())
        ##return null, the name assigned to the buffer, if any?
        # view.set_name("name")
        # print("view.name = ",view.name())
        # self.random
