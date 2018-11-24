 var options = {
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

       var chart = new ApexCharts(
            document.querySelector("#chart2"),
            options
        );
        
        chart.render();