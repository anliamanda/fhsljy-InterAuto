# -*- coding:utf-8 -*-
"""
@Time:2022/11/28 10:54 上午
@Auth:amanda
@Function:请输入模块功能描述
"""
from util.baseApi import baseApi

class teacherPage(baseApi):
	def getTeacherPage(self,clazs,grade,keyWord,queryType,type):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/custom/api/v1/user/getTeacherPage",
			"headers": {
				"Access-Token": self.token,
				"charset": "UTF-8"
			},
			"json": {
				"clazs": clazs,
				"grade": grade,
				"keyWord": keyWord,
				"queryType": queryType,
				"schoolId": self.schoolId,
				"type":type,
				"current":1,
				"size":10
				
			}
		}
		
		return self.send(data)
