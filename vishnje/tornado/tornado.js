
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
 /*     .style('fill', function(d){
            if(d>1000){
                return 'red';
            }
            else{
                return 'steelblue';
            }
        })*/
        .style('fill-opacity', 0.5);

    g.append('text')
        .text(function(d){return d3.round(d);});

    window.scrollTo(0,1000000);
}
window.onload = draw
