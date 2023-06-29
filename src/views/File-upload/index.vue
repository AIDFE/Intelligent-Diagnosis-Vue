<template>
  <uploader :options="options" class="uploader-example" :file-status-text="statusText">
    <uploader-unsupport />
    <uploader-drop>
      <i class="el-icon-upload" />
      <p style="margin-left: 150px; font-size: 15px; color: gray;">温馨提示：可拖拽文件上传或点击下方按钮上传</p>
      <p style="margin-left: 150px; font-size: 15px; color: gray;">请上传患者的dicom文件或文件夹</p>

    </uploader-drop>
    <uploader-btn>选择文件</uploader-btn>
    <uploader-btn :directory="true">选择文件夹</uploader-btn>
    <uploader-list />
    <el-alert
      title="文件上传成功"
      type="success"
      description="正在进行图像分析，请前往病例列表查看患者信息及分析结果"
      show-icon
    />
  </uploader>
</template>

<script>
export default {
  data() {
    return {
      options: {
        target: '/api/uploadfile',
        testChunks: false
      },
      // 上传状态
      statusText: {
        success: '上传成功',
        error: '上传失败',
        uploading: '上传中...',
        paused: '等待中...',
        waiting: '等待中...'
      }
    }
  }
}
</script>

<style >
  .uploader-example {
    width: 660px;
    height: 480px;
    padding: 15px;
    margin: 40px auto 0;
    font-size: 12px;
    box-shadow: 0 0 10px rgba(0, 0, 0, .4);
  }
  .uploader-example .uploader-btn {
    margin-top: 15px;
    font-weight: bold;
    border: none;
    color: white;
    padding: 0.5em;
    border-radius: 3px;
    background-color: #409EFF;
    margin-right: 15px;
    width: 100px;
    height: 40px;
    font-size: 15px;
    line-height: 23px;
    text-align: center;

  }
  .uploader-example .uploader-list {
    margin-top: 25px;
    max-height: 440px;
    overflow: auto;
    overflow-x: hidden;
    overflow-y: auto;
  }
  .uploader-drop{
    height: 400px;
  }
  .el-icon-upload{
    font-size: 200px;
    color: #C5C2C2;
    margin-top: 50px;
    margin-left: 200px;

  }
  .info{
    margin-top:50px
  }
  ::v-deep.el-alert{
    font-size: 100px;
  }
</style>
