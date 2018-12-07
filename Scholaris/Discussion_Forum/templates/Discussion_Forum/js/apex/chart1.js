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
            series: [70],
            labels: ['Your percentage'],

        }

        var chart = new ApexCharts(
            document.querySelector("#chart1"),
            options
        );

        chart.render();