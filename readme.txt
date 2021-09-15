Skripti convert-po-to-xlsx.bat in convert-xlsx-to-po.bat pretvorita PO datoteko v XLSX datoteko in nazaj. 
Namen teh skript je, da olajša delo prevajalcu, tako da ni več potrebno poznavanje strukture PO datoteke, 
prevod le vnese v ustrezne celice v tabeli.

Kristjan Šoln

==============================================================================================================

OPOMBE:

Potrebuje python3. Testirano s python 3.9.6.

Če je potrebno generiranje PO datoteke, pred uporabo inštaliraj GetText in med inštalacijo obkljukaj 
"Add Delphi GetText functions in context menus".

Dobro je shraniti prvotni PO file, saj se med pretvorbo (PO->XLSX->PO) izgubi del headerja v PO datoteki. 

Če funkcija nekega tipa komentarja ne najde, med pretvorbo doda komentar # None na tistem mestu. 

Osnovano na knjižnicah po_excel_translate in polib. V njih je spremenjena interpretacija komentarjev in 
izpisovanje napak. Tam kjer so urejene, je označeno s komentarjem # Edited. Za primerjavo sprememb v 
prihodnosti je v support-files dodan še zip originalnih knjižnic.

==============================================================================================================

NAVODILA:

Postopek pretvorbe PO datoteke v XLSX tabelo:
1. Če še ne obstaja, generiraj default.po z desnim klikom na mapo s sourci in "Extract translations to template"
   NOTE: Path do source kode naj bo brez presledkov, drugače ne bo znal pretvorit nazaj.
2. V default.po dopiši jezik, za katerega gre. V headerju dodaj/uredi vrstico na "Language: bg_BG\n" ipd. 
   Za več info glej https://www.gnu.org/software/gettext/manual/gettext.html#The-LANGUAGE-variable
3. Premakni ga v mapo user-files
4. Zaženi convert-po-to-xlsx.bat in vnesi ime vhodnih ter izhodnih datotek. 

Postopek pretvorbe XLSX tabele v PO datoteko:
1. Premakni tabelo v mapo user-files
   NOTE: Preveri, da je poimenovanje stolpca s prevodi v XLSX datoteki pravilno, torej oblike "bg_BG".
2. Zaženi convert-xlsx-to-po.bat
3. Vnesi podatke o jeziku (bg_BG ipd.) in ime vhodnih ter izhodnih datotek.
