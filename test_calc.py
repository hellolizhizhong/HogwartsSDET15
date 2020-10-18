#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pytest
from pythononcode.calculator import Calculator

"""calcaulator类的测试类 ，测试add、sub、mul、div等方法"""


class TestCalc:
	# setup_class 、 tearddown_class只在类中开始、结束运行一次
	def setup_class(self):
		self.calc = Calculator()
		print("【开始计算】")

	def teardown_class(self):
		print("【计算结束】")

	@pytest.mark.parametrize("a,b,expect",
	                         [[1, 1, 2], [0.1, 0.9, 1], [1, 99, 100],
	                          [-1, 10, 9]])
	def test_add(self, a, b, expect):
		result = self.calc.add(a, b)
		assert result == expect

	@pytest.mark.parametrize("a,b,expect",
	                         [[1, 1, 0], [0.1, -1, 1.1], [100, 1, 99]])
	def test_sub(self, a, b, expect):
		result = self.calc.sub(a, b)
		assert result == expect

	@pytest.mark.parametrize("a,b,expect",
	                         [[1, 1, 1], [0.1, -1, -0.1], [3, 3.3456, 10.0368]])
	def test_mul(self, a, b, expect):
		result = self.calc.mul(a, b)
		assert result == expect

	@pytest.mark.parametrize("a,b,expect",
	                         [[1, 1, 1], [123456, 7891011, 0.02],
	                          [10.0368, 3, 3.35]])
	def test_div(self, a, b, expect):
		result = self.calc.div(a, b)
		assert round(result, 2) == expect

	@pytest.mark.parametrize("a", [0, -10, 999999, 0.1])
	def test_div_zero(self, a):
		with pytest.raises(ZeroDivisionError):
			self.calc.div(a, 0)
