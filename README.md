# ♻️ Aplikacja webowa do segregacji odpadów i edukacji ekologicznej

Aplikacja webowa oparta na frameworku **Django**, wykorzystująca głębokie sieci neuronowe (**TensorFlow/Keras**)  
do automatycznej klasyfikacji odpadów i wskazywania odpowiedniego pojemnika do ich utylizacji.

Projekt został stworzony w ramach pracy dyplomowej/inżynierskiej.

---

## 🚀 Funkcjonalności

- **Klasyfikacja obrazów:** użytkownik przesyła zdjęcie odpadu, a system rozpoznaje jego kategorię.
- **Sekcja edukacyjna:** aplikacja wyświetla odpowiedni kolor kosza (niebieski, żółty, zielony, brązowy, czarny) wraz z instrukcją dotyczącą poprawnej segregacji.
- **Modele AI:** możliwość wyboru między modelem autorskim a modelem ResNet50V2 (oba znajdują się w katalogu `classifier/cnn_model`).

---

## 🛠️ Technologie

- **Backend:** Python 3.12, Django  
- **AI/ML:** TensorFlow, Keras, NumPy  
- **Frontend:** HTML, CSS  

---

## ⚙️ Instrukcja uruchomienia

Aby uruchomić projekt lokalnie, wykonaj poniższe kroki:

### 1. Klonowanie repozytorium

```bash
git clone https://github.com/MK396/praca_smieci.git
cd praca_smieci
```

### 2. Konfiguracja środowiska wirtualnego

#### Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```
#### macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalacja zależności
```bash
pip install -r requirements.txt
```

### 4. Konfiguracja zmiennych (.env)

Ze względów bezpieczeństwa plik konfiguracyjny nie jest dołączony do repozytorium.

1. Wejdź do katalogu praca_site (tam, gdzie znajduje się plik manage.py).
2. Utwórz nowy plik o nazwie .env.
3. Wklej do niego swój unikalny klucz:
```bash
SECRET_KEY = 'twoj_unikalny_klucz_django_mozesz_wpisac_cokolwiek_dlugiego'
```
5. Uruchomienie serwera

Będąc w katalogu praca_site uruchom serwer za pomocą poniższego polecenia
```bash
python manage.py runserver
```
Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000/




