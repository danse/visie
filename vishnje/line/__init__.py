# Based on http://www.janwillemtulp.com/2011/04/01/tutorial-line-chart-in-d3/ 
head_start = '''
<!DOCTYPE html>
<html>
  <head>
    <!--<meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="0" />-->
    <title>fun with d3</title>
    <!--script type="text/javascript" src="static/d3-v1.8.2.js"></script-->
    '''

    
head_end = '''
  </head>
  <body>
  '''
bottom = '''
  </body>
</html>
'''

name = 'line'

def run():
    from vishnje import glossary
    from vishnje import feeder
    from vishnje import server
    from vishnje.d3 import source as d3_source
    from vishnje.process import history
    import pkg_resources

    data_y = [1, 2, 3, 4]
    data_y = feeder.read_standard_input(glossary.DataType.Line)
    data_x = list(range(len(data_y)))

    data_y = '<script type="text/javascript">var data_y = {0!r};</script>'.format(data_y)
    data_x = '<script type="text/javascript">var data_x = {0!r};</script>'.format(data_x)
    source = pkg_resources.resource_string(__name__, name+'.js')
    source = '<script type="text/javascript">'+source.decode()+'</script>'
    style = pkg_resources.resource_string(__name__, name+'.css')
    style = '<style type="text/css">'+style.decode()+'</style>'
    page = head_start + style + head_end + d3_source + data_x + data_y + source + bottom

    server.present(page)

if __name__=='__main__': run()
