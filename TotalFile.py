# -*- coding: utf-8 -*-
import re
import sublime, sublime_plugin

class TotalFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		cleaned = []
		numbers = []

		region = sublime.Region(0, self.view.size());

		for lineRegion in self.view.lines(region):
			line = self.view.substr(lineRegion)

			if (line == ""):
				break

			try:
				m = re.match(ur"£\s*([0-9\.,]{1,9})\s(.*)", line)

				if (m): 
					cost = float(m.group(1).strip(' '))
					numbers.append(cost)
					desc = m.group(2)

					cleaned.append(u"£{0:>9.2f} {1}".format(cost, desc))
			except ValueError:
				cleaned.append(line)

		total = sum(numbers)
		while cleaned[-1].strip() == '':
			del cleaned[-1]

		cleaned.append("")
		cleaned.append(u"£{0:>9.2f} Total".format(total))
		cleaned = '\n'.join(cleaned)

		edit = self.view.begin_edit("")
		self.view.erase(edit, region)
		self.view.insert(edit, 0, cleaned)
		self.view.end_edit(edit)

