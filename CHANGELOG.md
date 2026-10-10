# Änderungen

## 1.27.0
- Garagentor: Torart Sektionaltor oder Rolltor (mit Rollkasten und Führungsschienen innen)
- Garagentor über Taster/Impuls steuerbar (Knopf, Schalter, Skript) – Klick aufs Tor öffnet „Tor auf / zu“, auf Wunsch mit Sicherheitsabfrage (zweimal tippen); Impulsdauer für Schalter einstellbar
- Torzustand ohne Cover aus Torkontakt (offen/zu) und optional Endlage „ganz offen“ – Tor wird offen, halb offen oder zu dargestellt
- Raum-Menü: Knöpfe und Skripte haben jetzt „Auslösen“

## 1.26.0
- Neu: Wandfarbe außen (Fassade) pro Raum einstellbar – getrennt von der Wandfarbe innen
- Neu: einzelne Wand (Raumkante) mit getrennter Farbe innen (Raumseite) und außen (andere Seite); „Farben dieser Wand zurücksetzen“
- Freie Wände: Farbe Seite 1 und Seite 2 getrennt
- Kein Flimmern mehr an Hausecken, wenn angrenzende Wände unterschiedliche Farben haben

## 1.25.0
- Neu: Raumbeschriftung (Name, Temperatur) frei verschieben – im Bearbeiten-Modus Raum wählen und den lila Punkt ziehen; „Beschriftung zurück in die Raummitte“
- Beim Verschieben des ganzen Raums wandert die Beschriftung mit
- Neu: Beschriftung/Symbol von Objekten versetzen (nach rechts, vorne, oben) – z. B. wenn Symbole übereinander liegen

## 1.24.0
- Neu: Lichtgruppen – bereits gesetzte Spots/Lampen zu einer Gruppe zusammenfassen: ein gemeinsamer Schalter, in der Ansicht nur ein Symbol (am mittleren Spot)
- Im Bearbeiten-Modus am Spot „Lichtgruppe“: neue Gruppe anlegen, Namen und Schalter festlegen, „Alle weiteren Einbaustrahler im Raum hinzufügen“, Gruppe auflösen
- Einzelne Einbaustrahler leuchten jetzt auch von oben sichtbar

## 1.23.0
- PV-Feld: „Leistung / Symbol an diesem Feld anzeigen" – bei mehreren Feldern am selben (parallel gemessenen) Sensor den Wert nur einmal anzeigen; Hinweis im Feld, wenn der Sensor mehrfach verknüpft ist
- PV-Leuchten wird bei gemeinsamem Sensor auf die kWp aller betroffenen Felder bezogen
- Neu: Solarthermie-Kollektor (Flachkollektor oder Vakuumröhren) fürs Dach – Kollektortemperatur färbt warm, Solarpumpe, Wärmeleistung, Speichertemperatur
- Neu: Windrad (3 Flügel horizontal, vertikal Helix oder Savonius) – dreht nach Leistung oder Windgeschwindigkeit, richtet sich nach der Windrichtung aus

