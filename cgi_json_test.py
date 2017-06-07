#!/usr/bin/env python
# json test ${NoProductionReady}$
import sys
import os
import cgi
import json

APP_BASE_DIR = '/tmp/iarlypyapp'
APP_DATA_DIR = APP_BASE_DIR+'/data'
APP_TEMPLATE_DIR = APP_BASE_DIR+'/templates/'

class iarlyWebApp:
        def printException(self):
                return '<b>Application Exception:</b>'

        def http_header(self, contentType='html'):
                if contentType == 'json':
                        return 'Content-type: application/json\r\n\r\n'
                else:
                        return 'Content-type: text/html\r\n\r\n'

        def html_template(self, part_name):
                part_name_path = APP_TEMPLATE_DIR+'/'+part_name+'.tmpl'
                try:
                        output = ''
                        template_fileh = open(part_name_path, 'r')
                        for l in template_fileh.readlines():
                                output += l
                        return output
                        template_fileh.close()
                except:
                        return self.printException()

class iarlyRestApp:
        def printException(self):
                return '{ "responseStatus": "Exception", }'

        def jsonRead(self, json):
                return json.replace('\\','\\\\').replace('\\"','\\\\"')

app = iarlyWebApp()
rest = iarlyRestApp()

if __name__ == "__main__":
        try:
                print(app.http_header('json'))
                with open('/tmp/iarlypyapp/data/import/x.json', 'r') as js_line:
                        d = json.loads(rest.jsonRead(js_line.read()), strict=False)
                        #print d['conditions'][0]['name'] #overrideAttributes']['eventText']
                        print d['conditions'][0]['overrideAttributes']['eventText']
                        print json.dumps(d, sort_keys=True, indent=4)
                        json.dump(js_line, open('/tmp/test.json','w'), sort_keys = True, indent = 4, ensure_ascii=Fasle)
        except:
                print(app.printException(), sys.exc_info())
