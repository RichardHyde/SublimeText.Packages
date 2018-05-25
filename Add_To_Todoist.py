import http.client
import sublime
import sublime_plugin
import urllib.parse
import uuid

class AddToTodoistCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    results = ""

    for region in self.view.sel():
        if not region.empty():
          items = view.split_by_newlines(region)

          for i in items:
            itemText = view.substr(i)
            indent = 1

            while(itemText.startswith("  ")):
              indent = indent + 1
              itemText = itemText[2:]

            itemText = itemText.replace("\"", "\\\"")

            if len(results) > 0:
              results += ","

            if itemText != "":
              results += """{ "type" : "item_add", 
                               "uuid" : "%s", 
                               "temp_id" : "%s", 
                               "args" : { "content" : "%s", 
                                          "indent" : %s } 
                             }""" % (uuid.uuid4(), uuid.uuid4(), itemText, indent)

    if len(results) > 0:
      self.postToTodoist(results)

  def postToTodoist(self, tasks):
    postData = { "token" : "3f70a4ae21ea2d05c8f0cf7689159700d7cbe60a", "commands" : "[" + tasks + "]" }
    postHeaders = {
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Origin': 'http://www.website.com',
                    'Referer': 'http://www.website.com/',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/37.0.2062.120 Chrome/37.0.2062.120 Safari/537.36',
                    "Content-type": "application/x-www-form-urlencoded", 
                    "Accept": "text/plain"
                }

    conn = http.client.HTTPSConnection("todoist.com")
    conn.request("POST", "/api/v7/sync", urllib.parse.urlencode(postData), postHeaders)
    response = conn.getresponse()
    data = response.read()
    conn.close()

    if (response.status != 200):
      sublime.error_message('Request returned %s : %s' % (response.status, data))
    else:
      sublime.status_message('Posted OK')
