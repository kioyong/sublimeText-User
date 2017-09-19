import sublime
import sublime_plugin
class xxxCommand(sublime_plugin.WindowCommand):
    def run(self, reverse=False):
        window = self.window
        window.run_command("select_all")
        window.run_command("split_selection_into_lines")