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
            series: [79, 52, 61],
            labels: ['Highest', 'Mean', 'Your'],
           
            markers: {
           		colors: ['#ffff00']
           	}
            
        }

       var chart = new ApexCharts(
            document.querySelector("#chart"),
            options
        );
        
        chart.render();



// Line Chart 


var options1 = {
            chart: {
                height: 300,
                type: 'line',
                zoom: {
                    enabled: false,
                },
                foreColor: 'white',
             },
           
            fill:{
                colors: ['#f4c613']
            },
            dataLabels: {
                enabled: false
            },
            stroke: {
                curve: 'straight',


            },
            series: [{
                name: "Marks",
                data: [30, 41, 35, 51, 49, 62, 69, 91, 73],

            }],
            title: {
                text: 'Recent Test Results',
                align: 'center',
                margin: 20,
                offsetY: 20,
                style: {
                    fontSize: '25px',
                    color: '#212226', 
                },
            },
            grid: {
                row: {
                    colors: ['transparent', 'transparent'], // takes an array which will be repeated on columns
                    opacity: 0.5
                },
            },
            xaxis: {
                categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
            },
            colors: ['#f4c613'],
        }

        var chart1 = new ApexCharts(
            document.querySelector("#chart-1"),
            options1
        );

        chart1.render();