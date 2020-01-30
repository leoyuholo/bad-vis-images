labels_from_tags_mapping = {
    'Triangle': ['form:pyramid'],
    'Pyramid': ['form:pyramid'],
    'TriangleChart': ['form:pyramid'],

    'Iconography': ['layout:infographics'],
    'ISOTYPE': ['layout:infographics'],

    'Euler': ['form:venn', 'data:set'],
    'Venn': ['form:venn', 'data:set'],
    'EulerDiagram': ['form:venn', 'data:set'],

    'NotPartToWhole': ['fault:percentage'],
    'NotPartWhole': ['fault:percentage'],
    'PartToWhole': ['fault:percentage'],
    'Percentages': ['fault:percentage'],
    'Percentage': ['fault:percentage'],

    'StackedBarChart': ['encoding:rectangle', 'form:barchart', 'encoding:stacked'],
    'BarChart': ['encoding:rectangle', 'form:barchart'],
    'bar graph': ['encoding:rectangle', 'form:barchart'],
    'bar graphs': ['encoding:rectangle', 'form:barchart'],
    'BarCharts': ['encoding:rectangle', 'form:barchart'],

    '3D': ['fault:3d'],
    '3D is Cool!': ['fault:3d'],

    'LineChart': ['encoding:line', 'form:linechart'],
    'line chart': ['encoding:line', 'form:linechart'],
    'line graph': ['encoding:line', 'form:linechart'],

    'Radial': ['layout:circular'],
    'PieChart': ['layout:circular', 'form:piechart'],
    'Pie Gore': ['layout:circular', 'form:piechart'],
    'PieCharts': ['layout:circular', 'form:piechart'],
    'pie chart': ['layout:circular', 'form:piechart'],
    'DonutChart': ['layout:circular', 'form:donutchart'],
    'DonutCharts': ['layout:circular', 'form:donutchart'],
    'Wedges': ['layout:circular'],
    'CoxcombChart': ['layout:circular'],

    'NetworkDiagram': ['data:network'],
    'NetworkGraph': ['data:network'],
    'Network': ['data:network'],
    'Graph': ['data:network'],

    'Map': ['data:geospatial'],
    'maps': ['data:geospatial'],
    'choropleth': ['data:geospatial'],

    'AreaChart': ['encoding:area'],
    'Area/Volume': ['encoding:area'],

    'LabelLines': ['fault:label'],
    'Labeling': ['fault:label'],

    'Bad Scale': ['fault:scale'],
    'Units': ['fault:scale'],

    'Axes': ['fault:axis'],

    'Clusterfuck': ['fault:cluttering'],

    'Timeline': ['data:timeseries'],

    'Rainbow': ['fault:color'],

    'BubbleChart': ['form:scatterplot'],
    'Scatterplot': ['form:scatterplot'],

    'NotPeriodic': ['metaphor:periodictable'],
    'Gears': ['metaphor:gear'],
    'Clock': ['metaphor:clock'],
    'Dial': ['metaphor:gauge'],

    'Ratios': ['fault:description'],

    'RadarPlot': ['form:radarchart'],

    'Arrows': ['fault:connection'],
    'Flawed Flows': ['fault:connection'],
    'FlowChart': ['fault:connection']
}

def labels_from_tags (tags):
    return list({l for t in tags if t in labels_from_tags_mapping for l in labels_from_tags_mapping[t]})