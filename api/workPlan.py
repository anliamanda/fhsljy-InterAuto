# -*- coding:utf-8 -*-
"""
@Time:2022/11/21 9:56 上午
@Auth:amanda
@Function:课后服务类型接口
"""
from util.baseApi import baseApi


class workPlan(baseApi):
	#作业方案列表查询
	def search_workPlan(self, term, state,type):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/custom/api/v1/workPlan/page",
			"headers": {
				"Access-Token": self.token
				
			},
			"json": {
				"schoolId": self.schoolId,
				"size": 10,
				"current": 1,
				"term": term,
				"state": state,
				"type":type
				
			}
		}
		
		return self.send(data)
	
	#新增作业方案上报
	def save_workPlan(self, term,phaseType,content,type,annexUrl,annexName):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/custom/api/v1/workPlan/save",
			"headers": {
				"Access-Token": self.token
				
			},
			"json": {
				"term": term,
				"phaseType": phaseType,
				"contents": content,
				"schoolId": self.schoolId,
				"schoolName": self.schoolName,
				"type": type,
				"annexUrl": annexUrl,
				"annexName":annexName
			}
		}
		
		return self.send(data)
	
	#更新作业方案
	def update_workPlan(self, term,phaseType,content,type,annexUrl,annexName,id):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/custom/api/v1/workPlan/update",
			"headers": {
				"Access-Token": self.token
				
			},
			"json": {
				"term": term,
				"phaseType": phaseType,
				"contents": content,
				"schoolId": self.schoolId,
				"schoolName": self.schoolName,
				"type": type,
				"annexUrl": annexUrl,
				"annexName":annexName,
				"id":id
			}
		}
		return self.send(data)
	
	def info_workPlan(self, id):
		data = {
			"method": "get",
			"url": "https://" + self.set_url() + "/custom/api/v1/workPlan/info/"+id,
			"headers": {
				"Access-Token": self.token
				}
			
		}
		return self.send(data)
	
	