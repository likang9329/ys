from runner.runner_test import Runner

class Start:
    def run(self):
        Runner().runner()
        print('我成功了')
if __name__ == '__main__':
    Start().run()