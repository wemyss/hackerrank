import unittest


# Write a program to find the angle between hands on a clock.
def clockAngle(hour, minute):
	m_angle = minute * 6
	h_angle = hour * 30 + (30 * minute / 60)

	angle = abs(h_angle - m_angle)
	angle = min(360 - angle, angle)

	return angle


class TestStringMethods(unittest.TestCase):
	def test_12_00(self):
		self.assertEqual(clockAngle(12, 00), 0)

	def test_11_59(self):
		self.assertEqual(clockAngle(11, 59), 5.5)


if __name__ == '__main__':
    unittest.main()
