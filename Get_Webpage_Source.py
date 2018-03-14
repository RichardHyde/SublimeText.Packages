import sublime
import sublime_plugin
import urllib

class GetWebpageSourceCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    url = self.view.substr(self.view.sel()[0])

    if len(url) == 0:
      return

    output = ""

    r = urllib.request.urlopen(url)

    output = str(r.read(), encoding='utf8')

    newView = sublime.active_window().new_file()

    newView.insert(edit, 0, output)
