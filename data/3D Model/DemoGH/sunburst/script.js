var data = [
  {
    id: "0",
    parent: "",
    name: " ",
    color: "#FFFFFF"
  },
  {
    id: "B0",
    parent: "0",
    name: "Block 0",
    color: "#ecb37c"
  },
  {
    id: "B1",
    parent: "0",
    name: "Block 1",
    color:"#7CB5EC"
  },
  {
    id: "B2",
    parent: "0",
    name: "Block 2",
    color:"#7CB4EC"
  },
  {
    "parent": "B0",
    "name": "unit 0",
    "value": 609
  },
  {
    "parent": "B0",
    "name": "unit 1",
    "value": 762
  },
  {
    "parent": "B0",
    "name": "unit 2",
    "value": 914
  },
  {
    "parent": "B0",
    "name": "unit 3",
    "value": 762
  },
  {
    "parent": "B0",
    "name": "unit 4",
    "value": 892
  },
  {
    "parent": "B0",
    "name": "unit 5",
    "value": 914
  },
  {
    "parent": "B0",
    "name": "unit 6",
    "value": 1076
  },
  {
    "parent": "B0",
    "name": "unit 7",
    "value": 535
  },
  {
    "parent": "B0",
    "name": "unit 8",
    "value": 457
  },
  {
    "parent": "B0",
    "name": "unit 9",
    "value": 762
  },
  {
    "parent": "B1",
    "name": "unit 1",
    "value": 430
  },
  {
    "parent": "B1",
    "name": "unit 2",
    "value": 516
  },
  {
    "parent": "B1",
    "name": "unit 3",
    "value": 2730
  },
  {
    "parent": "B1",
    "name": "unit 4",
    "value": 344
  },
  {
    "parent": "B1",
    "name": "unit 5",
    "value": 516
  },
  {
    "parent": "B1",
    "name": "unit 6",
    "value": 516
  },
  {
    "parent": "B1",
    "name": "unit 7",
    "value": 2184
  },
  {
    "parent": "B2",
    "name": "unit 1",
    "value": 3040
  },
  {
    "parent": "B2",
    "name": "unit 2",
    "value": 384
  },
  {
    "parent": "B2",
    "name": "unit 3",
    "value": 3040
  }
];

Highcharts.setOptions({
  colors: ["#ecb37c", "#ECE100"]
});
Highcharts.chart("container", {
  chart: {
    height: "100%"
  },

  title: {
    text: "Summary of BTA"
  },
  subtitle: {
    text:
      'Data generated from BlockTool by SOS'
  },
  series: [
    {
      type: "sunburst",
      data: data,
      allowDrillToNode: true,
      cursor: "pointer",
      borderWidth: 3,
      borderColor: "#000000",
      dataLabels: {
        format: "{point.name}",
        filter: {
          property: "innerArcLength",
          operator: ">",
          value: 16
        },
        style: {
          textOutline: false,
          color: "#000000"
        }
      },
      levels: [
        {
          level: 1,
          levelIsConstant: false,
          dataLabels: {
            filter: {
              property: "outerArcLength",
              operator: ">",
              value: 64
            }
          }
        },
        {
          level: 2,
          colorByPoint: true
        },
        {
          level: 3,
          colorVariation: {
            key: "brightness",
            to: -0.5
          }
        },
        {
          level: 4,
          colorVariation: {
            key: "brightness",
            to: 0.5
          }
        }
      ]
    }
  ],
  tooltip: {
    headerFormat: "",
    pointFormat: "The area of <b>{point.name}</b> is <b>{point.value}</b> kvm"
  }
});