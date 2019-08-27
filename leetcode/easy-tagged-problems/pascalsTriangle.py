from typing import List
import tkinter

from pip._vendor.webencodings.mklabels import generate


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        x = []
        for l in range(1, numRows + 1):
            Z = []
            x.append(Z)
            C = 1
            for i in range(1, l+1):
                Z.append(C)
                C = int(C * (l - i) / i)
        return x

