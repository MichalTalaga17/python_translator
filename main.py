from tkinter import *
import googletrans  # biblioteka tłumaczeń
import textblob  # biblioteka pobrania tekstu
from tkinter import ttk, messagebox


# stworzenie okna
okno = Tk() # stworzenie okna
okno.title('Tłumacz')
ikona = PhotoImage(file="logo.png")
okno.iconphoto(False, ikona)
okno.geometry("880x300")


def tlumacz():
	# wyczyszczenie drugiego pola
	po_tlumaczeniu.delete(1.0, END)

	try:
		# pobranie języka z pierwszego pola
		for key, value in jezyki.items():
			if (value == wybor1.get()):
				kod_jezyka1 = key

		# pobranie języka z drugiego pola
		for key, value in jezyki.items():
			if (value == wybor2.get()):
				kod_jezyka2 = key

		# przetłumaczenie
		tekst = textblob.TextBlob(do_tlumaczenia.get(1.0, END))
		tekst = tekst.translate(from_lang=kod_jezyka1, to=kod_jezyka2)
		po_tlumaczeniu.insert(1.0, tekst)

	except Exception as e:
		# błędy
		messagebox.showerror("Błąd", e)


# pobranie listy języków
jezyki = googletrans.LANGUAGES
lista_jez = list(jezyki.values())


# stworzenie elementów
do_tlumaczenia = Text(okno, height=10, width=40)
przycisk = Button(okno, text="Translate!", font=("Helvetica", 24), command=tlumacz)
po_tlumaczeniu = Text(okno, height=10, width=40)
wybor1 = ttk.Combobox(okno, width=50, value=lista_jez)
wybor2 = ttk.Combobox(okno, width=50, value=lista_jez)


# ułożenie elementów
do_tlumaczenia.grid(row=1, column=0, pady=20, padx=10)
po_tlumaczeniu.grid(row=1, column=2, pady=20, padx=10)
przycisk.grid(row=1, column=1, padx=10)
wybor1.grid(row=0, column=0, pady=20)
wybor2.grid(row=0, column=2, pady=20)

# domyślne języki
wybor1.current(73)
wybor2.current(21)

okno.mainloop()
