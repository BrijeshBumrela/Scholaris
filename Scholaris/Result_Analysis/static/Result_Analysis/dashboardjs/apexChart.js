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
    document.querySelector("#chart"),
    options
);

chart1.render();



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
                data: marks,

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
                categories: test,
            },
            colors: ['#f4c613'],
        }

        var chart1 = new ApexCharts(
            document.querySelector("#chart-1"),
            options1
        );

        chart1.render();