<template>
    <el-breadcrumb :separator-icon="ArrowRight">
        <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
        <el-breadcrumb-item>数据管理</el-breadcrumb-item>
        <el-breadcrumb-item>统计列表</el-breadcrumb-item>
    </el-breadcrumb>
    <div id="chart" class="chart"></div>
    <div class="charts">
        <div id="chart1"></div>
        <div id="chart2"></div>
        <div id="chart3"></div>
    </div>
</template>
<script setup>
import { ArrowRight } from '@element-plus/icons-vue'
import { getCurrentInstance, onMounted } from 'vue';
import api from '@/api/index.js';

// 获取当前实例
const { proxy } = getCurrentInstance();
// 第1个张大图
let optionBig = {
  title: {
    text: 'Temperature Change in the Coming Week'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {},
  toolbox: {
    show: true,
    feature: {
      dataZoom: {
        yAxisIndex: 'none'
      },
      dataView: { readOnly: false },
      magicType: { type: ['line', 'bar'] },
      restore: {},
      saveAsImage: {}
    }
  },
  xAxis: {
    type: 'category',
    boundaryGap: false,
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value',
    axisLabel: {
      formatter: '{value} °C'
    }
  },
  series: [
    {
      name: 'Highest',
      type: 'line',
      data: [10, 11, 13, 11, 12, 12, 9],
      markPoint: {
        data: [
          { type: 'max', name: 'Max' },
          { type: 'min', name: 'Min' }
        ]
      },
      markLine: {
        data: [{ type: 'average', name: 'Avg' }]
      }
    },
    {
      name: 'Lowest',
      type: 'line',
      data: [1, -2, 2, 5, 3, 2, 0],
      markPoint: {
        data: [{ name: '周最低', value: -2, xAxis: 1, yAxis: -1.5 }]
      },
      markLine: {
        data: [
          { type: 'average', name: 'Avg' },
          [
            {
              symbol: 'none',
              x: '90%',
              yAxis: 'max'
            },
            {
              symbol: 'circle',
              label: {
                position: 'start',
                formatter: 'Max'
              },
              type: 'max',
              name: '最高点'
            }
          ]
        ]
      }
    }
  ]
};

// 定义第1张小图的数据
let option1 = {
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            data: [150, 230, 224, 218, 135, 147, 260],
            type: 'line'
        }
    ]
};
// 定义第2张小 图的数据
let option2 = {
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: [120, 200, 150, 80, 70, 110, 130],
      type: 'bar'
    }
  ]
};
// 定义第3张小图的数据
let option3 = {
  legend: {
    top: 'bottom'
  },
  toolbox: {
    show: true,
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  series: [
    {
      name: 'Nightingale Chart',
      type: 'pie',
      radius: [50, 170],
      center: ['50%', '50%'],
      roseType: 'area',
      itemStyle: {
        borderRadius: 8
      },
      data: [
        { value: 40, name: 'rose 1' },
        { value: 38, name: 'rose 2' },
        { value: 32, name: 'rose 3' },
        { value: 30, name: 'rose 4' },
        { value: 28, name: 'rose 5' },
        { value: 26, name: 'rose 6' },
        { value: 22, name: 'rose 7' },
        { value: 18, name: 'rose 8' }
      ]
    }
  ]
};

// 页面渲染完运行
onMounted(() => {
    getCateGroup()
    proxy.$echarts('chart',optionBig)
    proxy.$echarts('chart1',option1)
    proxy.$echarts('chart3',option3)
})

// 获取分类数据
const getCateGroup =() => {
    api.get_category_group().then(res=>{
        console.log(res)
        // 更新option2中的数据
        option2.series[0].data = res.data.data.series
        // 更新option2中的横轴数据
        option2.xAxis.data =  res.data.data.xAxis
        // 渲染第2张小图
        proxy.$echarts('chart2',option2)
    })
}
</script>
<style scoped>
.chart {
    width: 100%;
    height: 500px;
    margin-top: 20px;
    background-color: white;
}

.charts {
    display: flex;
}

.charts div {
    flex: 1;
    height: 400px;
    background-color: white;
    margin: 10px;
    padding: 10px;
}
</style>