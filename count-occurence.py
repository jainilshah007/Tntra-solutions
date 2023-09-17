def count_char(input_str, char_to_count):
    count = input_str.count(char_to_count)
    result_string = "Count of '" + char_to_count + "' in the string is: " + str(count)
    print(result_string)


input_str = input("Enter a string: ")
char_to_count = input("Enter the character to count: ")

count_char(input_str, char_to_count)