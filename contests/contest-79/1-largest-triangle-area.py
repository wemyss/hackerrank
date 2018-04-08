class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        p_len = len(points)
        maxArea = 0
        for a_i in range(0, p_len - 2):
            a = points[a_i]
            for b_i in range(a_i + 1, p_len - 1):
                b = points[b_i]
                for c_i in range(b_i + 1, p_len):
                    c = points[c_i]

                    # https://www.mathopenref.com/coordtrianglearea.html
                    area = abs(
                        (
                            a[0] * (b[1] - c[1]) +
                            b[0] * (c[1] - a[1]) +
                            c[0] * (a[1] - b[1])
                        ) / 2
                    )
                    maxArea = max(maxArea, area)

        return maxArea
