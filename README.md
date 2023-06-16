# Projekt numer 2 - Informatyka geodezyjna
  Wykonali: Piotr Zawistowski, Maja Wiśniewska, Julia Surała

# SPIS TREŚCI:
  * Cel projektu (do czego służy program)
  * Jakie wymagania trzeba spełnić, by program działał na danym komputerze
  * Dla jakiego systemu operacyjnego została stworzona wtyczka
  * Jak używać programu
  * Przykładowe wywołania programu 

Pliki z zipa należy umieścić w folderze o nazwie: 'wtyczka_pr2'


## Cel projektu
  * Utworzenie wtyczki za pomocą programów: QGIS, python,  QT designer, która: 
      - liczy różnicę wysokości między dwoma wybranymi punktami i podaje na pasku informacyjnym interfejsu QGIS tekst wynikowy
      - oblicza pole powierzchni na podstawie współrzędnych zaznaczonychpunktów metodą Gaussa po wyborze minimum 3 punktów i podaje na pasku informacyjnym interfejsu QGIS tekst wynikowy

## Jakie wymagania trzeba spełnić, by program działał na danym komputerze
  * Wtyczka została utworzona za pomocą programów: QGIS w wersji 3.28.4, python w wersji 3.9,  QT designer w wersji QGIS 3.28.4 , aby wtyczka działała poprawnie, należy uruchomić ją w środowisku QGIS wersji 3.28.4 lub nowszej, z zainstalowaną odpowiednią wersją Pythona (3.9 lub nowsza)
  * pole przechowujące wysokość nazywa się 'H_PLEVRF2007NH', a więc aby skorzystać z programu potrzebny jest plik zawierający atrybuty H z układu PL-EVER2007-NH, jeżeli w tabeli atrybutów danej warstwy nie będzie pola 'H_PLEVRF2007NH', wtyczka nie zadziała.

## Dla jakiego systemu operacyjnego została stworzona wtyczka
  * Wtyczka została stworzona dla systemu Windows, aczkolwiek będzie działa w systemach, które obsługują powyższe programy w tych konkretnych wersjach tj. Linux i Mac. 

## Jak używać programu
  * Zainstalowaną wtyczkę należy uruchomić, wyświetli się nam okno, gdzie będą do wyboru 2 opcje: albo wybór 2 punktów aby obliczyć przewyższenie albo wybór co najmniej 3 punktów do obpiczenia powierzchni. Jeśli wybierzemy inną liczbę punktów niż 2 do obliczenia różnicy wysokości to wyskoczy błąd z informacją, że wybrano za dużo bądź za mało punktów, podobnie jeśli wybierzemy mniej punktów niż 3 do obliczenia powierzchni, dostaniemy informację o tym, aby wybrać co najmniej 3 punkty. Aby zakończyć obliczenia wystarczy kliknąć 'ok' a okno się zamknie.


##  Przykładowe wywołania programu 
  * Naszą wtyczkę testowaliśmy na wartswie z zajęć sit-u.  
tak wygląda osnowa wysokościowa:  
![tak wygląda osnowa wysokościowa](https://github.com/harrypjoterr/Projetk2_ig/assets/129081913/8b65dbac-5a6a-4d3e-a773-a18f61a1f908)  
  * Przykładowe wyniki po zaznaczeniu przypadkowych 2 punktów dla różnicy wysokości (w metrach) oraz kilku punktów dla pola powierzchni (w metrach kwadratowych):  
![image](https://github.com/harrypjoterr/Projetk2_ig/assets/129081913/1e9b9e22-cc90-4276-9639-0aed4948a7c9)  

  * Przykładowe wyniki działania wtyczki, w przypadku gdy wybierzemy nieodpowiednią liczbę punktów:  
![image](https://github.com/harrypjoterr/Projetk2_ig/assets/129081913/ce4e730b-f9c7-4ed1-ad13-dcbacc0713b4)  
jak widać otrzymujemy komunikaty, o dokonaniu błędu.



