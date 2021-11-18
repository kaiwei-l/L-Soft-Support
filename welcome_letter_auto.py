number_of_lists = int(input("Number of lists: "))
node_name = input("Node name(listserv.**.**): ")
node = input("Node(wa-**): ")
owner = input("Owner email (Separated by comma if more than 1): ")

support_email = "L-SOFT@" + node_name
bcc = "NEWLIST@SPIDER.EASE.LSOFT.COM"
subject = None

if number_of_lists == 1:
    name_of_list = input("Name of list: ")

    subject = "Welcome to LISTSERV! / " + name_of_list + " mailing list created on " + node_name

    file_in = open("Welcome_Message.txt", "rt")
    file_out = open("Welcome_Message_Delete_After_Use.txt", "wt")
    for line in file_in:
        if "[NAMEOFLIST]" in line:
            line = line.replace("[NAMEOFLIST]", name_of_list)
        if "[NODENAME]" in line:
            line = line.replace("[NODENAME]", node_name)
        if "[NODE]" in line:
            line = line.replace("[NODE]", node)
        file_out.write(line)

    file_in.close()
    file_out.close()
else:
    name_of_lists = input("Name of lists(Separated by comma, Limited 2): ")
    arr_of_lists = name_of_lists.split(",")
    name_of_list = arr_of_lists[0]
    name_of_list2 = arr_of_lists[1]

    subject = "Welcome to LISTSERV! / " + name_of_list + " and " + name_of_list2 + " mailing lists created on " + node_name

    file_in = open("Multi-List_Welcome_Message.txt", "rt")
    file_out = open("Multi-List_Welcome_Message_Delete_After_Use.txt", "wt")
    for line in file_in:
        if "[NAMEOFLIST]" in line:
            line = line.replace("[NAMEOFLIST]", name_of_list)
        if "[NAMEOFLIST2]" in line:
            line = line.replace("[NAMEOFLIST2]", name_of_list2)
        if "[NODENAME]" in line:
            line = line.replace("[NODENAME]", node_name)
        if "[NODE]" in line:
            line = line.replace("[NODE]", node)
        file_out.write(line)

    file_in.close()
    file_out.close()

print("========Email Header==========")
print("From: Ease-Support@lsoft.com")
print("To: " + owner)
print("Cc: " + support_email)
print("Bcc: " + bcc)
print("Subject: " + subject)
print("===============================")
