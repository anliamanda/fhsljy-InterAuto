# -*- coding:utf-8 -*-
"""
@Time:2022/11/28 11:14 上午
@Auth:amanda
@Function:请输入模块功能描述
"""
import allure
import pytest
import yaml

from api.TeacherPage import teacherPage
from testCase.testBase import TestBase

@allure.feature("教师&学生管理")
class TestTeacherPage(TestBase):
	teacherPage=teacherPage()
	
	@allure.story("教师&学生查询")
	@pytest.mark.parametrize("clazs,grade,keyWord,queryType,type", yaml.safe_load(open("./config/teacherPage.yaml"))["get"])
	def test_getTeacherPage(self,clazs,grade,keyWord,queryType,type):
		assert self.teacherPage.getTeacherPage(clazs,grade,keyWord,queryType,type)["success"] ==True