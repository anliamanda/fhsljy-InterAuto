# -*- coding:utf-8 -*-
"""
@Time:2022/11/25 3:41 下午
@Auth:amanda
@Function:请输入模块功能描述
"""
from util.baseApi import baseApi


class workReport(baseApi):
	def isExist_workPlan(self, term, type):
		data = {
			"method": "post",
			"url": "https://" + self.set_url() + "/custom/api/v1/workReport/isExist",
			"headers": {
				"Access-Token": self.token
				
			},
			"json": {
				
				"term": term,
				"type": type,
				"schoolId": self.schoolId
			}
			
		}
		return self.send(data)
