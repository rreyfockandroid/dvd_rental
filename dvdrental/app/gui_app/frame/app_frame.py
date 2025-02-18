import tkinter as tk
from repository.film_repository import FilmRepository
from model.gui_model import film_model
from frame.gui_frame import WidgetBox

class App:
    _widgets = []
    _id_film__to_update = None
    _filmRepository = FilmRepository()

    def __init__(self, window):
        self._window = window
        window.title("Example tkiner app")
        window.minsize(400, 400)
        window.maxsize(800, 800)

        self._top_frame = tk.Frame(window)

    def run(self):
        self._buildmenu()
        self._window.mainloop()
    
    def _buildmenu(self):
        menu = tk.Menu()
        self._window.config(menu=menu)

        filemenu = tk.Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=self._new_file_action)
        filemenu.add_command(label="Open...", command=self._open_file_action)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self._window.quit)

        helpmenu = tk.Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=self._about_action)

        dbmenu = tk.Menu(menu)
        menu.add_cascade(label="Dvd rental", menu=dbmenu)
        dbmenu.add_command(label="Film", command=self._find_film)

    def _find_film(self):
        self._drop_top_frame()
        
        frame_id = tk.Frame(master=self._top_frame)
        frame_id.grid(row=3)
        label = tk.Label(master=frame_id, text="Film id")
        label.grid(row=0, column=0)
        entry = tk.Entry(master=frame_id)
        entry.grid(row=0, column=1)
        self._find_film_id_entry = entry
       
        confirm = tk.Button(master=frame_id, text="search")
        confirm.bind("<Button-1>", self._handle_find_film)
        confirm.grid(row=1)  

        self._top_frame.pack()                                                                   
            
    def _handle_find_film(self, event):
        self._widgets = []
        film_id = self._find_film_id_entry.get()
        self._film_detail_frame(film_id)
        self._id_film__to_update = film_id

    def _film_detail_frame(self, film_id):
        self._drop_top_frame()

        frame_info = tk.Frame(master=self._top_frame, width=100, borderwidth=2, relief="groove")
        frame_info.grid(row=0, column=0)
        result_label = tk.Label(master=frame_info, width=100, text="Film details", bg="gray", fg="black")
        result_label.grid(row=0)


        frame_form = tk.Frame(master=self._top_frame)
        frame_form.grid(row=1, column=0)

        ridx = 0
        film = self._filmRepository.getFilm(film_id)
        for key in film_model:
            model = film_model[key]
            label = tk.Label(master=frame_form, text=model.name)
            label.grid(row=ridx, column=0, sticky="e")
            tx = tk.StringVar()
            tx.set(film[model.name])
            entry = tk.Entry(master=frame_form, width=model.width, textvariable=tx)
            entry.grid(row=ridx, column=1, sticky="w")
            self._widgets.append(WidgetBox(model, label, entry))
            ridx += 1
        
        confirm = tk.Button(master=frame_form, text="update")
        confirm.bind("<Button-1>", self._handle_update_film)
        confirm.grid(row=ridx, sticky="w")

        self._top_frame.pack()

    def _handle_update_film(self, event):
        son = []
        validate = True
        for idx, widget in enumerate(self._widgets):
            if not widget.validate():
                validate = False
                break
            son.append((widget.getName(), widget.getValue()))

        self._widgets = []
        status = ""
        if validate:
            status = "update "
            if self._filmRepository.updateFilm(self._id_film__to_update, son):
                status += " success"
            else:
                status += " failure"
        else:
            status = " invalid data"
        
        self._drop_top_frame()
        label = tk.Label(master=self._top_frame, text="Operation status: " + status)
        label.grid(row=0)
        self._top_frame.pack()

    def _add_label1(self, text):
        self._drop_top_frame()
        label = tk.Label(self._top_frame, text=text)
        label.pack()
        self._top_frame.pack()

    def _drop_top_frame(self):
        self._top_frame.destroy()
        self._top_frame = tk.Frame(self._window)

    def _new_file_action(self):
        self._drop_top_frame()
        self._add_label1("New file action")

    def _open_file_action(self):
        self._drop_top_frame()
        self._add_label1("Open file action")

    def _about_action(self):
        self._drop_top_frame()
        text = tk.Text(self._top_frame)
        text.pack(expand=True, fill='both')
        text.insert(tk.END, "This is a simple text editor")
        text.configure(state='disabled')
        self._top_frame.pack()