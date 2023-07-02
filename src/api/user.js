import request from '@/utils/request'

export function login(data) {
  return request({
    url: '/api/login/loginbypassword',
    method: 'post',
    data: data,
    headers:{'Content-Type': 'application/json;charset=UTF-8'}
  })
}

export function getInfo(token) {
  return request({
    url: '/api/login/logingetinfo',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/api/login/loginout',
    method: 'post'
  })
}

export function regeisted(data){
  return request({
    url: '/api/login/regeistedbyadmin',
    method: 'post',
    data: data,
    headers:{'Content-Type': 'application/json;charset=UTF-8'}
  })
}