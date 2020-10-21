#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""被测代码：计算器(+ - * /)"""
from numbers import Number


class Calculator:
	def add(self, a, b):
		if isinstance(a, Number) | isinstance(b, Number):
			return a + b;
		else:
			print("不支持非数字的输入")

	def sub(self, a, b):
		if isinstance(a, Number) | isinstance(b, Number):
			return a - b;
		else:
			print("不支持非数字的输入")

	def mul(self, a, b):
		if isinstance(a, Number) | isinstance(b, Number):
			return a * b;
		else:
			print("不支持非数字的输入")

	def div(self, a, b):
		if isinstance(a, Number) | isinstance(b, Number):
			return a / b;
		else:
			print("不支持非数字的输入")
