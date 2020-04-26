const verticalLinePlugin = {
    getLinePosition: function (chart, pointIndex) {
        const meta = chart.getDatasetMeta(0); // first dataset is used to discover X coordinate of a point
        const data = meta.data;
        return data[pointIndex]._model.x;
    },
    renderVerticalLine: function (chartInstance, pointIndex, label, scaleIndex) {
        const lineLeftOffset = this.getLinePosition(chartInstance, pointIndex);
        const scale = chartInstance.scales[scaleIndex];
        const context = chartInstance.chart.ctx;

        // render vertical line
        context.beginPath();
        context.strokeStyle = '#ff0000';
        context.moveTo(lineLeftOffset, scale.top);
        context.lineTo(lineLeftOffset, scale.bottom);
        context.stroke();

        // write label
        context.fillStyle = "#ff0000";
        context.textAlign = 'center';
        context.fillText(label, lineLeftOffset, scale.bottom - 10);
    },

    afterDatasetsDraw: function (chart, easing) {
        if (chart.config.options.lineAtIndex) {
            chart.config.options.lineAtIndex.points.forEach(pointIndex => this.renderVerticalLine(chart, pointIndex.index, pointIndex.label, chart.config.options.lineAtIndex.scale));
        }
    }
};

Chart.plugins.register(verticalLinePlugin);