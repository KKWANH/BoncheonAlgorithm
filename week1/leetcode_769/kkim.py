# leetcode [Max Chunks To Make Sorted] https://leetcode.com/problems/max-chunks-to-make-sorted/
# 구현

from typing import List

class Solution:
	def maxChunksToSorted(self, _arr: List[int]) -> int:
		_rst = 0
		_max = 0
		for _nm1, _nm2 in enumerate(_arr):
			_max = max(_max, _nm2)
			if _max == _nm1:
				_rst += 1
		return	_rst

