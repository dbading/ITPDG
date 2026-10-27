# Interaktive Mathematik

**Mathematik durch interaktive Visualisierungen verstehen.**

Eine Sammlung interaktiver mathematischer Animationen, die abstrakte Konzepte anschaulich und intuitiv zugänglich machen sollen.

Das Projekt beschäftigt sich insbesondere mit mathematischer Analysis, Fourier-Analysis und Signalverarbeitung. Durch die Veränderung verschiedener Parameter können mathematische Zusammenhänge untersucht und in Echtzeit visualisiert werden.

### [Zur interaktiven Website](https://dbading.github.io/)

---

## Über das Projekt

Mathematik wird häufig durch Definitionen, Sätze und Gleichungen vermittelt. Diese bilden die Grundlage einer rigorosen mathematischen Theorie. Visualisierungen können jedoch zusätzlich helfen, ein intuitives Verständnis für abstrakte Zusammenhänge zu entwickeln.

Dieses Projekt verfolgt das Ziel, eine Verbindung zwischen **mathematischer Theorie und geometrischer Anschauung** herzustellen.

Anstatt mathematische Gleichungen ausschließlich analytisch zu betrachten, können Nutzer mit mathematischen Objekten experimentieren, Parameter verändern und beobachten, wie bestimmte Eigenschaften und Strukturen entstehen.

Die Visualisierungen dienen als ergänzende Lernmaterialien für Studierende und alle, die sich für Mathematik interessieren.

## Mathematische Themengebiete

### 1. Faltung

Die Faltung ist eine grundlegende mathematische Operation mit Anwendungen in der Analysis, Wahrscheinlichkeitstheorie, Theorie der Differentialgleichungen und Signalverarbeitung.

Für geeignete Funktionen $f,g:\mathbb{R}\to\mathbb{R}$ ist ihre Faltung definiert durch

$$
(f*g)(x)=\int_{-\infty}^{\infty}f(t)\,g(x-t)\,dt.
$$

Die interaktiven Animationen veranschaulichen, wie zwei Funktionen miteinander gefaltet werden und wie sich durch wiederholte Faltung zunehmend glatte Funktionen konstruieren lassen.

**Behandelte Themen:**
- Grafische Interpretation der Faltung
- Faltung von B-Splines
- Konstruktion und Eigenschaften von Spline-Funktionen

[Zu den Faltungsanimationen](https://dbading.github.io/Faltung/)

### 2. Fourier-Reihen

Fourier-Reihen ermöglichen es, periodische Funktionen als Summen trigonometrischer Funktionen darzustellen.

Für eine geeignete $2\pi$-periodische Funktion besitzt die Fourier-Reihe die Form

$$
f(x)\sim\frac{a_0}{2}
+\sum_{n=1}^{\infty}
\left(a_n\cos(nx)+b_n\sin(nx)\right).
$$

Die interaktiven Visualisierungen zeigen, wie Fourier-Partialreihen unterschiedliche Funktionen approximieren und wie sich die Approximation mit zunehmender Anzahl an Fourier-Moden verändert.

**Behandelte Themen:**
- Fourier-Approximation verschiedener Funktionen
- Heaviside-Funktion
- Identitätsfunktion
- Sinusfunktion
- Konvergenz und Gibbs-Phänomen

[Zu den Fourier-Reihen](https://dbading.github.io/Fourier_Reihen/main_fourier_reihen_website.html)

### 3. Fourier-Transformation

Die Fourier-Transformation stellt einen Zusammenhang zwischen dem Zeit- beziehungsweise Ortsbereich und dem Frequenzbereich her.

Mit der Konvention

$$
\widehat{f}(\omega)
=\int_{-\infty}^{\infty}
f(t)e^{-i\omega t}\,dt
$$

lässt sich eine Funktion hinsichtlich ihrer Frequenzanteile analysieren.

Die interaktiven Visualisierungen verdeutlichen den Zusammenhang zwischen einer Funktion und ihrer Fourier-Transformierten.

**Behandelte Themen:**
- Funktionen im Zeitbereich
- Fourier-Spektrum und Frequenzanteile
- Rotierende komplexe Exponentialfunktion
- Interpretation des Fourier-Integrals

[Zur Fourier-Transformation](https://dbading.github.io/Fourier_Transformation/fouriertransformation_interaktiv.html)

---

## Funktionen der Website

- **Interaktive Steuerelemente:** Mathematische Zusammenhänge durch die Veränderung von Parametern untersuchen.
- **Dynamische Visualisierungen:** Mathematische Beziehungen durch Animationen nachvollziehen.
- **Mathematische Erklärungen:** Verbindung zwischen anschaulicher Interpretation und formalen Definitionen.
- **Browserbasierte Nutzung:** Die veröffentlichten Animationen können ohne zusätzliche Installation verwendet werden.
- **Erweiterbare Sammlung:** Weitere mathematische Themen und Visualisierungen können ergänzt werden.

## Projektstruktur

```text
dbading.github.io/
│
├── index.html
├── styles.css
├── README.md
│
├── Faltung/
│   └── index.html
│
├── Fourier_Reihen/
│   └── main_fourier_reihen_website.html
│
└── Fourier_Transformation/
    └── fouriertransformation_interaktiv.html
```

Jedes mathematische Themengebiet besitzt ein eigenes Verzeichnis mit den zugehörigen Webseiten und Visualisierungen.

*Die dargestellte Struktur ist vereinfacht und enthält nicht sämtliche Animationsdateien.*

## Verwendete Technologien

Das Projekt verwendet folgende Technologien:

- **Python** zur Erstellung mathematischer Visualisierungen und Animationen
- **HTML** zur Strukturierung der Webseiten
- **CSS** zur Gestaltung des Layouts
- **JavaScript** zur Umsetzung browserbasierter Interaktivität
- **GitHub Pages** zur Veröffentlichung und Bereitstellung der Website

## Lokale Ausführung

Das Repository zunächst klonen:

```bash
git clone https://github.com/dbading/dbading.github.io.git
```

Anschließend in das Projektverzeichnis wechseln:

```bash
cd dbading.github.io
```

Die Datei `index.html` kann direkt im Browser geöffnet werden.

Alternativ lässt sich ein lokaler Webserver starten:

```bash
python3 -m http.server 8000
```

Anschließend ist die Website unter folgender Adresse erreichbar:

http://localhost:8000

## Zukünftige Entwicklung

Dieses Projekt wird kontinuierlich weiterentwickelt. Geplant ist die Ergänzung weiterer mathematischer Konzepte, Animationen und interaktiver Experimente.

Langfristig soll eine frei zugängliche Sammlung mathematischer Visualisierungen entstehen, die das klassische Lernen und Lehren von Mathematik sinnvoll ergänzt.

## Autor

**Daniel Bading**

GitHub: [@dbading](https://github.com/dbading)

Website: [dbading.github.io](https://dbading.github.io/)

---

*Mathematik nicht nur durch Gleichungen verstehen, sondern auch durch Interaktion und Visualisierung.*