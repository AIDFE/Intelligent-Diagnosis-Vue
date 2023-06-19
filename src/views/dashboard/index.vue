<template>
  <div class="dashboard-container">
    <div class="dashboard-text">在线智能诊断系统</div>
    <div class="dashboard-tips">提示</div>
    <div class="dashboard-instructions">用户使用说明</div>
    <hr color="gray" size="5">
    <div class="dashboard-chosen">
      <button class="dashboard-button">
        <router-link to="/example/table" style="color:rgba(255,255,255,1)">查看病例<br></router-link>
        <a href="#"> 提示:xxx </a>
      </button>
      <button class="dashboard-button">
        <router-link to="/File-upload" style="color:rgba(255,255,255,1)">上传数据<br></router-link>
        <a href="#"> 提示:xxx </a>
      </button>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name'
    ])
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
    font-weight:700
  }
  &-instructions {
    margin-bottom: 100px;
    font-size: 15px;
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
    background-color: rgba(51, 109, 255, 1);
    border: 1px solid rgba(156, 11, 246, 0.186);
    border-radius: 5px;
  }
  &-button > a{
    margin-top: 25px;
    font-size: 5px;
    color: rgba(139, 0, 46, 0.816);
  }
  &-button:nth-of-type(2) {
    margin-left: 50px;
  }
}
</style>
