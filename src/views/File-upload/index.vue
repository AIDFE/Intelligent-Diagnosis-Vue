<template>
  <div class="upload-container">
    <div class="upload-text">数据上传</div>
    <div class="upload-fileimg">
      <div class="upload-mask">
        <div class="upload-rectangle"></div>
      </div>
      <div class="upload-oval">
        <br/>
        <div></div>
      </div>
    </div>
    <div class="upload-chosen">
      <button class="upload-button">
        <input type="file" id="filename" name="filename" multiple class="upload-visuallyhidden" @change="updateImageDisplay"/>
        <label for="filename" class="upload-uploadbutton">上传文件</label>
      </button>
      <div class="upload-preview">
        <p>No files currently selected for upload</p>
      </div>
      <div class = "upload-confirm">
        <button class="upload-button">
          <a href="#"> 确认上传 </a>
        </button>
        <button  class="upload-button">
          <a href="#"> 取消 </a>
        </button>
      </div>

    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Upload ',
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  data() {
    return {
      fileTypes:[
        "image/apng",
        "image/bmp",
        "image/gif",
        "image/jpeg",
        "image/pjpeg",
        "image/png",
        "image/svg+xml",
        "image/tiff",
        "image/webp",
        "image/x-icon"
      ]
    }
  },
  methods: {
    updateImageDisplay() {
      console.log(5)

      const input = document.querySelector('input');
      const preview = document.querySelector('.upload-preview');
      input.style.opacity = 0;
      while(preview.firstChild) {
        preview.removeChild(preview.firstChild);
      }
      const curFiles = input.files;
      if (curFiles.length === 0) {
        const para = document.createElement('p');
        para.textContent = 'No files currently selected for upload';
        preview.appendChild(para);
      } else {
        const list = document.createElement('ol');
        preview.appendChild(list);
        for (const file of curFiles) {
          const listItem = document.createElement('li');
          const para = document.createElement('p');
          if (this.validFileType(file)) {
            para.textContent = `File name ${file.name}, file size ${this.returnFileSize(file.size)}.`;
            // const image = document.createElement('img');
            // image.src = URL.createObjectURL(file);

            // listItem.appendChild(image);
            listItem.appendChild(para);
          } else {
            para.textContent = `File name ${file.name}: Not a valid file type. Update your selection.`;
            listItem.appendChild(para);
          }

          list.appendChild(listItem);
        }
      }
    },

    validFileType(file) {
      // return this.fileTypes.includes(file.type);
      return true;
    },
    returnFileSize(number) {
      if (number < 1024) {
        return `${number} bytes`;
      } else if (number >= 1024 && number < 1048576) {
        return `${(number / 1024).toFixed(1)} KB`;
      } else if (number >= 1048576) {
        return `${(number / 1048576).toFixed(1)} MB`;
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.upload {
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
  &-fileimg {
    width: 150px;
    margin: auto;
  }
  &-chosen {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    // border: 1px solid rgba(156, 11, 246, 0.186);
  }
  &-confirm {
    margin: auto;
    width: 180px;
    display: flex;
  }
  &-button {
    margin: auto;
    width: 70px;
    height: 35px;
    font-size:10px;
    background-color: rgba(51, 109, 255, 1);
    border: 1px solid rgba(156, 11, 246, 0.186);
    border-radius: 5px;
  }
  &-button > a {
    margin-top: 25px;
    font-size: 5px;
    color: rgba(255, 255, 255, 1);
  }
  &-button > a:hover {
    color: rgba(139, 0, 46, 0.816);
  }
  // &-button:nth-of-type(1) {
  //   margin-left: 225px;
  // }
  // &-button:nth-of-type(2) {
  //   margin-left: 120px;
  // }
  // &-button:nth-of-type(3) {
  //   margin-left: 50px;
  // }

  &-mask {
    margin-top: 55.51px;
    width: 148px;
    height: 160.8px;
    opacity: 1;
    border-radius: 0px 0px, 4px, 4px;
    background: rgba(215, 219, 236, 1);
  }
  &-oval {
    margin-left: 100px;
    margin-top: -60px;
    width: 96.2px;
    height: 99.54px;
    opacity: 1;
    background: rgba(51, 109, 255, 1);
    border-radius: 50%;
  }
  &-rectangle {
    margin-left: 0px;
    margin-top: 55.51px;
    width: 148px;
    height: 38.29px;
    opacity: 1;
    background: rgba(19, 21, 35, 1);
  }
  &-oval > div {
    margin-left: 40%;
    width: 22px;
    height: 45px;
    border-right:7px solid rgba(255, 255, 255, 1);
    border-bottom:7px solid rgba(255, 255, 255, 1);
    transform: rotate(40deg);
  }
  &-visuallyhidden {
    position: absolute !important;
    height: 1px;
    width: 1px;
    overflow: hidden;
    clip: rect(1px, 1px, 1px, 1px);
  }
  &-uploadbutton {
    color:rgba(255,255,255,1);
  }
  &-uploadbutton:hover{
    color:rgba(139, 0, 46, 0.816);
  }
  &-preview {
    width: 30%;
    text-align: center;
    margin: auto;
  }
}
</style>
