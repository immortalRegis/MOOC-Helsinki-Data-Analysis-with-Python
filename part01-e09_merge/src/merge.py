#!/usr/bin/env python3

def merge(L1, L2):
    sorted_list = []
    list1 = L1.copy()
    list2 = L2.copy()

    while list1 and list2:
        if list1[0] < list2[0]:
            sorted_list.append(list1.pop(0))
        else:
            sorted_list.append(list2.pop(0))
    sorted_list.extend(list1)
    sorted_list.extend(list2)
    return sorted_list


def main():
    pass

if __name__ == "__main__":
    main()
