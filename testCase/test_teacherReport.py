# -*- coding:utf-8 -*-
"""
@Time:2022/11/17 2:19 下午
@Auth:amanda
@Function:测试用例
"""
import pytest
import allure
import yaml
import time
from testCase.testBase import TestBase
from api.teachReport import teacherReport
@allure.feature("一教一辅")

class TestTeacherReport(TestBase):
	teacherReport=teacherReport()
	id=""
	result=""

	@allure.story("查询一教一辅")
	@pytest.mark.parametrize("term,state", yaml.safe_load(open("./config/teacherReport.yaml"))["search"])
	@pytest.mark.run(order=1)
	# @pytest.mark.skip
	def test_search_all(self, term,state):
		self.log.info("查询2022-2023秋学期一教一辅")
		TestTeacherReport.result=self.teacherReport.search_teacherReport(term,state)
		assert self.teacherReport.search_teacherReport(term,state)["success"] ==True

	@allure.story("一教一辅详情")
	@pytest.mark.parametrize("phaseType,term",[("1","2022-2023秋学期")])
	@pytest.mark.run(order=2)
	def test_info(self,phaseType,term):
		self.log.info("一教一辅详情")
		if self.teacherReport.isExtend(TestTeacherReport.result,"teachReportName"):
			teachReportName=TestTeacherReport.result["data"]["records"][0]["teachReportName"]
			print(teachReportName)
			self.teacherReport.info_teacherReport(phaseType,teachReportName,term)["success"]==True
	
	@pytest.mark.skip
	@allure.story("一教一辅修改")
	@pytest.mark.run(order=3)
	def test_update(self):
		
		nowtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		print(type(nowtime))
		newdata={
			"schoolId":self.teacherReport.schoolId,
			"schoolName":self.teacherReport.schoolName,
			"updateTime":nowtime,
			"teachReportName":self.teacherReport.schoolName+'_'+"秋学期"+"_"+"小学一教一辅方案",
			"createTime":nowtime,
			"term":"2022-2023秋学期"
		}
		flexidata=teacherReport.newData("./data/test.json", newdata)
		print(flexidata)
		self.teacherReport.update_teacherReport(flexidata)

	