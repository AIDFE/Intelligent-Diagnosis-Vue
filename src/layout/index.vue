<template>
  <div :class="classObj" class="app-wrapper">
    <div v-if="device==='mobile'&&sidebar.opened" class="drawer-bg" @click="handleClickOutside" />
    <div class="bar-head">
      <div style="display:flex">
        <img v-if="logo" :src="logo" style="width:80px;height:80px;margin-top:0px;margin-left:20px">
        <h1 style="line-height:40px">  脑膜瘤智能分级诊断系统 (IGDS-M) </h1></div>
      <div class="right-menu">
        <el-dropdown class="avatar-container" trigger="click" placement="bottom-end" :hide-on-click="true">
          <div class="avatar-wrapper">
            <el-avatar :size="40" :src="circleUrl" style="margin-top:12px" />
            <div class="user-name">{{ userName }}</div>
            <i class="el-icon-caret-bottom" />
          </div>
          <el-dropdown-menu slot="dropdown" class="user-dropdown">
            <router-link to="/">
              <el-dropdown-item>
                首页
              </el-dropdown-item>
            </router-link>
            <el-dropdown-item divided @click.native="logout">
              <span style="display: block">登出</span>
            </el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </div>
    <sidebar class="sidebar-container" style="margin-top:87px;" />
    <div class="main-container">
      <div :class="{'fixed-header':fixedHeader}">
        <navbar />
      </div>
      <app-main />
    </div>
  </div>
</template>

<script>
import Logo from '../assets/logo/logo.png'
import { Navbar, Sidebar, AppMain } from './components'
import ResizeMixin from './mixin/ResizeHandler'
import jsCookie from 'js-cookie'

export default {
  name: 'Layout',
  components: {
    Navbar,
    Sidebar,
    AppMain
  },
  mixins: [ResizeMixin],
  data() {
    return {
      logo: Logo,
      circleUrl: require('@/assets/logo/avatar.png'),
      userName: jsCookie.get('username')
    }
  },
  computed: {
    sidebar() {
      return this.$store.state.app.sidebar
    },
    device() {
      return this.$store.state.app.device
    },
    fixedHeader() {
      return this.$store.state.settings.fixedHeader
    },
    classObj() {
      return {
        hideSidebar: !this.sidebar.opened,
        openSidebar: this.sidebar.opened,
        withoutAnimation: this.sidebar.withoutAnimation,
        mobile: this.device === 'mobile'
      }
    }
  },
  methods: {
    handleClickOutside() {
      this.$store.dispatch('app/closeSideBar', { withoutAnimation: false })
    },
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    }
  }
}
</script>

<style lang="scss" scoped>
  @import "~@/styles/mixin.scss";
  @import "~@/styles/variables.scss";

  .app-wrapper {
    @include clearfix;
    position: relative;
    height: 100%;
    width: 100%;
    &.mobile.openSidebar{
      position: fixed;
      top: 0;
    }
  }

  .drawer-bg {
    background: #000;
    opacity: 0.3;
    width: 100%;
    top: 0;
    height: 100%;
    position: absolute;
    z-index: 999;
  }

  .fixed-header {
    position: fixed;
    top: 87px;
    right: 0;
    z-index: 9;
    width: calc(100% - #{$sideBarWidth});
    transition: width 0.28s;
  }

  .hideSidebar .fixed-header {
    width: calc(100% - 54px)
  }

  .mobile .fixed-header {
    width: 100%;
  }
  .bar-head{
    height: 87px;
    line-height: 87px;
    display: flex;
    justify-content: space-between;
    // background: url("~@/assets/head/head.png") no-repeat !important;
    // background-size: 100% 100% !important;
  }
  .user-name {
  float: left;
  line-height: 50px;
  height: 100%;
  text-align: center;
  vertical-align: top;
  margin: 8px 0px 10px 12px;
  color: rgba(90, 96, 127, 1);
  }
  .right-menu {
    float: right;
    height: 100%;
    line-height: 48px;

    &:focus {
      outline: none;
    }

    .right-menu-item {
      display: inline-block;
      padding: 0 8px;
      height: 100%;
      font-size: 18px;
      color: #5a5e66;
      vertical-align: text-bottom;

      &.hover-effect {
        cursor: pointer;
        transition: background 0.3s;

        &:hover {
          background: rgba(0, 0, 0, 0.025);
        }
      }
    }

    .avatar-container {
			float: left;
      margin-right: 30px;

      .avatar-wrapper {
        position: relative;
        display: flex;
        .user-avatar {
          cursor: pointer;
          width: 40px;
          height: 40px;
          border-radius: 10px;
        }

        .el-icon-caret-bottom {
          cursor: pointer;
          position: absolute;
          right: -20px;
          top: 27px;
          font-size: 12px;
        }
      }
    }
  }
</style>
