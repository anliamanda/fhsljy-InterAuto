import os

import requests
import yaml

class baseApi:
	
	def __init__(self):
		self.token = self.get_userinfo()["token"]
		self.id = str(self.get_userinfo()["id"])
		self.schoolId = str(self.get_userinfo()["schoolId"])
		self.schoolName=self.get_userinfo()["schoolName"]
		
	def send(self,data):
		return requests.request(**data).json()
		
	def set_url(self):
		if os.path.exists("../config/env.yaml"):
			self.env =yaml.safe_load(open("../config/env.yaml"))
			url=self.env["ksedu"][self.env["default"]]
		return url
	
		
	def userinfo(self):
		data=yaml.safe_load(open("../config/login.yaml"))
		print(self.send(data))
		return self.send(data)
	
	def write_userinfo(self):
		self.token = self.userinfo()["data"]["token"]
		self.schoolId = self.userinfo()["data"]["schoolId"]
		self.id = self.userinfo()["data"]["id"]
		self.schoolName=self.userinfo()["data"]["schoolName"]
		
		data = {
			"token": self.token,
			"schoolId": self.schoolId,
			"id": self.id,
			"schoolName":self.schoolName
			
		}
		allow_unicode = True
		with open("../config/userinfo.yaml", "w",encoding="utf-8") as f:
			yaml.safe_dump(data=data, stream=f,allow_unicode = True)
			
	def get_userinfo(self):
		if os.path.exists("../config/userinfo.yaml"):
			with open("../config/userinfo.yaml", "r",encoding="utf-8") as f:
				data = yaml.load(f,Loader=yaml.FullLoader)
		else:
			self.write_userinfo()
			with open("../config/userinfo.yaml", "r",encoding="utf-8") as f:
				data = yaml.load(f,Loader=yaml.FullLoader)
		return data
	
	def getKeys(self, data):
		keysAll_list = []
		
		def getkeys(data):
			if (type(data)) == type({}):
				keys = data.keys()
				for key in keys:
					value = data.get(key)
					if (type(value) != type({}) and type(value) != type([])):
						keysAll_list.append(key)
					elif (type(value) == type({})):
						keysAll_list.append(key)
						getkeys(value)
					elif (type(value) == type([])):
						keysAll_list.append(key)
						for para in value:
							if (type(para) == type({}) or type(para) == type([])):
								getkeys(para)
							else:
								keysAll_list.append(para)
		getkeys(data)
		return keysAll_list
	
	def isExtend(self,data,tagkey):
		if (type(data)!=type({})):
			print("please input a json")
		else:
			key_list=self.getKeys(data)
			for key in key_list:
				if(key==tagkey):
					return True
		return False
	
	def get_key_value(self,data,keyword):
		if isinstance(data,dict):
			for key,value in data.items():
				print(key+":"+value)
				print(key(keyword))

	
if __name__ == '__main__':
	baseApi()