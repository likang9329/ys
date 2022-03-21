import unittest
from ddt import ddt, file_data

from pages.get_phone_code_page import Get_phone_code


class Get_phone_code_test(unittest.TestCase):

    def test_get_phone(self, **kwargs):
        res = Get_phone_code().get_phone_code().json()['msg']
        flag ='操作成功'
        self.assertEqual(res, flag, msg='失败')