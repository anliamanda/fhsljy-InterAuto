# -*- coding:utf-8 -*-
"""
@Time:2022/11/17 2:19 下午
@Auth:amanda
@Function:测试用例
"""
import pytest
import allure

from testCase.testBase import TestBase
from api.teachReport import teacherReport
@allure.feature("教学上报")

class Testcase(TestBase):
	teacherReport=teacherReport()
	id=""
	
  
	@allure.story("查询上报")
	@allure.step("查询2022-2023秋学期所有状态的教学上报")
	@pytest.mark.parametrize("term,state",[("2022-2023秋学期","")])
	@pytest.mark.run(order=1)
	#@pytest.mark.skip
	def test_search_all(self,term,state):
		self.log.info("查询2022-2023秋学期所有状态的教学上报")
		assert self.teacherReport.search_teacherReport(term,state)["success"] ==True
	
	# @allure.step("查询2022-2023秋学期已提交的教学上报")
	# @pytest.mark.parametrize("term,state", [("2022-2023秋学期", "1")])
	# @pytest.mark.run(order=2)
	# def test_search_state1(self,term,state):
	# 	self.log.info("查询2022-2023秋学期已提交的教学上报")
	# 	assert self.teacherReport.search_teacherReport(term, state)["success"] == True
	#
	# @allure.step("查询2022-2023秋学期未提交的教学上报")
	# @pytest.mark.parametrize("term,state", [("2022-2023秋学期", "0")])
	# @pytest.mark.run(order=2)
	# def test_search_state2(self, term, state):
	# 	self.log.info("查询2022-2023秋学期未提交的教学上报")
	# 	assert self.teacherReport.search_teacherReport(term, state)["success"] == True


		

	
	
	