<template>
  <div>
    <div class="tech-box">
      <div class="tech-title">
        <div class="tech-title-line" />
        <div class="tech-title-text">数据上传</div>
      </div>
    </div>

    <el-upload
      class="upload-demo"
      drag
      action="https://jsonplaceholder.typicode.com/posts/"
      :data="uploadData"
      multiple
      :on-exceed="handleExceed"
      :on-error="uploadError"
      :on-success="uploadSuccess"
      :on-remove="onRemoveTxt"
      :before-upload="onBeforeUpload"
      :file-list="files"
    >
      <i class="el-icon-upload" />
      <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
    </el-upload>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Upload',
  data() {
    return {
      uploadData: ''
    }
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}

</script>

<style lang="scss" scoped>
.upload-demo ::v-deep .el-upload-dragger{
  height:400px;
  width:800px;
  margin-left: 300px;
  position:absolute;

}

.upload-demo ::v-deep .el-icon-upload{
  margin-top: 100px;
  height:100px;
  width:100px;}

.upload-demo ::v-deep .el-upload-list{
  margin-top: 400px;
  width:800px;
  margin-left: 300px;
}
</style>
