import sublime, sublime_plugin

class AppendToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selections = self.view.sel()
		clipboard = ""
		for sel in selections:
			clipboard = clipboard + self.view.substr(sel)

		clipboard = sublime.get_clipboard() + clipboard

		sublime.set_clipboard(clipboard)

