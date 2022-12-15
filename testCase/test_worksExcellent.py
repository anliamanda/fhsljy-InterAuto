# -*- coding:utf-8 -*-
"""
@Time:2022/11/28 2:20 下午
@Auth:amanda
@Function:请输入模块功能描述
"""
import allure
import pytest
import yaml

from api.worksExcellent import worksExcellent
from testCase.testBase import TestBase

@allure.feature("优秀作业管理")
class TestWorksExcellent(TestBase):
	worksExcellent=worksExcellent()
	result=""
	id=""
	@allure.story("优秀作业列表")
	@pytest.mark.parametrize("designName,grade,publishing,state,subjectName,type,schoolId,term",yaml.safe_load(open("./config/worksExcellent.yaml"))["page"])
	def test_worksExcellentPage(self,designName,grade,publishing,state,subjectName,type,schoolId,term):
		worksExcellent.result=self.worksExcellent.worksExcellentPage(designName,grade,publishing,state,subjectName,type,schoolId,term)
		print(worksExcellent.result)
		assert self.worksExcellent.worksExcellentPage(designName,grade,publishing,state,subjectName,type,schoolId,term)["success"]==True
	
	def test_worksExcellentInfo(self):
		print(worksExcellent.result)
		#assert self.worksExcellent.worksExcellentInfo(str(worksExcellent.id))["success"]==True