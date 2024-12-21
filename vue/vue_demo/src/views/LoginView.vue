<template>
    <div class="main">
        <div class="login">
            <div class="logo">
                <img src="../assets/logo1.png" alt="">
            </div>
            <el-form :model="user" class="user_form" :rules="userRules" ref="userFormRef">
                <el-form-item prop="name">
                    <el-input v-model="user.name" placeholder="用户名" :prefix-icon="User" />
                </el-form-item>
                <el-form-item prop="pwd">
                    <el-input v-model="user.pwd" placeholder="密码" :prefix-icon="Lock" show-password />
                </el-form-item>
                <el-form-item class="btns">
                    <el-button type="primary" @click="submitForm(userFormRef)">登录</el-button>
                    <el-button type="success" @click="restForm(userFormRef)">重置密码</el-button>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script setup>
import { reactive, ref } from 'vue';
import { User, Lock } from '@element-plus/icons-vue';
import api from "@/api/index.js"; //导入api接口
import { useRouter } from 'vue-router'; //导入路由对象

const user = reactive({
  name: '',
  pwd: '',
});

const userRules = reactive({
  name: [
    { required: true, message: "用户名不能为空", trigger: "blur" },
    { min: 3, max: 10, message: "长度在3到10个字符", trigger: 'blur' }
  ],
  pwd: [
    { required: true, message: "密码不能为空", trigger: "blur" },
    { min: 3, max: 10, message: "长度在3到10个字符", trigger: 'blur' }
  ],
});

const router = useRouter();
const userFormRef = ref(null); // 确保 userFormRef 被正确定义
const errorMessage = ref('');

//定义重置表单的方法
const restForm = (formRef) => {
  if (formRef) {
    formRef.resetFields();
  } else {
    console.log('formRef is undefined');
  }
};

//定义登录功能
const submitForm = (formRef) => {
  if (formRef) {
    formRef.validate((valid) => { // 确保 formRef 被正确使用
      if (valid) {
        console.log('验证通过可以提交');
        api.login(user).then(res => {
          //根据相应的状态码进行处理
          if (res.data.status == 200) {
            ElMessage({
              message: res.data.msg,
              type: 'success',
            });
            console.log(res.data);
            //记录登录token的值
            sessionStorage.setItem('token', res.data.data.token);
            //登录成功后，跳转到主页
            router.push('/');
          } else {
            ElMessage.error(res.data.msg);
            console.log('登录失败:', res.data.msg);
          }
        })
        .catch(err => {
          console.log('API 请求错误:', err);
          ElMessage.error('登录失败，请稍后再试');
        });
      } else {
        console.log('验证失败');
      }
    });
  } else {
    console.log('formRef is undefined');
  }
};
</script>

<style scoped>
.main {
    width: 100%;
    height: 100%;
    background-color: rgb(166, 239, 21);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 5px;
    border-radius: 20px;
    box-shadow: 0 0 10px #eee;
}

.login {
    width: 450px;
    height: 300px;
    background-color: white;
}

.logo {
    width: 200px;
    border: 1px solid #eee;
    margin: 0 auto;
    margin-top: -100px;
}

img {
    width: 100%;
    height: 100%;
}

.user_form {
    padding: 30px;
}

.btns {
    display: flex;
    justify-content: space-between;
}

.btns button {
    flex: 1;
}
</style>