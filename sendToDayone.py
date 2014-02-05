import sublime, sublime_plugin
import urllib, webbrowser

class PostToDayOneCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selections = self.view.sel()
		selection = self.view.substr(selections[0])

		url = "dayone://post?entry=%s" %  urllib.quote(selection)

		f = webbrowser.open(url)

		self.view.replace(edit, selections[0],  "")
		