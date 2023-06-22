<template>
  <div class="black-container">
    <div class="imagelist-bar">
      <!-- TODO:患者信息显示 -->

      <div class="study-item">
        <div class="flex-row">
          <div class="text-white">{{ date }}</div>
          <div class="text-blue">
            <svg-icon icon-class="group-layers" style="width: 1rem;height: 25px;margin-right: 0.5rem" />
            {{ numInstances }}
          </div>
        </div>
        <div class="flex-row">
          <div class="moda">{{ modalities }}</div>
          <div class="desc">
            {{ description }}
          </div>
        </div>
      </div>

      <div class="Thumbnail-list">
        <div class="flex-row">
          <div class="thumbnail flex-col">
            <div :class="activeIndex===1?'img-active':'img-nonactive'">
              <img
                :src="imageSrc"
                alt="Thumbnail Image"
                style="object-fit: none;max-width: 100%;height: auto;"
              >
            </div>
            <div class="flex-row">
              <div class="s-number">
                <span style="color: rgb(9 68 179);font-weight: 700;">S: </span>
                {{ seriesNumber }}
              </div>
              <div class="s-number">
                <svg-icon icon-class="countIcon" style="width: 0.75rem;height: 19;margin-right: 0.5rem" />
                {{ numInstances }}
              </div>
            </div>
            <div style="word-break: break-all;">{{ description }}</div>
          </div>
        </div>

        <div class="flex-row">
          <div class="thumbnail flex-col">
            <div :class="activeIndex===2?'img-active':'img-nonactive'">
              <img
                :src="imageSrc"
                alt="Thumbnail Image"
                style="object-fit: none;max-width: 100%;height: auto;"
              >
            </div>
            <div class="flex-row">
              <div class="s-number">
                <span style="color: rgb(9 68 179);font-weight: 700;">S: </span>
                {{ seriesNumber }}
              </div>
              <div class="s-number">
                <svg-icon icon-class="countIcon" style="width: 0.75rem;height: 19;margin-right: 0.5rem" />
                {{ numInstances }}
              </div>
            </div>
            <div style="word-break: break-all;">{{ description }}</div>
          </div>
        </div>

        <div class="flex-row">
          <div class="thumbnail flex-col">
            <div :class="activeIndex===2?'img-active':'img-nonactive'">
              <img
                :src="imageSrc"
                alt="Thumbnail Image"
                style="object-fit: none;max-width: 100%;height: auto;"
              >
            </div>
            <div class="flex-row">
              <div class="s-number">
                <span style="color: rgb(9 68 179);font-weight: 700;">S: </span>
                {{ seriesNumber }}
              </div>
              <div class="s-number">
                <svg-icon icon-class="countIcon" style="width: 0.75rem;height: 19;margin-right: 0.5rem" />
                {{ numInstances }}
              </div>
            </div>
            <div style="word-break: break-all;">{{ description }}</div>
          </div>
        </div>

        <div class="flex-row">
          <div class="segmentation flex-col">
            <!-- TODO:无缩略图的图像分割 -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import thumbnailImg from '@/assets/logo/thumbnailImg.png'
export default {
  data() {
    return {
      date: '11-Apr-2017',
      numInstances: 263,
      modalities: 'CT',
      description: 'CT NECK SOFT TISSUE  W/ CONTR',
      activeIndex: 1,
      imageSrc: thumbnailImg,
      seriesNumber: 2

    }
  },
  methods: {
    onSubmit() {
      this.$message('submit!')
    }

  }
}
</script>

<style scoped>
.imagelist-bar{
  margin-left: 0px;
  max-width: 248px;
  width: 248px;
  display: flex;
  box-sizing: content-box;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
}
.study-item{
  border-width: 0px;
  outline: 2px solid transparent;
  outline-offset: 2px;
  border-color: rgb(58 63 153);
  background-color: rgb(4 28 74);
  cursor: pointer;
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
  padding: 0 0.5rem 1rem 1rem;

  .text-white{
    color: rgb(255 255 255);
    font-size: 0.8125rem;
    height: 25px;
    line-height: 25px;
  }
  .text-blue{
    margin-left: auto;
    margin-right: 12px;
    color: rgb(144 205 244);
    font-size: 0.8125rem;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -ms-flex-direction: row;
    flex-direction: row;
    -webkit-box-align: center;
    -ms-flex-align: center;
    align-items: center;
  }
  .moda{
    color: rgb(144 205 244);
    font-size: 1.25rem;
    padding-right: 1.25rem;
  }
  .desc{
    overflow: hidden;
    overflow-wrap: break-word;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    line-height: 1.3;
    height: 2.1rem;
    color: rgb(144 205 244);
    font-size: 0.8125rem;
  }
}
.flex-row {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    display: flex;
    -webkit-box-orient: horizontal;
    -webkit-box-direction: normal;
    -ms-flex-direction: row;
    flex-direction: row;
}
.flex-col {
  display: flex;
  -webkit-box-orient: vertical;
  -webkit-box-direction: normal;
  -ms-flex-direction: column;
  flex-direction: column;
}
.Thumbnail-list{
  min-height: 450px;
  overflow-y: auto;
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  padding-left: 0.75rem;
  padding-right: 0.75rem;

  /* 定义滚动条样式 */
  &::-webkit-scrollbar {
      width: 7px;
      height: 6px;
      background-color: rgb(0 0 0);
  }
  /*定义滚动条轨道 内阴影+圆角*/
  /* &::-webkit-scrollbar-track {
      box-shadow: inset 0 0 0px rgba(240, 240, 240, .5);
      border-radius: 10px;
      background-color: rgba(240, 240, 240, .5);
  } */
  /*定义滑块 内阴影+圆角*/
  &::-webkit-scrollbar-thumb {
      border-radius: 10px;
      /* box-shadow: inset 0 0 0px rgba(237, 44, 37, .5); */
      background-color: rgb(23,50,57);
  }

  .thumbnail{
    margin-left: 1.75rem;
    margin-right: 1.75rem;
    font-size: 0.8125rem;
    color: rgb(255 255 255);
    cursor: pointer;
    .img-active{
      display: flex;
      border: 2px solid rgb(90 204 230);
      border-radius: 0.375rem;
      margin: 0;
      min-height: 8rem;
    }
    .img-nonactive{
      display: flex;
      border: 2px solid rgb(58 63 153);
      border-radius: 0.375rem;
      margin: 0;
      min-height: 8rem;
    }
    .s-number{
      display: flex;
      -webkit-box-align: center;
      -ms-flex-align: center;
      align-items: center;
      color: rgb(144 205 244);
      font-size: 0.8125rem;
      padding-top: 0.5rem;
      margin-right: 1rem;
      height: 25px;
      line-height: 25px;
    }
  }
  .segmentation{
    cursor: pointer;
  }
}
</style>

