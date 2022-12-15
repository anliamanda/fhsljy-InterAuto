# -*- coding:utf-8 -*-
"""
@Time:2022/11/28 11:47 上午
@Auth:amanda
@Function:请输入模块功能描述
"""
import allure
import pytest
import yaml

from api.book import book
from testCase.testBase import TestBase

@allure.feature("教材管理")
class TestBook(TestBase):
	book=book()
	id=""
	result=""
	
	@allure.story("教科书列表")
	@pytest.mark.parametrize("grade,publishing,subjectName",yaml.safe_load(open("./config/book.yaml"))["page"])
	def test_page(self,grade,publishing,subjectName):
		TestBook.result=self.book.schoolTextbookPage(grade,publishing,subjectName)
		assert self.book.schoolTextbookPage(grade,publishing,subjectName)["success"]== True
		
	@allure.story("教科书详情")
	def test_info(self):
		TestBook.id=TestBook.result["data"]["records"][0]["id"]
		assert self.book.infoSchoolTextbook(TestBook.id)["success"]== True
		
	@allure.story("辅导书列表")
	@pytest.mark.parametrize("grade,publishing,subjectName",yaml.safe_load(open("./config/book.yaml"))["teacherPage"])
	def test_teacherPage(self,grade,publishing,subjectName):
		assert self.book.teachbookPage(grade,publishing,subjectName)["success"]== True
	
	
	
	