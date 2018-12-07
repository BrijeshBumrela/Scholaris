var options = {
    chart: {
        height: 350,
        type: 'radialBar',
		
    },
    plotOptions: {
        radialBar: {
            hollow: {
                size: '70%',
            }
        },
    },
    series: [ percentage ],
    labels: ['Your percentage'],
    fill:{
                colors: ['#f4c613']
            },
}

var chart1 = new ApexCharts(
    document.querySelector("#chart1"),
    options
);

chart1.render();


var options1 = {
            chart: {
                height: 350,
                type: 'bar',
            },
            plotOptions: {
                bar: {
                    horizontal: true,
                }
            },
            dataLabels: {
                enabled: false
            },
            fill:{
                colors: ['#f4c613']
            },
            series: [{
                data: marks
            }],
            xaxis: {
                categories: test
            },
            yaxis: {
                
            },
            tooltip: {

            }
        }

       var chart2 = new ApexCharts(
            document.querySelector("#chart2"),
            options1
        );
        
        chart2.render();