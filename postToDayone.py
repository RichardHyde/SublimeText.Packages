import sublime, sublime_plugin
import urllib.request, webbrowser

class PostToDayOneCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selections = self.view.sel()
		selection = self.view.substr(selections[0])

		url = "dayone://post?entry=%s" %  urllib.request.quote(selection)

		f = webbrowser.open(url)

		self.view.replace(edit, selections[0],  "")
		