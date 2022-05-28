# 입국심사: https://programmers.co.kr/learn/courses/30/lessons/43238
# 이진탐색

def	solution(_cnt, _tims):
	_rst = 0
	_lft = min(_tims)
	_rgt = max(_tims) * _cnt
	while (_lft <= _rgt):
		_mid = (_lft + _rgt) // 2
		_cur = 0
		for (_tim) in (_tims):
			_cur += _mid // _tim
			if	(_cur >= _cnt):
				break
		if	(_cur >= _cnt):
			_rst = _mid
			_rgt = _mid - 1
		elif(_cur < _cnt):
			_lft = _mid + 1
	return	_rst