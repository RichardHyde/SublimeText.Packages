# -*- coding: utf-8 -*-
import re
import sublime, sublime_plugin

class UnderlineCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sel = self.view.sel()[0]
    line = self.view.substr(self.view.line(sel))

    underline = "\n" + ("-" * len(line))
 
    insertPos = sel
    while(self.view.substr(sublime.Region(insertPos.a, insertPos.a+1)) != '\n' and insertPos.a < self.view.size()):
      insertPos = sublime.Region(insertPos.a+1, insertPos.a+1)

    if (insertPos.a == self.view.size()):
      underline += "\n"

    self.view.insert(edit, insertPos.begin(), underline)
    self.view.sel().clear()
    self.view.sel().add(sublime.Region(insertPos.a+len(underline)+1, insertPos.a+len(underline)+1))
    
