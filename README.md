# 基于时间序列的牛发情检测系统1.0

本系统基于ARIMA模型

## 运行环境

### 前端

+ node.js 6.14 以及以上版本
+ vue 3.12.1

### 后端

anaconda 4.8.5

Django 3.1.5

### 中间件

nginx 1.18.0

## 运行方式

### 前端

安装vue-cli

`npm install -g @vue/cli@3.12.1`

创建vue项目

`vue create 项目名`

将前端代码拷贝到项目中

运行

```bash
npm run serve
```

### 后端

切换到后端代码目录

```bash
python manage.py runserver 0.0.0.0:8000
```

### 中间件配置

```bash
server {
    listen    8080;
    server_name   localhost;	# 前端项目运行地址和端口

    location ^~ /api/ {
    	proxy_pass   http://localhost:8000/; # 后端代码运行的地址和端口
    }

}
```

