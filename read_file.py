import pandas as pd
import polars as pl


class Task:
    def __init__(self, file_path, file_path1):
        self.df = None
        self.df1 = None
        self.file_path = file_path
        self.file_path1 = file_path1

    def readings(self):
        self.df = pd.read_csv(self.file_path)
        self.df1 = pl.read_parquet(self.file_path1)
        return self.df

    def writings(self):
        self.df1.write_parquet('C:/Users/nara1005/Documents/samples/sample2.parquet')
        self.df.to_csv('C:/Users/nara1005/Documents/samples/sample1.csv')
        return self.df1


def main():
    file_path = 'C:/Users/nara1005/Documents/samples/Tasks.csv'
    file_path1 = 'C:/Users/nara1005/Documents/samples/sample.parquet'
    assign_class = Task(file_path, file_path1)
    reads = assign_class.readings()
    writes = assign_class.writings()


if main() == "__name__":
    main()
