#Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. Example:

#('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def sort_by_3rd_char(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1][2])

result= sort_by_3rd_char([('abc', 'bcd'), ('abc', 'zza')])
print(result)