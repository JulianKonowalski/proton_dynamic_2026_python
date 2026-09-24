# Zadanie rekrutacyjne Proton Dynamic 2026 - Python

Bolid wyścigowy został wyposażony w dedykowaną płytkę do lokalnego zapisywania
danych odczytanych z czujników - czterech termometrów oraz dwóch akcelerometrów.
Płytka równolegle przesyła te dane do mobilnego serwera znajdującego się w picie,
który dalej umieszcza je w bazie danych Influx. W czasie jazdy bolid niestety
na stałe utracił połączenie sieciowe z serwerem, co spowodowało dziurę w
telemetrii, jednakże udało się odzyskać kopię danych z pamięci flash płytki oraz
zapisać ją w postaci pliku `resources/test_data.txt`. Struktura danych w tym
pliku wygląda następująco:
yyyy-mm-dd hh-mm-ss __typ_czujnika__ __id_czujnika__ __pomiar__

Typ czujnika może być jedną z dwóch predefiniowanych wartości. __ACC__ oznacza
akcelerometr, natomiast __TEMP__ sygnalizuje termometr. ID czujnika jest
nieujemną wartością całkowitoliczbową, a wartości pomiarów zapisane są w formie
liczb zmiennoprzecinkowych.

Aby móc umieścić zebrane informacje w bazie danych, potrzebne będzie ich wstępne
przetworzenie do obsługiwanego przez nią formatu. W tym celu, na podstawie
szkieletu klasy `DataProcessor` umieszczonego w pliku `src/DataProcessor.py`
zaimplementuj logikę przetwarzania danych z formatu `.txt` do formatu `.json`.
Oczekiwana struktura pliku `.json` wygląda następująco:

```
{
    "ACC": {
        "ACC_<ID>": [
            {
                "time": <timestamp>,
                "data": <data>
            },
            .
            .
            .
        ],
        .
        .
        .
    },
    "TEMP": {
        "TEMP_<ID>": [
            {
                "time": <timestamp>,
                "data": <data>
            },
            .
            .
            .
        ],
        .
        .
        .
    }
}
```

# Klonowanie
Aby sklonować projekt do folderu, w którym został otwarty wiersz poleceń,
posłuż się komendą:
```
git clone https://github.com/JulianKonowalski/proton_dynamic_2026_python.git
```

# Uruchamianie
Skrypt może zostać uruchomiony z poziomu konsoli w IDE:
```
python src/main.py
```

# Przesyłanie
Ukończone zadanie należy przesłać na adres `juliankon.protondynamic@gmail.com`.

_Powodzenia!_
