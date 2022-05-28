from typing import List

class Solution:
	def wordBreak(self, _str: str, _dic: List[str]) -> bool:
		# dp 선언 파트. str의 length만큼 선언한 뒤 첫번째 원소를 true로 설정한다.
		_dp = [False for i in range(len(_str) + 1)]
		_dp[0] = True

		# dp의 길이만큼 반복문을 돌린다
		for _idx in range(len(_str) + 1):
			print("- idx ", _idx)
			for	_jdx in range(_idx):
				if	_dp[_idx] == False and _dp[_jdx] and _str[_jdx:_idx] in _dic:
					_dp[_idx] = True
					break
		
		return _dp[-1]

"""
[True, False, False, False, False, False, False, False, False, False, False, False, False, False]
- idx  0
- idx  1
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 1 ]=( a ) bool= False
- idx  2
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 2 ]=( ap ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 2 ]=( p ) bool= False
- idx  3
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 3 ]=( app ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 3 ]=( pp ) bool= False
- - jdx 2  :  dp[ 2 ]=( False ) str[ 2 : 3 ]=( p ) bool= False
- idx  4
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 4 ]=( appl ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 4 ]=( ppl ) bool= False
- - jdx 2  :  dp[ 2 ]=( False ) str[ 2 : 4 ]=( pl ) bool= False
- - jdx 3  :  dp[ 3 ]=( False ) str[ 3 : 4 ]=( l ) bool= False
- idx  5
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 5 ]=( apple ) bool= True
- idx  6
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 6 ]=( applep ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 6 ]=( pplep ) bool= False
- - jdx 2  :  dp[ 2 ]=( False ) str[ 2 : 6 ]=( plep ) bool= False
- - jdx 3  :  dp[ 3 ]=( False ) str[ 3 : 6 ]=( lep ) bool= False
- - jdx 4  :  dp[ 4 ]=( False ) str[ 4 : 6 ]=( ep ) bool= False
- - jdx 5  :  dp[ 5 ]=( True ) str[ 5 : 6 ]=( p ) bool= False
- idx  7
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 7 ]=( applepe ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 7 ]=( pplepe ) bool= False
- - jdx 2  :  dp[ 2 ]=( False ) str[ 2 : 7 ]=( plepe ) bool= False
- - jdx 3  :  dp[ 3 ]=( False ) str[ 3 : 7 ]=( lepe ) bool= False
- - jdx 4  :  dp[ 4 ]=( False ) str[ 4 : 7 ]=( epe ) bool= False
- - jdx 5  :  dp[ 5 ]=( True ) str[ 5 : 7 ]=( pe ) bool= False
- - jdx 6  :  dp[ 6 ]=( False ) str[ 6 : 7 ]=( e ) bool= False
- idx  8
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 8 ]=( applepen ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 8 ]=( pplepen ) bool= False
- - jdx 2  :  dp[ 2 ]=( False ) str[ 2 : 8 ]=( plepen ) bool= False
- - jdx 3  :  dp[ 3 ]=( False ) str[ 3 : 8 ]=( lepen ) bool= False
- - jdx 4  :  dp[ 4 ]=( False ) str[ 4 : 8 ]=( epen ) bool= False
- - jdx 5  :  dp[ 5 ]=( True ) str[ 5 : 8 ]=( pen ) bool= True
- idx  9
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 9 ]=( applepena ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 9 ]=( pplepena ) bool= False
- - jdx 2  :  dp[ 2 ]=( False ) str[ 2 : 9 ]=( plepena ) bool= False
- - jdx 3  :  dp[ 3 ]=( False ) str[ 3 : 9 ]=( lepena ) bool= False
- - jdx 4  :  dp[ 4 ]=( False ) str[ 4 : 9 ]=( epena ) bool= False
- - jdx 5  :  dp[ 5 ]=( True ) str[ 5 : 9 ]=( pena ) bool= False
- - jdx 6  :  dp[ 6 ]=( False ) str[ 6 : 9 ]=( ena ) bool= False
- - jdx 7  :  dp[ 7 ]=( False ) str[ 7 : 9 ]=( na ) bool= False
- - jdx 8  :  dp[ 8 ]=( True ) str[ 8 : 9 ]=( a ) bool= False
- idx  10
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 10 ]=( applepenap ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 10 ]=( pplepenap ) bool= False
- - jdx 2  :  dp[ 2 ]=( False ) str[ 2 : 10 ]=( plepenap ) bool= False
- - jdx 3  :  dp[ 3 ]=( False ) str[ 3 : 10 ]=( lepenap ) bool= False
- - jdx 4  :  dp[ 4 ]=( False ) str[ 4 : 10 ]=( epenap ) bool= False
- - jdx 5  :  dp[ 5 ]=( True ) str[ 5 : 10 ]=( penap ) bool= False
- - jdx 6  :  dp[ 6 ]=( False ) str[ 6 : 10 ]=( enap ) bool= False
- - jdx 7  :  dp[ 7 ]=( False ) str[ 7 : 10 ]=( nap ) bool= False
- - jdx 8  :  dp[ 8 ]=( True ) str[ 8 : 10 ]=( ap ) bool= False
- - jdx 9  :  dp[ 9 ]=( False ) str[ 9 : 10 ]=( p ) bool= False
- idx  11
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 11 ]=( applepenapp ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 11 ]=( pplepenapp ) bool= False
- - jdx 2  :  dp[ 2 ]=( False ) str[ 2 : 11 ]=( plepenapp ) bool= False
- - jdx 3  :  dp[ 3 ]=( False ) str[ 3 : 11 ]=( lepenapp ) bool= False
- - jdx 4  :  dp[ 4 ]=( False ) str[ 4 : 11 ]=( epenapp ) bool= False
- - jdx 5  :  dp[ 5 ]=( True ) str[ 5 : 11 ]=( penapp ) bool= False
- - jdx 6  :  dp[ 6 ]=( False ) str[ 6 : 11 ]=( enapp ) bool= False
- - jdx 7  :  dp[ 7 ]=( False ) str[ 7 : 11 ]=( napp ) bool= False
- - jdx 8  :  dp[ 8 ]=( True ) str[ 8 : 11 ]=( app ) bool= False
- - jdx 9  :  dp[ 9 ]=( False ) str[ 9 : 11 ]=( pp ) bool= False
- - jdx 10  :  dp[ 10 ]=( False ) str[ 10 : 11 ]=( p ) bool= False
- idx  12
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 12 ]=( applepenappl ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 12 ]=( pplepenappl ) bool= False
- - jdx 2  :  dp[ 2 ]=( False ) str[ 2 : 12 ]=( plepenappl ) bool= False
- - jdx 3  :  dp[ 3 ]=( False ) str[ 3 : 12 ]=( lepenappl ) bool= False
- - jdx 4  :  dp[ 4 ]=( False ) str[ 4 : 12 ]=( epenappl ) bool= False
- - jdx 5  :  dp[ 5 ]=( True ) str[ 5 : 12 ]=( penappl ) bool= False
- - jdx 6  :  dp[ 6 ]=( False ) str[ 6 : 12 ]=( enappl ) bool= False
- - jdx 7  :  dp[ 7 ]=( False ) str[ 7 : 12 ]=( nappl ) bool= False
- - jdx 8  :  dp[ 8 ]=( True ) str[ 8 : 12 ]=( appl ) bool= False
- - jdx 9  :  dp[ 9 ]=( False ) str[ 9 : 12 ]=( ppl ) bool= False
- - jdx 10  :  dp[ 10 ]=( False ) str[ 10 : 12 ]=( pl ) bool= False
- - jdx 11  :  dp[ 11 ]=( False ) str[ 11 : 12 ]=( l ) bool= False
- idx  13
- - jdx 0  :  dp[ 0 ]=( True ) str[ 0 : 13 ]=( applepenapple ) bool= False
- - jdx 1  :  dp[ 1 ]=( False ) str[ 1 : 13 ]=( pplepenapple ) bool= False
- - jdx 2  :  dp[ 2 ]=( False ) str[ 2 : 13 ]=( plepenapple ) bool= False
- - jdx 3  :  dp[ 3 ]=( False ) str[ 3 : 13 ]=( lepenapple ) bool= False
- - jdx 4  :  dp[ 4 ]=( False ) str[ 4 : 13 ]=( epenapple ) bool= False
- - jdx 5  :  dp[ 5 ]=( True ) str[ 5 : 13 ]=( penapple ) bool= False
- - jdx 6  :  dp[ 6 ]=( False ) str[ 6 : 13 ]=( enapple ) bool= False
- - jdx 7  :  dp[ 7 ]=( False ) str[ 7 : 13 ]=( napple ) bool= False
- - jdx 8  :  dp[ 8 ]=( True ) str[ 8 : 13 ]=( apple ) bool= True
"""

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        
        for indx in range(1, len(s) + 1):
            
            for word in wordDict:
                if dp[indx - len(word)] and s[:indx].endswith(word):
                    dp[indx] = True
            
        return dp[-1]
"""