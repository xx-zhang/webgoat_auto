# webgoat auto （2021/4/16 重新修订）

## 靶场搭建
```bash

docker run -itd --name=webgoat \
  --restart=always \
  -p 9090:9090 \
  -p 8090:8080  \
  registry.cn-beijing.aliyuncs.com/redaus/webgoat:dev
```

## 项目转移
- [webgoat_auto](https://code.aliyun.com/sangfor/webgoat_auto)


## 目的
- 问题验证



