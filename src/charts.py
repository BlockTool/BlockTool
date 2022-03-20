__author__ = "Sanjay Somanath"

import Grasshopper as gh
import csv
import json
import os
import random
gh_path = str(os.path.dirname(gh.Instances.DocumentServer.Document[0].FilePath))+'\chart'
if not os.path.exists(gh_path):
    os.makedirs(gh_path)




#Geth the local directory
gh_path = os.path.dirname(gh.Instances.DocumentServer.Document[0].FilePath)
csvFilePath = str(gh_path) +'\\csv\\' + 'BTA_Summary.csv'


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath):
    # create a dictionary
    data = {}
    row = ['parent','name','value']
    # Open a csv reader called DictReader
    with open(csvFilePath, 'r') as readFile:
        csvReader = csv.DictReader(readFile, fieldnames=row)
        m_dict = list(csvReader)
        return m_dict
header_list = []

data = make_json(csvFilePath)
colors = ['#001219ff',
'#005f73ff',
'#0a9396ff'
'#94d2bdff',
'#e9d8a6ff',
'#ee9b00ff',
'#ca6702ff',
'#bb3e03ff',
'#ae2012ff',
'#9b2226ff']
key = ['id','parent','name','color']
value = ["0","", " ", "#FFFFFF"]
mydict = dict(zip(key,value))

header_list.append(mydict)
num_curves = len(crv)
# Automate list creation
#block_list = ["B0","B1","B2"]
block_list = []
parent_list = []
name_list = []
color_list = []
for i in range(num_curves):
    block_list.append('B'+str(i+1))
    parent_list.append("0")
    name_list.append("Block "+str(i+1))
    color_list.append(clr[i])
#parent_list = ["0","0","0"]
#name_list = ["Block 1","Block 2","Block 3"]
#Automate color list creation
#color_list = ['#001219ff','#005f73ff','#0a9396ff']

for i in range(len(block_list)):
    val =[block_list[i], parent_list[i], name_list[i], color_list[i]]
    mydict = dict(zip(key,val))
    header_list.append(mydict)

for d_dict in data:
    if 'value' in d_dict.keys():
        v_str = d_dict['value']
        d_dict['value'] = int(v_str)
    if 'Block ' in d_dict['parent']:
        b_str = d_dict['parent']
        b_str = b_str.replace('Block ', 'B')
        d_dict['parent'] = b_str

header = json.dumps(header_list,indent = 4)
header = header.replace("\"color\"","color").replace("\"parent\"","parent").replace("\"id\"","id").replace("\"name\"","name").replace("]",",")
footer = json.dumps(data, indent = 4).replace("[","")

a = header+footer+';'

script_str = """
var data = CHANGEME


Highcharts.setOptions({
  colors: ["#ecb37c", "#ECE100"]
});
Highcharts.chart("container", {
  chart: {
    height: "100%"
  },

  title: {
    text: "SCRIPTTITLE"
  },
  subtitle: {
    text:
      'SCRIPTSUBTITLE'
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
          color: "TEXTCOLOR"
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
"""


html = """
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>HTMLTITLE</title>
  <link rel="stylesheet" href="./style.css">

</head>
<body>
<!-- partial:index.partial.html -->
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://code.highcharts.com/modules/sunburst.js"></script>
<script src="https://code.highcharts.com/modules/exporting.js"></script>
<script src="https://code.highcharts.com/modules/accessibility.js"></script>

<div id="container"></div>
<!-- partial -->
  <script  src="./script.js"></script>

</body>
</html>

"""

css = """
#container {
	min-width: 310px;
	max-width: 500px;
	margin: 0 auto
}
"""

if write_chart:
    scriptFilePath = str(gh_path) +'\\chart\\' + 'script.js'
    script_str = script_str.replace('CHANGEME', a).replace('SCRIPTSUBTITLE',scriptsubtitle).replace('SCRIPTTITLE',scripttitle).replace('TEXTCOLOR',textcolor)
    with open(scriptFilePath, 'w') as f:
        f.write(script_str)
    htmlFilePath = str(gh_path) +'\\chart\\' + 'index.html'
    cssFilePath = str(gh_path) +'\\chart\\' + 'style.css'
    with open(htmlFilePath, 'w') as f:
        f.write(html.replace('HTMLTITLE',htmltitle))
    with open(cssFilePath, 'w') as f:
        f.write(css)
html_path = str(gh_path) +'\\chart\\' + 'index.html'