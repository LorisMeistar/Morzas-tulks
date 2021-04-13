print('***Programma atbalsta tekstu tikai bez garumzīmēm***\n') #prosta brīdinājums
print('***************MORZAS KODA TULKOTĀJS****************\n')
i=1

vesture= input('Vai vēlies nelielu ieskatu morzas koda izmantošanā/vēsturē (jā/nē)? \n')

if vesture=='jā' or vesture=='Jā':
    print('*Galvenais ieguvums, zinot morzas kodu, ir iespēja nosūtīt ziņojumus daudz lielākos attālumos (tūkstošiem jūdžu) \n'
          'un ar daudz mazāku jaudu, nekā tipiskas balss ziņas.\n'
          '*Morzas kodu izgudroja amerikāņu mākslinieks un izgudrotājs Semjuels F.B. Morze 1830. gados.\n'
          '*ASV Jūras spēki un krasta apsardze joprojām izmanto signāllampas, lai sazinātos, izmantojot morzas kodu.\n')
elif vesture=='nē' or vesture=='Nē':
    print('')
else:
    vesture = input('Vai vēlies nelielu ieskatu morzas koda izmantošanā/vēsturē (jā/nē)? \n')

while True:
    funkcija = input(
        'Vai vēlies ģenerēt morzas kodu no teksta(A) vai pārtulkot morzas kodu tekstā(B)?\n')  # paprasa lietotājam, ko viņš gribēs darīt (A vai B)

    # viss morzas alfabēts definēts, piešķirot katram burtam/ciparam/simbolam noteiktu apzīmējumu (vērtību)
    # burts/cipars/simbols šajā gadījumā ir KEY (lv atslēga laikam), bet tie morzas punktiņi ir VALUE (attiecīgās atslēgas vērtība)
    morzas_koda_alfab = {'A': '.-', 'B': '-...',
                         'C': '-.-.', 'D': '-..', 'E': '.',
                         'F': '..-.', 'G': '--.', 'H': '....',
                         'I': '..', 'J': '.---', 'K': '-.-',
                         'L': '.-..', 'M': '--', 'N': '-.',
                         'O': '---', 'P': '.--.', 'Q': '--.-',
                         'R': '.-.', 'S': '...', 'T': '-',
                         'U': '..-', 'V': '...-', 'W': '.--',
                         'X': '-..-', 'Y': '-.--', 'Z': '--..',
                         '1': '.----', '2': '..---', '3': '...--',
                         '4': '....-', '5': '.....', '6': '-....',
                         '7': '--...', '8': '---..', '9': '----.',
                         '0': '-----', ', ': '--..--', '.': '.-.-.-',
                         '?': '..--..', '/': '-..-.', '-': '-....-',
                         '(': '-.--.', ')': '-.--.-'}

    if funkcija == 'A' or funkcija == 'a':  # ja lietotājs ievada, ka grib A darbību
        # tad prasa ievadīt tekstu, kuru pārveidot uz morzas kodu
        teksta_ievade = input(
            'Ievadi tekstu bez garumzīmēm, ciparus, simbolus, kurus vēlies pārtulkot uz morzas kodu:\n')

        morzas_kods = ''  # definējam, kā pagaidām "tukšu" vērtību, lai pēc tam var tur samest attiecīgus burtu apzīmējumus

        for burts in teksta_ievade:  # kamēr burts ir lietotāja ievadītā vardā

            if burts != ' ':  # ja burts user input tekstā nav atstarpe
                morzas_kods += morzas_koda_alfab[
                                   burts.upper()] + ' '  # sameklē definētajā morzas koda alfabētā attiecīgo burtu,
                # un kad for loop sākas atkārtoti pievieno nākamo burtu jau esošajiem
                # un aiz katra burta ieliek 1 atstarpi

            else:
                morzas_kods += ' '  # ja tiek ievadīta atstarpe starp vārdiem, tad printējot ārā tā izskatīsies kā 2 atstarpes
        print('Morzas kods no Tava ievadītā teksta ir sekojošs: \n', morzas_kods)  # izprintējam iegūto kodu


    elif funkcija == 'B' or funkcija == 'b':  # ja lietotājs grib veikt B darbību
        koda_ievade = input('Ievadi morzas kodu, kuru vēlies pārtulkot uz tekstu:\n')  # pieprasa ievadīt morzas kodu
        # def no_morzas_koda(message):
        # extra space added at the end to access the
        # last morse code
        koda_ievade += ' '

        teksts = ''
        zime = ''
        for burts in koda_ievade:

            if (burts != ' '):  # ja burts nav space

                # counter to keep track of space
                i = 0
                zime += burts  # apkopo vienas zīmes morzas kodu


            else:  # ja ievada space

                i += 1  # 1 space ir starp katru zīmi

                if i == 2:  # 2 atstarpes ir starp katriem vārdiem

                    # adding space to separate words
                    teksts += ' '  # ja ievadītajā kodā ir 2 atstarpes, tad arī izvadītajā tekstā ir atstarpe starp vārdiem
                else:

                    # piekļuve burtiem alfabētā (atslēgām), meklējot pēc apzīmējumiem (vērtībām)
                    teksts += list(morzas_koda_alfab.keys())[list(morzas_koda_alfab
                                                                  .values()).index(zime)]
                    zime = ''
        print('Teksts no Tava ievadītā morzas koda ir sekojošs: \n', teksts)