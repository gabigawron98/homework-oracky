# Korona Science - Prace domowe

## Wstęp

Prace domowe realizowane są na platformie GitHub Classrooom. 
Sprawdzanie pracy domowej odbywa się przy pomocy zautomatyzowanych testów jednostkowych (`pytest`),
ponadto prace domowe są sprawdzane przez system antyplagiatowy.

## Jak rozwiązywać?

Rozwiązania prac domowych z poszczególnych dni należy umieszczać w poszczególnych plikach,
których szablony będą pojawiać się [tutaj](https://github.com/korona-science/assignments).
Pliki muszą znajdować się w głównym folderze repozytorium oraz ich nazwy muszą być **takie same** jak nazwy szablonów. 

Każda praca domowa składać się będzie z jednego lub więcej zadań. 
W celu rozwiązania zadania należy zedytować szablony poprzez dopisanie ciał funckji, **bez zmiany ich nazw oraz argumentów**.
Do każdego zadania będą podane przykładowe dane wejściowe oraz spodziewany wynik. 
Zestaw danych testów automatycznych do zadań jest niejawny i różny od przykładów.

Edytowanie plików znajdujących się w folderze `.github` może uszkodzić konfigurację powodując nieprawidłowe wyniki testów. 

## Jak sprawdzić poprawność rozwiązań?

Po każdym pushu do repozytorium testy wykonują się automatycznie,
a ich status można sprawdzić na głównej stronie repozytorium przy informacji o ostatnim commitcie. 
Czerwony krzyżyk oznacza, że testy nie przeszły, natomiast zielony tick oznacza, że przeszły.
Historie testów oraz więcej informacji można uzyskać w sekcji *Actions* dostępnej na głównym pasku repozytorium.

## Problemy

Jakiekolwiek problemy prosimy zgłaszać w postaci Issue w **swoim** repozytorium.
