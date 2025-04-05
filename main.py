class App:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Welcome to {self.name}!")

if __name__ == "__main__":
    app = App("My Python Project")
    app.run()
