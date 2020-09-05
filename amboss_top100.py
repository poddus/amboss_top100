#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import pynput

keyboard = pynput.keyboard.Controller()

mouse = pynput.mouse.Controller()

top100test = [
    "Diabetes mellitus",
    "Mammakarzinom",
    "Lungenkarzinom",
    "Ischämischer Schlaganfall",
    "Ovarialtumoren",
    "Divertikulose und Divertikulitis",
    "Kolorektales Karzinom"
]

top100 = [
    "Diabetes mellitus",
    "Mammakarzinom",
    "Lungenkarzinom",
    "Ischämischer Schlaganfall",
    "Ovarialtumoren",
    "Divertikulose und Divertikulitis",
    "Kolorektales Karzinom",
    "Meningitis",
    "Pneumonie",
    "Morbus Crohn",
    "Lungenembolie",
    "Arterielle Hypertonie",
    "Anorexia nervosa",
    "Allergische Erkrankungen",
    "Pneumothorax",
    "Zytostatika",
    "Multiple Sklerose",
    "Bandscheibenprolaps",
    "Vigilanzminderung und intrakranielle Volumenzunahme",
    "Phlebothrombose",
    "Herzinsuffizienz",
    "Myokardinfarkt",
    "Nosokomiale Infektionen",
    "Tuberkulose",
    "Vorhofflimmern",
    "Epilepsie",
    "Depression",
    "Bösartige Knochentumoren",
    "Reaktionen auf schwere Belastungen und Anpassungsstörungen",
    "Hyperthyreose",
    "Polymyalgia rheumatica und Riesenzellarteriitis",
    "Periphere arterielle Verschlusskrankheit",
    "Angeborene Herzfehler",
    "Rettungsablauf am Unfallort und klinische Primärversorgung",
    "Lyme-Borreliose",
    "Antidepressiva",
    "Rheumatoide Arthritis",
    "HIV",
    "Reanimation",
    "Sepsis",
    "Leberzirrhose",
    "Infektiöse Endokarditis",
    "Weichteilläsionen der Schulter",
    "Chronisch obstruktive Lungenerkrankung",
    "Sarkoidose",
    "Psychopathologischer Befund",
    "Magenkarzinom",
    "Antibiotika - Übersicht",
    "Akute Leukämien",
    "Sterilität, Infertilität und Impotenz",
    "Pankreaskarzinom",
    "Asthma bronchiale",
    "Neurologische Untersuchung",
    "Appendizitis",
    "Hepatitis B",
    "Subarachnoidalblutung",
    "Antipsychotika",
    "Infektiöse Mononukleose",
    "Cholelithiasis, Cholezystitis und Cholangitis",
    "Morbus Perthes",
    "Psoriasis vulgaris",
    "Parkinson-Syndrom und Morbus Parkinson",
    "Epidemiologie und Wahrscheinlichkeiten",
    "Studientypen der medizinischen Forschung",
    "Schock",
    "Nicht-orale Antikoagulation",
    "Gesetzliche Krankenversicherung",
    "Chronische Niereninsuffizienz",
    "Juvenile idiopathische Arthritis",
    "Nebennierenrindeninsuffizienz",
    "Urolithiasis",
    "Angststörungen und Phobien",
    "Endometriose",
    "Immunsuppressiva",
    "Osteoporose",
    "Wirbelkörperfraktur",
    "Kindesmisshandlung",
    "Alkohol (Intoxikation und Abhängigkeit)",
    "Ärztliche Rechtskunde",
    "Diagnostik in der Gynäkologie",
    "Psychotherapeutische Verfahren (Klinik)",
    "Cushing-Syndrom",
    "Allgemeinanästhesie",
    "Morbus Bechterew",
    "Systemischer Lupus erythematodes",
    "Glutensensitive Enteropathie",
    "Akute Pankreatitis",
    "Morbus Alzheimer",
    "Urothelkarzinom",
    "Tiefgreifende Entwicklungsstörungen",
    "Strangulation und Ersticken",
    "Antidiabetika",
    "Influenza",
    "Nierenzellkarzinom",
    "Guillain-Barré-Syndrom",
    "Hyperurikämie und Gicht",
    "Wundbehandlung",
    "Erkrankungen durch organische Lösungsmittel, Insektizide, Halogenkohlenwasserstoffe, Benzol und Homologe",
    "Prävention",
    "Gesetzliche Unfallversicherung"
]

time.sleep(5)
for x in top100:
    for char in x:
        keyboard.type(char)
        time.sleep(0.2)
    time.sleep(7)
    mouse.click(pynput.mouse.Button.left)
    time.sleep(2)
    with keyboard.pressed(pynput.keyboard.Key.shift):
        keyboard.press(pynput.keyboard.Key.tab)
        keyboard.release(pynput.keyboard.Key.tab)
    time.sleep(1)

