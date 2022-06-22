# Permittivitäts Messung

## Anforderungen

Ziel des Projektes:

Als Professor möchte ich Permittivitätsmessergebnisse miteinander vergleichen, um den optimalen Werkstoff auszuwählen.

### Veröffentlichen
Als Student möchte ich Permittivitätsmessergebnisse(CSV) in einer Datenbank speichern, um diese zu zu veröffentlichen.

Tasks:
* CSV einlesen
* Permittivitäts-Datenbank und Datenbankschema erstellen
* CSV in Permittivitäts-Datenbank ablegen

### Auswerten
Als Professor möchte ich Permittivitätsmessergebnisse miteinander vergleichen, um den optimalen Werkstoff auszuwählen.

#### Frequenz Vergleich: Eigenschaften der Werkstoffe auf einer Frequenz vergleichen
* Diagramm 1: Als Professor möchte ich die Frequenzverläufe aller Werkstoffe sehen, um ihre Permitivität zu vergleichen.
* Tabelle 1: Als Professor möchte ich die Messergebnisse aller Werkstoffe bei einer bestimmten Frequenz anzeigen, um diese zu vergleichen.
* Spalten-Filter: Als Professor möchte ich bestimmte Spalten ausblenden, damit ich eine bessere Übersicht habe.
* Frequenz-Filter: Als Professor möchte ich bestimmte Frequenzen auswählen, um Werkstoffe auf einer bestimmten Frequenz zu vergleichen.

### Werkstoffdetails: Eigenschaften eines Werkstoffes auf gemessenen Frequenzen vergleichen
* Tabelle 2: Als Professor möchte ich die Ergebnisse eines Werkstoffes in einer Tabelle anzeigen, um diese zu vergleichen.
* Spalten-Filter: Als Professor möchte ich bestimmte Spalten ausblenden, damit ich eine bessere Übersicht habe.
* Werkstoff-Auwahl: Als Professor möchte bereits gemessene Werkstoffe auswählen, um mir dessen Ergebnisse anzuzeigen.
* Diagramm 2: Als Professor möchte ich den Frequenzverlauf einer Messung sehen, um deren Verlauf zu analysieren.

## Implementierung

Datenbankschema
* Measurements/Mesungen (ID, Name,	Temperature [°C],	Humidity [%],	Material type,	Serial number, PDC output voltage (DC) [V],	FDS output voltage (AC) [V],	c0	Sample thickness [m])
* FDS RESULT/Messreihen (IDMessung(FK),	Frequency [Hz],	Tanδ	εr',	εr'',	|Z| [Ω],	Phase of Z [°],	|Y| [S],	Phase of Y [°],	Cp [F],	Rp [Ω],	c' [F],	c'' [F],	R [Ω],	X [Ω])
