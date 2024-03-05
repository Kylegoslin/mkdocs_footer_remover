import os



def list_files(directory_path):
    files = []
    for file_name in os.listdir(directory_path):
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            files.append(file_path)
        elif os.path.isdir(file_path):
            files.extend(list_files(file_path))
    return files


# folder where your site lives
directory_path = "site"
all_files = list_files(directory_path)
for file_path in all_files:
    print(file_path)
    x = file_path
    if ".html" in x:
        print(x)
        with open(x, "r") as f:
            lines = f.readlines()
        with open(x, "w") as f:
            for line in lines:
                if not "Built with " in line.strip("\n"):
                    f.write(line)


print("finished")
