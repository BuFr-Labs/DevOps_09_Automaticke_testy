# DevOps_09_Automaticke_testy
Repozitoř k 9. lekci

# DevOps Úkol 09: Automatické testy v CI/CD pipeline

Tento repozitář obsahuje řešení domácího úkolu zaměřeného na tvorbu automatizovaného smoke testu dostupnosti webové stránky a jeho integraci do GitHub Actions pipeline.

## 🎯 Cíle projektu
* Vytvoření automatického testu v Pythonu pomocí frameworku `unittest`.
* Kontrola dostupnosti webové stránky (HTTP status 200) a ověření přítomnosti signifikantního řetězce v HTML kódu.
* Konfigurace automatizované CI/CD pipeline v GitHub Actions (`.github/workflows/devops-test.yml`).
* Zajištění přerušení pipeline v případě, že test selže (splnění volitelné části).
* Čistý stav repozitáře díky správně nakonfigurovanému `.gitignore`.

## 📂 Struktura projektu
Projekt je rozdělen na samotný testovací skript a definiční soubor pipeline:

* `test_web.py` - Python skript využívající knihovny `unittest` a `requests`. Stahuje HTML kód zadaného webu a provádí ověření obsahu.
* `.github/workflows/devops-test.yml` - Konfigurace GitHub Actions, která definuje spuštění testu na Ubuntu workeru při každém pushi.

## 🚀 Návod k použití

### 1. Prerekvizity (Lokální běh na RHEL10)
* Nainstalovaný **Python 3**.
* Vytvořené a zaktivované virtuální prostředí (`venv`).
* Nainstalovaná knihovna `requests`.

### 2. Lokální spuštění a testování
Založení virtuálního prostředí a instalace závislostí:
```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
```

Spuštění testu na lokální virtuálce:
```Bash
python3 test_web.py
```

### 3. Integrace a ověření v CI/CD
Po pushnutí kódu do vzdáleného repozitáře se automaticky spustí pipeline v záložce Actions na GitHubu.
* **Úspěšný scénář**: Pokud testovaný web obsahuje hledaný řetězec, skript vrátí exit code 0 a pipeline svítí zeleně.
* **Neúspěšný scénář (Ověření failu)**: Pokud se řetězec v HTML nenajde, skript vyvolá AssertionError, vrátí exit code 1 a GitHub Actions pipeline se okamžitě přeruší jako neúspěšná.

### Bezpečnost a čistota kódu
Lokální složky virtuálního prostředí (`venv/`, .`venv/`), dočasné soubory Pythonu (`__pycache__/`) a specifické konfigurační adresáře vývojového prostředí (`.vscode/`) jsou záměrně ignorovány pomocí `.gitignore`, aby repozitář obsahoval pouze čistý zdrojový kód.