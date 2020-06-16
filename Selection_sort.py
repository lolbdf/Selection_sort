import generat_random_list
import time


def selection_sort(list):
    for index in range(len(list)):
        minimum_index = index
        for i in range(minimum_index + 1, len(list)):
            if list[minimum_index].lower() > list[
                i].lower():  # min indexmuss größer sein als i in list dann wird true zurück gegeben
                minimum_index = i
        cache = list[index]
        list[index] = list[minimum_index]
        list[minimum_index] = cache

    return list


if __name__ == "__main__":
    # unsorted_list = ["Haus", "brot", "Brot", "haus", "boot", "Boot", "hund", "Hund"]
    unsorted_list = generat_random_list.create(9999)
    start = time.time()
    sortet_list = selection_sort(unsorted_list)
    end = time.time()
    dauer = end - start
    print(sortet_list)
    print(dauer)
    for i in range(len(sortet_list) - 1):
        assert sortet_list[i].lower() <= sortet_list[i + 1].lower()
