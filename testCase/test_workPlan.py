# -*- coding:utf-8 -*-
"""
@Time:2022/11/21 10:04 上午
@Auth:amanda
@Function:请输入模块功能描述
"""
import allure
import pytest
import yaml
import jsonpath

from api.workPlan import workPlan
from testCase.testBase import TestBase
from api.workReport import workReport


@allure.feature("作业方案上报")
class TestWorkPlan(TestBase):
	
	workReport = workReport()
	workPlan=workPlan()
	id=""
	
	@allure.story("查询作业方案上报")
	@pytest.mark.parametrize("term,state,type",yaml.safe_load(open("./config/worPlan.yaml"))["search"])
	@pytest.mark.run(order=1)
	# @pytest.mark.skip
	def test_search_all(self, term, state,type):
		self.log.info("查询2022-2023秋学期作业方案上报")
		assert self.workPlan.search_workPlan(term, state,type)["success"] == True

	@allure.story("新增作业方案上报")
	@pytest.mark.run(order=2)
	@pytest.mark.parametrize("term,phaseType,content,type,annexUrl,annexName",
	                         yaml.safe_load(open("./config/worPlan.yaml"))["save"])
	def test_save(self, term, phaseType, content, type, annexUrl, annexName):
		self.log.info("新增作业方案上报")
		result= self.workReport.isExist_workPlan("2022-2023秋学期", "plan")
		if self.workPlan.isExtend(result,"phaseType"):
			assert self.workPlan.save_workPlan(term, phaseType, content, type, annexUrl, annexName)["success"] == True

		else:
			print("不需要新增")
			pass

	@allure.story("修改作业方案保存后提交")
	@pytest.mark.run(order=3)
	@pytest.mark.parametrize("term,phaseType,content,type,annexUrl,annexName",
	                         yaml.safe_load(open("./config/worPlan.yaml"))["update"])
	def test_update(self, term, phaseType, content, type, annexUrl, annexName):
		state=self.workPlan.search_workPlan("2022-2023秋学期", "", "school")["data"]["records"][0]["state"]
		if 0 ==state:
			assert self.workPlan.update_workPlan(term, phaseType, content, type, annexUrl, annexName, Testcase.id)["success"] == True
		self.log.info("修改作业方案保存")


	@allure.story("作业方案详情")
	@pytest.mark.run(order=4)
	def test_info(self):
		TestWorkPlan.id = self.workPlan.search_workPlan("2022-2023秋学期", "", "school")["data"]["records"][0]["id"]
		assert self.workPlan.info_workPlan(str(TestWorkPlan.id))["success"] == True
		self.log.info("作业方案详情")
		



