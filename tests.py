from unittest import TestCase
from septext import Septext


class SeptextTestCase(TestCase):
    def test_septext(self):
        septext = Septext("\t", text="serial\tnumber\n111\t12345\n222\t54321\n333\t67890\n444\t09876")

        line_list = septext.get_line_list()
        self.assertEqual(line_list[0], "111\t12345")
        self.assertEqual(line_list[3], "444\t09876")

        arry = septext.get_array()
        self.assertEqual(arry[1,1], "54321")
        self.assertEqual(arry[2,0], "333")