## 1.22.0
- Neu: Wetter, Sonne und Mond außen (Einstellungen → „Wetter, Sonne & Mond")
- Sonne nach echtem Sonnenstand (Standort aus Home Assistant) mit Tagesbahn, Uhrzeiten und Himmelsrichtungen; Licht und Schatten folgen der Sonne
- Mond mit aktueller Phase, Sterne bei klarer Nacht; Himmel färbt sich nach Tageszeit (Dämmerung, Nacht) und Bewölkung
- Wolken, Regen, Starkregen, Schnee, Schneeregen, Hagel, Gewitter mit Blitzen, Nebel – aus einer Wetter-Entität, Wind treibt Regen und Wolken
- Schnee, Reif, Tau oder Nässe auf Dach, PV-Modulen, Carport, Terrassendach, Garten und Gelände (automatisch aus Wetter, Temperatur und Luftfeuchte oder fest wählbar; optional Sensor „Schnee liegt")
- Norden einstellbar; Vorschau mit simuliertem Wetter und Uhrzeit; Wetter-Anzeige unten rechts

## 1.21.0
- Neu: Geräte pro Raum ein- und ausblenden – im Raum-Menü über „☰ Auswahl" oder im Bearbeiten-Modus unter „Geräte im Raum-Menü"
- „alle einblenden / alle ausblenden" pro Raum; die Auswahl wird mit dem Plan gespeichert

## 1.20.0
- Neu: Spot-Feld (Licht) – beliebig viele Einbaustrahler als ein Objekt mit nur einem Symbol
- Matrix im Bearbeiten-Modus: einzelne Spots entfernen/einsetzen und bis zu 4 Gruppen zuordnen, jede Gruppe mit eigenem Licht
- Ein Klick schaltet das Feld; bei mehreren Gruppen öffnet sich die Liste der Gruppen
- Raum: Lampen-Symbole (Schalter) aller Lampen im Raum auf einmal aus- oder einblenden

## 1.19.0
- Neu: Mülltonne (Garten & Außenanlage) – Restmüll grau, Gelbe Tonne, Papier blau, Bio grün/braun oder eigene Farbe
- Abholtermin verknüpfbar (Sensor mit Tagen, Datum, Text wie „Morgen" oder Kalender) – Anzeige z. B. „So 11.10. (5 T.)", „Morgen", „Heute!"
- Tonne füllt sich mit der Zeit bis zur Abholung (Abholrhythmus einstellbar) oder nach Füllstand-Sensor; Füllstandsanzeige vorne, Deckel hebt sich wenn voll
- Deckel pulsiert am Tag vor und am Tag der Abholung (Vorlauf einstellbar)

## 1.18.2
- Neu: Dunstabzugshaube (Wandhaube, Kopffreihaube, Flachschirm, Inselhaube) mit Lüfter, Licht und Leistung
- Neu: Briefkasten (Standfuß, hängend, Paketbox) mit „Post da“-Anzeige

## 1.18.1
- PV-Feld bleibt auf dem Hauptdach, wenn es um eine Gaube herum gelegt wird (legt sich nur noch auf die Gaube, wenn es darauf passt); neu „Liegt auf: Automatisch / Hauptdach / Gaubendach“
- Gaube: Front lässt sich auch bei „Raumwand“ verkleiden (z. B. Schiefer); die Fenster der Raumwand bleiben ausgespart
- Dach: Unterkante der Giebelfläche in der Höhe einstellbar

## 1.18.0
- Dach: Giebel-/Firsthöhe direkt in Metern einstellbar (die Neigung ergibt sich daraus)
- PV-Module: Modulmaße frei einstellbar, Modulfarbe (Full Black, Schwarz mit Alurahmen, Blau, Dunkelblau) – auch bei PV an Wand/Zaun/Balkon
- Neu: Sat-Schüssel fürs Dach (auf Mast) und für die Wand, mit Durchmesser, Ausrichtung, Neigung und zweitem LNB

## 1.17.1
- Neu: Türklingel mit Kamera (Optik Ring, Reolink, Aqara G4 oder neutral) mit Kamerabild, Klingeltaste, Bewegung, Akku und Türöffner

## 1.17.0
- Schaltschrank: beliebig viele Geräte (Shelly, Sonoff, Aktoren, Sicherungen, FI …) mit eigener Zuordnung zu Licht, Schalter, Rollladen usw.; per Klick auf den Schrank schaltbar, Status-LED je Gerät, Sichtfenster/geschlossen/offen
- Neu: Tastatur, Maus mit Mauspad, Rollcontainer, Wandbild (Motive oder eigenes Bild)

## 1.16.1
- Dach: Klick auf einen hellen Punkt fügt wieder eine Ecke ein (zum Anpassen der Dachfläche); Regenrinnen und Fallrohre werden nur noch im Menü geschaltet
- Rinnen-/Fallrohr-Auswahl bleibt erhalten, wenn Dachecken eingefügt oder gelöscht werden

## 1.16.0
- Hang / schiefes Gelände: Höhen an den vier Hausseiten einstellbar; Rasen, Wege, Zäune und Gartenobjekte folgen dem Hang, Treppen nach unten können am Gelände enden
- Kühlschränke: Bauart (1 Tür, Kombi, Side-by-Side, French Door, Getränkekühler), Glasfront, Innenlicht, Eis-/Wasserspender, Display; smarte Werte (Soll-Temperaturen, Modus, zwei Türkontakte)
- Garten: Gartenstuhl, Glastisch mit Mittelpfosten, Gartenbank (auch Bierbank, Steinbank), Gasgrill / Kugelgrill / Außenküche, Feuerschale mit Dreibein
- Whirlpool (eckig, rund) und Pool (Stahlwand, Frame, eingelassen, aufblasbar) mit Steuerung: Temperatur, Filter, Blubber, Heizung, Licht, Abdeckung
- Säulen: Material (Beton, Stahl, Edelstahl, Holz), über mehrere Etagen
- Deckkraft für Terrassenüberdachung, Carport, Pavillon und PV-Modulfelder
- Klick-Menü steuert jetzt auch Zahlenwerte, Auswahllisten und Warmwasser-/Pool-Heizungen

## 1.15.0
- Dach bleibt in der Ansicht seiner eigenen Etage (z. B. Dachboden) als durchsichtige Hülle sichtbar – der Raum liegt sichtbar im Dach
- Fallrohre getrennt von den Regenrinnen abwählbar: insgesamt am Dach und je Dachkante
- Hintergrund der 3D-Ansicht: Farbe, Himmel-Verlauf oder eigenes Bild
- Neu im Außenbereich: Straße (Mittellinie, Gehwege, Parkstreifen) und Nachbarhaus (Geschosse, Dachform, Farben, auch halb durchsichtig)
- Neue Geräte: Kaffeemaschine (Vollautomat, Siebträger, Kapsel, Filter), Fritteuse / Heißluftfritteuse, Router / Modem (FRITZ!Box), Serverschrank groß und klein, NAS, Home Assistant auf Raspberry Pi im Argon-Gehäuse

## 1.14.0
- Wärmepumpe Innengerät: eigene Felder für Warmwasserspeicher, Pufferspeicher, Vorlauf und Rücklauf; alle Werte stehen am Gerät
- Knopf „Beschriftung“: Raumnamen, Raumwerte, Gerätewerte und Symbole einzeln oder alle ein-/ausblenden
- Je Raum und je Gerät: „Beschriftung in der Ansicht ausblenden“
- Sensor-Auswahl mit Suchfeld (bei langen Listen)

## 1.13.1
- Neu: Brandschutztür (Stahl, mit Türschließer und Kennzeichnung T30 / T30-RS / T90); Türblatt „Stahl (Brandschutz)“ und Türschließer auch an anderen Türen wählbar

## 1.13.0
- Wände enden jetzt unter jedem Dach an der Dachschräge – auch wenn das Dach über „Höhe über Wandkrone“ abgesenkt wurde und auch bei Wänden mit eigener Höhe
- Neu je Wand: „Ragt durchs Dach“ (Wand wird nicht gekürzt)
- Giebelflächen unter dem Dachrand in Fassadenfarbe statt Dachfarbe; abschaltbar und einfärbbar

## 1.12.1
- Neu: Eckschreibtisch (L-Form, Winkel links/rechts, Rollcontainer), Computer (Tower), Laptop, Drucker / Multifunktionsgerät (Status, Leistung, Toner)

## 1.12.0
- Betten: Bettart wählbar (Polster, Holz, Boxspring, Metall, Futon/Paletten, Etagenbett), Fußteil; neu Französisches Bett, Boxspringbett, Etagenbett
- Bad: Wand-WC mit Vorwandelement/Spülkasten, Duschrinne, bodengleiche Dusche mit Glaswand, Spiegelschrank, Wandspiegel
- Kleiderschrank: Spiegel an allen oder an bestimmten Türen
- Neue Kategorie Haustiere: Hundebett, Hundedecke, Napf, Kratzbaum, Aquarium/Terrarium
- Neue Kategorie Fahrzeuge: Limousine, SUV, Kombi, Kleinwagen, Transporter, Pickup, Cabrio, Anhänger (offen/Plane/Koffer), Wohnwagen, Motorrad, Roller, Fahrrad/E-Bike
- 3D-Drucker mit Druckstatus, Fortschritt, Düsentemperatur und Kamera
- Fernseher/Media Player: Ein/Aus, Wiedergabe, vor/zurück, Stumm, lauter/leiser, Quelle/App, Klangmodus

## 1.11.0
- Neu unter „Heizung & Klima“: Wärmepumpe Innengerät/Hydraulikmodul, Klima-Außengerät (Split, optional Wandkonsole), Warmwasserboiler (Wand), Durchlauferhitzer; Klima-Innengerät umbenannt
- Treppen: Deckkraft einstellbar, damit Türen dahinter sichtbar bleiben

## 1.10.1
- Treppen: Knopf „Seite schließen / Seite öffnen“ (Stufen, Podest und oberer Lauf als geschlossener Block bis zum Boden)

## 1.10.0
- Knopf „Haus“ ist immer sichtbar und führt zur Hauptübersicht (auch aus dem Bearbeiten-Modus)
- Bildliche Etagenübersicht (Hausschnitt mit Dach, Etagen, leuchtenden Fenstern bei Licht an, Hinweis auf offene Fenster) – Etage antippen zum Wechseln
- Darstellung wählbar: Automatisch, Desktop, Tablet quer, Tablet hochkant, Handy hochkant (wird je Gerät gemerkt)
- Hochkant: Kamera passt das Haus ins Bild, Navigation als Leiste unten

## 1.9.0
- Fensterbänke: Material innen/außen (Aluminium, Granit, Granit dunkel, Marmor, Naturstein, Holz, Kunststoff) mit Muster und eigener Farbe
- Treppe nach unten öffnet den Boden; Öffnungen entstehen auch, wenn die Treppe knapp an einer Wand liegt
- Bearbeiten: Treppen aus anderen Etagen, die auf der Etage ankommen, werden halbtransparent mit angezeigt
- Dach: „Dachboden als eigene Etage anlegen“ (Dach wird damit ein eigenes Stockwerk)
- „Farben zurücksetzen“ an jedem Objekt (Farben und Verglasung auf Standard)
- PV: Modulfeld legt sich auf Gaubendächer; Module einzeln belegen, zu Strings gruppieren, Strings Wechselrichter-Eingängen (MPPT) zuordnen, kWp je String/Eingang
- Plan-Vorlage im Bearbeiten-Modus ein-/ausblendbar (Knopf „Plan-Vorlage“)

## 1.8.0
- Gauben als Teil des Dachs: Dachseite anklicken → „Gaube auf dieser Seite“; Position, Breite, Wandhöhe, Abstand von der Außenwand einstellbar, am blauen Punkt verschiebbar
- In der Gaube laufen die Raumwände bis zur Gaubenhöhe hoch (Fenster wie gewohnt einsetzbar); alternativ Front mit Fenstern oder geschlossen
- Gaubendach: Schlepp-, Flach- oder Satteldach; Verkleidung Putz, Schiefer, Holz, Blech, Ziegel mit eigener Farbe
- Dachfläche wird im Bereich der Gaube ausgespart

## 1.7.3
- Türen (Haustür, Zimmertür): feste Glaselemente links, rechts und Oberlicht über die ganze Breite zum Anhaken; Breite, Höhe und Glasart einstellbar

## 1.7.2
- Neu im Katalog: „Festverglasung ohne Rollladen“ (Rollladen lässt sich weiterhin an jedem Fenster ein-/ausschalten)
- Farbe von Rollladenkasten und Rollladenpanzer einstellbar (Fenster, Türen, Schiebetür, einzelner Rollladen)

## 1.7.1
- Fix: Klick/Doppelklick auf die hellen Kantenpunkte funktioniert jetzt mehrmals hintereinander; alle Punkte des Raums bleiben sichtbar, wenn eine Wand gewählt ist

## 1.7.0
- Dach: Kniestock einstellbar (Dach setzt tiefer an, Wände enden unter der Dachschräge; Wände mit eigener Höhe bleiben stehen)
- Dachgaube: Front als Wand mit einzelnen Fenstern (Anzahl, Breite, Höhe, Brüstung)
- Raum-Grundriss: „Ecke einfügen“, „Aussparung (z. B. Treppe)“, „Erker“ im Wand-Menü; Doppelklick auf den hellen Punkt fügt eine Ecke ein
- Neu: Lichtschacht, Gelände (Hügel, Böschung, Aufschüttung)

## 1.6.2
- Beim Update zeigt das Panel „Version alt → neu“ an; Versionsnummer steht im Menü ⋮
- Icon (Ordner `brand`)

## 1.6.1
- Werkzeug „Etage verschieben“: ganze Etage mit der Maus ziehen, Ecken rasten an der Nachbar-Etage ein
- „Gesamtbreite der Etage“ skaliert eine zu groß/klein übernommene Etage

## 1.6.0
- Balkon (Geländer automatisch, optional Stützen), in der Etage darunter als Decke sichtbar
- Treppen: über Eck (L), Umdrehen, Spiegeln, Richtung nach unten (z. B. Terrasse → Garten)
- Etagen ausrichten (Umriss der Nachbar-Etage, „ausrichten“, Verschieben in Metern)
- Gelände-Höhe wählbar (Hanglage)

## 1.5.0
- Plan-Upload neu: Etage wählen/anlegen, Räume benennen, Ecken ziehen, Räume zeichnen, Maß abgreifen
- Erkennung ignoriert Schrift, farbige Pfeile, Maßketten und Maßstabsbalken

## 1.4.3
- HACS-Integration (flaches Repo), Regenrinnen je Kante, Ecken per Rechtsklick löschen
