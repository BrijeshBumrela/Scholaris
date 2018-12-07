var options = {
            chart: {
                height: 400,
                type: 'radialBar',
            },

            title: {
                text: 'Performance Comparison',
                align: 'center',
                margin: 20,
                offsetY: 20,
                style: {
                    fontSize: '25px',
                    color: '#212226',
                },
            },

            plotOptions: {
                circle: {
                    dataLabels: {
                        showOn: 'hover'
                    }
                },
                radialBar: {
                    hollow: {
                        margin: 5,
                        size: '60%',
                        background: 'transparent',
                        image: undefined,
                    },
                }
            },
            colors: ['#212226','#f4c613','#A9A9A9'],
            series: [highest, average, percentage],
            labels: ['Highest', 'Course Mean', 'Your Percentage'],
           
            markers: {
                colors: ['#ffff00']
            }
            
        }

       var chart = new ApexCharts(
            document.querySelector("#chart1"),
            options
        );
        
        chart.render();

var options1 = {
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
            options1
        );
        
        chart2.render();
