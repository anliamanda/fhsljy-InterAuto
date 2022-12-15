# -*- coding:utf-8 -*-
"""
@Time:2022/11/28 11:44 上午
@Auth:amanda
@Function:请输入模块功能描述
"""
from util.baseApi import baseApi


class book(baseApi):
	def schoolTextbookPage(self,grade,publishing,subjectName):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/custom/api/v1/schoolTextbook/page",
			"headers": {
				"Access-Token": self.token,
				"charset": "UTF-8"
			},
			"json": {
				"grade": grade,
				"publishing": publishing,
				"schoolId": self.schoolId,
				"subjectName": subjectName,
				"current": 1,
				"size": 10
				
			}
		}
		
		return self.send(data)

	def infoSchoolTextbook(self,id):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/custom/api/v1/schoolTextbook/info",
			"headers": {
				"Access-Token": self.token,
				"charset": "UTF-8"
			},
			"json": {
				"id": id,
				"schoolId": self.schoolId
	
			}
		}
		return self.send(data)
	
	def teachbookPage(self,grade,publishing,subjectName):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/custom/api/v1/teachbook/page",
			"headers": {
				"Access-Token": self.token,
				"charset": "UTF-8"
			},
			"json": {
				"current":1,
				"size":10,
				"grade":grade,
				"publishing":publishing,
				"subjectName": subjectName,
				"schoolId": self.schoolId
				
			}
		}
		return self.send(data)
	