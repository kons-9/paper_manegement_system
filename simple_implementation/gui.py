import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import toml

def reset_action():
    title.set("")
    url.set("")
    author.set("")
    motivation.delete("1.0","end")
    method.delete("1.0","end")
    insight.delete("1.0","end")
    contribution_summary.delete("1.0","end")


def make_action():
    ex = ".toml"
    try:
        try:
            dir_path = option_dir_name.get()
        except:
            dir_path = "toml/"

        filename = title.get()
        filename = filename.replace(' ', '_')
        path = dir_path + filename + ex
        with open(path, mode='w') as f:
            toml_dict = {}
            toml_dict["title"] = title.get()
            toml_dict["url"] = url.get()
            toml_dict["summarize_paper"] = {}
            toml_dict["summarize_paper"]["author"] = author.get()
            toml_dict["summarize_paper"]["motivation"] = motivation.get("1.0", 'end')
            toml_dict["summarize_paper"]["method"] = method.get("1.0", "end")
            toml_dict["summarize_paper"]["insight"] = insight.get("1.0", "end")
            toml_dict["summarize_paper"]["contribution_summary"] = contribution_summary.get("1.0", "end")
            toml.dump(toml_dict, f)

    except ValueError:
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.title("paper management")
    # root.geometry("620x1000+100+100")

    # main_frame = ttk.Frame(root,padding = "10 10 10 10")
    main_frame = ttk.Frame(root)
    main_frame.grid()

    ttk.Label(main_frame, text="title").grid()
    title = tk.StringVar()
    title_entry = ttk.Entry(main_frame,width=60, textvariable= title)
    title_entry.grid()

    ttk.Label(main_frame, text="url").grid()
    url = tk.StringVar()
    url_entry = ttk.Entry(main_frame,width=60, textvariable= url)
    url_entry.grid()

    ttk.Label(main_frame, text="author").grid()
    author = tk.StringVar()
    author_entry = ttk.Entry(main_frame, width=60,textvariable= author)
    author_entry.grid()

    ttk.Label(main_frame, text="motivation").grid()
    motivation = tk.Text(main_frame, width=60,height=10)
    motivation.grid()
    # motivation_entry = ttk.Entry(main_frame, textvariable= motivation)
    # motivation_entry.grid()

    ttk.Label(main_frame, text="method").grid()
    method = tk.Text(main_frame, width=60,height=10)
    method.grid()

    ttk.Label(main_frame, text="insight").grid()
    insight = tk.Text(main_frame, width=60,height=10)
    insight.grid()

    ttk.Label(main_frame, text="contribution_summary").grid()
    contribution_summary = tk.Text(main_frame, width=60, height=10)
    contribution_summary.grid()
    
    button_make = ttk.Button(main_frame, text = u"make", command=make_action)
    button_make.grid()

    button_reset = ttk.Button(main_frame, text = u"reest", command=reset_action)
    button_reset.grid()

    # ttk.Label(main_frame, text="dir_name").grid()
    option_dir_name = tk.StringVar()
    option_dir_name_entry = ttk.Entry(main_frame, width=60,textvariable= option_dir_name)
    option_dir_name_entry.grid()

    root.mainloop()
