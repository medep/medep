<template>
    <div style="width:100%;height:400px;">
        <line-chart :chart-data="datacollection" :options="options"></line-chart>
    </div>
</template>

<script>
    import LineChart from './LineChart.js'
    import moment from 'moment';

    let timeFormat = 'MM/DD/YYYY HH:mm';

    let green = 'rgba(0,255,0,0.1)';
    let red = 'rgba(255,0,0,0.1)';

    function newDate(days) {
        return moment('2020-03-01').startOf('day').add(days, 'd').toDate();
    }

    export default {
        components: {
            LineChart
        },
        data() {
            return {
                datacollection: {
                    labels: [ // Date Objects
                    ],
                    datasets: [
                        {
                            label: 'Currently Infected',
                            backgroundColor: ['#2ecc71', '#2ecc71', '#2ecc71', '#2ecc71', '#2ecc71', '#2ecc71', '#2ecc71', '#2ecc71', '#2ecc71', '#2ecc71', '#85c1e9', '#85c1e9', '#85c1e9', '#85c1e9', '#85c1e9', '#85c1e9', '#85c1e9', '#85c1e9', '#85c1e9', '#85c1e9', '#d2b4de', '#d2b4de', '#d2b4de', '#d2b4de', '#d2b4de', '#d2b4de', '#d2b4de', '#d2b4de', '#d2b4de', '#d2b4de', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#9b59b6', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c', '#e74c3c', '#f5b041', '#f5b041', '#f5b041', '#f5b041', '#f5b041'],
                            borderColor: '#00ff00',
                            fill: false,
                            data: [
                                {x: moment('2020-01-03').toDate(), y: 0}, {x: moment('2020-02-24').toDate(), y: 0}, {x: moment('2020-02-25').toDate(), y: 0}, {x: moment('2020-02-26').toDate(), y: 0}, {x: moment('2020-02-27').toDate(), y: 0}, {x: moment('2020-02-28').toDate(), y: 0}, {x: moment('2020-02-29').toDate(), y: 0}, {x: moment('2020-03-01').toDate(), y: 0}, {x: moment('2020-03-02').toDate(), y: 0}, {x: moment('2020-03-03').toDate(), y: 0}, {x: moment('2020-03-04').toDate(), y: 1}, {x: moment('2020-03-05').toDate(), y: 6}, {x: moment('2020-03-06').toDate(), y: 10}, {x: moment('2020-03-07').toDate(), y: 16}, {x: moment('2020-03-08').toDate(), y: 20}, {x: moment('2020-03-09').toDate(), y: 31}, {x: moment('2020-03-10').toDate(), y: 49}, {x: moment('2020-03-11').toDate(), y: 82}, {x: moment('2020-03-12').toDate(), y: 131}, {x: moment('2020-03-13').toDate(), y: 179}, {x: moment('2020-03-14').toDate(), y: 215}, {x: moment('2020-03-15').toDate(), y: 250}, {x: moment('2020-03-16').toDate(), y: 276}, {x: moment('2020-03-17').toDate(), y: 286}, {x: moment('2020-03-18').toDate(), y: 318}, {x: moment('2020-03-19').toDate(), y: 341}, {x: moment('2020-03-20').toDate(), y: 367}, {x: moment('2020-03-21').toDate(), y: 405}, {x: moment('2020-03-22').toDate(), y: 440}, {x: moment('2020-03-23').toDate(), y: 475}, {x: moment('2020-03-24').toDate(), y: 522}, {x: moment('2020-03-25').toDate(), y: 567}, {x: moment('2020-03-26').toDate(), y: 626}, {x: moment('2020-03-27').toDate(), y: 674}, {x: moment('2020-03-28').toDate(), y: 714}, {x: moment('2020-03-29').toDate(), y: 736}, {x: moment('2020-03-30').toDate(), y: 771}, {x: moment('2020-03-31').toDate(), y: 792}, {x: moment('2020-04-01').toDate(), y: 815}, {x: moment('2020-04-02').toDate(), y: 803}, {x: moment('2020-04-03').toDate(), y: 798}, {x: moment('2020-04-04').toDate(), y: 782}, {x: moment('2020-04-05').toDate(), y: 770}, {x: moment('2020-04-06').toDate(), y: 778}, {x: moment('2020-04-07').toDate(), y: 804}, {x: moment('2020-04-08').toDate(), y: 805}, {x: moment('2020-04-09').toDate(), y: 818}, {x: moment('2020-04-10').toDate(), y: 820}, {x: moment('2020-04-11').toDate(), y: 799}, {x: moment('2020-04-12').toDate(), y: 771}, {x: moment('2020-04-13').toDate(), y: 743}, {x: moment('2020-04-14').toDate(), y: 722}, {x: moment('2020-04-15').toDate(), y: 697}, {x: moment('2020-04-16').toDate(), y: 672}, {x: moment('2020-04-17').toDate(), y: 633}, {x: moment('2020-04-18').toDate(), y: 600}, {x: moment('2020-04-19').toDate(), y: 579}, {x: moment('2020-04-20').toDate(), y: 542}, {x: moment('2020-04-21').toDate(), y: 512}, {x: moment('2020-04-22').toDate(), y: 469}, {x: moment('2020-04-23').toDate(), y: 439}, {x: moment('2020-04-24').toDate(), y: 411}, {x: moment('2020-04-25').toDate(), y: 399},
                            ],
                        },
                        {
                            label: 'Economic Sentiment',
                            fill: false,
                            backgroundColor: ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'],
                            borderWidth: 0,
                            type: 'bar',
                            yAxisID: 'B',
                            data: [
                                {x: moment('2020-01-03').toDate(), y: 0.327}, {x: moment('2020-01-06').toDate(), y: 0.327}, {x: moment('2020-01-07').toDate(), y: 0.335}, {x: moment('2020-01-08').toDate(), y: 0.353}, {x: moment('2020-01-09').toDate(), y: 0.389}, {x: moment('2020-01-10').toDate(), y: 0.436}, {x: moment('2020-01-13').toDate(), y: 0.464}, {x: moment('2020-01-14').toDate(), y: 0.474}, {x: moment('2020-01-15').toDate(), y: 0.452}, {x: moment('2020-01-16').toDate(), y: 0.432}, {x: moment('2020-01-17').toDate(), y: 0.413}, {x: moment('2020-01-20').toDate(), y: 0.410}, {x: moment('2020-01-21').toDate(), y: 0.423}, {x: moment('2020-01-22').toDate(), y: 0.437}, {x: moment('2020-01-23').toDate(), y: 0.451}, {x: moment('2020-01-24').toDate(), y: 0.446}, {x: moment('2020-01-27').toDate(), y: 0.436}, {x: moment('2020-01-28').toDate(), y: 0.430}, {x: moment('2020-01-29').toDate(), y: 0.443}, {x: moment('2020-01-30').toDate(), y: 0.455}, {x: moment('2020-01-31').toDate(), y: 0.449}, {x: moment('2020-02-03').toDate(), y: 0.439}, {x: moment('2020-02-04').toDate(), y: 0.438}, {x: moment('2020-02-05').toDate(), y: 0.459}, {x: moment('2020-02-06').toDate(), y: 0.473}, {x: moment('2020-02-07').toDate(), y: 0.480}, {x: moment('2020-02-10').toDate(), y: 0.479}, {x: moment('2020-02-11').toDate(), y: 0.485}, {x: moment('2020-02-12').toDate(), y: 0.486}, {x: moment('2020-02-13').toDate(), y: 0.488}, {x: moment('2020-02-14').toDate(), y: 0.482}, {x: moment('2020-02-17').toDate(), y: 0.489}, {x: moment('2020-02-18').toDate(), y: 0.493}, {x: moment('2020-02-19').toDate(), y: 0.497}, {x: moment('2020-02-20').toDate(), y: 0.493}, {x: moment('2020-02-21').toDate(), y: 0.447}, {x: moment('2020-02-24').toDate(), y: 0.379}, {x: moment('2020-02-25').toDate(), y: 0.321}, {x: moment('2020-02-26').toDate(), y: 0.306}, {x: moment('2020-02-27').toDate(), y: 0.290}, {x: moment('2020-02-28').toDate(), y: 0.252}, {x: moment('2020-03-02').toDate(), y: 0.222}, {x: moment('2020-03-03').toDate(), y: 0.227}, {x: moment('2020-03-04').toDate(), y: 0.239}, {x: moment('2020-03-05').toDate(), y: 0.216}, {x: moment('2020-03-06').toDate(), y: 0.112}, {x: moment('2020-03-09').toDate(), y: 0.044}, {x: moment('2020-03-10').toDate(), y: -0.016}, {x: moment('2020-03-11').toDate(), y: -0.088}, {x: moment('2020-03-12').toDate(), y: -0.180}, {x: moment('2020-03-13').toDate(), y: -0.295}, {x: moment('2020-03-16').toDate(), y: -0.312}, {x: moment('2020-03-17').toDate(), y: -0.353}, {x: moment('2020-03-18').toDate(), y: -0.379}, {x: moment('2020-03-19').toDate(), y: -0.405}, {x: moment('2020-03-20').toDate(), y: -0.449}, {x: moment('2020-03-23').toDate(), y: -0.444}, {x: moment('2020-03-24').toDate(), y: -0.432}, {x: moment('2020-03-25').toDate(), y: -0.386}, {x: moment('2020-03-26').toDate(), y: -0.363}, {x: moment('2020-03-27').toDate(), y: -0.366}, {x: moment('2020-03-30').toDate(), y: -0.359}, {x: moment('2020-03-31').toDate(), y: -0.358}, {x: moment('2020-04-01').toDate(), y: -0.368}, {x: moment('2020-04-02').toDate(), y: -0.387}, {x: moment('2020-04-03').toDate(), y: -0.377}, {x: moment('2020-04-06').toDate(), y: -0.303}, {x: moment('2020-04-07').toDate(), y: -0.230}, {x: moment('2020-04-08').toDate(), y: -0.157}, {x: moment('2020-04-09').toDate(), y: -0.125}, {x: moment('2020-04-14').toDate(), y: -0.114}, {x: moment('2020-04-15').toDate(), y: -0.122}, {x: moment('2020-04-16').toDate(), y: -0.128}, {x: moment('2020-04-17').toDate(), y: -0.126}, {x: moment('2020-04-20').toDate(), y: -0.144}, {x: moment('2020-04-21').toDate(), y: -0.174}, {x: moment('2020-04-22').toDate(), y: -0.192}, {x: moment('2020-04-23').toDate(), y: -0.197}, {x: moment('2020-04-24').toDate(), y: -0.197},
                            ],
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    scales: {
                        xAxes: [{
                            type: 'time',
                            time: {
                                unit: 'day',
                                unitStepSize: 1,
                                parser: timeFormat,
                                // round: 'day',
                                displayFormats: {
                                    'millisecond': 'MMM DD',
                                    'second': 'MMM DD',
                                    'minute': 'MMM DD',
                                    'hour': 'MMM DD',
                                    'day': 'MMM DD',
                                    'week': 'MMM DD',
                                    'month': 'MMM DD',
                                    'quarter': 'MMM DD',
                                    'year': 'MMM DD',
                                },
                                tooltipFormat: 'll'
                            },
                            scaleLabel: {
                                display: true,
                                labelString: 'Date'
                            }
                        }],
                        yAxes: [{
                            id: 'A',
                            scaleLabel: {
                                display: true,
                                labelString: 'Number of infected'
                            }
                        },
                            {
                                id: 'B',
                                type: 'linear',
                                position: 'left',
                                ticks: {
                                    max: 1,
                                    min: -1
                                },
                                display: true,
                                gridLines: {
                                    drawOnChartArea: true,
                                    zeroLineWidth: 1,
                                    lineWidth:0,
                                },
                                scaleLabel: {
                                    display: true,
                                    labelString: 'Sentiment',

                                }
                            }
                        ]
                    }
                }

            }
        },
        mounted() {
            // this.fillData()
        },
        methods: {
            fillData() {
                this.datacollection = {
                    labels: [this.getRandomInt(), this.getRandomInt()],
                    datasets: [
                        {
                            label: 'Data One',
                            backgroundColor: '#f87979',
                            data: [this.getRandomInt(), this.getRandomInt()]
                        }, {
                            label: 'Data One',
                            backgroundColor: '#f87979',
                            data: [this.getRandomInt(), this.getRandomInt()]
                        }
                    ]
                }
            },
            getRandomInt() {
                return Math.floor(Math.random() * (50 - 5 + 1)) + 5
            }
        }
    }
</script>

<style>
    .small {
        max-width: 600px;
        margin: 150px auto;
    }
</style>