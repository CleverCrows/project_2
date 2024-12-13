from pet_rock_gui import *
#Imports GUI

def main() -> None:
    """
    Runs GUI. Sets title, geometry and disables resizing.
    :return: None
    """
    app = TkinterApp()
    app.title("Pet Rock Game")
    app.geometry("500x500")
    app.resizable(False, False)
    app.mainloop()
if __name__ == '__main__':
    main()
