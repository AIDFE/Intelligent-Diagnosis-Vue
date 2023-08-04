<template>

  <div>

    <div class="tech-box">
      <div class="tech-title">
        <div class="tech-title-line" />
        <div class="tech-title-text">病例查询</div>
      </div>
      <div class="tech-search">
        <div class="tech-search-item">
          <div class="tech-search-item-text">姓名</div>
          <el-input
            v-model="name"
            style="width:100%;"
            size="small"
            class="tech-search-item-input"
            placeholder="请输入姓名"
            clearable
          />
        </div>
        <div class="tech-search-item">
          <div class="tech-search-item-text">日期</div>
          <el-date-picker
            v-model="datesel"
            value-format="yyyy-MM-dd"
            type="daterange"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            size="small"
            style="width:100%;"
          />
        </div>

        <!-- <div class="tech-search-item">
          <div class="tech-search-item-text">病理亚型</div>
          <el-select
            v-model="sel_bingli"
            size="small"
            style="width:100%;"
            class="tech-search-item-input"
            placeholder="请选择"
          >
            <el-option
              v-for="item in p_sub_op"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </div> -->
        <!-- <div class="tech-search-item">
          <div class="tech-search-item-text">脑侵袭</div>
          <el-select
            v-model="sel_inverse"
            size="small"
            style="width:100%;"
            class="tech-search-item-input"
            placeholder="请选择"
          >
            <el-option
              v-for="item in p_inv_op"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </div> -->
        <!-- <div class="tech-search-item">
          <div class="tech-search-item-text">分级</div>
          <el-select
            v-model="sel_level"
            size="small"
            style="width:100%;"
            class="tech-search-item-input"
            placeholder="请选择"
          >
            <el-option
              v-for="item in p_lev_op"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select>
        </div> -->
        <div class="tech-search-control">
          <el-button class="tech-search-btn" type="primary" @click="search"> 查询 </el-button>
          <el-button class="tech-search-btn" @click="reset"> 重置 </el-button>
          <!-- <el-button class="tech-search-btn" type="danger" @click="deleteBatch"> 批量删除 </el-button> -->
        </div>
      </div>
    </div>

    <div class="tech-box">
      <div class="tech-title">
        <div class="tech-title-line" />
        <div class="tech-title-text">病例列表</div>
      </div>

      <div class="tech-table">
        <el-table
          ref="multipleTable"
          v-loading="listLoading"
          :data="filteredData.slice((currentPage-1)*pagesize,currentPage*pagesize)"
          element-loading-text="加载中"
          header-cell-class-name="tech-table-header"
          border="true"
          highlight-current-row
          :row-class-name="tableRowClassName"
          :header-cell-style="{background:'#f0f8ff',color:'#606266'}"
          @selection-change="handleSelectionChange"
        >

         <el-table-column label="患者临床信息" min-width="4" align="center">
          <el-table-column align="center" label="ID" min-width="1">
            <template slot-scope="scope">
                  {{ scope.row.study_info.id }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="患者姓名" min-width="1">
            <template slot-scope="scope">
                  {{ scope.row.study_info.name }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="F号" min-width="1">
            <template slot-scope="scope">
                  {{ scope.row.study_info.f_num }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="年龄" min-width="1">
            <template slot-scope="scope">
                  {{ scope.row.study_info.age }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="性别" min-width="1">
            <template slot-scope="scope">
                  {{ scope.row.study_info.sex }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="出生年月" min-width="1">
            <template slot-scope="scope">
                  {{scope.row.study_info.bdate|formatDate('yyyy-MM-dd')}}
            </template>
          </el-table-column>

          <el-table-column align="center" label="检查日期" min-width="1">
            <template slot-scope="scope">
                 {{scope.row.study_info.cdate|formatDate('yyyy-MM-dd')}}
            </template>
          </el-table-column>

        </el-table-column>


        <el-table-column label="成像信息" min-width="3" align="center">
          <el-table-column align="center" label="成像设备" min-width="1">
            <template slot-scope="scope">
                  {{ scope.row.image_info.device }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="模态个数" min-width="1">
            <template slot-scope="scope">
                  {{ scope.row.image_info.modality }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="切片个数" min-width="1">
            <template slot-scope="scope">
                  {{ scope.row.image_info.slice }}
            </template>
          </el-table-column>

          <el-table-column align="center" label="图像查看" min-width="1">
            <template slot-scope="scope">
                <div><el-button type="text" size="medium" @click="handle(scope.row.study_info.StudyInstanceUIDs)">查看图片</el-button></div>
            </template>
          </el-table-column>
          
        </el-table-column>

        
        <el-table-column label="AI诊断结果" min-width="1" align="center">
          <el-table-column align="center" label="脑侵袭" min-width="1">
            <template slot-scope="scope">
              <el-tag :type="[scope.row.AI_info.invasive==='否' ? 'success': 'danger']">{{ scope.row.AI_info.invasive }}</el-tag>
            </template>
          </el-table-column>

          <el-table-column align="center" label="分级" min-width="1">
            <template slot-scope="scope">
              <el-tag :type="[scope.row.AI_info.level==='非一级' ? 'success': 'danger']">{{ scope.row.AI_info.level }}</el-tag>
            </template>
          </el-table-column>

          <el-table-column align="center" label="图像分析" min-width="1">
            <template slot-scope="scope">
              <el-button type="success" :loading=scope.row.img_load round size="mini" @click="handle_image(scope.row.study_info.StudyInstanceUIDs, scope.row)"> 图像分析 </el-button>
            </template>
          </el-table-column>
          
        </el-table-column>

        </el-table> 
        <!-- 列表分页 -->
        <el-pagination
          background
          class="tech-table-pagination"
          :current-page.sync="currentPage"
          :page-size="pagesize"
          layout="total, sizes, prev, pager, next, jumper"
          :total="30"
          style="margin-top: 20px;"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
        />

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import {getSeg} from '@/api/seg'

export default {
  name: '',
  data() {
    return {
      list: null,
      name: '',
      listLoading: true,
      datesel: '',
      sel_bingli: '',
      sel_inverse: '',
      sel_level: '',
      cheif: '',
      remark: '',
      img_load:'false',
      save_disable:false,
      pagesize: 10, // 指定展示多少条
      currentPage: 1, // 当前页码
      p_inv_op: [
        { label: '是', value: '是' },
        { label: '否', value: '否' }],
      p_lev_op: [
        { label: '一级', value: '一级' },
        { label: '非一级', value: '非一级' }],
      p_sub_op: [
        { label: '脑膜皮型' , value: '脑膜皮型' },
        { label: '纤维型 (成纤维型)', value: '纤维型 (成纤维型)' },
        { label: '过渡型 (混合型)', value: '过渡型 (混合型)' },
        { label: '沙粒体型', value: '沙粒体型' },
        { label: '血管瘤型', value: '血管瘤型' },
        { label: '微囊型', value: '微囊型' },
        { label: '分泌型', value: '分泌型' },
        { label: '富淋巴-浆细胞型', value: '富淋巴-浆细胞型' },
        { label: '移行型', value: '移行型' },
        { label: '透明细胞型', value: '透明细胞型' },
        { label: '脊索瘤样型', value: '脊索瘤样型' },
        { label: '非典型', value: '非典型' },
        { label: '乳头状瘤型', value: '乳头状瘤型' },
        { label: '横纹肌样型', value: '横纹肌样型' },
        { label: '间变性 (恶性)', value: '间变性 (恶性)' }],
      p_zhuw: [
        { label: '是', value: '是' },
        { label: '否', value: '否' }],
      p_xinp: [
        { label: '一级', value: '一级' },
        { label: '二级' , value: '二级' },
        { label: '三级', value: '三级' },
        { label: '四级', value: '四级' }],
      p_region: [
        { label: '凸面', value: '凸面' },
        { label: '窦旁', value: '窦旁' },
        { label: '镰旁', value: '镰旁' },
        { label: '前颅底', value: '前颅底' },
        { label: '中颅底', value: '中颅底' },
        { label: '后颅窝', value: '后颅窝' },
        { label: '侧脑室', value: '侧脑室' },
        { label: '其他', value: '其他' }],
      searchText: '',
      multipleSelection: [] }
  },
  filters:{
        formatDate: function(value,args) {
            var dt = new Date(value);
            if(args == 'yyyy-M-d') {// yyyy-M-d
            let year = dt.getFullYear();
            let month = dt.getMonth() + 1;
            let date = dt.getDate();
            return `${year}-${month}-${date}`;
        } else if(args == 'yyyy-M-d H:m:s'){// yyyy-M-d H:m:s
            let year = dt.getFullYear();
            let month = dt.getMonth() + 1;
            let date = dt.getDate();
            let hour = dt.getHours();
            let minute = dt.getMinutes();
            let second = dt.getSeconds();
            return `${year}-${month}-${date} ${hour}:${minute}:${second}`;
        } else if(args == 'yyyy-MM-dd') {// yyyy-MM-dd
            let year = dt.getFullYear();
            let month = (dt.getMonth() + 1).toString().padStart(2,'0');
            let date = dt.getDate().toString().padStart(2,'0');
            return `${year}-${month}-${date}`;
        } else {// yyyy-MM-dd HH:mm:ss
            let year = dt.getFullYear();
            let month = (dt.getMonth() + 1).toString().padStart(2,'0');
            let date = dt.getDate().toString().padStart(2,'0');
            let hour = dt.getHours().toString().padStart(2,'0');
            let minute = dt.getMinutes().toString().padStart(2,'0');
            let second = dt.getSeconds().toString().padStart(2,'0');
            return `${year}-${month}-${date} ${hour}:${minute}:${second}`;
        }}},
  mounted: function () {
    axios.get('/api/Query', {
        params: {
          "find_state": 0,
          "name": this.name,
          "check_date1": this.datesel[0],
          "check_date2": this.datesel[1],
          "p_sub": this.sel_bingli,
          "p_invasive": this.sel_inverse,    
          "p_level": this.sel_level 
        }
      }).then(res => {
        this.listLoading = true
        this.list = res.data.result
        this.listLoading = false
      })
  },

  computed: {
    filteredData() {
      return this.list
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    // 改变斑马线的颜色
    tableRowClassName({ row, rowIndex }) {
      if (rowIndex % 2 === 1) {
        return 'row-style'
      }
      return ''
    },
    search() {
      axios.get('/api/Query', {
        params: {
          "find_state": 1,
          "name": this.name,
          "check_date1": this.datesel[0],
          "check_date2": this.datesel[1],
          "p_sub": this.sel_bingli,
          "p_invasive": this.sel_inverse,    
          "p_level": this.sel_level 
        }
      }).then(res => {
        this.listLoading = true
        this.list = res.data.result
        this.listLoading = false
      })
    },
    reset() {
      axios.get('/api/Query', {
        params: {
          "find_state": 0,
          "name": this.name,
          "check_date1": this.datesel[0],
          "check_date2": this.datesel[1],
          "p_sub": this.sel_bingli,
          "p_invasive": this.sel_inverse,    
          "p_level": this.sel_level 
        }
      }).then(res => {
        this.listLoading = true
        this.list = res.data.result
        this.listLoading = false
      })
      // 清空搜索项，重新调用查询接口
      this.name = ''
      this.datesel = ''
      this.sel_bingli = ''
      this.sel_inverse = ''
      this.sel_level = ''
    },
    info_reset(row) {
      row.cheif = ''
      row.remark = ''
      row.region = ''
      row.date = ''
      row.zhuw = ''
      row.xinp = ''
      row.p_invasive = ''
      row.p_level = ''
      row.p_vig = ''
      row.p_sub = ''
    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage
    },
    handleSizeChange: function(pagesize) { // 每页条数切换
      this.pagesize = pagesize
      this.handleCurrentChange(this.currentPage)
    },
    handle(url) {
      window.open("http://localhost:3000/viewer?StudyInstanceUIDs="+url, "_blank")
    },
    handle_image(study_id, row) {
      row.img_load = 'true'
      getSeg(study_id).then(res => {
        if (res.code === 20000){
        this.$message({
            message: '分析成功',
            type: 'success'
        })
          axios.get('/api/Query', {
          params: {
            "find_state": 0,
            "name": this.name,
            "check_date": this.datesel,
            "p_sub": this.sel_bingli,
            "p_invasive": this.sel_inverse,    
            "p_level": this.sel_level 
          }
        }).then(res => {
          this.listLoading = true
          this.list = res.data.result
          this.listLoading = false
          row.img_load = 'false'
        })
    }
        else{
          this.$message({
            message: '分析失败，请重新分析',
            type: 'error'
        })
        }
  })}

  }

}
</script>

<style scoped>
.el-divider--horizontal {
    display: block;
    height: 1px;
    width: 100%;
    margin: 8px 0px;
}

::v-deep .el-table .row-style {
   background: #f6fefd;
 }

 .wrap {
  height: 100%;
  overflow-x: hidden;
}

</style>
