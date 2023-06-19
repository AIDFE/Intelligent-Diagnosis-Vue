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
          <el-input v-model="form.passward" show-password />
        </el-form-item>
        <el-form-item label="用户类别">
          <el-radio-group v-model="form.resource">
            <el-radio label="高级用户" />
            <el-radio label="普通用户" />
          </el-radio-group>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">添加用户</el-button>
          <el-button @click="reset">重置</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      }
    }
  },
  methods: {
    onSubmit() {
      this.$message('提交!')
    },
    reset() {
      this.$message({
        message: '重置表单',
        type: 'warning'
      })
    }
  }
}
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

