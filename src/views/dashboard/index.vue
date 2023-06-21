<template>
  <div class="dashboard-container">
    <!-- <div class="dashboard-text">在线智能诊断系统</div> -->
    <el-badge is-dot class="item"><font class="dashboard-tips">提示</font></el-badge>
    <div class="dashboard-instructions">欢迎使用脑膜瘤智能分级诊断系统！本系统基于xx算法，可以快速准确地帮助您进行脑膜瘤的分级诊断。在使用本系统前，请您先仔细查看
      <el-link :underline="false" type="primary" style="font-size: 18px;line-height: 46px;margin-top: -3px;" @click.native="visGuide()">使用指南</el-link>。</div>
    <div class="dashboard-instructions">如有任何疑问，欢迎随时联系我们的运营人员。祝您健康！</div>

    <el-dialog title="使用指南" :visible.sync="dialogTableVisible" center :append-to-body="true" :lock-scroll="false" width="30%">

      <Add />
    </el-dialog>
    <el-divider><i class="el-icon-s-opportunity" /></el-divider>

    <el-row :gutter="100" style="margin-top:48px;">
      <el-col :span="12">
        <el-card shadow="hover" style="width: 100%;">
          <div slot="header">
            <span>快捷查看病例列表入口</span>
          </div>
          <div class="dashboard-chosen">
            <button class="dashboard-button">
              <router-link to="/example/table" style="color:rgba(255,255,255,1)">查看病例<br></router-link>
            </button>
          </div>
        </el-card>
      </el-col>
      <el-col :span="12">
        <el-card shadow="hover" style="width: 100%;">
          <div slot="header">
            <span>快捷上传数据入口</span>
          </div>
          <div class="dashboard-chosen">
            <button class="dashboard-button" style="background-color:#67C23A">
              <router-link to="/File-upload" style="color:rgba(255,255,255,1)">上传数据<br></router-link>
            </button>
          </div>
        </el-card>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  data() {
    return {
      dialogTableVisible: false
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  methods: {
    visGuide() {
      this.dialogTableVisible = true// 默认页面不显示为false,点击按钮将这个属性变成true
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-tips {
    margin-top: 50px;
    margin-bottom: 5px;
    font-size:25px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
    font-weight:700;
    margin-bottom: 48px;
  }
  &-instructions {
    font-size: 18px;
    line-height: 46px;
  }
  &-chosen {
    display: flex;
    justify-content: center;
  }
  &-button {
    width: 300px;
    height: 100px;
    color: rgba(255, 255, 255, 1);
    background-color: rgba(15, 95, 237);
    border: 1px solid rgba(156, 11, 246, 0.186);
    border-radius: 2px;
  }
  &-button > a{
    margin-top: 25px;
    font-size: 20px;
    color: rgba(139, 0, 46, 0.816);
  }
  &-button:nth-of-type(2) {
    margin-left: 50px;
  }
}
</style>
