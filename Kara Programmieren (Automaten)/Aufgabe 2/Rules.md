# Aufgabenbeschreibung: Verlorene Schlüssel sammeln

**Aufgabenstellung:**
Schreibe ein Programm für Kara, das alle Kleeblätter, die sich außen direkt an der Hauswand befinden, einsammelt und ins Haus bringt.

## Regeln
* Kara kann maximal ein Kleeblatt gleichzeitig tragen.
* Jedes Kleeblatt benötigt im Haus ein eigenes Feld (Kleeblätter dürfen nicht auf demselben Feld abgelegt werden).
* Der Hauseingang zählt auch als im Haus.
* Kara muss am Ende im Hauseingang stehenbleiben und in das Haus hineinschauen.
* Sollte das Haus voll sein, bevor alle Kleeblätter eingesammelt sind, lässt Kara die restlichen Blätter draußen liegen und begibt sich auf die Endposition (im Hauseingang, ins Haus schauend).

## Informationen zur Karte
* Kara kann an jeder beliebigen Stelle im Haus und mit einer zufälligen Blickrichtung starten. **Ausnahme:** Kara startet niemals direkt in der Tür.
* Das Haus kann jede beliebige Form haben, die folgende Kriterien erfüllt:
    * Es gibt nur eine Tür mit einer Breite von genau einem Feld.
    * **Rechteckige Häuser:** Die Innenfläche beträgt mindestens 3 × 3 Felder. Die Tür befindet sich an einer beliebigen Wand, jedoch nicht direkt in einer Ecke.
    * **L-förmige Häuser:** Es muss eine Mindestgrundfläche von 3 × 3 Feldern hineinpassen. Die Tür liegt an einer beliebigen Wand, jedoch nicht direkt in einer Ecke.
* Die Kleeblätter liegen immer direkt außen an der Hauswand.

## Zusatz auf meinen haupt Karten
* Im Haus wurde vorher nicht aufgeräumt, weshalb dort noch Stühle im Weg stehen (dargestellt durch Pilze im Haus).
* Der Grünstreifen um das Haus herum wurde lange nicht gepflegt, weshalb dort ebenfalls Pilze gewachsen sind.
