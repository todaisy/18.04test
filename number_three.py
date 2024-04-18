def check_string_brackets(input_str):
    count1 = 0
    count2 = 0
    if input_str[0] == '(' or input_str[0] == ' ':
        for i in input_str:
            if i == '(':
                count1 += 1
            if i == ')':
                count2 += 1
        if count1 == count2:
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'


print(check_string_brackets('(()())'))
