import request from '@/utils/request'

export function getSeg(download_study_id, study_id) {
    return request({
      url: '/api/Predict',
      method: 'post',
      data: { download_study_id, study_id },
      headers:{'Content-Type': 'application/json;charset=UTF-8'}

    })
  }