# -*- coding:utf-8 -*-
"""
@Time:2022/11/25 3:43 下午
@Auth:amanda
@Function:请输入模块功能描述
"""
import allure
import pytest

from testCase.testBase import TestBase

from api.workReport import workReport
class Testcase(TestBase):
	workReport=workReport()
	
	@allure.feature("工作上报记录是否存在")
	@pytest.mark.parametrize("term, type",[("2022-2023秋学期","teacher"),("2022-2023秋学期","plan")])
	def test_isExist(self,term, type):
		assert self.workReport.isExist_workPlan(term, type)["success"]==True
	

	