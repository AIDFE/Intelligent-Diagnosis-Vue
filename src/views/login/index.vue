<template>
  <div class="login-container">
    <div class="login-info">
      <img width="150" height="150" src="https://img.js.design/assets/img/647ed75af6ff16e94b822d47.jpg">

      <div class="title">脑膜瘤智能诊断系统</div>
      <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" auto-complete="on" label-position="left">
        <el-form-item prop="username">
          <span class="svg-container">
            <svg-icon icon-class="user" />
          </span>
          <el-input
            ref="username"
            v-model="loginForm.username"
            placeholder="用户名"
            name="username"
            type="text"
            tabindex="1"
            auto-complete="on"
          />
        </el-form-item>

        <el-form-item prop="password">
          <span class="svg-container">
            <svg-icon icon-class="password" />
          </span>
          <el-input
            :key="passwordType"
            ref="password"
            v-model="loginForm.password"
            :type="passwordType"
            placeholder="密码"
            name="password"
            tabindex="2"
            auto-complete="on"
            @keyup.enter.native="handleLogin"
          />
          <span class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
          </span>
        </el-form-item>

        <el-button :loading="loading" type="primary" class="button" style="width:100%;margin-bottom:30px;" @click.native.prevent="handleLogin">登录</el-button>

      <!-- <div class="tips">
        <span style="margin-right:20px;">username: admin</span>
        <span> password: any</span>
      </div> -->

      </el-form>
    </div>
  </div>
</template>

<script>
import { validUsername } from '@/utils/validate'

export default {
  name: 'Login',
  data() {
    const validateUsername = (rule, value, callback) => {
      if (!validUsername(value)) {
        callback(new Error('请输入正确的用户名'))
      } else {
        callback()
      }
    }
    const validatePassword = (rule, value, callback) => {
      if (value.length < 6) {
        callback(new Error('密码长度不小于6位'))
      } else {
        callback()
      }
    }
    return {
      loginForm: {
        username: 'admin',
        password: '111111'
      },
      loginRules: {
        username: [{ required: true, trigger: 'blur', validator: validateUsername }],
        password: [{ required: true, trigger: 'blur', validator: validatePassword }]
      },
      loading: false,
      passwordType: 'password',
      redirect: undefined
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  methods: {
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          this.loading = true
          this.$store.dispatch('user/login', this.loginForm).then(() => {
            this.$router.push({ path: this.redirect || '/' })
            this.loading = false
          }).catch(() => {
            this.loading = false
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
      // this.$axios({
      //   method: 'post',
      //   url: 'http://120.92.108.238:5051/login', // 接口地址
      //   data: {
      //     keyword: '1' // 传接口参数
      //   }
      // })
      //   .then(response => {
      //     console.log(response, 'success') // 成功的返回
      //   })
      //   .catch(error => console.log(error, 'error')) // 失败的返回

      // this.$axios.post('http://120.92.108.238:5051/login', {
      //   params: {
      //     number: this.loginForm.username,
      //     password: this.loginForm.password
      // }
      // }).then((res) => {
      //   console.log(res)
      // })
    }
  }
}
</script>

<style lang="scss">
/* 修复input 背景不协调 和光标变色 */
/* Detail see https://github.com/PanJiaChen/vue-element-admin/pull/927 */

$bg:#283443;
$light_gray:#000;
$cursor: #000;

@supports (-webkit-mask: none) and (not (cater-color: $cursor)) {
  .login-container .el-input input {
    color: $cursor;
  }
}

/* reset element-ui css */
.login-container {
  .el-input {
    display: inline-block;
    height: 47px;
    width: 85%;

    input {
      background: transparent;
      border: 0px;
      -webkit-appearance: none;
      border-radius: 0px;
      padding: 12px 5px 12px 15px;
      color: $cursor;
      height: 47px;
      caret-color: $cursor;

      &:-webkit-autofill {
        box-shadow: 0 0 0px 1000px #fff inset !important;
        -webkit-text-fill-color: $cursor !important;
      }
    }
  }

  .el-form-item {
    border: 1px solid #2d51ad;
    background: #fff;
    border-radius: 5px;
    color: #fff;
  }
}
</style>

<style lang="scss" scoped>
$bg:url(/bg.png);
$dark_gray:#889aa4;
$light_gray:#eee;

.login-container {
  background-image: $bg;
  // overflow: hidden;
  height: 100vh;
  background-size: 100% 100%;
  display: flex;
  justify-content: center;
  align-items: center;

  .login-info {
  width: 500px;
  /* height: 460px; */
  background: #fff;
  border-radius: 30px;
  padding: 20px 70px;
}

img {
    margin: 0 auto;
    text-align: center;
    display: flex;
  }

  .title {
    font-size: 40px;
    text-align: center;
    margin-top: 10px;
    font-weight: 700;
    color: rgba(12, 79, 145, 1);
    margin-bottom: 50px;
  }

  .login-form {
    position: relative;
    width: 520px;
    max-width: 100%;
    padding: 0 15px;
    margin: 0 auto;
    overflow: hidden;
  }

  .tips {
    font-size: 14px;
    color: #fff;
    margin-bottom: 10px;

    span {
      &:first-of-type {
        margin-right: 16px;
      }
    }
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: #2d51ad;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  // .title-container {
  //   position: relative;

  //   .title {
  //     font-size: 26px;
  //     color: $light_gray;
  //     margin: 0px auto 40px auto;
  //     text-align: center;
  //     font-weight: bold;
  //   }
  // }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: #000;
    cursor: pointer;
    user-select: none;
  }
}

.button {
    background: #2d51ad;
    border: none;
    color: #fff;
    display: flex;
    width: 100%;
    height: 48px;
    border-radius: 4px;
    justify-content: center;
    align-items: center;
    margin-top: 20px;
    cursor: pointer;
  }
</style>
