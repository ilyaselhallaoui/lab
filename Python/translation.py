menu = {"en": {"file": "File", "new": "New", "open": "Open", "save":
"Save", "save as": "Save as", "print preview": "Print Preview",
"print": "Print", "close": "Close", "exit": "Exit"},
"fr": {"file": "Fichier", "new": "Nouveau", "open": "Ouvrir",
"save": "Enregistrer", "save as": "Enregistrer sous",
"print preview": "Apercu avant impressioner", "print":
"Imprimer", "close": "Fermer", "exit": "Quitter"},
"de": {"file": "Datei", "new": "Neu", "open": "Öffnen",
"save": "Speichern", "save as": "Speichern unter",
"preview": "Druckansicht", "print": "Drucken", "close":
"Schließen", "exit": "Verlassen"},
"it": {"file": "File", "new": "Nuovo", "open": "Apri", "save":
"Salva", "save as": "Salva come", "print preview":
"Anteprima di stampa", "print": "Stampa", "close":
"Chiudi", "exit": "Esci"}}

language = input("Wich language? ")
current_dic = menu[language]
print(current_dic)
