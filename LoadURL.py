import urllib
import sublime, sublime_plugin

class LoadUrlCommand(sublime_plugin.TextCommand):
	def loadURL(self, url):
		sublime.status_message("Loading " + url)

		f = urllib.request.urlopen(url)

		if (f.status == 200):
			data = f.read()

			if (data != ""):
				outputView = sublime.active_window().new_file()
				outputView.set_scratch(True)
				outputView.run_command("append", {"characters": data.decode('UTF-8').replace("\r\n", "\n"), "force": True, "scroll_to_end": False})
				#outputView.set_syntax_file(self.view.settings().get('syntax'))

				sublime.status_message(str(len(data)))
			else:
				sublime.status_message("No Data Returned")	
		else:
			sublime.status_message("Returned status code " + str(f.reason))

	def run(self, edit):
		self.view.window().show_input_panel("Enter a URL to load:", "", self.loadURL, None, None)


## http://feeds.macrumors.com/MacRumors-All