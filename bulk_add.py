file_name = "rawlistnames.txt"
file_in_path = "c:/Users/kluo/Desktop/" + file_name
file_in = open(file_in_path, "rt")
file_out = open("c:/Users/kluo/Desktop/Bulk_Add_Commands.txt", "wt")
first_line = "ok begin pw=XYZ\n"
last_line = "ok end"
file_out.write(first_line)
for line in file_in:
    line_array = line.split(" ")
    if len(line_array[0]) > 21:
        if line_array[0][-1] == ".":
            continue
        else:
            list_name = line_array[0].rstrip("\n")
            quiet_command = "QUIET ADD " + list_name + " userId@host.com\n"
            file_out.write(quiet_command)
    elif line_array[-3] == "Full":
        list_name = line_array[-1].rstrip("\n")
        quiet_command = "QUIET ADD " + list_name + " userId@host.com\n"
        file_out.write(quiet_command)
    else:
        list_name = line_array[0].rstrip("\n")
        if list_name != "L-SOFT":
            quiet_command = "QUIET ADD " + list_name + " userId@host.com\n"
            file_out.write(quiet_command)

file_out.write(last_line)
file_in.close()
file_out.close()
