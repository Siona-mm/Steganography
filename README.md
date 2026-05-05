# Raport Laboratori: Sistemi i Steganografisë së Imazhit

## Përmbledhja e Sistemit

Sistemi përdor steganografinë e Bitit Më Pak të Rëndësishëm (LSB) për të fshehur të dhëna tekstuale brenda një imazhi bitmap. Duke modifikuar bitin e 7-të të kanalit të ngjyrës së gjelbër, sistemi arrin ruajtjen e të dhënave pa prezantuar ndryshime të dukshme për syrin e njeriut.

Sistemi mbështetet në një shpërndarje pseudo-rastësore. Për të parandaluar grumbullimin e të dhënave në një vend të vetëm, një çelës i përbashkët (2026) ushqen një gjenerator numrash rastësorë që përcakton një sekuencë jolineare të koordinatave të pikselëve për fshehjen e të dhënave. 14 bitët e parë të ngarkesës janë të rezervuar për një kokë (header) të gjatësisë, gjë që i mundëson nxjerrësit të identifikojë pikën e saktë të përfundimit të mesazhit të fshehtë. Sistemi përdor rreptësisht formatin BMP për të shmangur algoritmet e kompresimit që përndryshe do të dëmtonin shtresën e fshehur të biteve.

## Metodologjia Procedurale

Zhvillimi u ekzekutua në tri faza të dallueshme:

Faza I: Fshehja (Embedding)
Teksti burimor konvertohet në segmente 7-bitësh ASCII dhe një kokë binare 14-bitësh për gjatësinë i shtohet përpara vargut të biteve. Një listë e të gjithë indekseve të disponueshme të pikselëve përzjehet (shuffle) duke përdorur çelësin e paracaktuar për të krijuar një shteg të sigurt fshehjeje. Për çdo bit në varg, vlera e pikselit në koordinatën e synuar rregullohet me një madhësi prej 1 vetëm kur ekziston një mospërputhje midis bitit të imazhit dhe bitit të mesazhit.

Faza II: Nxjerrja (Extraction)
Nxjerrësi rigjeneron listën identike të indekseve të përziera duke përdorur të njëjtin çelës të përdorur gjatë fshehjes. 14 pikselët e parë në sekuencë kërkohen për të rikuperuar gjatësinë e mesazhit. Bitet pasuese merren në grupe prej shtatësh, kthehen përsëri në vlera ASCII dhe bashkohen për të formuar tekstin përfundimtar.
<img width="862" height="92" alt="image" src="https://github.com/user-attachments/assets/b6f64227-007a-450b-8d14-b164560467c8" />


Faza III: Vizualizimi
Çdo piksel që do të përdorej gjatë fshehjes së një mesazhi me 1,488 karaktere identifikohet. Këta pikselë mbishkruhen me ngjyrë të kuqe me kontrast të lartë për të verifikuar shpërndarjen hapësinore në të gjithë përmasat e imazhit.
<img width="628" height="375" alt="image" src="https://github.com/user-attachments/assets/09f022c1-5319-4b8e-893e-6e142ce335c0" />

Krahasimi Vizual:
<img width="629" height="380" alt="image" src="https://github.com/user-attachments/assets/eef3d113-0059-4b67-97df-f43c7ad8f9e6" />
<img width="626" height="385" alt="image" src="https://github.com/user-attachments/assets/7250eba6-7028-4445-8f59-e6e4dc761910" />


## Udhezimet e Ekzekutimit

Sistemi kërkon bibliotekën Python Imaging Library (Pillow). Instalimi mund të verifikohet përmes komandës: pip install Pillow. Të gjitha komandat duhet të ekzekutohen nga direktoria rrënjë STEGANOGRAPHY për të ruajtur integritetin e shtigjeve relative.

Fshehja e të dhënave: python steg_lab/embed.py
Kjo gjeneron skedarin steg_lab/stego-image.bmp që përmban mesazhin e fshehur.

Nxjerrja e të dhënave: python steg_lab/extract.py
Kjo shfaq tekstin e rikuperuar direkt në terminal.

Vizualizimi i mbulimit: python steg_lab/highlight.py
Kjo gjeneron skedarin steg_lab/highlighted-image.bmp për analizë ligjore.

## Udhëzues për Vendosjen e Provave

Provat e Terminalit
Vendosni një screenshot të terminalit tuaj VS Code që tregon rezultatin e suksesshëm të extract.py pas seksionit të Nxjerrjes. Kjo shërben si provë e vlefshmërisë së logjikës.

Provat Strukturore
Vendosni një screenshot të shiritit anësor (Explorer) të VS Code brenda seksionit Përmbledhja e Sistemit. Kjo konfirmon që struktura e direktorive përputhet me kërkesat.

Provat Ligjore 
Vendosni një imazh të highlighted-image.bmp brenda seksionit të Vizualizimit për të ilustruar efikasitetin e algoritmit të shpërndarjes rastësore.

##Struktura e Fajllave
<img width="372" height="443" alt="image" src="https://github.com/user-attachments/assets/789fa27c-ece6-4a38-a3e3-41bfd7ceb9c9" />
