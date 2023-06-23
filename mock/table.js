const Mock = require('mockjs')

const data = Mock.mock({
  'items|30': [{
    id: '@id',
    name: '@cname',
    age: '@integer(1,100)',
    cdate: '@date',
    bdate: '@date',
    'sex|1': ['男', '女'],
    f_num: '@integer(300, 5000)',
    'invasive|1': ['是', '否'],
    'level|1': ['良性', '非良性'],
    'consist_inv|1': ['是', '否'],
    'consist_lev|1': ['是', '否'],
    device: '@string(2)',
    modality: '@integer(1,4)',
    slice: '@integer(100,300)',
    url_view: 'http://localhost:3000/viewer?StudyInstanceUIDs=2.16.840.1.114362.1.11972228.22789312658.616067305.306.2'
  }]
})

module.exports = [
  {
    url: '/vue-admin-template/table/list',
    type: 'get',
    response: config => {
      const items = data.items
      return {
        code: 20000,
        data: {
          total: items.length,
          items: items
        }
      }
    }
  }
]
