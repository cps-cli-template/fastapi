# 项目简介

<div>
     <img flex="left" src="https://img.shields.io/badge/python-%3E%3D3.10.0-3776AB"/>
     <img src="https://img.shields.io/badge/Swagger-85EA2D?style=flat&logo=Swagger&logoColor=white">
</div>

个人自用的 fastapi 项目基础模板集成很多自己常用的服务器基础功能，上手即用

**[English](README.en.md) | 简体中文**

# 功能特色

- [x] 集成中间件
  - [x] gzip
  - [x] 一键跨域
  - [x] 定时任务
    - [x] 基于`asyncio`的原生装饰器方式
    - [ ] `fastapi-gino-arq-uvicorn`
    - [ ] `apscheduler`
    - [ ] `Celery`

- [x] 数据库操作
  - [x] redis
  - [ ] mongodb
  - [ ] mysql
- [x] 文件上传
  - [ ] 根据文件类型自动分类（类型 >上传日期 > 文件名）
  - [x] 小文件上传，直接通过内存接收整个文件
  - [x] 大文件上传，以流的形式接收文件，每次指定大小
- [x] 离线的`swagger-ui`修复
- [x] static静态服务器文件夹
- [x] 日志系统
  - [x] 基于logging
  - [x] 基于loguru
- [x] 其他功能
  - [x] 基于ini配置文件
  - [x] 所有集成的功能都带一键开关
  - [x] 自动创建常用文件夹



## 目录结构

```yaml
DIR:template-fastapi                 #
   |-- dependencies/                 # 「dependencies」
   |   `-- __init__.py               #
   |-- docs/                         # 「docs」存放说明相关的文件
   |   |-- __init__.py               #
   |   `-- description.py            #
   |-- events/                       # 「events」事件层
   |   |-- __init__.py               #
   |   |-- startup.py                # 所有startup事件汇总的入口文件
   |   `-- config_check.py           # 检查config中所有key为*_path结尾的目录是否存在，自动创建对应目录
   |-- internal/                     # 「internal」
   |   `-- __init__.py               #
   |-- middleware/                   # 「middleware」中间件层，常用的中间件
   |   |-- logger.py                 #
   |   |-- gzip.py                   #
   |   `-- cors.py                   #
   |-- routers/                      # 「routers」路由层
   |   |-- v1/                       # 「v1」如果是定制
   |   |   `-- __init__.py           #
   |   |-- __init__.py               #
   |   |-- upload_router_template.py #
   |   |-- upload.py                 #
   |   |-- test.py                   #
   |   |-- static.py                 #
   |   `-- docs.py                   #
   |-- static/                       # 「static」默认的静态文件目录，可以在config.py指定
   |   |-- swagger-ui.css            #
   |   |-- swagger-ui-bundle.js      #
   |   `-- redoc.standalone.js       #
   |-- test/                         # 「test」测试
   |   `-- async_test.py             #
   |-- tools/                        # 「tools」全局组件层
   |   |-- __init__.py               #
   |   |-- uploader.py               # 上传组件
   |   |-- test.py                   #
   |   `-- schedule.py               # 定时组件
   |-- utils/                        # 「utils」
   |   `-- logger.py                 #
   |-- __init__.py                   #
   |-- Types.py                      # 一些全局类型存放
   |-- tree.yaml                     # 项目结构文件
   |-- test.py                       #
   |-- requirements.txt              #
   |-- README                        #
   |-- main.py                       #
   |-- config.py                     # 「关键文件」所有配置
   |-- config.ini                    # 「关键文件」
   `-- .gitignore                    #

```

# 安装 | Install

```bash
npm i @mucpsing/cli -g
```

# 使用 | Usage

```bash
cps -t fastapi <project_name>
```
