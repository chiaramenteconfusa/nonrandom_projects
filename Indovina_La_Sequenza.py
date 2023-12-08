import random
from collections import Counter

def diff_colori():
    print("Scegli con quanti colori vuoi giocare:"
      "\n2 - Sei una pippa ma non ti giudico"
      "\n3 - Apprezzo l'impegno"
      "\n4 - Numero onesto dai"
      "\n5 - Ammettilo che vuoi solo scriverti i colori sui polpastrelli"
      "\n6 - Ti vuoi un po' male ma mi gusti"
      "\n7 - La situazione è complessa ma 7 è il numero perfetto"
      "\nA te la scelta: ")
    while True:
        num_colori = int(input())
        if num_colori > 7 or num_colori <= 1:
            print("\nDaaai sii partecipe"
                  "\nRiprova suvvia:\n")
        else:
            print("Perfetto\n")
            break
    return(num_colori)

def diff_lunghezza():
    print("Adesso dimmi quanto deve essere lunga la sequenza?\n")
    while True:
        lung_sequenza = int(input())
        if lung_sequenza == 0:
            print("Ahah sto ridendo -_-\n"
                  "riprova dai:")
        elif lung_sequenza >= 10:
            print("Vuoi che chiami uno psicologo?\n")
            risp = str(input())
            if risp.lower() == "si":
                print("\nSul sito di RomaTre trovi tutte le informazioni per lo sportello psicologico, baci <3")
                input("\nPremi INVIO per chiudere l'applicazione")
                quit()
            else:
                print("Bene allora dicevamo...\n")
        elif lung_sequenza == 1:
            print("\nMa così il gioco non è molto divertente :("
                  "\nVuoi comunque continuare con questo numero? Si/no\n")
            risp = str(input())
            if risp.lower() == "si":
                print("Come vuoi tu\n")
                break
            else:
                print("Menomale, allora riprova:\n")
        else:
            print("Gud :]\n")
            break
    return(lung_sequenza)

def scelta_disponibile(num_colori, opzioni):
    for i in range(num_colori):
        print("-", opzioni[i])
        nuove_opz.append(opzioni[i])
    return(nuove_opz)

def seq_generatore(opz, lung_seq, num_col):
    sequenza = []
    col_opz = opz[:num_col]
    for i in range(lung_seq):
        tributo = random.choice(col_opz)
        sequenza.append(tributo)
    return(sequenza, col_opz)

def ipotizzatore(lung_seq):
    ipo_seq = []
    for i in range(lung_seq):
        ipo_col = str(input())
        if ipo_col not in col_opz:
            print("ehddaje")
        else:
            ipo_seq.append(ipo_col)
    return(ipo_col, ipo_seq)

def giustamente(ipo_seq, sequenza):
    pos_giusta = 0
    j = 0
    for i in ipo_seq:
        m = 0
        for k in sequenza:
            if (ipo_seq[j] == sequenza[m]) and (j == m):
                pos_giusta += 1
                m += 1
            else:
                m += 1
        j += 1
    return pos_giusta

def sbagliatamente(ipo_seq, sequenza, pos_giusta):
    valori_incomune = Counter(ipo_seq) & Counter(sequenza)
    lista_incomune = list(valori_incomune.elements())
    pos_sbagliata = len(lista_incomune) - pos_giusta
    return pos_sbagliata

def sbagli(ipo_seq, sequenza, pos_giusta):
    in_comune = set(ipo_seq) & set(sequenza)
    pos_sbagliata = len(in_comune) - pos_giusta
    return pos_sbagliata

print("SalveSalvino pronto per il mio indovinellino?")
risp = str(input())
if risp.lower() == "si":
    print("\nMagico :]\n")
else:
    print("\nAspetterò")
    input("\nPremi INVIO per chiudere l'applicazione")
    quit()

opzioni = ('rosso', 'giallo', 'blu', 'verde', 'viola', 'bianco', 'arancione')

num_colori = diff_colori()
lung_sequenza = diff_lunghezza()
nuove_opz = []

print("\nBene ecco i colori tra cui scegliere:")
scelta_disponibile(num_colori, opzioni)

sequenza, col_opz = seq_generatore(opzioni, lung_sequenza, num_colori)

print("\nOra tocca a te, indicami un colore alla volta:")
while True:
    ipo_col, ipo_seq = ipotizzatore(lung_sequenza)
    if ipo_seq == sequenza:
        print("HAI INDOVINATO! O_O\nLe mie più sincere congratulazioni\nLa sequenza era davvero", ", ".join(sequenza))
        break
    else:
        pos_giusta = giustamente(ipo_seq, sequenza)
        pos_sbagliata = sbagliatamente(ipo_seq, sequenza, pos_giusta)
        print("Hai ", pos_giusta, " colori nella posizione giusta e ", pos_sbagliata, " nella posizione sbagliata\nRiprova:")

input("Premi INVIO per chiudere l'applicazione")