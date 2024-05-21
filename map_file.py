#python 3.7.1

class MapFile:
    def __init__(self, filename):
        self.filename = filename

class Drawer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def add_map_file(self, map_file):
        if len(self.stack) < self.capacity:
            self.stack.append(map_file)
            print(map_file.filename, "added to the drawer.")
        else:
            print("Drawer is full. Cannot add", map_file.filename)

    def remove_map_file(self):
        if self.stack:
            removed_file = self.stack.pop()
            print(removed_file.filename, "removed from the drawer.")
        else:
            print("Drawer is empty.")

def main():
    drawer = Drawer(5)  # Contoh kapasitas laci 5 file
    map_files = ["map" + str(i) + ".txt" for i in range(1, 8)]  # 7 file peta
    for filename in map_files:
        map_file = MapFile(filename)
        drawer.add_map_file(map_file)

    # Keluarkan beberapa file dari laci
    for _ in range(2):
        drawer.remove_map_file()

    # Tambahkan file baru ke laci
    new_map_file = MapFile("map8.txt")
    drawer.add_map_file(new_map_file)

if __name__ == "__main__":
    main()