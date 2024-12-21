import * as echarts from 'echarts';

export default {
    // echarts 作为全局变量使用
    install:app=>{
        // 配置全局变量,element代表将图表渲染到哪个元素上
        app.config.globalProperties.$echarts = (element,option) => {
            // 创建一个echarts实例
            let myChart = echarts.init(document.getElementById(element));
            // 创建图表需要显示的数据
     
            // 渲染图表
            myChart.setOption(option);
        }
    }
}