import pyperclip
import xml.etree.ElementTree as ET

tree = ET.parse('E:\Sutter 30 Bed\XML\L2 Facilitated Model 03-04-19.xml')
root = tree.getroot()

clashtest_name = []
clashtest_total = []


for x in root.iter('clashtest'):
    clashtest_name.append(x.get('name'))

for x in root.iter('summary'):
    clashtest_total.append(int(x.get('active')))



clash_and_total = list(zip(clashtest_name,clashtest_total))

first_two_letters = []
for x in clashtest_name:
    a = x[0:][0:2]
    first_two_letters.append(a)


first_two_letters = list(set(first_two_letters))


el = []
pw = []
pt = []
pp = []
pl = []
hv = []
li = []
fp = []
fr = []

for x,y in clash_and_total:
    a = x[0:2]
    b = y
    if a == 'EL':
        el.append(b)
    elif a == 'PW':
        pw.append(b)
    elif a == 'PT':
        pt.append(b)
    elif a == 'PP':
        pp.append(b)
    elif a == 'PL':
        pl.append(b)
    elif a == 'HV':
        hv.append(b)
    elif a == 'LI':
        li.append(b)
    elif a == 'FP':
        fp.append(b)
    elif a == 'FR':
        fr.append(b)

clashtest_sum = sum(clashtest_total)

el = sum(el)/clashtest_sum
pw = sum(pw)/clashtest_sum
pt = sum(pt)/clashtest_sum
pp = sum(pp)/clashtest_sum
pl = sum(pl)/clashtest_sum
hv = sum(hv)/clashtest_sum
li = sum(li)/clashtest_sum
fp = sum(fp)/clashtest_sum
fr = sum(fr)/clashtest_sum



abv_clash_tuple = (('EL',el),('PW',pw),('PT',pt),('PP',pp),('PL',pl),('HV',hv),('LI',li),('FP',fp),('FR',fr))
sorted_values = sorted(abv_clash_tuple,key=lambda tup: tup[1], reverse = True)


def pipify (i):
    a = '|'.join(i)
    return(a)

def commafy (i):
    a = ','.join(i)
    return(a)


sorted_trades = []

for x in sorted_values:
    sorted_trades.append(x[0])

sorted_trades = pipify(sorted_trades)

# print(sorted_trades)

sorted_clashes = []

for x in sorted_values:
    a = str(x[1])
    sorted_clashes.append(a)



sorted_clashes = commafy(sorted_clashes)





image_charts = str(f"https://image-charts.com/chart?cht=p3&chs=700x200&chco=E625FF,00FFBA&chd=t:{sorted_clashes}&chdl={sorted_trades}")
print(image_charts)
pyperclip.copy(image_charts)






# #Replace & with v
#
# clashtest_name_v = []
#
# for x in clashtest_name:
#     a = x.replace('&','v')
#     clashtest_name_v.append(a)
#
#
# #Convert strings from xtree to ints
# clashtest_ints = []
#
# for x in clashtest_total:
#     a = int(x)
#     clashtest_ints.append(a)
#
#
# #Source dictionary
# my_dict = dict(list(zip(clashtest_name_v,clashtest_ints)))
#
#
# #Convert to tuples
# my_tuples = [(k, v) for k, v in my_dict.items()]
#
# #First sort the values from highest to lowest
#
# sorted_values = sorted(my_tuples,key=lambda tup: tup[1], reverse = True)
#
#
# #Find total value of tuple values
#
# test_values = []
#
# for x in sorted_values:
#     y = (x[1])
#     test_values.append(y)
#
# total_value = sum(test_values)
#
# #Find half of total tuples values
# half_value = (total_value/2)
#
# #Sum each int in series and check if sum is equal to or less than half
# #of the tests' value
#
# my_list = []
# my_tests = []
# k = 0
# while (sum(my_list) <= half_value):
#     my_list.append(sorted_values[k][1])
#     my_tests.append(sorted_values[k][0])
#     k = k + 1
#
# def createPrecents (i):
#     a = []
#     for x in i:
#         precent = str((x/total_value))
#         a.append(precent)
#     b = ','.join(a)
#     return(b)
#
# def remainder (i):
#     a = []
#     for x in i:
#         precent = (x/total_value)
#         a.append(precent)
#     b = (1-sum(a))
#     return(b)
#
# def pipify (i):
#     a = '|'.join(i)
#     return(a)
#
# def percentify (i):
#     l = []
#     # ints = int(i)
#     for x in i:
#         a = (x*100)
#         b = int(a)
#         c = l.append(b)
#     # d = '|'.join(c)
#     return(c)
#
# labels = percentify(my_list)
#
# top_test_precents = createPrecents(my_list)
# the_rest_precents = (remainder(my_list))
#
#
# my_tests_joined = '|'.join(my_tests)
#
# image_charts = str(f"https://image-charts.com/chart?cht=p3&chs=700x200&chco=FF0000,F2F2F2&chd=t:{top_test_precents},{the_rest_precents}&chdl={my_tests_joined}|Remainder")
# print(image_charts)
# pyperclip.copy(image_charts)
