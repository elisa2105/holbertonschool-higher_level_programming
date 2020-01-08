#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    resultList = []
    for i in range(list_length):
        try:
            resultList.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print('wrong type')
            resultList.append(0)
        except ZeroDivisionError:
            print('division by 0')
            resultList.append(0)
        except IndexError:
            print('out of range')
            resultList.append(0)
        finally:
            pass
    return resultList
