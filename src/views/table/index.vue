
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
          <div class="tech-search-item-text">检查日期</div>
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

        <div class="tech-search-item">
          <div class="tech-search-item-text">手术日期</div>
          <el-date-picker
            v-model="opdatesel"
            value-format="yyyy-MM-dd"
            type="daterange"
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            size="small"
            style="width:100%;"
          />
        </div>
        
        <div class="tech-search-item">
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
        </div>
        <div class="tech-search-item">
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
        </div>
        <div class="tech-search-item">
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
        </div>
        <div class="tech-search-control">
          <el-button class="tech-search-btn" type="primary" @click="search"> 查询 </el-button>
          <el-button class="tech-search-btn" @click="reset"> 重置 </el-button>
          <el-button class="tech-search-btn" type="danger" @click="deleteBatch"> 批量删除 </el-button>
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

          <el-table-column
            type="selection"
            align="center"
            min-width="1"
          />

          <el-table-column
            align="center"
            label="ID"
            min-width="2"
          >
            <el-table-column align="center" label="患者姓名" min-width="2">
              <el-table-column label="F号" min-width="2" align="center">
                <template slot-scope="scope">
                  {{ scope.row.study_info.id }} <el-divider /> {{ scope.row.study_info.name }} <el-divider /> {{ scope.row.study_info.f_num }}
                </template>
              </el-table-column>
            </el-table-column>
          </el-table-column>

         <el-table-column label="患者临床信息" min-width="4" align="center">
            <template slot-scope="scope">
              <div>年龄：{{ scope.row.study_info.age }} 性别：{{ scope.row.study_info.sex }}</div>
              <div>出生年月：{{scope.row.study_info.bdate|formatDate('yyyy-MM-dd')}}<br>
                检查日期：{{scope.row.study_info.cdate|formatDate('yyyy-MM-dd')}}</div>
              <div>主诉：<el-input v-model="scope.row.clinic_info.cheif" 
                                  :disabled="scope.row.save_disable" 
                                  type="textarea" :rows="1" size="mini" 
                                  placeholder="请输入" style="width: 60%;" /></div>
              <div>备注：<el-input v-model="scope.row.clinic_info.remark" 
                                  :disabled="scope.row.save_disable" type="textarea" :rows="1" size="mini" 
                                  placeholder="请输入" style="width: 60%;" /></div>
            </template>
          </el-table-column>

          <el-table-column label="成像设备" min-width="2" align="center">
            <el-table-column align="center" label="模态个数" min-width="2">
              <el-table-column align="center" label="切片个数" min-width="2">
                <template slot-scope="scope">
                  {{ scope.row.image_info.device }} <el-divider /> {{ scope.row.image_info.modality }} <el-divider /> {{ scope.row.image_info.slice }} <el-divider />

                  <div><el-button type="text" size="medium" @click="handle(scope.row.study_info.StudyInstanceUIDs)">查看图片</el-button></div>

                </template>
              </el-table-column>
            </el-table-column>
          </el-table-column>

          <el-table-column class-name="status-col" label="AI诊断结果" min-width="2" align="center">
            <template slot-scope="scope">
              <div>脑侵袭：<el-tag :type="[scope.row.AI_info.invasive==='否' ? 'success': 'danger']">{{ scope.row.AI_info.invasive }}</el-tag></div> <br>
              <div>分级：<el-tag :type="[scope.row.AI_info.level==='非一级' ? 'success': 'danger']">{{ scope.row.AI_info.level }}</el-tag></div>
               <el-button style="margin-top: 28px;" type="success" :disabled=scope.row.image_info.available :loading=scope.row.img_load round size="mini" @click="handle_image(scope.row.study_info.StudyInstanceUIDs, scope.row)"> 图像分析 </el-button> <br>
            </template>
          </el-table-column>

          <el-table-column label="手术信息" min-width="4" align="center">
            <template slot-scope="scope">
              <div style="display: flex;width:100%;">
                <div style="width:40%">手术日期：</div>
                <el-date-picker
                  v-model="scope.row.surgery_info.date"
                  :disabled="scope.row.save_disable"
                  type="date"
                  placeholder="选择日期"
                  :picker-options="pickerOptionsStart(scope.row)"
                  size="mini"
                  style="width:60%"
                />
              </div>
              <div style="display: flex;width:100%;">
                <div style="width:40%">病变部位：</div>
                <el-select
                  v-model="scope.row.surgery_info.region"
                  :disabled="scope.row.save_disable"
                  size="mini"
                  placeholder="请选择"
                  style="width:60%"
                >
                  <el-option
                    v-for="item in p_region"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select></div>
              <div style="display: flex;width:100%;">
                <div style="width:40%">蛛网膜界面破坏：</div>
                <el-select
                  v-model="scope.row.surgery_info.zhuw"
                  :disabled="scope.row.save_disable"
                  size="mini"
                  placeholder="请选择"
                  style="width:60%"
                >
                  <el-option
                    v-for="item in p_zhuw"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select></div>

              <div style="display: flex;width:100%;">
                <div style="width:40%">辛普森分级：</div>
                <el-select
                  v-model="scope.row.surgery_info.xinp"
                  :disabled="scope.row.save_disable"
                  size="mini"
                  placeholder="请选择"
                  style="width:60%"
                >
                  <el-option
                    v-for="item in p_xinp"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select>
              </div>
              <div>
              </div>
            </template>
          </el-table-column>

          <el-table-column label="术后病理结果" min-width="4" align="center">
            <template slot-scope="scope">
              <div style="display: flex;width:100%;">
                <div style="width:40%">脑侵袭：</div>
                <el-select
                  v-model="scope.row.pathology_info.p_invasive"
                  :disabled="scope.row.save_disable"
                  size="mini"
                  placeholder="请选择"
                  style="width:60%"
                >
                  <el-option
                    v-for="item in p_inv_op"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select>
              </div>

              <div style="display: flex;width:100%;">
                <div style="width:40%">分级：</div>
                <el-select
                  v-model="scope.row.pathology_info.p_level"
                  :disabled="scope.row.save_disable"
                  size="mini"
                  placeholder="请选择"
                  style="width:60%"
                >
                  <el-option
                    v-for="item in p_lev_op"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select></div>

              <div style="display: flex;width:100%;">
                <div style="width:40%">增值指数：</div>
                <el-input v-model="scope.row.pathology_info.vig"
                          :disabled="scope.row.save_disable" size="mini" 
                          placeholder="请输入" style="width:60%"
                          oninput="value=value.replace(/[^\d.]/g,'').replace(/^0+(\d)/, '$1').replace(/^\./, '0.').replace(/^(\-)*(\d+)\.(\d\d\d\d).*$/,'$1$2.$3')" />
              </div>

              <div style="display: flex;width:100%;">
                <div style="width:40%">病理亚型：</div>
                <el-select
                  v-model="scope.row.pathology_info.p_sub"
                  :disabled="scope.row.save_disable"
                  size="mini"
                  placeholder="请选择"
                  style="width:60%"
                >
                  <el-option
                    v-for="item in p_sub_op"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value"
                  />
                </el-select></div> 

            </template>
          </el-table-column>

          <el-table-column class-name="status-col" label="是否一致" min-width="2" align="center">
            <template slot-scope="scope">
              <div>脑侵袭：<el-tag :type="[scope.row.result_info.consist_inv==='否' ? 'danger': 'success']">{{ scope.row.result_info.consist_inv }}</el-tag></div> <br>
              <div>分级：<el-tag :type="[scope.row.result_info.consist_lev==='否' ? 'danger': 'success']">{{ scope.row.result_info.consist_lev }}</el-tag></div>
            </template>
          </el-table-column>

          <el-table-column class-name="status-col" label="保存信息" min-width="2" align="center">
            <template slot-scope="scope">
              <el-button class="tech-search-btn" type="primary" size="small" @click="info_save(scope.row)"> 保存 </el-button> <br>
            </template>
          </el-table-column>

        </el-table> 
        <!-- 列表分页 -->
        <el-pagination
          background
          class="tech-table-pagination"
          :current-page.sync="currentPage"
          :page-size="pagesize"
          layout="total, sizes, prev, pager, next, jumper"
          :total=this.list.length
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
      opdatesel:'',
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
      multipleSelection: [] 
      }
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
        console.log(this.list)
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
    pickerOptionsStart (row = {}) {
    return {
      disabledDate (time) {
        return time.getTime() < new Date(row.study_info.bdate).getTime()
      }
    }},
    deleteBatch() {
      if (this.$refs.multipleTable.selection.length === 0){
        this.$confirm('请选择要删除的文件', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })}
      else{
        this.$confirm('此操作将永久删除文件, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'error'
        }).then(() => {
          this.$confirm('确定要删除吗？', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'error'
        }).then(() => {
          var d = this.list
          this.$refs.multipleTable.selection.forEach((Ele, index) => {
            for (var i = 0; i < d.length; i++) {
              var t = d[i].study_info.StudyInstanceUIDs

              if (t === Ele.study_info.StudyInstanceUIDs) {

                  axios.get('/api/Mri_delete', {
                  params: {
                  "study_id":t,
                  "pid":Ele.study_info.f_num
                  }
                }).then(res => {
                  if (res.data.code == 20000){
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
                  })
                    this.$message({
                    type: 'success',
                    message: '删除成功!'
                  })
                  }
                  else{
                    this.$message({
                    type: 'error',
                    message: '删除失败!'
                  })
                  this.listLoading = false}
                })
              }
            }
          })
          }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
      }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })}
    }
    ,
    search() {
      axios.get('/api/Query', {
        params: {
          "find_state": 1,
          "name": this.name,
          "check_date1": this.datesel[0],
          "check_date2": this.datesel[1],
          "op_date1": this.opdatesel[0],
          "op_date2": this.opdatesel[1],
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
          "op_date1": this.opdatesel[0],
          "op_date2": this.opdatesel[1],
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
      this.opdatesel = ''
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
    info_save(row) {
      axios.post('/api/Mri_update', {
        data: {
          "study_id": row.study_info.StudyInstanceUIDs,
          "clinic_info": {"cheif":row.clinic_info.cheif, "remark":row.clinic_info.remark},
          "surgery_info": {"date":row.surgery_info.date, "region":row.surgery_info.region, "zhuw":row.surgery_info.zhuw, "xinp":row.surgery_info.xinp},
          "pathology_info": {"p_invasive":row.pathology_info.p_invasive, "p_level":row.pathology_info.p_level, "vig":row.pathology_info.vig, "p_sub":row.pathology_info.p_sub}
        },
        headers:{'Content-Type': 'application/json;charset=UTF-8'}
      }).then(res => {
        if (res.data.code == 20000){
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
      })
        this.$message({
          message: '保存成功',
          type: 'success'
        })
    }
    else{
      this.$message({
          message: '保存失败',
          type: 'error'
        })
    }
  })
     
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
        if (res.status === 20000){
        this.$message({
            duration:0,
            message: '分析成功',
            showClose: true,
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
    if (res.status === 5000){
      this.$message({
            duration:0,
            showClose: true,
            message: '该病例无肿瘤或未分割出肿瘤, 分析失败',
            type: 'error'
        })
        axios.get('/api/Query', {
          params: {
            "find_state": 0,
            "name": this.name,
            "check_date": this.datesel,
            "p_sub": this.sel_bingli,
            "p_invasive": this.sel_inverse,    
            "p_level": this.sel_level,
            "op_date":this.opdatesel
          }
        }).then(res => {
          this.listLoading = true
          this.list = res.data.result
          this.listLoading = false
          row.img_load = 'false'
        })
    }
    if (res.status === 10000){
      this.$message({
        duration:0,
        showClose: true,
        message: '该病例存在模态缺失, 分析失败',
        type: 'error'
    })
    axios.get('/api/Query', {
          params: {
            "find_state": 0,
            "name": this.name,
            "check_date": this.datesel,
            "p_sub": this.sel_bingli,
            "p_invasive": this.sel_inverse,    
            "p_level": this.sel_level,
            "op_date":this.opdatesel
          }
        }).then(res => {
          this.listLoading = true
          this.list = res.data.result
          this.listLoading = false
          row.img_load = 'false'
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
