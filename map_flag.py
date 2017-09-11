#coding=utf-8
#created by yong.a.liang
#created date 2017-09-11
#modified by xxx
#auto changed
import sublime
import sublime_plugin

class MapFlagCommand(sublime_plugin.TextCommand):
    def run(self,reverse=False):
        view = self.view
        point = view.find("pipeline",0)
        point1 = view.find("aggregate",0)
        if point:
            print("pipeline")
            view.window().run_command('run_to_agg')
        elif point1:
            print("aggregate")
            view.window().run_command('agg_to_run')
        print("false")
        # text = args.get('formula')
        # points = self.view.sel()
        # print("",points[0])
        # self.view.replace(self.view.id(),"aaa","bbb")

        # points =view.sel()
        # print(view.sel())

        # print(view.name())
        # print(view.substr(view.line(points[0])))
        # view.replace(edit,view.line(points[0]),"bbb")
        # print("hello,")
        # for x in range(0,len(points)):
