<template>
  <div class="studylist">

    <div class="deleteSearch">
      <div style="margin-top:10px; max-resolution: 10px; margin-left: 20px;">检索：<el-input v-model="searchText" placeholder="姓名检索" clearable size="medium" />
        筛选：
        <el-date-picker
          v-model="datasel"
          type="daterange"
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
          size="medium"
        />
        病理亚型：
        <el-select
          v-model="sel_bingli"
          filterable
          allow-create
          default-first-option
          size="medium"
          placeholder="请选择"
        >
          <el-option
            v-for="item in p_sub_op"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
        脑侵袭：<el-select
          v-model="sel_inverse"
          filterable
          allow-create
          default-first-option
          size="medium"
          placeholder="请选择"
        >
          <el-option
            v-for="item in p_inv_op"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select> <br>

        分级：
        <el-select
          v-model="sel_level"
          filterable
          allow-create
          default-first-option
          size="medium"
          placeholder="请选择"
        >
          <el-option
            v-for="item in p_lev_op"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          />
        </el-select>
        <el-button class="my-button" type="danger" icon="el-icon-delete" size="medium" @click="deleteBatch()">删除</el-button></div>
    </div>

    <el-table
      ref="multipleTable"
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
      @selection-change="handleSelectionChange"
    >

      <el-table-column
        type="selection"
        align="center"
        :selectable="checkSelectable"
        width="55"
      />

      <el-table-column
        align="center"
        label="ID"
        width="95"
      >
        <el-table-column align="center" label="患者姓名" width="95">
          <el-table-column label="F号" width="100" align="center">
            <template slot-scope="scope">
              {{ scope.$index }} <br> {{ scope.row.name }} <br> {{ scope.row.f_num }}
            </template>
          </el-table-column>
        </el-table-column>
      </el-table-column>

      <el-table-column label="患者临床信息" width="400" align="center">
        <template slot-scope="scope">
          <div>年龄：{{ scope.row.age }} 性别：{{ scope.row.sex }}</div> <br>
          <div>出生年月：{{ scope.row.bdate }} 检查日期：{{ scope.row.cdate }}</div><br>
          <div>主诉：<el-input v-model="scope.row.vig" size="mini" placeholder="请输入" class="square" style="display:inline" /></div><br>
          <div>备注：<el-input v-model="scope.row.vig" size="mini" placeholder="请输入" class="square" style="display:inline" /></div><br>
          <div><el-button type="primary" size="small">上传</el-button></div>

          <!-- <span>{{ scope.row.author }}</span> -->
        </template>
      </el-table-column>

      <el-table-column label="成像设备" width="110" align="center">
        <el-table-column align="center" label="模态个数" width="110">
          <el-table-column align="center" label="切片个数" width="110">
            <template slot-scope="scope">
              {{ scope.row.device }} <br> {{ scope.row.modality }} <br> {{ scope.row.slice }}

              <div><el-button type="primary" size="small">查看图片</el-button></div>

            </template>
          </el-table-column>
        </el-table-column>
      </el-table-column>

      <el-table-column class-name="status-col" label="AI诊断结果" width="150" align="center">
        <template slot-scope="scope">
          <div>脑侵袭：<el-tag :type="[scope.row.invasive==='否' ? 'success': 'danger']">{{ scope.row.invasive }}</el-tag></div> <br>
          <div>分级：<el-tag :type="[scope.row.level==='良性' ? 'success': 'danger']">{{ scope.row.level }}</el-tag></div>
        </template>
      </el-table-column>

      <el-table-column label="手术信息" width="400" align="center">
        <template slot-scope="scope">
          <div class="block">手术日期：
            <el-date-picker
              v-model="scope.row.data"
              type="date"
              placeholder="选择日期"
              size="mini"
            />
          </div> <br>

          <div>病变部位：
            <el-select
              v-model="scope.row.region"
              filterable
              allow-create
              default-first-option
              size="mini"
              placeholder="请选择"
              class="square"
            >
              <el-option
                v-for="item in p_region"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select></div><br>

          <div>蛛网膜隔离：
            <el-select
              v-model="scope.row.zhuw"
              filterable
              allow-create
              default-first-option
              size="mini"
              placeholder="请选择"
              class="square"
            >
              <el-option
                v-for="item in p_zhuw"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select></div>

          <div>辛普森分级：
            <el-select
              v-model="scope.row.xinp"
              filterable
              allow-create
              default-first-option
              size="mini"
              placeholder="请选择"
              class="square"
            >
              <el-option
                v-for="item in p_xinp"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select></div>

          <div><el-button type="primary" size="small">上传</el-button></div>

        </template>
      </el-table-column>

      <el-table-column label="术后病理结果" width="200" align="center">
        <template slot-scope="scope">
          <div>脑侵袭：<el-select
            v-model="scope.row.p_invasive"
            filterable
            allow-create
            default-first-option
            size="mini"
            placeholder="请选择"
            class="square"
          >
            <el-option
              v-for="item in p_inv_op"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            />
          </el-select></div> <br>

          <div>分级：
            <el-select
              v-model="scope.row.p_level"
              filterable
              allow-create
              default-first-option
              size="mini"
              placeholder="请选择"
              class="square"
            >
              <el-option
                v-for="item in p_lev_op"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select></div><br>

          <div>增值指数：<el-input v-model="scope.row.vig" size="mini" placeholder="请输入" class="square" style="display:inline" /></div><br>

          <div>病理亚型：
            <el-select
              v-model="scope.row.p_sub"
              filterable
              allow-create
              default-first-option
              size="mini"
              placeholder="请选择"
              class="square"
            >
              <el-option
                v-for="item in p_sub_op"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select></div>

          <div><el-button type="primary" size="small">上传</el-button></div>

        </template>
      </el-table-column>

      <el-table-column align="center" prop="created_at" label="是否一致" width="200">
        <template slot-scope="scope">
          <el-tag :type="[scope.row.consist==='否' ? 'success': 'danger']">{{ scope.row.consist }}</el-tag>
        </template>
      </el-table-column>

    </el-table>
  </div></template>

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
      listLoading: true,
      datasel: '',
      sel_bingli: '',
      sel_inverse: '',
      sel_level: '',
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
        { value: '选项3', label: '四级' }],
      p_region: [
        { value: '选项1', label: '无' }],
      searchText: '',
      multipleSelection: [] }
  },
  computed: {
    studylist: function() {
      return this.list.filter(item => {
        return item.name.include(this.searchText)
      })
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList().then(response => {
        this.list = response.data.items
        console.log(this.list)
        this.listLoading = false
      })
    },
    deleteBatch() {
      var d = this.list
      this.$refs.multipleTable.selection.forEach((Ele, index) => {
        for (var i = 0; i < d.length; i++) {
          var t = d[i].name
          if (t === Ele.name) {
            d.splice(i, 1)
          }
        }
      })
    }
  }

}
</script>

<style scoped>
  .square /deep/ .el-input__inner {
    width: 90px !important;
  }

.my-button{
  width: 80px;
  margin-left: 1300px;
  margin-bottom: 10px;
}
.el-button--primary{
  margin-top: 20px;
}

.el-input{
  width: 180px;

}
</style>
