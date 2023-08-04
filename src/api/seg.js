import request from '@/utils/request'

export function getSeg(study_id) {
    return request({
      url: '/api/Predict',
      method: 'post',
      data: {study_id},
      headers:{'Content-Type': 'application/json;charset=UTF-8'}

    })
  }