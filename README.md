# Statistik für BWL: von Daten zu ML und LLMs

Browserbasierter Übungskurs mit 10 Jupyter-Notebooks. Die Studierenden brauchen keine lokale Python-Installation und kein VS Code.

## Start

Für jede Übung einfach auf **Open in Colab** klicken. In Colab anschließend:

1. **Datei → Kopie in Drive speichern**
2. Zellen von oben nach unten ausführen
3. Ergebnisse und Management-Checkpoint im eigenen Notebook dokumentieren

| # | Übung | Schwerpunkt | Start |
|---|---|---|---|
| 1 | Daten, Stichprobe und Bias | Rohdaten prüfen, Analysepopulation definieren, Bias diskutieren | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kqc-real/statistik-bwl-ml-llm/blob/main/notebooks/01_daten_stichprobe_bias.ipynb) |
| 2 | Deskriptive Statistik und EDA | Bestellungen aggregieren, Verteilungen und Kundenkonzentration beschreiben | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kqc-real/statistik-bwl-ml-llm/blob/main/notebooks/02_deskriptive_statistik_eda.ipynb) |
| 3 | Wahrscheinlichkeit und Bayes | Kaufwahrscheinlichkeiten, bedingte Wahrscheinlichkeiten und Bayes | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kqc-real/statistik-bwl-ml-llm/blob/main/notebooks/03_wahrscheinlichkeit_bayes.ipynb) |
| 4 | Zufallsvariablen und Verteilungen | Rechtsschiefe Geschäftsdaten und empirische Verteilungen | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kqc-real/statistik-bwl-ml-llm/blob/main/notebooks/04_zufallsvariablen_verteilungen.ipynb) |
| 5 | Stichprobe und Unsicherheit | Stichprobenvariabilität und Bootstrap-Konfidenzintervalle | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kqc-real/statistik-bwl-ml-llm/blob/main/notebooks/05_stichprobe_unsicherheit_bootstrap.ipynb) |
| 6 | Korrelation, Kausalität und Leakage | Perfekte Prognosen kritisch prüfen | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kqc-real/statistik-bwl-ml-llm/blob/main/notebooks/06_korrelation_kausalitaet_leakage.ipynb) |
| 7 | Lineare Regression | Nachfrage prognostizieren und Fehler auf Testdaten bewerten | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kqc-real/statistik-bwl-ml-llm/blob/main/notebooks/07_lineare_regression.ipynb) |
| 8 | Logistische Regression | Kaufwahrscheinlichkeiten modellieren | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kqc-real/statistik-bwl-ml-llm/blob/main/notebooks/08_logistische_regression.ipynb) |
| 9 | Generalisierung und Modellvergleich | Baseline, Overfitting, Precision, Recall und Schwellenwerte | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kqc-real/statistik-bwl-ml-llm/blob/main/notebooks/09_generalisierung_modellvergleich.ipynb) |
| 10 | Statistik hinter LLMs | Logits, Softmax, Temperatur, Entropie und Sampling | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kqc-real/statistik-bwl-ml-llm/blob/main/notebooks/10_statistik_hinter_llms.ipynb) |

## Kursprinzip

> Der Agent darf rechnen und Code erzeugen. Die Studierenden müssen jede Kennzahl, Grafik und Modellentscheidung fachlich erklären können.

Die Notebooks sind für etwa 90 Minuten ausgelegt. Jede Übung kombiniert eine betriebswirtschaftliche Ausgangssituation, statistische Aufgaben, gezielte Agentenaufträge und einen Management-Checkpoint.

## Technische Struktur

```text
notebooks/      10 studentische Colab-Notebooks
course_data.py  reproduzierbare didaktische Kursdaten
```

Die Notebooks laden nur ein kleines Kursdaten-Modul aus demselben Repository. Die Datensätze werden anschließend deterministisch im Browser erzeugt. Ein manueller Datei-Upload ist nicht nötig.

## Datenhinweis

Die drei Datensätze werden **reproduzierbar und deterministisch** für die Übungen erzeugt und orientieren sich strukturell an folgenden bekannten UCI-Lehrdatensätzen:

- Online Retail
- Online Shoppers Purchasing Intention
- Bike Sharing Dataset

Dadurch erhalten alle Studierenden dieselbe Ausgangslage. Die statistisch relevanten Eigenschaften wie fehlende Werte, Stornierungen, Rechtsschiefe, Klassenungleichgewicht, zeitliche Struktur und Data Leakage sind gezielt eingebaut.

## Lehrbetrieb

Für myCampus stehen fertige Direktlinks in `MYCAMPUS_LINKS.md`. Die Musterlösungen gehören nicht in dieses öffentliche Repository und werden separat verwaltet.
