import tkinter
from spacetest import summary


def displayout():
    article_url = entry.get()
    try:
        content = summary(article_url)
    except ValueError:
        content = 'Malformed URL! Please enter an actual news article.'
    except TypeError:
        content = 'Sorry, this news website is not supported at this time.'
    finally:
        output.delete('1.0', tkinter.END)
        output.insert(tkinter.INSERT, content)


master = tkinter.Tk()
master.title("Article Summary Machine")

tkinter.Label(master, text="Article URL: ").grid(row=0)
entry = tkinter.Entry(master, width="107")
entry.grid(row=0, column=1)

entry.focus_set()

tkinter.Label(master, text="Summary: ").grid(row=1)

output = tkinter.Text(master)
output.grid(row=1, column=1)

tkinter.Button(master, text="Summarize!", command=displayout).grid(columnspan=2)

master.mainloop()
