data = {
    46: {'Front': None, 'Back': '48,49', 'Context': '46wagawg', 'Author': '<CustomUser: asdasd>'},
    47: {'Front': None, 'Back': None, 'Context': '47awegweag', 'Author': '<CustomUser: asdasd>'},
    48: {'Front': '46', 'Back': None, 'Context': '48awegwage', 'Author': '<CustomUser: asdasd>'},
    49: {'Front': '46', 'Back': '50', 'Context': '49awegaweg', 'Author': '<CustomUser: asdasd>'},
    50: {'Front': '49', 'Back': None, 'Context': '50ㅁㅈㅎㅁㅈㄷㅎ', 'Author': '<CustomUser: asdasd>'}
}



# def print_structure(key, data, is_dict=False, depth=0):
#     result = ""
#     if data[key]['Back'] is not None:
#         result += "{" +f"{key}:Context:{value['Context'],}"
#         back_values = data[key]['Back'].split(',')
#         if len(back_values) == 1:
#             result += print_structure(int(back_values[0]), data, False, depth + 1)
#         else:
#             if is_dict:
#                 result += "{"
#             for idx, back in enumerate(back_values):
                
#                 result += print_structure(int(back), data, True, depth)
#                 if idx < len(back_values) - 1:
#                     result += f"Context:{value['Context']}, "
#             if is_dict:
#                 result += "}"
#     else:
#         result += "{"+f"{key}:Context:{value['Context']}"+"}"
#     result += "}"
#     return result


# final_result = ""
# for key, value in data.items():
#     if value['Front'] is None:
#         final_result += print_structure(key, data, True)

# print(final_result)


# data = {
#     46: {'Front': None, 'Back': '48,49', 'Context': '46wagawg', 'Author': '<CustomUser: asdasd>'},
#     47: {'Front': None, 'Back': None, 'Context': '47awegweag', 'Author': '<CustomUser: asdasd>'},
#     48: {'Front': '46', 'Back': None, 'Context': '48awegwage', 'Author': '<CustomUser: asdasd>'},
#     49: {'Front': '46', 'Back': '50', 'Context': '49awegaweg', 'Author': '<CustomUser: asdasd>'},
#     50: {'Front': '49', 'Back': None, 'Context': '50ㅁㅈㅎㅁㅈㄷㅎ', 'Author': '<CustomUser: asdasd>'}
# }

def extract_author_name(author):
    author_string =str(author)
    author_string = author_string.replace(" ", "")
    return author_string.replace(" ", "")



def print_structure(key, data):
    node = {
        "id": key,
        "Context": data[key]['Context'],
        "Author":extract_author_name( data[key]['Author']),
        "replies": []
    }
    if data[key]['Back'] is not None:
        print(key)
        back_values = data[key]['Back'].split(',')
        for back in back_values:
            node["replies"].append(print_structure(int(back), data))
    return node

final_result = [print_structure(key, data) for key, value in data.items() if value['Front'] is None]
print(final_result)


for comment in final_result:
    print(f"Replies for comment with id {comment['id']}:")
    for reply in comment['replies']:
        print(reply)
    print('\n')

