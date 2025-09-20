def read_file(filename):
    try:
        with open(filename, "r") as f:
            print("Reading file content: ")
            lines = f.readlines()

            for i in range(len(lines)):
                print(f"Line {i+1}: {lines[i].strip()}")

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")

read_file("sample.txt")
