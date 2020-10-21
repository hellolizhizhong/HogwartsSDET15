#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest
import yaml
from pythononcode.calculator import Calculator

"""calcaulator类的测试类 ，测试add、sub、mul、div等方法"""


def get_datas(calc_func):
	with open('./datas/calc.yml', encoding='utf-8')as f:
		datas = yaml.safe_load(f)
		calc_datas = datas[calc_func]['datas']
		calc_ids = datas[calc_func]['ids']
		return [calc_datas, calc_ids]


def steps(path, calc,calc1,f1,f2, a, b, expect):
	with open(path, encoding='utf-8')as f:
		steps = yaml.safe_load(f)
	for step in steps:
		if f1 == step:
			result = calc(a, b)
		elif f2 == step:
			result = calc1(a, b)
			print(step)
		assert round(result, 2) == expect

class TestCalc:
	# setup_class 、 tearddown_class只在类中开始、结束运行一次
	def setup_class(self):
		self.calc = Calculator()
		print("【开始计算】")

	def teardown_class(self):
		print("【计算结束】")

	@pytest.mark.parametrize("a,b,expect", get_datas('add')[0],ids=get_datas('add')[1])
	def test_add(self, a, b, expect):
		steps('./steps/add_steps.yml',self.calc.add,self.calc.add_1,'add','add_1', a, b,expect)

	@pytest.mark.parametrize("a,b,expect",get_datas('sub')[0],ids=get_datas('sub')[1])
	def test_sub(self, a, b, expect):
		steps('./steps/sub_steps.yml',self.calc.sub,self.calc.sub_1,'sub', 'sub_1', a, b,expect)

	@pytest.mark.parametrize("a,b,expect",get_datas('mul')[0],ids=get_datas('mul')[1])
	def test_mul(self, a, b, expect):
		steps('./steps/mul_steps.yml',self.calc.mul,self.calc.mul_1,'mul', 'mul_1', a, b,expect)

	@pytest.mark.parametrize("a,b,expect",get_datas('div')[0],ids=get_datas('div')[1])
	def test_div(self, a, b, expect):
		steps('./steps/div_steps.yml',self.calc.div,self.calc.div_1,'div', 'div_1', a, b,expect)

	@pytest.mark.parametrize("a", [0, -10, 999999, 0.1])
	def test_div_zero(self, a):
		with pytest.raises(ZeroDivisionError):
			self.calc.div(a, 0)
