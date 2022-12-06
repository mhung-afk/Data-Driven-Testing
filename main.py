from driver.B_F5_1 import B_F5_1
from helper.base import Dataframe

DF = Dataframe()
DF.read_excel(io='test-data/F5_F6_NF1.xlsx', sheet_name=['B-F5.1','B-F5.2','B-F5.3'], skiprows=1)
DF.read_excel(io='test-data/F5_F6_NF1.xlsx', sheet_name=['B-F6','B-NF1'], skiprows=None)
TEST_B_F5_1 = B_F5_1()

if __name__ == '__main__':
    DF.print_df()
    # TEST_B_F5_1.run()