import sublime
import sublime_plugin
import random

class TestCommand(sublime_plugin.TextCommand):
    def run(self,edit,**args):
        view = self.view
        # print("view.id = ",view.id())
        # print("buffer.id = ",view.buffer_id())
        # print("is_primary = ",view.is_primary())

        ##file_name 包含路径 和文件名，如果是未保存的文件，返回None
        # print("view.file_name = ",view.file_name())
        ##return null, the name assigned to the buffer, if any?
        # view.set_name("testName")
        # print("view.name = ",view.name())
        ## return true if is loading for disk
        # print("view.is_loading = ",view.is_loading())

        # print("view.is_dirty = ",view.is_dirty())
        # print("view.is_read_only = ",view.is_read_only())
        # # print("view.is_scratch = ",view.is_scratch())

        # ##retur contect characters size
        # print("view.size = ",view.size())
        # # print("view.is_scratch = ",view.is_read_only())

        # selection = view.sel()
        # print("selection = ",selection)
        # region = view.find_by_selector("aa");
        # print("region = ",region)
        # chosen = args.get('chosen')
        # print('chosen =',chosen)
        # if (chosen > len(func) - 1):
            # print("chosen ",chosen)

        # random测试

        print("random test")
