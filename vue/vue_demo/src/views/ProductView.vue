<template>
    <el-breadcrumb :separator-icon="ArrowRight">
        <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
        <el-breadcrumb-item>商品管理</el-breadcrumb-item>
        <el-breadcrumb-item>商品列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card">
        <el-row>
            <el-col :span="8">
                <el-input v-model="productTable.searchKey" placeholder="请输入要搜索的商品" clearable @clear="getProductList">
                    <template #append>
                        <el-button :icon="Search" @click="getProductList" />
                    </template>
                </el-input>
            </el-col>
            <el-col :span="4">
                <el-button type="primary" @click="addProduct">添加商品</el-button>
            </el-col>
        </el-row>
        <el-row>
            <el-table :data="productTable.data">
                <el-table-column type="index" width="50" />
                <el-table-column label="商品名称" prop="name" show-overflow-tooltip></el-table-column>
                <el-table-column label="商品价格" prop="price" width="150"></el-table-column>
                <el-table-column label="商品数量" prop="number" width="150"></el-table-column>
                <el-table-column label="商品状态" prop="state" width="150"></el-table-column>
                <el-table-column label="操作">
                    <template #default="scope">
                        <el-button type="primary" size="small">编辑</el-button>
                        <el-button type="danger" size="small" @click="removeProduct(scope.row)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-row>
    </el-card>
</template>

<script setup>
import { ArrowRight, Search } from '@element-plus/icons-vue'
import { onMounted, reactive } from 'vue';
import api from '../api/index.js'
import { useRouter } from 'vue-router';

const productTable = reactive({
    data: [],
    searchKey: null
})
const router = useRouter()

onMounted(() => {
    getProductList()
})
const getProductList = () => {
    api.get_product_list(productTable.searchKey).then(res => {
        //console.log(res)
        // //console.log(res.data.dat
        // // 将接口传递来的商品数据赋值给productTable.data
        productTable.data = res.data.data
    })
}
const removeProduct = (row) => {
    console.log(row)
    ElMessageBox.confirm(
        '是否要删除' + row.name + '该商品？',
        '删除商品',
        {
            confirmButtonText: '确定',
            cancelButtonText: '取消',
            type: 'warning',
        }
    ).then(() => {
        // 调用删除商品接口
        api.delete_product(row.id).then(res => {
            if (res.data.status == 200) {
                ElMessage({
                    type: 'success',
                    message: res.data.msg,
                })
                // 删除成功后重新获取商品列表
                getProductList()
            } else {
                ElMessage({
                    type: 'info',
                    message: res.data.msg,
                })
            }

        })
    })
        .catch(() => {
            ElMessage({
                type: 'info',
                message: '已取消删除',
            })
        })
}
const addProduct = () => {
    router.push('/add_product')
}
</script>

<style scoped>
.box-card {
    margin-top: 20px;
}
</style>