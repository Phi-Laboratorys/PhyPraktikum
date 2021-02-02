LaTeX-Template zum Erstellen einer Praktikumsauswertung
-------------------------------------------------------
(Wolfgang Sch�pf, Januar 2013)


Dieses Paket enth�lt folgende Dateien, die Ordnerstruktur sollte beibehalten werden:

readme.txt:      diese Datei

Auswertung.tex:  Masterdatei zum Erstellen der Arbeit, welche folgende Dateien einliest:

                 Grundlagen.tex: Kapitel 2 der Arbeit
                 Aufbau.tex:     Kapitel 3 der Arbeit
                 Diskussion.tex: Kapitel 4 der Arbeit

Auswertung.bib:  Bibliotheksdatei, welche die Literaturzitate enth�lt

Auswertung.bst:  Stildatei, welche den verwendeten Zitierstil definiert

titel.eps:       Bild f�r die Titelseite

Auswertung.ps:   Postscriptausgabe des fertigen Dokumentes

Auswertung.pdf:  PDF-Ausgabe des fertigen Dokumentes

bilder:          Unterordner, welche folgende im Dokument verwendete Bilder enth�lt:
                 Fuss_Kernspin.eps
                 MM_MagnetischesMoment.eps
                 MM_Permanentmagnet.eps

Die Ausgaben wurden durch folgende Befehlsfolgen erstellt:
latex Auswertung
bibtex Auswertung
latex Auswertung
latex Auswertung
dvips Auswertung bzw. dvipdfm Auswertung

EDIT 20.09.2018:

Befehlsfolgen (als schnelles �bersetzen) f�r aktuelste Version von texmaker auf Windows 10:
	latex
	latex
	bibtex
	latex
	dvips
	ps2pdf


-um pdfs als Bilder einzubinden ---> Struktur f�r schnelles �bersetzen:
	pdflatex
	pdflatex
	bibtex
	pdflatex