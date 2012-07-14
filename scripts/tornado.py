#!/usr/bin/python
from string import Template
import logging
import sys
import optparse

from vishnje.launch import launch, javascript_exit_handling

template = Template('''
<!DOCTYPE html>
<html>
  <head>
    <!--<meta http-equiv="cache-control" content="no-cache" />
    <meta http-equiv="pragma" content="no-cache" />
    <meta http-equiv="expires" content="0" />-->
    <title>tornado average visualization</title>
    <!--script type="text/javascript" src="static/d3-v1.8.2.js"></script-->
    <script type="text/javascript" src="http://d3js.org/d3.v2.min.js"></script>
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
        
        var data = $data
		var compress = $compress
        var h = 20
        var w = 600
        var biggest_label_size = 100
        var biggest_point_radius = 50
		if(compress){
			var total_h = 800;
		}
		else{
			var total_h = h * data.length;
		}
        var total_w = w + h + biggest_point_radius + biggest_label_size
        var chart = d3.select('body').append('svg')
            .attr('width',  total_w)
            .attr('height', total_h)
        function draw(){
            var x_scale    = d3.scale.linear().domain([d3.min(data), d3.max(data)]).range([0, w]);
            var y_scale    = d3.scale.linear().domain([0, data.length]).range([0, total_h]);
            var size_scale = d3.scale.linear().domain([0, data.length]).range([1, biggest_point_radius]);
            var g = chart.selectAll('g')
                .data(data)
                .enter().append('g')
                .attr('transform', function(d, i){
                    return 'translate('+x_scale(d)+', '+y_scale(i)+')';
                    });

            g.append('circle')
                .attr('r', function(d, i){
                    return size_scale(data.length - i);
                })
                .style('fill', function(d){
                    if(d<0){
                        return 'red';
                    }
                    else{
                        return 'steelblue';
                    }
                })
                .style('fill-opacity', 0.5);

            if(!compress){
				g.append('text')
		            .text(function(d, i){return d3.round(d) ;}).attr('x', biggest_point_radius + 40);
		        g.append('text')
		            .text(function(d, i){return (data.length - i) ;}).attr('fill', 'grey').attr('x', biggest_point_radius);
			}

            window.scrollTo(0,1000000);
        }
        window.onload = draw
        $exit_handling
        </script>
  </body>
</html>
''')


def history(ll):
    '''
    >>> [c for c in history((1, 1, 1, 1, 1))]
    [1.0, 1.0, 1.0, 1.0, 1.0]
    >>> [c for c in history((1, 2, 3, 4, 5, 6, 7))]
    [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    '''
    s = 0
    for i,l in enumerate(ll):
        s += float(l)
        yield(s/(i+1))

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)

    data = list(reversed(list(history(reversed(list(map(float, sys.stdin)))))))

    javascript_data = repr(data)

    logging.debug(data)

    parser = optparse.OptionParser()
    parser.add_option(
        '-c', '--compress', action='store_true',
        dest='compress', default=False
        )
    parser.add_option(
        '-d', '--debug', action='store_true',
        dest='debug', default=False
        )
    options, args = parser.parse_args()
    compress = 'true' if options.compress else 'false'
    if options.debug: print(data)

    page = template.safe_substitute(
        data=javascript_data,
        exit_handling=javascript_exit_handling,
        compress=compress,
        )

    logging.debug(page)

    launch(page)
