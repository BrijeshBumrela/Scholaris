var options1 = 
		{
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
            fill:{
                colors: ['#f4c613']
            },
            series: [percentage],
            labels: ['course percentage'],

        }

        var chart1 = new ApexCharts(
            document.querySelector("#chart1"),
            options1
        );

        chart1.render();
var options2 = {
            chart: {
                height: 400,
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
            options2
        );
        
        chart2.render();
