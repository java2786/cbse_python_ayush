
# absolute path
# filename = '/Volumes/My Shared Files/shared/python/CBSE/batch/t7/abc.txt'

# relative path
filename = 't7/file_handling.txt'

with open(filename) as f_obj:
    content = f_obj.read()
    
print(content)