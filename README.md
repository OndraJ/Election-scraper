# Election-scraper
Třetí projekt Python akademie od Engeta.

## Popis projektu

Projekt slouží k extrahování volebních výsledků v roce 2017. 
Odkaz k prohlednutí [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).
> Script jako první argument vezme URL vybraného okresu (například Uherské Hradiště, preš Výběr obce a [X](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202)). Poté pro každou obec extrahuje číslo obce, název obce, voliči v seznamu, vydané obálky, platné hlasy, politické strany a jejich hlasy. Následně data uloží do CSV souboru jehož název uvdeme jako druhý argument.

## Instalace knihoven

Použité knihovny jsou uloženy v souboru `requirements.txt`. Pro instalaci doporučuji použít nové virtuální prostředí s naistalovaným **pip-manager** a následně spustit:
```
> $ pip --version 
> $ pip install -r requirements.txt
```

## Spuštění projektu 

Jak již bylo zmíněno výše, spuštění souboru election_scraper.py vyžaduje dva povinné argumenty.
> python election_scraper.py \<odkaz-uzemniho-celku\> \<nazev-souboru\>

## Ukázka projektu

Výsledky hlasování pro okres Uherské Hradiště:
1. argument: `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202`
2. argument: `vysledky_uher_hradiste.csv`

Spuštění programu z příkazové řádky:
```
python election_scraper.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202' 'vysledky_uher_hradiste.csv'
```
Průběh stahování:
```
Stahuji data z  URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202
Uloženo do souboru: vysledky_uher_hradiste.csv
UKONČUJI election_scraper
```
Částečný výstup:
```
Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy...
592013,Babice,1452,873,870,79,0,0,60,0,55,66,5,6,3,0,2,74,0,23,254,1,0,95...
592021,Bánov,1707,1070,1069,92,2,1,75,0,117,62,10,1,11,1,2,71,1,11,293,1,0...
592030,Bílovice,1473,1018,1018,98,0,0,67,1,66,80,10,5,14,0,1,90,0,28,264,0...
```
