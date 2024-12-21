<template>
    <el-breadcrumb :separator-icon="ArrowRight">
        <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
        <el-breadcrumb-item>订单管理</el-breadcrumb-item>
        <el-breadcrumb-item>订单列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card">
        <el-row>
            <el-col :span="8">
                <el-input placeholder="请输入要搜索的订单ID" clearable>
                    <template #append>
                        <el-button :icon="Search"/>
                    </template>
                </el-input>
            </el-col>
        </el-row>
        <el-row>
            <el-table :data="orderTable.data">
                <el-table-column type="index" width="50" />
                <el-table-column label="订单用户" prop="user" width="150"></el-table-column>
                <el-table-column label="订单价格" prop="price" width="150"></el-table-column>
                <el-table-column label="订单数量" prop="number" width="150"></el-table-column>
                <el-table-column label="是否支付" prop="pay_status" width="150">
                    <template #default="scope">
                        <el-tag v-if="scope.row.pay_status === 1" type="success">已支付</el-tag>
                        <el-tag v-else type="danger">未支付</el-tag>
                    </template>
                </el-table-column>
                <el-table-column label="是否发货" prop="is_send" width="150">
                    <template #default="scope">
                        <el-tag v-if="scope.row.is_send === 1" type="success">已发货</el-tag>
                        <el-tag v-else type="danger">未发货</el-tag>
                    </template>
                </el-table-column>
                <el-table-column label="操作">
                    <template #default="scope">
                        <el-button type="primary" :icon="Promotion" size="small" @click="showExpress(scope.row.id)">查看物流</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-row>
    </el-card>
    <!-- 物流信息 -->
    <el-dialog title ='物流信息' v-model="epressDialogVisible">
        <el-timeline>
            <el-timeline-item
            v-for="(exp, index) in expressInfo.data"
            :key="index"
            :timestamp="exp.update_time"
            >
            {{ exp.content }}
            </el-timeline-item>
        </el-timeline>
    </el-dialog>
</template>

<script setup>
import { ArrowRight,Search,Promotion } from '@element-plus/icons-vue'
import { onMounted, reactive,ref } from 'vue';
import api from '@/api/index'

const orderTable = reactive({
    data: []
})
// 定义物流信息弹窗是否显示
let epressDialogVisible = ref(false)
// 定义物流信息
let expressInfo = reactive({
    data: []
})
onMounted(() => {
    getOrderList()
})
// 获取订单列表
const getOrderList =  () => {
    api.get_orders().then(res => {
        // console.log(res.data)
        orderTable.data = res.data.data
    })
}
// 查看物流
const showExpress = (id) => {
    epressDialogVisible.value =true
    api.get_express(id).then(res=>{
        expressInfo.data = res.data.data
        console.log(expressInfo.data)
    })
}
</script>

<style scoped>
.box-card {
    margin-top: 20px;
}
</style>