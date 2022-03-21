import os
import time
import unittest

from base.html_test_runner import HTMLTestRunner


class Runner:
    def runner(self):
        '''收集并运行用例'''
        # 实例化 TestSuite 类，创建测试套件
        suite = unittest.TestSuite()
        # 添加测试用例到测试套件中
        if os.path.exists('cases'):
            dir = 'cases' #相对路径
        else:
            dir = '../cases'
        # 添加多个用例|开始加载TestLoader|怎么加载、在哪加载discover|有什么特征
        suite.addTests(unittest.TestLoader().discover(start_dir=dir,pattern='test*.py'))
        # 创建报告文件,b是二进制
        # 把时间戳转换成我们能看懂的时间。
        t = time.strftime('%Y-%m-%d_%H-%M-%S')
        if os.path.exists('results'):
            report_path = 'results/reports/test_report%s.html' % t
        else:
            report_path = '../results/reports/test_report%s.html' % t
        report_file = open(report_path,'wb')

        # 实例化HTMLTestRunner类，运行用例和把测试结果写入到报告文件
        htm_test_runner = HTMLTestRunner(stream=report_file,
                       title='达博威小程序自动化测试报告',
                       description='报告详细信息')
        # 运行用例
        htm_test_runner.run(suite)
        # 关闭报告文件，如果不关闭有可能会导致报告内容为空
        report_file.close()

if __name__ == '__main__':
    Runner().runner()