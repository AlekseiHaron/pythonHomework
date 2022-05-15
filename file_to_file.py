import os
class FileToFile:

    def __init__(self):
        pass

    def copy_from_file(self):
        # File name
        file = 'first.txt'
        # File location
        location = "C:/Users/Oleksii_Kushnir/PycharmProjects/pythonHomework/"
        # Path
        path = os.path.join(location, file)
        print(path)
        with open(r'first.txt', 'r') as firstfile,\
                open(r'test.txt', 'a') as secondfile:

            # read content from first file
            for line in firstfile:

                # write content to second file
                try:
                    if line.istitle():
                        line
                    else:
                        line = line.upper().capitalize()
                finally:
                    line
                # join_words = ''.join(line)
                # print(join_words)
                # print(line.split("\n"))
                line = line.replace('\n', '')
                # line = ' '.join(line)
                print(line)
                # li = line.lower().capitalize()

                secondfile.write(f"\n{line}")
        secondfile.close()
        firstfile.close()
        try:
            os.remove(path)
            print("% s removed successfully" % path)
        except OSError as error:
            print(error)
            print("File path can not be removed")