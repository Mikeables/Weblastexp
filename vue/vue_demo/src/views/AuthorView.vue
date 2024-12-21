<template>
    <el-breadcrumb :separator-icon="ArrowRight">
        <el-breadcrumb-item :to="{ path: '/' }">Home</el-breadcrumb-item>
        <el-breadcrumb-item>权限管理</el-breadcrumb-item>
        <el-breadcrumb-item>角色列表</el-breadcrumb-item>
    </el-breadcrumb>
    <el-card class="box-card">
        <el-row>
            <el-button type="primary" :icon="CirclePlus" @click="authDialogVisible">添加角色</el-button>
        </el-row>
        <el-row>
            <el-table :data="tableData.authorList" stripe class="table">
                <el-table-column type="expand">
                    <template #default="scope">
                        <el-row v-for="(m, i) in scope.row.menus" :key="m.id"
                            :class="['padding bottom', i === 0 ? 'top' : '']">
                            <el-col :span="2"><el-tag class="margin-t10" closable @click="removeMenu(scope.row, m.id)">{{
                                m.name }}</el-tag></el-col>
                            <el-col :span="1"><el-icon class="margin-t15">
                                    <CaretRight />
                                </el-icon></el-col>
                            <el-col :span="21"><el-tag class="margin-t10" type="success" v-for="cm in m.children"
                                    :key='cm.id' closable @click="removeMenu(scope.row, cm.id)">{{ cm.name
                                    }}</el-tag></el-col>
                        </el-row>
                    </template>
                </el-table-column>
                <el-table-column prop="id" label="id" width="50" />
                <el-table-column prop="name" label="名称" />
                <el-table-column prop="desc" label="详情" />
                <el-table-column label="操作">
                    <template #default="scope">
                        <el-button>编辑</el-button>
                        <el-button type="primary" @click="showMenuDialog(scope.row)">分配权限</el-button>
                        <el-button type="danger">删除</el-button>
                    </template>
                </el-table-column>


            </el-table>
        </el-row>
    </el-card>
    <!--分配权限-->
    <el-dialog v-model="menuDialogVisible" title="分配权限" width="40%" :before-close="handleClose">
        <el-tree :data="menuList" :props="menuProps" @node-click="handleNodeClick" show-checkbox node-key="id" ref="treeRef" default-expand-all	/>
        <template #footer>
            <span class="dialog-footer">
                <el-button @click="menuDialogVisible = false">取消</el-button>
                <el-button type="primary" @click="submitMenu">
                    确定
                </el-button>
            </span>
        </template>
    </el-dialog>
    <!--增加角色-->
    <el-dialog v-model="authDialogVisible" title="增加角色">

    </el-dialog>
        
</template>
<script setup>
import { ArrowRight, CaretRight, CirclePlus, Failed, TrendCharts } from '@element-plus/icons-vue'
import api from '@/api/index.js'
import { reactive, onMounted, ref ,nextTick} from 'vue';


let menuDialogVisible = ref(false)
let authDialogVisible=ref(false)
let menuList = reactive([])
const menuProps = {
    children: 'children',
    label: 'name',
}
const treeRef = ref(null)
const tableData = reactive({
    authorList: []

})

let KeyList = reactive([])
let rid = ref(null)


onMounted(() => {
    get_author_list()
    getMenuList()
})
//获取角色列表

const get_author_list = () => {
    api.get_roles().then(res => {
        console.log(res)
        tableData.authorList = res.data.data
    })

}

//删除角色权限
const removeMenu = (row, mid) => {
    ElMessageBox.confirm(
        '确认删除该角色的权限吗？',
        '提示',
        {
            confirmButtonText: '确认',
            cancelButtonText: '取消',
            type: 'warning',
        }
    )
        .then(() => {
            ElMessage({
                type: 'success',
                message: '删除成功',
            })
            api.del_role_menu(row.id, mid).then(res => {
                console.log(res.data)
                get_author_list()
            })
        })
        .catch(() => {
            ElMessage({
                type: 'info',
                message: '已取消删除',
            })
        })
}
const showMenuDialog = (row) => {
    menuDialogVisible.value = true
    //初始化选中的菜单
    KeyList =[]
    //获取一级菜单
    row.menus.forEach(item => {
        //获取二级菜单
        item.children.forEach(citem =>{
            //记录选中的菜单id
            KeyList.push(citem.id)

        })        
    });
    //给书机构填写默认值
    //console.log(KeyList)
    nextTick(() =>{//当前Dom渲染完以后执行
        treeRef.value.setCheckedKeys(KeyList)
    })
    //给角色id复制
    rid.value = row.id

}
const getMenuList = () => {
    api.get_menu().then(res => {
        menuList = res.data.data
    })
}
const submitMenu =() =>{
    //获取菜单id
    let mids =[
        treeRef.value.getCheckedKeys(),
        treeRef.value.getHalfCheckedKeys(),
    ]
    mids = mids.join(',')
    console.log(mids)
    //获取角色id
    console.log(rid.value)
    //提交数据
    api.set_menu(rid.value,{'mids':mids}).then(res =>{
        console.log(res.data)
        menuDialogVisible.value = false
        get_author_list()
    })
}
</script>
<style scoped>
.box-card {
    margin-top: 20px;
}

.padding {
    padding-left: 200px;
}

.top {
    border-top: 1px solid #eee;
}

.bottom {
    border-bottom: 1px solid #eee;
}

.margin-t10 {
    margin: 10px;
}

.margin-t15 {
    margin: 15px;
}
</style>