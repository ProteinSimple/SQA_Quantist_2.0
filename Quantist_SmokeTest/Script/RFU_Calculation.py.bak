
from statistics import mean, pstdev


def LOQ(coeffs, kc_rfu_pairs):
    dict = KC_RFU_dict(coeffs, kc_rfu_pairs)
    passed, pf = calc_pass(dict)

    if not passed:   # no possible lloq or uloq indices
        return -1
    return pf


def KC_RFU_dict(coeffs, kc_rfu_pairs):
    pairs = kc_rfu_pairs
    d = {}
    for i in range(len(pairs)):
        KC = pairs[i][0]
        RFU = pairs[i][1]
        CC = calc_CC(coeffs, RFU)

        if CC == float('inf'):  # don't include value b/c it would affect pass/fail test
            continue

        if KC in d:
            d[KC].append(CC)
        else:
            d.update({KC: [CC]})
    return d


# find calculated concentrations
def calc_CC(coeffs, RFU):  # pairs = [KC, RFU]
    a = coeffs[0]
    b = coeffs[1]
    c = coeffs[2]
    d = coeffs[3]
    g = coeffs[4]

    if RFU <= a:
        RFU = a
    elif RFU >= d:
        # RFU = d
        return float('inf')  # return inf b/c RFU = d would cause division by 0

    return c * pow(pow(((a - d) / (RFU - d)), (1 / g)) - 1, (1/b))


# calculate whether each KC will pass the CV and recovery restrictions
def calc_pass(KC_dict):
    pf = {}  # pass/fail dictionary for KC values
    passed = False
    for KC in KC_dict:
        CCs = KC_dict.get(KC)
        CC_stdDev = pstdev(CCs)
        CC_mean = mean(CCs)
        CV = CC_stdDev / CC_mean * 100

        if KC != 0.0:
            recovery = int(CC_mean / KC * 100)
        else:
            recovery = 0  # set to 0 so it won't pass CV/recovery check

        if CV <= 20 and 80 <= recovery <= 120:
            pf.update({KC: "Pass"})
            passed = True
        else:
            pf.update({KC: "Fail"})
    return passed, pf


# read in data from Excel file and run code above to determine LLOQ and ULOQ
# prints Pass or Fail for all known concentration (kc) values
# For end cases for Pass or Fail, do a visual check (i.e. only one pass)
def main():
    import pandas as pd

    while True:
        try:
            print("Enter filename (format: file.xlsx): ")
            filename = input()
            file = pd.read_excel(filename, sheet_name='Sheet1')
            break
        except OSError:
            print("Could not find file")

    coeffs = []
    kc_rfu = []
    print("Expected LOQ values:")
    for i in file.index:
        if 8 <= i <= 12:
            coeffs += [file['Unnamed: 1'][i]]
        if 13 <= i <= 14:
            # prints LLOQ and ULOQ
            loq = str(file['Concentration Curve Data'][i])
            value = str(file['Unnamed: 1'][i])
            print(loq + ": " + value)
        if i >= 17:
            kc = file['Unnamed: 3'][i]
            rfu = file['Unnamed: 4'][i]
            kc_rfu += [[kc, rfu]]

    print("Calculated LOQ values: ")
    print(LOQ(coeffs, kc_rfu))
if __name__ == '__main__':
    print('LOQLimits v.1.0.0.0')
    main()


