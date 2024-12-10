from tkinter import *
from tkinter import ttk, filedialog, messagebox
from functional import *


#root init
root = Tk()
root.title("R A L S")
root.geometry("310x100")

root["bg"] = "#393f45"

#basic functions
def ask_for_path():
    filedial = filedialog.askdirectory()
    if change_path_to_rust(filedial):
        messagebox.showinfo("SUCCESS", "RUST PATH IS CORRECT")
        init_files()
        label_count.config(text=f"Total files: {len(list_of_files)}")
    else:
        messagebox.showerror("ERROR", "Please, select valid path")

def ask_for():
    filedial = filedialog.askopenfilenames(filetypes=[(f"To fill: {len(list_of_files)}", ".jpg")])
    if len(filedial) > 0:
        replace(filedial)
        messagebox.showinfo("SUCCESS", "Done")
    else:
        messagebox.showwarning("WARNING", "Error handler: select more then one file")

style = ttk.Style()
style.configure("TLabel", foreground="white", background="#393f45")
style.configure("TButton", foreground="black", background="#393f45")

#init ui elements
frame = Frame(root)
frame.config(bg="#393f45")
frame.pack()
btn_change_folder = ttk.Button(frame, text="CHANGE RUST PATH", command=ask_for_path, width=30, style="TButton")
label_count, label_subtitle = ttk.Label(frame, text="n/a", style="TLabel",width=50), ttk.Label(text="RustAutoLoadingScreen(b3) by Swetychek", style="TLabel")
btn_select = ttk.Button(text="Select files", command=ask_for, width=60, style="TButton")

def ui_pack():
    #pack ui elements
    btn_change_folder.pack(side=LEFT, pady=10, padx=15)
    label_count.pack(side=LEFT, padx=0)
    btn_select.pack(anchor=W, padx=15)
    label_subtitle.pack(anchor=W, padx=15, pady=5)


def initialisating_files():
    global label_count, path_to_rust
    #init all files
    if path_to_rust != "none":
        print("sadasdsad")
        init_files()
        label_count.config(text=f"Total files: {len(list_of_files)}")

if __name__ == "__main__":
    if not "config.ini" in os.listdir():
        config_file = open("config.ini", "w")
        config_file.write("[MAIN_CONFIG]\nrust_path = NONE\ndebug = none")
        config_file.close()
    init_functions()
    initialisating_files()
    ui_pack()

root.mainloop()