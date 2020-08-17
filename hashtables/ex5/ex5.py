path_dict = {}

def finder(files, queries):
    global path_dict
    result = []

    for path in files:
        #find the file name in each path
        full_path = path
        path = path.split('/')
        file_name = path[-1]

        #if the file name already exists the the new path to the list
        if file_name in path_dict:
            path_dict[file_name].append(full_path)
        #other wise add a new entry to path_dict (file_name: [path])
        else:
            path_dict[file_name] = [full_path]

    #loop through the query array and add every path that has a file name that = the query
    for query in queries:
        if query in path_dict:
            for file_path in path_dict[query]:
                result.append(file_path)

    path_dict = {}
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
