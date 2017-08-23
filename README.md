# zabbix-RDS-monitor-sqlserver
Aliyun RDS-mssql status monitor with zabbix   

本项目源代码出自   https://github.com/XWJR-Ops/zabbix-RDS-monitor   提供的Mysql监控脚本
   
zabbix通过阿里云python core api 自动发现、监控阿里云RDS-sqlserver数据库      
本版本数据的图表展示，是以**监控项进行分组**，后期会再发布**以rds实例分组**的版本。

### 版本记录
Ver 0.1 Pythons脚本已测试通过,模板暂未配置完毕

Ver 0.2 模板配置完毕导入即可，建立cpu超过80%的报警，和默认的若干图形
 

## 使用方法
### 注意事项
1. 脚本会收集RDS别名，
2. 不要默认别名，如果相同请修改别名
3. 不要使用中文别名（zabbix不识别）
4. 切记aliyun-python-sdk-core==2.3.5，新版本的sdk有bug
### 环境要求
python = 2.7
### 模块安装
```shell
/usr/local/python2.7/bin/pip2.7 install aliyun-python-sdk-core==2.3.5 aliyun-python-sdk-rds datetime
```
### 使用方法

1. 从阿里云控制台获取 **AccessKey** ,并修改脚本中的 **阿里云ID** 与 **阿里云API Secret**     
2. 修改区域 **RegionId**
3. 将两个脚本放置于以下目录
```conf
/etc/zabbix/script
```
```shell
chmod +x /etc/zabbix/script/*
```
4. 修改zabbix-agentd.conf，添加以下内容 (如python路径不同请自行修改)
```conf
#rds
UserParameter=rds.discovery,/usr/bin/python2.7 /etc/zabbix/script/discovery_rds.py
UserParameter=check.rds[*],/usr/bin/python2.7 /etc/zabbix/script/check_rds.py $1 $2 $3
```
5. 重启zabbix-agent
6. zabbix设置导入模板，并在Zabbix Server添加中添加此模板关联主机

