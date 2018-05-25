import sublime
import sublime_plugin


class AddLineNumbersCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		docRegion = sublime.Region(0, self.view.size())
		docText = self.view.substr(docRegion)
		docLines = docText.split("\n")

		lineCount = 1
		for i in range(1,len(docLines)):
			if docLines[i].startswith(","):
				docLines[i] = str(lineCount) + docLines[i]
				lineCount += 1

		docText = "\n".join(docLines)

		self.view.replace(edit, docRegion, docText)
