def min_in_shifted_lst(lst):
    '''
    Function -- min_in_shifted_lst
        Find min in a shifted list
    Parameter:
        lst -- a sorted list but has some unkonwn number shifted
    Returns:
        Minimum of the list.
    '''
    mid = len(lst) // 2
    if len(lst) == 1:
        return lst[0]
    else:
        if lst[mid] < lst[mid + 1]:
            return min_in_shifted_lst(list)
            
        min_value = lst[0]
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                min_value = lst[i + 1]
                break
        return min_value



def main():
    # lst = [1,4,5,6,9,10,55]
    # lst = [9,10,55,0, 1,4,5,6]
    # lst = [9,10,55,120,0, 1,4,5,6]
    # lst = [18, 25, 38, 1, 12, 13]
    # lst = [2, 1]
    # lst = [1]
    lst = []
    print(min_in_shifted_lst(lst))


main()
