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
            v-model="filterText"
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
          :data="filteredData"
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
                  {{ scope.$index }} <el-divider /> {{ scope.row.name }} <el-divider /> {{ scope.row.f_num }}
                </template>
              </el-table-column>
            </el-table-column>
          </el-table-column>

          <el-table-column label="患者临床信息" min-width="4" align="center">
            <template slot-scope="scope">
              <div>年龄：{{ scope.row.age }} 性别：{{ scope.row.sex }}</div>
              <div>出生年月：{{ scope.row.bdate }} <br>
                检查日期：{{ scope.row.cdate }}</div>
              <div>主诉：<el-input v-model="scope.row.cheif" type="textarea" :rows="1" size="mini" placeholder="请输入" style="width: 60%;" /></div>
              <div>备注：<el-input v-model="scope.row.remark" type="textarea" :rows="1" size="mini" placeholder="请输入" style="width: 60%;" /></div>
              <!-- <el-divider /> -->
              <!-- <div><el-button type="primary" size="small">上传</el-button></div> -->
            </template>
          </el-table-column>

          <el-table-column label="成像设备" min-width="2" align="center">
            <el-table-column align="center" label="模态个数" min-width="2">
              <el-table-column align="center" label="切片个数" min-width="2">
                <template slot-scope="scope">
                  {{ scope.row.device }} <el-divider /> {{ scope.row.modality }} <el-divider /> {{ scope.row.slice }} <el-divider />

                  <div><el-button type="text" size="medium">查看图片</el-button></div>

                </template>
              </el-table-column>
            </el-table-column>
          </el-table-column>

          <el-table-column class-name="status-col" label="AI诊断结果" min-width="3" align="center">
            <template slot-scope="scope">
              <div>脑侵袭：<el-tag :type="[scope.row.invasive==='否' ? 'success': 'danger']">{{ scope.row.invasive }}</el-tag></div> <br>
              <div>分级：<el-tag :type="[scope.row.level==='良性' ? 'success': 'danger']">{{ scope.row.level }}</el-tag></div>
            </template>
          </el-table-column>

          <el-table-column label="手术信息" min-width="4" align="center">
            <template slot-scope="scope">
              <div style="display: flex;width:100%;">
                <div style="width:40%">手术日期：</div>
                <el-date-picker
                  v-model="scope.row.date"
                  type="date"
                  placeholder="选择日期"
                  size="mini"
                  style="width:60%"
                />
              </div>
              <div style="display: flex;width:100%;">
                <div style="width:40%">病变部位：</div>
                <el-select
                  v-model="scope.row.region"
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
                <div style="width:40%">蛛网膜隔离：</div>
                <el-select
                  v-model="scope.row.zhuw"
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
                  v-model="scope.row.xinp"
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
              <!-- <el-divider /> -->
              <div>
                <!-- <el-button type="primary" size="small">上传</el-button> -->
              </div>
            </template>
          </el-table-column>

          <el-table-column label="术后病理结果" min-width="4" align="center">
            <template slot-scope="scope">
              <div style="display: flex;width:100%;">
                <div style="width:40%">脑侵袭：</div>
                <el-select
                  v-model="scope.row.p_invasive"

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
                  v-model="scope.row.p_level"
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
                <el-input v-model="scope.row.vig" size="mini" placeholder="请输入" style="width:60%" />
              </div>

              <div style="display: flex;width:100%;">
                <div style="width:40%">病理亚型：</div>
                <el-select
                  v-model="scope.row.p_sub"
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
              <!-- <el-divider /> -->
              <!-- <div><el-button type="primary" size="small">上传</el-button></div> -->

            </template>
          </el-table-column>

          <el-table-column class-name="status-col" label="是否一致" min-width="3" align="center">
            <template slot-scope="scope">
              <div>脑侵袭：<el-tag :type="[scope.row.consist_inv==='否' ? 'danger': 'success']">{{ scope.row.consist_inv }}</el-tag></div> <br>
              <div>分级：<el-tag :type="[scope.row.consist_lev==='否' ? 'danger': 'success']">{{ scope.row.consist_lev }}</el-tag></div>
            </template>
          </el-table-column>

          <el-table-column class-name="status-col" label="保存信息" min-width="2" align="center">
            <template slot-scope="scope">
              <el-button class="tech-search-btn" type="primary" size="small" @click="info_save(scope.row)"> 保存 </el-button> <br>
              <el-button class="tech-search-btn" size="small" style="margin-top: 20px;" @click="info_reset(scope.row)"> 重置 </el-button>
            </template>
          </el-table-column>

        </el-table>
        <!-- 列表分页 -->
        <el-pagination
          class="tech-table-pagination"
          :current-page.sync="currentPage"
          :page-sizes="[10, 50, 150, 200]"
          :page-size="pageSizeNum"
          layout="total, sizes, prev, pager, next, jumper"
          :total="totalPages"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
        />

      </div>
    </div>

  </div>
