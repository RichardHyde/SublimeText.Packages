import sublime, sublime_plugin
import time 

class AppendToFileCommand(sublime_plugin.TextCommand):
	def run(self, edit, filename):
		newRegion = sublime.Region(0, self.view.size())
		self.view.sel().clear()
		self.view.sel().add(newRegion)
		text = self.view.substr(newRegion)
		
		newView = self.view.window().open_file(filename)

		# wait whilst loading
		# while (newView.is_loading()):
		#	time.sleep(1)

		newEdit = newView.begin_edit()
		newView.insert(newEdit, newView.size(), text)
		newView.end_edit(newEdit)
		newView.window().run_command("save")
		newView.window().run_command("close")

