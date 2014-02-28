import sublime, sublime_plugin

class CopyAppendToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selections = self.view.sel()
		clipboard = ""
		for sel in selections:
			clipboard = clipboard + self.view.substr(sel)

		clipboard = sublime.get_clipboard() + clipboard

		sublime.set_clipboard(clipboard)

class CutAppendToClipboardCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selections = self.view.sel()
		clipboard = ""
		for sel in selections:
			clipboard = clipboard + self.view.substr(sel)
			self.view.replace(edit, sel,  "")

		clipboard = sublime.get_clipboard() + clipboard

		sublime.set_clipboard(clipboard)

