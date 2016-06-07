import luigi
import datetime as dt


class MyTask(luigi.Task):

    today = luigi.DateParameter(default=dt.date.today())

    def requires(self):
        return []

    def output(self):
        f_path = 'date_%s.txt' % str(self.today)
        return luigi.LocalTarget(path=f_path)

    def run(self):
        f = self.output().open('w')
        f.write(str(self.today) + '\n')
        f.write("This is a file.")
        f.close()

class PrintDate(luigi.Task):
    today = MyTask.today

    def requires(self):
        return MyTask()

    def run(self):
        f_path = 'date_%s.txt' % str(self.today)
        print f_path
        f = open(f_path, 'r')
        for line in f:
            print line
        f.close()


if __name__ == '__main__':
    luigi.run(['PrintDate', '--local-scheduler'])
