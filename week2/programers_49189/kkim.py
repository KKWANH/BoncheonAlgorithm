from collections import deque

def	solution(_num, _edges):
	# allocates
	_rst = 0
	_gph = [[] for _idx in range(_num + 1)]
	_vst = [0] * (_num + 1)

	# connect each nodes from graph
	for _nod1, _nod2 in _edges:
		_gph[_nod1].append(_nod2)
		_gph[_nod2].append(_nod1)

	# deque, visited setting
	_que = deque([1])
	_vst[1] = 1

	# BFS
	while _que:
		_tmp = _que.popleft()
		for _nxt in _gph[_tmp]:
			if	not _vst[_nxt]:
				_vst[_nxt] = _vst[_tmp] + 1
				_que.append(_nxt)
	
	# find the max distance
	_max = max(_vst)
	_cnt = _vst.count(_max)

	# return the result
	if _cnt > 0:
		return _cnt
	return 1
