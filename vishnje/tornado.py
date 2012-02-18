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
    '''
    
head2 = '''
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
        <script type="text/javascript">
        
        //var data = [3, 6, 2, 7, 5, 2, 1, 3, 8, 9, 2, 5, 7],
        var data = '''
bottom = ''';

        var w = 600;
        var h = 20;
        var biggest_label_size = 100;
        var chart = d3.select('body').append('svg')
            .attr('width', w + h + biggest_label_size)
            .attr('height', h * data.length);
        function draw(){
            var x_scale = d3.scale.linear().domain([0, d3.max(data)]).range([0, w]);
            var g = chart.selectAll('g')
                .data(data)
                .enter().append('g')
                .attr('transform', function(d, i){
                    return 'translate('+x_scale(d)+', '+(i*h)+')';
                    });

            g.append('circle')
                .attr('r', function(d, i){
                    return data.length - i;
                })
                .style('fill', function(d){
                    if(d>1000){
                        return 'red';
                    }
                    else{
                        return 'steelblue';
                    }
                })
                .style('fill-opacity', 0.5);

            g.append('text')
                .text(function(d){return d3.round(d);});

            window.scrollTo(0,1000000);
        }
        window.onload = draw
        </script>
        <!--input type='button' onclick='draw()' /-->
        <!--div name='chart' class='chart' /-->
  </body>
</html>
'''

def run():
    from . import glossary
    from . import feeder
    from . import server
    from . profile import history
    import pkg_resources

   #try:
    if True:
        data = feeder.read_standard_input(glossary.DataType.Line)
   #except:
   #    data = [3, 6, 2, 7, 5, 2, 1, 3, 8, 9, 2, 5, 7]
    data = history(data)

    d3_source = pkg_resources.resource_string(__name__, 'd3.js')
    d3_source = '<script type="text/javascript">'+d3_source.decode()+'</script>'
    page = head + d3_source + head2 + repr(data) + bottom

    server.present(page)

if __name__=='__main__': run()
