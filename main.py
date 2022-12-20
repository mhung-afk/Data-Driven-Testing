from driver.B_F5_1 import B_F5_1
from driver.B_F5_2 import B_F5_2
from driver.B_F5_3 import B_F5_3
from driver.B_F6 import B_F6
from driver.B_F2_1 import B_F2_1
from driver.A_F2 import A_F2
from helper.base import Dataframe

def main(feature, io, sheet, skiprows):
    test = None

    if feature == 'B-F5.1':
        test = B_F5_1()
    elif feature == 'B-F5.2':
        test = B_F5_2()
    elif feature == 'B-F5.3':
        test = B_F5_3()
    elif feature == 'B-F6':
        test = B_F6()
    elif feature == "B-F2.1":
        test = B_F2_1()
    elif feature == 'A-F2':
        test = A_F2()
    
    if test:
        DF = Dataframe()
        DF.read_excel(io=f'test-data/{io}', sheet_name=sheet, skiprows=skiprows)
        result = test.run(DF.storage[sheet])
        DF.write_result(result)
        return
    raise Exception('Something is wrong')

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--feature', metavar='path', required=True)
    parser.add_argument('--io', metavar='path', required=True)
    parser.add_argument('--sheet', metavar='path', required=True)
    parser.add_argument('--skiprows', metavar='path')

    [feature, io, sheet, skiprows] = [arg[1] for arg in parser.parse_args()._get_kwargs()]
    if not skiprows:
        skiprows = 0

    main(feature, io, sheet, int(skiprows))