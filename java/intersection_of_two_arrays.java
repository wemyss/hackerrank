// https://leetcode.com/problems/intersection-of-two-arrays-ii/description

class Solution {
	public int[] intersect(int[] nums1, int[] nums2) {
		Map<Integer, Integer> m = new HashMap<>();

		for (int num: nums1) {
			if (m.containsKey(num)) {
				m.put(num, m.get(num) + 1);
			} else {
				m.put(num, 1);
			}
		}

		List<Integer> l = new ArrayList<>();

		for (int num: nums2) {
			Integer val = m.get(num);
			if (val != null) {
				l.add(num);
				val--;
				if (val == 0) {
					m.remove(num);
				} else {
					m.put(num, val);
				}
			}
		}
		return l.stream().mapToInt(x -> x).toArray();
	}
}
