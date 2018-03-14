# -*- coding: utf-8 -*-
import re
import sublime, sublime_plugin

class TotalFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    cleaned = []
    numbers = []
    totalCurrency = ""

    region = sublime.Region(0, self.view.size());

    for lineRegion in self.view.lines(region):
      line = self.view.substr(lineRegion)

      if (line == ""):
        break

      try:
        m = re.match(u"([£$€])\s*([0-9\.,]{1,9})\s*(.*)", line, re.U)

        if (not m):
          m = re.match(u"\s*([0-9\.,]{1,9})\s*(.*)", line, re.U)

        if (m):
          currency = ""
          gl = len(m.groups())
          if gl >= 3:
            currency = m.group(1).strip(' ')
            if len(totalCurrency) == 0:
              totalCurrency = currency

          cost = float(m.group(gl-1).strip(' '))
          numbers.append(cost)
          desc = m.group(gl)

          cleaned.append(u"{0}{1:>9.2f} {2}".format(currency, cost, desc))
        else:
          cleaned.append(line)
      except ValueError:
        cleaned.append(line)

    total = sum(numbers)
    if (len(cleaned) > 0):
      while cleaned[-1].strip() == '':
        del cleaned[-1]

    cleaned.append("")
    cleaned.append(u"{0}{1:>9.2f} Total".format(totalCurrency, total))
    cleaned = '\n'.join(cleaned)

    #edit = self.view.begin_edit("")
    self.view.erase(edit, region)
    self.view.insert(edit, 0, cleaned)
    #self.view.end_edit(edit)