</template>

<script>
import { getList } from '@/api/table'

export default {
  name: '',
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'gray',
        deleted: 'danger'
      }
      return statusMap[status]
    }
  },

  data() {
    return {
      list: null,
      filterText: '',
      listLoading: true,
      datesel: '',
      sel_bingli: '',
      sel_inverse: '',
      sel_level: '',
      cheif: '',
      remark: '',
      p_inv_op: [
        { value: '选项1', label: '是' },
        { value: '选项2', label: '否' }],
      p_lev_op: [
        { value: '选项1', label: '一级' },
        { value: '选项2', label: '二级' },
        { value: '选项3', label: '三级' }],
      p_sub_op: [
        { value: '选项1', label: '脑膜皮型' },
        { value: '选项2', label: '纤维型 (成纤维型)' },
        { value: '选项3', label: '过渡型 (混合型)' },
        { value: '选项4', label: '沙粒体型' },
        { value: '选项5', label: '血管瘤型' },
        { value: '选项6', label: '微囊型' },
        { value: '选项7', label: '分泌型' },
        { value: '选项8', label: '富淋巴-浆细胞型' },
        { value: '选项9', label: '移行型' },
        { value: '选项10', label: '透明细胞型' },
        { value: '选项11', label: '脊索瘤样型' },
        { value: '选项12', label: '非典型' },
        { value: '选项13', label: '乳头状瘤型' },
        { value: '选项14', label: '横纹肌样型' },
        { value: '选项15', label: '间变性 (恶性)' }],
      p_zhuw: [
        { value: '选项1', label: '是' },
        { value: '选项2', label: '否' }],
      p_xinp: [
        { value: '选项1', label: '一级' },
        { value: '选项2', label: '二级' },
        { value: '选项3', label: '三级' },
        { value: '选项4', label: '四级' }],
      p_region: [
        { value: '选项1', label: '无' }],
      searchText: '',
      multipleSelection: [] }
  },
  computed: {
    filteredData() {
      if (!this.filterText) {
        return this.list
      }
      const filterText = this.filterText.toLowerCase()
      return this.list.filter(item => item.name.toLowerCase().includes(filterText))
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
    fetchData() {
      this.listLoading = true
      getList().then(response => {
        this.list = response.data.items
        console.log(this.list)
        this.listLoading = false
      })
    },
    handleSelectionChange(val) {
      // 多选时怎么处理
    },
    deleteBatch() {
      this.$confirm('此操作将永久删除文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        var d = this.list
        this.$refs.multipleTable.selection.forEach((Ele, index) => {
          for (var i = 0; i < d.length; i++) {
            var t = d[i].name
            if (t === Ele.name) {
              d.splice(i, 1)
            }
          }
        })
        this.$message({
          type: 'success',
          message: '删除成功!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    search() {
      this.filteredData()
    },
    reset() {
      // 清空搜索项，重新调用查询接口
      this.filterText = ''
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
    info_save(row) {

    }
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

</style>
