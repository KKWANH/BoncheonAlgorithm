from typing import List

class Solution:
	def lastStoneWeight(self, _lst: List[int]) -> int:
		if len(_lst) == 0:
			return 0

		while (len(_lst) > 1):
			_lst.sort()
			_big, _sml = _lst[-1], _lst[-2]
			_big -= _sml
			_lst.pop(-1)
			_lst.pop(-1)
			if _big >= 1:
				_lst.append(_big)

		if len(_lst) == 1:
			return _lst[0]
		return 0

"""
while (len(_lst) > 1):
	_lst.sort()
	_big, _sml = _lst[-1], _lst[-2]
	_big -= _sml
	_lst.pop(-1)
	_lst.pop(-1)
	if _big == 1:
		_lst.append(_big)
	print(_lst)
"""