// Chart Options

const options = {
    chart: {
        height:450,
        width:'100%',
        type:'line',
        background:'#f4f4f4',
        foreColor:'#333'
    },
    series: [
        {
            name: 'sales-1',
            data: [30,40,35,50,49,60,70,91,125,21]
        },
        {
            name: 'sales-2',
            data: [31,43,54,78,10,30,48,80,10,31]
        },
        {
            name: 'sales-3',
            data: [30,40,35,50,49,60,70,91,125,50]
        }
    ],
    xaxis: {
        categories: ['New York','Los Angeles','Chicago','Houston','Philadelphia','Phoenix'
        ,'San Antonio','San Diego','Dallas','San Jose']
    },
    plotOptions: {
        bar: {
            horizontal: false,
        }
    },
    fill: {
        type: 'gradient',
        gradient: {
          shade: 'dark',
          type: "horizontal",
          shadeIntensity: 0.5,
          gradientToColors: undefined, // optional, if not defined - uses the shades of same color in series
          inverseColors: true,
          opacityFrom: 1,
          opacityTo: 1,
          stops: [0, 50, 100]
        }
    },
    dataLabels: {
        enabled:false,
    },
    title: {
        text: 'Largest US Cities by Population',
        align: 'center',
        margin: 20,
        offsetY: 20,
        style: {
            fontSize: '25px',
        }
    },
    theme: {
        palette:'palette1'
    }
};


const options2 = {
    chart: {
      height: 350,
      type: 'radialBar',
      toolbar: {
        show: true
      }
    },
    plotOptions: {
      radialBar: {
        startAngle: 0,
        endAngle: 275,
         hollow: {
          margin: 0,
          size: '70%',
          background: '#fff',
          image: undefined,
          imageOffsetX: 0,
          imageOffsetY: 0,
          position: 'front',
          dropShadow: {
            enabled: true,
            top: 3,
            left: 0,
            blur: 4,
            opacity: 0.24
          }
        },
        track: {
          background: '#fff',
          strokeWidth: '67%',
          margin: 0, // margin is in pixels
          dropShadow: {
            enabled: true,
            top: -3,
            left: 0,
            blur: 4,
            opacity: 0.35
          }
        },

        dataLabels: {
          showOn: 'always',
          name: {
            offsetY: -20,
            show: true,
            color: '#888',
            fontSize: '17px'
          },
          value: {
            formatter: function(val) {
              return 75;
            },
            color: '#111',
            fontSize: '36px',
            show: true,
          }
        }
      }
    },
    fill: {
      type: 'gradient',
      gradient: {
        shade: 'dark',
        type: 'horizontal',
        shadeIntensity: 0.5,
        gradientToColors: ['#ABE5A1'],
        inverseColors: true,
        opacityFrom: 1,
        opacityTo: 1,
        stops: [0, 100]
      }
    },
    series: [75,91],
    stroke: {
      lineCap: 'round'
    },
    labels: ['Percent','You got'],

  }

// Init Chart

const chart = new ApexCharts(document.querySelector('#chart'), options);
const chart2 = new ApexCharts(document.querySelector('#chart-2'), options2);

// Render Chart

chart.render();
chart2.render();