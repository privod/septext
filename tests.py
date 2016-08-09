from unittest import TestCase
from septext import Septext
import os

class SeptextTestCase(TestCase):
    def test_septext(self):
        text = "serial\tnumber\n111\t12345\n222\t54321\n333\t67890\n444\t09876"
        septext = Septext("\t", text=text)

        self.assertEqual(septext.count(), 4)

        line_list = septext.get_line_list()
        self.assertEqual(line_list[0], "111\t12345")
        self.assertEqual(line_list[3], "444\t09876")

        arry = septext.get_array()
        self.assertEqual(arry[1][1], "54321")
        self.assertEqual(arry[2][0], "333")

        temp_file_name = "tmp.txt"
        try:
            with open(temp_file_name, 'w') as file:
                file.write(text)
                file.close()

            septext = Septext("\t", temp_file_name)

            self.assertEqual(septext.count(), 4)

            self.assertEqual(septext.get_dict(2), {"serial": "333", "number": "67890"})
        finally:
            os.remove(temp_file_name)