import time
from selenium import webdriver
from selenium.webdriver.common.by import By

username = 'hithere@example.com'
password = 'fakepass1234'

top100 = [
        "Diabetes mellitus",
        "Mammakarzinom",
        "Lungenkarzinom",
        "Divertikulose und Divertikulitis",
        "Ischämischer Schlaganfall",
        "Meningitis",
        "Kolorektales Karzinom",
        "Allergische Erkrankungen",
        "Multiple Sklerose",
        "Pneumothorax",
        "Pneumonie",
        "Hyperthyreose",
        "Anorexia nervosa",
        "Ovarialtumoren",
        "Zytostatika",
        "Arterielle Hypertonie",
        "Lungenembolie",
        "Sepsis",
        "Vigilanzminderung und intrakranielle Volumenzunahme",
        "Polymyalgia rheumatica und Riesenzellarteriitis",
        "Myokardinfarkt",
        "Bandscheibenprolaps",
        "Vorhofflimmern",
        "Nosokomiale Infektionen",
        "Angeborene Herzfehler",
        "Asthma bronchiale",
        "Reaktionen auf schwere Belastungen und Anpassungsstörungen",
        "Lyme-Borreliose",
        "Phlebothrombose",
        "HIV",
        "Weichteilläsionen der Schulter",
        "Magenkarzinom",
        "Chronisch obstruktive Lungenerkrankung",
        "Psychopathologischer Befund",
        "Herzinsuffizienz",
        "Infektiöse Endokarditis",
        "Pankreaskarzinom",
        "Epidemiologie und Wahrscheinlichkeiten",
        "Morbus Crohn",
        "Antibiotika - Übersicht",
        "Infektiöse Mononukleose",
        "Hyperurikämie und Gicht",
        "Rettungsablauf am Unfallort und klinische Primärversorgung",
        "Sterilität, Infertilität und Impotenz",
        "Depression",
        "Angststörungen und Phobien",
        "Sarkoidose",
        "Akute Leukämien",
        "Periphere arterielle Verschlusskrankheit",
        "Cholelithiasis, Cholezystitis und Cholangitis",
        "Subarachnoidalblutung",
        "Phenprocoumon und neue orale Antikoagulantien",
        "Gesetzliche Krankenversicherung",
        "Leberzirrhose",
        "Antidepressiva",
        "Tuberkulose",
        "Multiples Myelom",
        "Zöliakie",
        "Studientypen der medizinischen Forschung",
        "Ärztliche Rechtskunde",
        "Diagnostik in der Gynäkologie",
        "Urolithiasis",
        "Endometriose",
        "Antipsychotika",
        "Osteoporose",
        "Hepatitis B",
        "Wirbelkörperfraktur",
        "Morbus Perthes",
        "Schock",
        "Nicht-orale Antikoagulation",
        "Neurologische Untersuchung",
        "Juvenile idiopathische Arthritis",
        "Systemische Sklerose",
        "Epileptische Anfälle und Epilepsien",
        "Migräne",
        "Bösartige Knochentumoren",
        "Psychotherapeutische Verfahren (Klinik)",
        "Cushing-Syndrom",
        "Nebennierenrindeninsuffizienz",
        "Psoriasis vulgaris",
        "Neuroendokrine Neoplasien",
        "Parkinson-Syndrom und Morbus Parkinson",
        "Urothelkarzinom",
        "Kindesmisshandlung",
        "Alkohol (Intoxikation und Abhängigkeit)",
        "Tiefgreifende Entwicklungsstörungen",
        "Malignes Melanom",
        "Antidiabetika",
        "Influenza",
        "Morbus Alzheimer",
        "Amyotrophe Lateralsklerose",
        "Zystische Fibrose",
        "Immunsuppressiva",
        "Systemischer Lupus erythematodes",
        "Wundbehandlung",
        "Thanatologie",
        "Strangulation und Ersticken",
        "Allgemeine Onkologie",
        "Nierenzellkarzinom",
        "Schmerztherapie"
]

driver = webdriver.Firefox()

driver.get("https://next.amboss.com/de/customsession")
driver.find_element_by_id('signin_username').send_keys(username)
driver.find_element_by_id('signin_password').send_keys(password)
driver.find_element(By.XPATH, "//input[@value='Akzeptieren und Anmelden']").click()

time.sleep(5)

driver.find_element(By.XPATH, "//div[@data-e2e-test-id=\"checkbox-Kapitel\"]/div").click()
driver.find_element(By.XPATH, "//div[@data-e2e-test-id=\"row-Klinische & ärztliche Kapitel\"]/div[3]").click()
for topic in top100:
	driver.find_element(By.XPATH, "//div[@data-e2e-test-id=\"row-{}\"]/div[3]/span".format(topic)).click()

# driver.quit()