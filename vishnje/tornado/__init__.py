# Based on http://www.janwillemtulp.com/2011/04/01/tutorial-line-chart-in-d3/ 
head = '''
<!DOCTYPE html>
<html>
  <head>
    <!--<meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="0" />-->
    <title>fun with d3</title>
    <!--script type="text/javascript" src="static/d3-v1.8.2.js"></script-->
    <style type="text/css">
        /*
        .chart div {
            font: 10px sans-serif;
            background-color: steelblue;
            text-align: right;
            padding: 3px;
            margin: 1px;
            color: white;
        }

        circle {
            stroke: white;
            fill: steelblue;
        }

        text {
            fill: white;
            font-size: 13px;
        }
        */
    </style>

    
  </head>
  <body>
  '''
bottom = '''
  </body>
</html>
'''

name = 'tornado'

def run():
    from vishnje import glossary
    from vishnje import feeder
    from vishnje import server
    from vishnje.d3 import source as d3_source
    from vishnje.process import history
    import pkg_resources

    data = feeder.read_standard_input(glossary.DataType.Line)
    data = history(data)

    data = '<script type="text/javascript">var data = {0!r};</script>'.format(data)
    source = pkg_resources.resource_string(__name__, name+'.js')
    source = '<script type="text/javascript">'+source.decode()+'</script>'
    page = head + d3_source + data + source + bottom

    server.present(page)

if __name__=='__main__': run()
