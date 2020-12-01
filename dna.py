from tkinter import *
from tkinter import messagebox
import textwrap

#Tkinter window
window = Tk()
window.title('Got Protein?')
window.configure(background = "#171617")
window.geometry("500x500")

#Tkinter Questionare
var = StringVar()
label = Label(window, textvariable=var, bg='#171617', fg='#fdff8c',font='helvetica 30 bold')
var.set("INSERT DNA:")
label.pack()

#Tkinter textbox
dnaInput = Entry(window, width=50, bd=0)
dnaInput.pack()

#TKinter button
def click():
	inputText = dnaInput.get() 

	#flip into oppposite strand and switch T's into U's (turn into RNA)
	newText = inputText.replace('a', 'U').replace('t', 'A').replace('g', 'C').replace('c', 'G')
	
	#use Codon chart to turn each 3 pairs into an amino acid
	for x in newText:
		if x == "AUG":
			print("Methionine") #start codon
		elif x == 'GCU' or x == 'GCC' or x == 'GCA' or x == 'GCG':
			print("Alanine")
		elif x == 'CGU' or x == 'CGC' or x == 'CGA' or x == 'CGG' or x == 'AGA' or x == 'AGG':
			print("Arginine")
		elif x == 'AAU' or x == 'AAC':
			print("Asparagine")
		elif x == 'GAU' or x == 'GAC':
			print("Aspartate")
		elif x == 'UGU' or x == 'UGC':
			print("Cysteine")
		elif x == 'GAA' or x == 'GAG':
			print("Glutamate")
		elif x == 'CAA' or x == 'CAG':
			print("Glutamine")
		elif x == 'GGU' or x == 'GGC' or x == 'GGA' or x == 'GGG':
			print("Glycine")
		elif x == 'CAU' or x == 'CAC':
			print("Histidine")
		elif x == 'AUU' or x == 'AUC' or x == 'AUA':
			print("Isoleucine")
		elif x == 'UUA' or x == 'UUG' or x == 'CUU' or x == 'CUC' or x == 'CUA' or x == 'CUG':
			print("Leucine")
		elif x == 'AAA' or x == 'AAG':
			print("Lysine")
		elif x == 'UUU' or x == 'UUC':
			print("Phenylalanine")
		elif x == 'CCU' or x == 'CCC' or x == 'CCA' or x == 'CCG':
			print("Proline")
		elif x == 'UCU' or x == 'UCC' or x == 'UCA' or x == 'UCG' or x == 'AGU' or x == 'AGC':
			print("Serine")
		elif x == 'ACU' or x == 'ACC' or x == 'ACA' or x == 'ACG':
			print("Threonine")
		elif x == 'UGG':
			print("Tryptophan")
		elif x == 'UAU' or x == 'UAC':
			print("Tyrosine")
		elif x == "AUG":
			print("Valine")
		elif x == "UAA" or "UAG" or "UGA": #stop codon
	 		break

#cut the DNA data into multiples of 3
three = textwrap.wrap(newtext, 3)

#output the resulting amino acid sequence to user
aminoAcid = three
sequence =  " ".join(amino acid)
print("Amino Acid Sequence: " + sequence)

B = Button(window, text = "SUBMIT",command = click)
B.pack()

#end of program
window.mainloop()
