$('#memory').highcharts({
        title: {
            text: 'Memory Used',
            x: 0 //center
        },
        
        xAxis: {
			categories: [memtime]
        },
        yAxis: {
            title: {
                    text: 'Memory'
            },
            plotLines: [{
                value: 0,
                width: 0.1,
                color: '#808080'
			}],
			min:0,
			max:memtotal
        },
       
        
        series: [{
            name: 'Memory Used',
			data: [memused]
        }
		]
    });
