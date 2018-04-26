# -*- coding: UTF-8 -*-
import pandas
import numpy
import array

a = array.array("u")
strs = "1,2,3,4,5,6"
strlist = strs.split(",")
# a.fromlist(strlist)
#df = pandas.DataFrame(numpy.random.randn(2, 3), columns=['a', 'b', 'c'])
#增加一列d
#df['d'] = pandas.Series(numpy.random.randn(len(df['a'])), index=df.index)
#增加一行2
#df.ix[2] = pandas.Series(numpy.random.rand(4), index=df.columns)


def process_one_line(one_line):
    split_str = []
    option_part = ""
    main_part = ""
    split_str = one_line.split("[", 1)
    if len(split_str) == 2:
        option_part = split_str[1]
    main_part = split_str[0]
    process_main_part(main_part)
    process_option_part(option_part)


def process_option_part(one_line_option_part):
    return


def process_main_part(one_line_main_part):
    split_str = []
    secondary_list = []
    tertiary_list = []
    split_str = one_line_main_part.split(";")
    primary_str_list = ';'.join(split_str[0:323])
    cell_id_str = split_str[40]
    if split_str[172] != "":
        number_secondary = int(split_str[172])
    else:
        number_secondary = 0
    point = 324
    if split_str[323] == "|":
        return primary_str_list, secondary_list, tertiary_list
    i = 1
    while i <= number_secondary:
        i = i+1
        one_secondary = (split_str[point:point+49])
        one_secondary.insert(0, cell_id_str)
        secondary_list.append(';'.join(one_secondary))
        point = point+50
    if split_str[point-1] != "|":
        while point < len(split_str):
            one_tertiary = split_str[point:point+42]
            one_tertiary.insert(0, cell_id_str)
            tertiary_list.append(';'.join(one_tertiary))
            point = point+43
    return primary_str_list, secondary_list, tertiary_list


if __name__ == '__main__':
    file_object = open('e:\\test.pcmd')
    lines = file_object.readlines()
    num_line = 1
    for one_line in lines:
        process_one_line(one_line)
        num_line = num_line + 1
        print (num_line)
