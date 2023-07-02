<template>
  <div>
    <div class="tech-box">
      <div class="tech-title">
        <div class="tech-title-line" />
        <div class="tech-title-text">添加用户</div>
      </div>
    </div>

    <el-card style="width:25%;margin: auto;">
      <el-form ref="form" :model="form" label-width="120px">
        <el-form-item label="用户名">
          <el-input v-model="form.name" />
        </el-form-item>
        <el-form-item label="设置密码" prop="password">
          <el-input v-model="form.password" show-password />
        </el-form-item>
        <el-form-item label="用户类别">
          <el-radio-group v-model="form.access">
            <el-radio label="高级用户" />
            <el-radio label="普通用户" />
          </el-radio-group>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">添加用户</el-button>
          <el-button @click="reset">重置</el-button>
        </el-form-item>
      </el-form>
    </el-card></div>
</template>

<script>
import {regeisted} from '@/api/user'
export default {
  data() {
    return {
      form: {
        name: '',
        access: '',
        password: ''
      }
    }
  },
  methods: {
    onSubmit() {
      regeisted(this.form).then(res => {
          console.log(res)
          if (res.code === 20000){
            this.$message({
            message: '注册成功',
            type: 'success'
        })}
  })

},
    reset() {
      this.$message({
        message: '重置表单',
        type: 'warning'
      })
      this.form.name = ''
      this.form.resource = ''
      this.form.password = ''
    },
    }}

</script>

<style scoped>
.line{
  text-align: center;
}

.el-input {
    display: inline-block;
    height: 47px;
    width: 200px;
  }

</style>

