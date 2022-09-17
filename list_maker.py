file = open("temp_list_in.txt", "r")

text = file.readlines()
file.close()
text2 = ""
for x in text:
    if x[-1] == '\n':
        x = x.replace (".\n", "\n") #This strips out the ending period if there is any
        text2 += ('"' + x[:-1] + '",\n')


print(text2)

file = open("temp_list_out.txt", "w")
for x in text2:
    file.write(x)

file.close()
