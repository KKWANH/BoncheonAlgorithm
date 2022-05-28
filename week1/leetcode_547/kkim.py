# leetcode [Number of Province] https://leetcode.com/problems/number-of-provinces/
# Depth First Search

from typing import List
# 주석 버전
# class	Solution:
# 	def findCircleNum(self, _map: List[List[int]]) -> int:
# 		_len = len(_map)
# 		_rst = 0
# 		_vst = set()
# 		print("~~~~~~~~~~~")
# 		print("len :", _len)
# 		print("~~~~~~~~~~~\n")
# 		for _idx in range(_len):
# 			print("--------------")
# 			print("idx :", _idx)
# 			if (_idx in _vst):
# 				print("skipped")
# 				print("--------------\n")
# 				continue
# 			_rst += 1
# 			_tmp = [_idx]
# 			_vst.add(_idx)
# 			print("rst :", _rst)
# 			print("vst :", _vst)
# 			print("tmp :", _tmp)
# 			while (_tmp):
# 				_cur = _tmp.pop()
# 				print("- in while")
# 				print("cur :", _cur)
# 				print("tmp :", _tmp)
# 				for _jdx in range(_len):
# 					print("- in for in while")
# 					print("jdx :", _jdx)
# 					print("vst :", _vst)
# 					print("map :", _map[_cur][_jdx], ": must be 1")
# 					if (_jdx not in _vst and _map[_cur][_jdx] == 1):
# 						print("- in if in for in while")
# 						_tmp.append(_jdx)
# 						_vst.add(_jdx)
# 						print("tmp :", _tmp)
# 						print("vst :", _vst)
# 						print("--------------\n")
# 		return _rst

class	Solution:
	def findCircleNum(self, _map: List[List[int]]) -> int:
		_len = len(_map)
		_rst = 0
		_vst = set()
		for _idx in range(_len):
			if (_idx in _vst):
				continue
			_rst += 1
			_tmp = [_idx]
			_vst.add(_idx)
			while (_tmp):
				_cur = _tmp.pop()
				for _jdx in range(_len):
					if (_jdx not in _vst and _map[_cur][_jdx] == 1):
						_tmp.append(_jdx)
						_vst.add(_jdx)
		return _rst