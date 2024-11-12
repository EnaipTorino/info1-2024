# Il terminale

si avvia lanciando l'applicazione **Prompt dei comandi**
in ogni istante sono posizionato in un percorso nel file system (come in esplora risorse).
`C:\Users\mattia.folcarelli>` vuol dire che sono nella cartella `mattia.folcarelli` sotto la cartella user
con dir (ls in linux e mac) visualizzo tutti i file e cartelle contenute nel percorso in cui sono.

con cd (uguale in unix) posso spostarmi tra cartelle

cd Desktop
```
C:\Users\mattia.folcarelli\Desktop>
```
```
C:\Users\mattia.folcarelli\Desktop>cd Padre\Figlio
C:\Users\mattia.folcarelli\Desktop\Padre\Figlio
```

Percorso assoluto:
```
C:\Users\mattia.folcarelli\Desktop\Padre\Figlio
```
Percorso relativo:
```
.\Padre\Figlio
```

. cartella in cui sono  
.. cartella padre


`cd C:\Users\mattia.folcarelli\Desktop\Padre\Figlio`  
`cd percorsoassoluto passa direttamente alla cartella`

Premendo tab il terminale spesso può suggerirmi il contenuto

## EXTRA
### SSH
`ssh root@123.123.123.123 -p 2299`

`ssh bandit0@bandit.labs.overthewire.org -p 2220`

https://overthewire.org/wargames/bandit/bandit0.html

The goal of this level is for you to log into the game using SSH. The host to which you need to connect is bandit.labs.overthewire.org, on port 2220. The username is bandit0 and the password is bandit0. Once logged in, go to the Level 1 page to find out how to beat Level 1.

`ls -al` per visualizzare file nascosti
`mkdir nome cartella` per generare cartelle
`cat readme.txt` per leggere un file

