from vishnje import Application

page = '''
<html>
 <head>
 {exit} <!-- optional -->
 </head>
 <body>
  It's simple, isn't it?
 </body>
</html>
'''

if __name__=='__main__':
    Application(page).launch()
