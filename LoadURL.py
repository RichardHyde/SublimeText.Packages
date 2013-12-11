import sublime, sublime_plugin
import urllib2

class LoadUrlCommand(sublime_plugin.TextCommand):
	def loadURL(self, url):
		sublime.status_message("Loading " + url)

		f = urllib2.urlopen(url)
		data = f.read()

		if (data != ""):
			outputView = sublime.active_window().new_file()
			newEdit = outputView.begin_edit()
			outputView.insert(newEdit, 0, data)
			outputView.end_edit(newEdit)

	def run(self, edit):
		self.view.window().show_input_panel("Enter a URL to load:", "", self.loadURL, None, None)
