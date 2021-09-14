Skripti convert_po_to_xlsx.bat in convert_xlsx_to_po.bat pretvorita .po datoteko v .xlsx datoteko in nazaj.

==============================================================================================================

Potrebuje inštaliran python3. Testirano s python 3.9.6.
Pred uporabo inštaliraj GNU GetText in med inštalacijo obkljukaj "Add Delphi GetText functions in context menus".

==============================================================================================================
 
Priprava pretvorbe prevodov v XLSX tabelo
1. Generiraj default.po z desnim klikom na mapo s sourci in "Extract translations to template"
2. V default.po dopiši jezik, za katerega gre. Uredi vrstico "Language: \n" na "Language: bg_BG\n" ipd. 
   Za več info glej https://www.gnu.org/software/gettext/manual/gettext.html#The-LANGUAGE-variable
3. Premakni ga v ta direktorij
4. Zaženi convert_po_to_xlsx.bat, ki generira excel tabelo, v kateri se urejajo prevodi.

NOTE: Path do source kode naj bo brez presledkov, drugače ne bo znal pretvorit nazaj.

Pretvorba XLSX v PO
1. Premakni tabelo v ta direktorij
2. Zaženi convert_xlsx_to_po.bat
3. Vnesi podatke o jeziku (bg_BG ipd.) in ime xlsx datoteke.
4. Skripta generira datoteko xlsx_output.po

NOTE: Prej preveri, da je poimenovanje stolpca s prevodi v XLSX datoteki pravilno, torej oblike "bg_BG".