from driver.B_F5_1 import B_F5_1
from driver.B_F2_1 import B_F2_1
from helper.base import Dataframe

def main(feature, io, sheet, skiprows):
    test = None

    if feature == 'B-F5.1':
        test = B_F5_1()
    elif feature == "B-F2.1":
        test = B_F2_1()
    
    if test:
        DF = Dataframe()
        DF.read_excel(io=f'test-data/{io}', sheet_name=sheet, skiprows=skiprows)
        DF.print_df()
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