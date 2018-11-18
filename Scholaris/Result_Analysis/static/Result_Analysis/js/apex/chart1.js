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
    series: [percentage],
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
                data: [90, 50, 78, 70, 40, 86, 60, 39, 72, 81]
            }],
            xaxis: {
                categories: ['Test1', 'Test2', 'Test3', 'Test4', 'Test5', 'Test6', 'Test7', 'Test8', 'Test9', 'Test10'],
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