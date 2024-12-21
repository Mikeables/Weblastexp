<template>
    <el-breadcrumb :separator-icon="ArrowRight">
        <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
        <el-breadcrumb-item>权限管理</el-breadcrumb-item>
        <el-breadcrumb-item>权限列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card">
        <el-row>
            <el-table :data="tableData.menuList" stripe class="table">
                <el-table-column prop="id" label="id" width="50" />
                <el-table-column prop="name" label="名称" />
                <el-table-column prop="path" label="路径" />
                <el-table-column prop="level" label="等级">
                    <template #default="scope">
                    <el-tag v-if="scope.row.level == 1">一级</el-tag>
                    <el-tag v-else type="success">二级</el-tag>
                    </template>
                </el-table-column>


            </el-table>
        </el-row>


    </el-card>
</template>
<script setup>
import { ArrowRight } from '@element-plus/icons-vue'
import { reactive,onMounted } from 'vue';
import api from '@/api/index.js'
const tableData = reactive({
    menuList: []
})
onMounted(()=>{
    get_menu_list()
})
const get_menu_list =() =>{
    api.get_menu_list().then(res =>{
        tableData.menuList = res.data.data
    })

}
</script>

<style scoped>
.box-card {
    margin-top: 20px;
}
</style>