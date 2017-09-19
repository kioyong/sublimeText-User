import sublime
import sublime_plugin
class xxxCommand(sublime_plugin.WindowCommand):
    def run(self, reverse=False):
        window = self.window
        window.run_command("select_all")
        window.run_command("split_selection_into_lines")
        window.run_command("move_to",{"extend":False,"to":"bol"})
        window.run_command("insert", {"characters": "\""})
        window.run_command("move_to",{"extend":False,"to":"bol"})
        window.run_command("move_to",{"extend":False,"to":"eol"})
        window.run_command("insert", {"characters": "\","})
        window.run_command("right_delete")
        window.run_command("move_to",{"extend":False,"to":"eol"})
        window.run_command("left_delete")