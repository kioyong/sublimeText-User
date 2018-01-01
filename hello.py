import re
import sublime
import sublime_plugin

class HelloCommand(sublime_plugin.TextCommand):
    def run(self,edit):
        view = self.view
        region = view.find(r"www.baidu.com",0)
        if region:
            str = view.substr(region)
            view.replace(edit, region,"www.taobao.com")
            return
        region = view.find(r"hello",0)
        if region:
            str = view.substr(region)
            view.replace(edit, region,"helloWorld")
            return