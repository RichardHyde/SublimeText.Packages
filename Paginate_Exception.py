import sublime
import sublime_plugin
import re

class PaginateExceptionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		docRegion = sublime.Region(0, self.view.size())
		
		docText = self.view.substr(docRegion)

		docText = re.sub("\s+at ", "\nat ", docText)
		docText = re.sub("\n\n", "\n", docText)

		self.view.replace(edit, docRegion, docText)

