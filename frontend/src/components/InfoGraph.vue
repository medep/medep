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
                    datasets: [{
                        label: 'Dataset 1',
                        backgroundColor: '#005f00',
                        borderColor: '#00ff00',
                        fill: false,
                        data: [
                            {x: moment('2020-03-01').toDate(), y: 1},
                            {x: moment('2020-03-02').toDate(), y: 2},
                            {x: moment('2020-03-03').toDate(), y: 5},
                            {x: moment('2020-03-04').toDate(), y: 8},
                            {x: moment('2020-03-05').toDate(), y: 15},
                            {x: moment('2020-03-06').toDate(), y: 23},
                            {x: moment('2020-03-07').toDate(), y: 30},
                            {x: moment('2020-03-08').toDate(), y: 45},
                            {x: moment('2020-03-09').toDate(), y: 60},
                            {x: moment('2020-03-10').toDate(), y: 70},
                        ],
                    }, {
                        label: 'Dataset 2',
                        fill: false,
                        backgroundColor: '#7f0000',
                        borderColor: '#FF0000',
                        data: [
                            {x: moment('2020-03-01').toDate(), y: 1},
                            {x: moment('2020-03-02').toDate(), y: 3},
                            {x: moment('2020-03-03').toDate(), y: 10},
                            {x: moment('2020-03-04').toDate(), y: 20},
                            {x: moment('2020-03-05').toDate(), y: 30},
                            {x: moment('2020-03-06').toDate(), y: 60},
                            {x: moment('2020-03-07').toDate(), y: 120},
                            {x: moment('2020-03-08').toDate(), y: 190},
                            {x: moment('2020-03-09').toDate(), y: 200},
                            {x: moment('2020-03-10').toDate(), y: 300},
                        ],
                    },
                        {
                            label: 'Sentiment',
                            fill: false,
                            backgroundColor: [green, green, green, green, green, green, red, red, red, red],
                            borderWidth: 0,
                            type: 'bar',
                            yAxisID: 'B',
                            data: [
                                {x: moment('2020-03-01').toDate(), y: 0.5},
                                {x: moment('2020-03-02').toDate(), y: 0.4},
                                {x: moment('2020-03-03').toDate(), y: 0.3},
                                {x: moment('2020-03-04').toDate(), y: 0.2},
                                {x: moment('2020-03-05').toDate(), y: 0.1},
                                {x: moment('2020-03-06').toDate(), y: 0},
                                {x: moment('2020-03-07').toDate(), y: -0.5},
                                {x: moment('2020-03-08').toDate(), y: -1},
                                {x: moment('2020-03-09').toDate(), y: -0.5},
                                {x: moment('2020-03-10').toDate(), y: -0.5},
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