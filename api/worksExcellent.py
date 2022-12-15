# -*- coding:utf-8 -*-
"""
@Time:2022/11/28 2:16 下午
@Auth:amanda
@Function:请输入模块功能描述
"""
from util.baseApi import baseApi


class worksExcellent(baseApi):
	#优秀作业列表
	def worksExcellentPage(self,designName,grade,publishing,state,subjectName,type,schoolId,term):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/custom/api/v1/worksExcellent/page",
			"headers": {
				"Access-Token": self.token,
				"charset": "UTF-8"
			},
			"json": {
				"current": 1,
				"size": 10,
				"designName": designName,
				"grade": grade,
				"publishing": publishing,
				"state": state,
				"subjectName":subjectName,
				"type":type,
				"schoolId":schoolId,
				"term":term
				
				
			}
		}
		return self.send(data)
	
	def worksExcellentInfo(self,id):
		data = {
			"method": "get",
			"url": "https://" + self.set_url() + "/custom/api/v1/worksExcellent/info/"+id,
			"headers": {
				"Access-Token": self.token,
				"charset": "UTF-8"
			}
		}
		
		return self.send(data)