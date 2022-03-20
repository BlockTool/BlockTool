
var data = [
    {
        color: "#FFFFFF", 
        id: "0", 
        parent: "", 
        name: " "
    }, 
    {
        color: "#005F73", 
        id: "B1", 
        parent: "0", 
        name: "Block 1"
    }
,
    {
        "value": 8375, 
        "parent": "B1", 
        "name": "unit 0"
    }, 
    {
        "value": 9189, 
        "parent": "B1", 
        "name": "unit 1"
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
      'Summary of data generated by Blocktool'
  },
  series: [
    {
      type: "sunburst",
      data: data,
      allowDrillToNode: true,
      cursor: "pointer",
      borderWidth: 0.5,
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
          color: "#FFFFFF"
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
