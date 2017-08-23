#coding=utf-8
#Auther：35315.org
from aliyunsdkcore import client
from aliyunsdkrds.request.v20140815 import DescribeResourceUsageRequest,DescribeDBInstancePerformanceRequest
import json,sys,datetime

ID = '阿里云ID'
Secret = '阿里云API Secret'
RegionId = 'cn-hangzhou'

clt = client.AcsClient(ID,Secret,RegionId)

Type = sys.argv[1]
DBInstanceId = sys.argv[2]
Key = sys.argv[3]


UTC_End = datetime.datetime.today() - datetime.timedelta(hours=8)
UTC_Start = UTC_End - datetime.timedelta(minutes=25)

StartTime = datetime.datetime.strftime(UTC_Start, '%Y-%m-%dT%H:%MZ')
EndTime = datetime.datetime.strftime(UTC_End, '%Y-%m-%dT%H:%MZ')

#获取资源信息
def GetResourceUsage(DBInstanceId,Key):
    ResourceUsage = DescribeResourceUsageRequest.DescribeResourceUsageRequest()
    ResourceUsage.set_accept_format('json')
    ResourceUsage.set_DBInstanceId(DBInstanceId)
    ResourceUsageInfo = clt.do_action_with_exception(ResourceUsage)
    #print ResourceUsageInfo
    Info = (json.loads(ResourceUsageInfo))[Key]
    print Info

#获取性能信息
def GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime):
    Performance = DescribeDBInstancePerformanceRequest.DescribeDBInstancePerformanceRequest()
    Performance.set_accept_format('json')
    Performance.set_DBInstanceId(DBInstanceId)
    Performance.set_Key(MasterKey)
    Performance.set_StartTime(StartTime)
    Performance.set_EndTime(EndTime)
    PerformanceInfo = clt.do_action_with_exception(Performance)
    #print PerformanceInfo
    Info = (json.loads(PerformanceInfo))
    Value = Info['PerformanceKeys']['PerformanceKey'][0]['Values']['PerformanceValue'][-1]['Value']
    print str(Value).split('&')[IndexNum]


if (Type == "Disk"):

	#日志空间使用量
	if (Key == "LogSize"):
		MasterKey = "LogSize"
		GetResourceUsage(DBInstanceId,MasterKey)
	
	#数据空间使用量
	elif (Key == "DataSize"):
		MasterKey = "DataSize"
		GetResourceUsage(DBInstanceId,MasterKey)
		
	#备份空间总体使用量
	elif (Key == "BackupSize"):
		MasterKey = "BackupSize"
		GetResourceUsage(DBInstanceId,MasterKey)
		
	#磁盘空间总体使用量
	elif (Key == "DiskUsed"):
		MasterKey = "DiskUsed"
		GetResourceUsage(DBInstanceId,MasterKey)
		
	
		
elif (Type == "Performance"):

    #平均每秒钟事物数
    if (Key == "SQLServer_Transactions"):
        IndexNum = 0
        MasterKey = "SQLServer_Transactions"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime)

    #当前总连接数
    elif (Key == "SQLServer_Sessions"):
        IndexNum = 0
        MasterKey = "SQLServer_Sessions"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime)

	#缓存命中率
    elif (Key == "SQLServer_BufferHit"):
        IndexNum = 0
        MasterKey = "SQLServer_BufferHit"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime)  
		
	#平均每秒全表扫描次数
    elif (Key == "SQLServer_FullScans"):
        IndexNum = 0
        MasterKey = "SQLServer_FullScans"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime)  

	#每秒SQL编译
    elif (Key == "SQLServer_SQLCompilations"):
        IndexNum = 0
        MasterKey = "SQLServer_SQLCompilations"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime)

	#每秒检查点写入Page数
    elif (Key == "SQLServer_CheckPoint"):
        IndexNum = 0
        MasterKey = "SQLServer_CheckPoint"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 

	#每秒登录次数
    elif (Key == "SQLServer_Logins"):
        IndexNum = 0
        MasterKey = "SQLServer_Logins"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 
		
	#每秒锁超时次数
    elif (Key == "SQLServer_LockTimeout"):
        IndexNum = 0
        MasterKey = "SQLServer_LockTimeout"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 
		
	#每秒死锁次数
    elif (Key == "SQLServer_Deadlock"):
        IndexNum = 0
        MasterKey = "SQLServer_Deadlock"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 
				
	#每秒锁等待次数
    elif (Key == "SQLServer_LockWaits"):
        IndexNum = 0
        MasterKey = "SQLServer_LockWaits"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 
		
	#SQLServer实例平均每秒钟的输入/输出流量。单位为KB
    elif (Key == "SQLServer_NetworkTraffic_Out"):
        IndexNum = 0
        MasterKey = "SQLServer_NetworkTraffic"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 
		
	#SQLServer实例平均每秒钟的输入/输出流量。单位为KB
    elif (Key == "SQLServer_NetworkTraffic_In"):
        IndexNum = 1
        MasterKey = "SQLServer_NetworkTraffic"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 
		
	#平均每秒SQL语句执行次数
    elif (Key == "SQLServer_QPS"):
        IndexNum = 0
        MasterKey = "SQLServer_QPS"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 
	
	#MSSQL实例CPU使用率(占操作系统总数)
    elif (Key == "SQLServer_InstanceCPUUsage"):
        IndexNum = 0
        MasterKey = "SQLServer_InstanceCPUUsage"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 

	#MSSQL实例的IOPS（每秒IO请求次数）
    elif (Key == "SQLServer_IOPS"):
        IndexNum = 0
        MasterKey = "SQLServer_IOPS"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 

	#MSSQL实例空间占用
    elif (Key == "SQLServer_SpaceUsage"):
        IndexNum = 0
        MasterKey = "SQLServer_SpaceUsage"
        GetPerformance(DBInstanceId,MasterKey,IndexNum,StartTime,EndTime) 

		
