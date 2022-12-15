# -*- coding:utf-8 -*-
"""
@Time:2022/11/17 2:19 下午
@Auth:amanda
@Function:教室信息接口
"""

from util.baseApi import baseApi



class teacherReport(baseApi):
	#查询教学方案列表
	def search_teacherReport(self,term,state):
	
		data = {
			"method": "post",
			"url": "https://"+self.set_url()+"/custom/api/v1/teachReport/page",
			"headers":{
				"Access-Token":self.token,
				"charset":"UTF-8"
				},
			"json": {
				"schoolId":self.schoolId,
				"size": 10,
				"current": 1,
				"term":term,
				"state":state
				
		}
		}
		
		return self.send(data)
	
	
	def info_teacherReport(self,phaseType,teachReportName,term):
		#作业方案详情接口
		data = {
			"method": "get",
			"url": "https://" + self.set_url() + "/custom/api/v1/teachReport/info",
			"headers": {
				"Access-Token": self.token
				},
			"json": {
				"phaseType": phaseType,
				"schoolId": self.schoolId,
				"teachReportName": teachReportName,
				"term": term
			}
			
		}
		return self.send(data)
	
	def update_teacherReport(self,flexidata:str):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/custom/api/v1/teachReport/update",
			"headers": {
				"Access-Token": self.token
			},
			"json":flexidata
			}
		
		return self.send(data)