import util
import os

if __name__ == "__main__":
    # Test max_kernel function
    nums = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    result = util.max_kernel(nums, k)
    print(result)  # Kết quả là [5, 5, 5, 5, 10, 12, 33, 33]
    print("Câu hỏi 1: ")
    assert util.max_kernel([3, 4, 5, 1, -44], 3) == [5, 5, 5]
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    print(util.max_kernel(num_list, k))

    # count character
    s = "hello world"
    result = util.character_count(s)
    # Kết quả là {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    print(result)
    print("Câu hỏi 2: ")
    assert util.character_count("Baby") == {'B': 1, 'a': 1, 'b': 1, 'y': 1}
    print(util.character_count("smiles"))

    # count word
    current_directory = os.getcwd()
    # Path to txt file
    file_path = os.path.join(current_directory, 'P1_data.txt')
    result = util.count_word(file_path)
    print(result)
    print("Câu hỏi 3: ")
    assert result['who'] == 3
    print(result['man'])

    # Sử dụng hàm
    source = "kitten"
    target = "sitting"
    distance = util.levenshtein_distance(source, target)
    print(
        f"Levenshtein distance between '{source}' and '{target}' is {distance}")
    print("Câu hỏi 4: ")
    assert util.levenshtein_distance('hi', 'hello') == 4
    print(util.levenshtein_distance('hola', 'hello'))

    print("Câu hỏi 5: ")
    N = 7
    assert util.check_the_number(N) == "False"
    N = 2
    results = util.check_the_number(N)
    print(results)

    print("Câu hỏi 6: ")
    my_list = [5, 2, 5, 0, 1]
    max = 1
    min = 0
    assert util.my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
    my_list = [10, 2, 5, 0, 1]
    max = 2
    min = 1
    print(util.my_function(max=max, min=min, data=my_list))

    print("Câu hỏi 7: ")
    my_list = [5, 2, 5, 0, 1]
    max = 1
    min = 0
    assert util.my_function(max=max, min=min, data=my_list) == [1, 1, 1, 0, 1]
    my_list = [10, 2, 5, 0, 1]
    max = 2
    min = 1
    print(util.my_function(max=max, min=min, data=my_list))

    print("Câu hỏi 8: ")
    my_list = [1, 22, 93, -100]
    assert util.my_function_min(my_list) == -100
    my_list = [1, 2, 3, -1]
    print(util.my_function_min(my_list))

    print("Câu hỏi 9: ")
    my_list = [1001, 9, 100, 0]
    assert util.my_function_max(my_list) == 1001
    my_list = [1, 9, 9, 0]
    print(util.my_function_max(my_list))

    print("Câu hỏi 10: ")
    my_list = [1, 3, 9, 4]
    assert util.my_function_compare(my_list, -1) == False
    my_list = [1, 2, 3, 4]
    print(util.my_function_compare(my_list, 2))

    print("Câu hỏi 11: ")
    my_list = [4, 6, 8]
    assert util.my_function_average(my_list) == 6
    my_list = [1, 2, 3, 4]
    print(util.my_function_average())

    print("Câu hỏi 12: ")
    my_list = [3, 9, 4, 5]
    assert util.my_function_div3(my_list) == [3, 9]
    my_list = [1, 2, 3, 5, 6]
    print(util.my_function_div3(my_list))

    print("Câu hỏi 13: ")
    assert util.my_factorial(8) == 40320
    print(util.my_factorial(4))

    print("Câu hỏi 14: ")
    assert util.my_function_reverse('I can do it') == "ti od nac I"
    print(util.my_function_reverse('apricot'))

    print("Câu hỏi 15: ")
    data = [10, 0, -1, -1]
    assert util.my_function_helper(data) == ["T", "N", "N", "N"]
    data = [2, 3, 5, -1]
    print(util.my_function_helper(data))

    print("Câu hỏi 16: ")
    data = [10, 10, 9, 7, 7]
    assert util.my_function_helper_remove_duplicate(data) == [10, 9, 7]
    data = [9, 9, 8, 1, 1]
    print(util.my_function_helper_remove_duplicate(data))
