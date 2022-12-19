class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, name, child_type, attribute):
        # Attribute will be either a reference to a new directory, or the filesize if it's a file
        if child_type == 'dir':
            self.children.append([name, 'dir', attribute])
        else:
            self.children.append([name, 'file', attribute])

    def get_size(self):
        total_size = 0
        for child in self.children:
            if child[1] == 'file':
                total_size += int(child[2])
            else:
                total_size += child[2].get_size()
        return int(total_size)


directories = {}
navigation = []

with open("input.txt", "r") as f:
    for x in f:
        command = x.strip().split(' ')
        print(command)
        if command[0] == '$' and command[1] == 'cd':
            if command[2] == '..':
                navigation.pop()
                print("We moved back to", navigation[-1])
            else:
                if command[2] == '/':
                    print("Creating root and moving there")
                    navigation.append("root")
                    directories["root"] = (Directory("root", ''))
                else:
                    fullPath = navigation[-1] + "/" + command[2]
                    navigation.append(fullPath)
                print("We moved to folder", navigation[-1])
        elif command[0] == '$' and command[1] == 'ls':
            print("We are printing the contents of", navigation[-1])
        elif command[0] != '$':
            parent_dir = directories[navigation[-1]]
            if command[0] == 'dir':
                name = fullPath = navigation[-1] + "/" + command[1]
                print("Creating directory", name, "under", navigation[-1])
                directories[name] = (Directory(name, parent_dir))
                parent_dir.add_child(name, 'dir', directories[name])
            else:
                print("Adding file", command[1], "with size", command[0], "under", navigation[-1])
                parent_dir.add_child(command[1], 'file', command[0])

directory_sum = 0
for name, directory in directories.items():
    dir_size = directory.get_size()
    if dir_size < 100000:
        directory_sum += dir_size

print(directory_sum)



# root = Directory('/', None)
# root.add_child('a', 'file', 25)
# root.add_child('b', 'file', 15)
# c = Directory('c', root)
# root.add_child('c', 'dir', c)
# c.add_child('d', 'file', 10)
# c.add_child('e', 'file', 20)
# print(root.get_size())



