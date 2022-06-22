# Permittivitäts Messung

## Anforderungen

Als X kann ich y damit Nutzen z erziele. 


* Einlesen von x CSV Messungen
* CSV Messungen in Datenbank ablegen
* Datenbankschema
  * Measurements/Mesungen (ID, Name,	Temperature [°C],	Humidity [%],	Material type,	Serial number, PDC output voltage (DC) [V],	FDS output voltage (AC) [V],	c0	Sample thickness [m])
  * FDS RESULT/Messreihen (FK,	Frequency [Hz],	Tanδ	εr',	εr'',	|Z| [Ω],	Phase of Z [°],	|Y| [S],	Phase of Y [°],	Cp [F],	Rp [Ω],	c' [F],	c'' [F],	R [Ω],	X [Ω])

## Implementierungs steps

* Einlesen von x CSV Messreihen
