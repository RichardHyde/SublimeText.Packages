import sublime
import sublime_plugin
import re

class RemoveBlankLinesCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		docRegion = sublime.Region(0, self.view.size())

		docText = self.view.substr(docRegion)

		docText = re.sub("\n\s*\n", "\n", docText)

		self.view.replace(edit, docRegion, docText)
