# -*- coding:utf-8 -*-
"""
@Time:2022/11/17 2:19 下午
@Auth:amanda
@Function:教室信息接口
"""

from util.baseApi import baseApi



class teacherReport(baseApi):
	#查询教学方案
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
	
	 