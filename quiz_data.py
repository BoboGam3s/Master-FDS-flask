# quiz_data.py

quiz_questions = [
    {
        'id': 1,
        'question': "01) Les Warrants donnent la possibilité de vendre à découvert :",
        'options': {'A': "Vrai", 'B': "Faux"},
        'correct_answer': 'B' 
    },
    {
        'id': 2,
        'question': "02) Les capitaux propres sont des ressources apportées par les actionnaires et peuvent également être dégagées par l'entreprise :",
        'options': {'A': "Vrai", 'B': "Faux"},
        'correct_answer': 'A'
    },
    {
        'id': 3,
        'question': "03) La couverture sur un marché est :",
        'options': {'A': "Une assurance de gains.", 'B': "Une assurance de certitude."},
        'correct_answer': 'B' 
    },
    {
        'id': 4,
        'question': "04) La prime :",
        'options': {'A': "D'un call dépend positivement du prix à payer ou du taux d'intérêt.", 'B': "D'un call dépend positivement des taux d'intérêt.", 'C': "D'une option dépend négativement de la volatilité de l'actif sous-jacent."},
        'correct_answer': 'B' 
    },
    {
        'id': 5,
        'question': "05) Les 2 composantes de la prime d'option :",
        'options': {'A': "La valeur intrinsèque.", 'B': "La valeur de temps."},
        'correct_answer': 'A' 
    },
    {
        'id': 6,
        'question': "06) Le marché des valeurs mobilières de placement est :",
        'options': {'A': "Un marché financier.", 'B': "Un marché interbancaire.", 'C': "Un marché monétaire."},
        'correct_answer': 'A'
    },
    {
        'id': 7,
        'question': "07) Qu'est-ce que la finance durable ?",
        'options': {'A': "La finance durable, privilégie les opérations financières qui prennent en compte des critères extra financiers à long terme.", 'B': "La finance durable, privilégie des investissements à haut rendement.", 'C': "La finance durable, privilégie des investissements à court terme."},
        'correct_answer': 'A'
    },
    {
        'id': 8,
        'question': "08) Les « green bonds » sont entre autres :",
        'options': {'A': "Des obligations qui permettent de financer des projets d'entreprises respectueux de l'environnement.", 'B': "Des obligations à haut rendement."},
        'correct_answer': 'A'
    },
    {
        'id': 9,
        'question': "09) On quantifie un taux d'intermédiation bancaire de 60 % si :",
        'options': {'A': "60 % des crédits sont effectués par les banques.", 'B': "Cela mesure la part des financements indirects par rapport aux financements directs.", 'C': "Cela mesure l'autofinancement des entreprises."},
        'correct_answer': 'B' 
    },
    {
        'id': 10,
        'question': "10) En quoi consiste un swap ?",
        'options': {'A': "Un contrat, passé entre deux parties, qui sert généralement aux banques pour s'assurer des flux financiers selon une échéance déterminée.", 'B': "Un titre qui donne à son détenteur le droit et non l'obligation d'acheter ou de vendre, à une certaine échéance et à un certain prix."},
        'correct_answer': 'A'
    },
    {
        'id': 11,
        'question': "11) La notation extra-financière des acteurs économiques met en évidence :",
        'options': {'A': "La performance de l'entreprise face aux enjeux environnementaux, sociaux et liés à leur gouvernance.", 'B': "L'augmentation de leur niveau d'émissions de CO2 et leur consommation d'électricité.", 'C': "Uniquement la rémunération des dirigeants."},
        'correct_answer': 'A'
    },
    {
        'id': 12,
        'question': "12) Faire le choix de l'Investissement Socialement Responsable pour son épargne c'est :",
        'options': {'A': "Soutenir le social et le développement des entreprises durables.", 'B': "Connaître le type d'acteurs économiques que l'on finance.", 'C': "Entrer dans une démarche de progrès pour soi et pour la société."},
        'correct_answer': 'A'
    },
    {
        'id': 13,
        'question': "13) Un investissement de 1000 Dh procure des recettes nettes sur quatre années respectivement de 300, 400, 400 et 500. Le taux d'actualisation est de 11%. Quel est le montant de la valeur actuelle nette VAN ?",
        'options': {'A': "261,759", 'B': "216,759", 'C': "221,759"},
        'correct_answer': 'B' 
    },
    {
        'id': 14,
        'question': "14) L'investissement est rentable si :",
        'options': {'A': "VAN > 0", 'B': "VAN < 1", 'C': "VAN < 0"},
        'correct_answer': 'A'
    },
    {
        'id': 15,
        'question': "15) Le projet est rentable si l'indice de profitabilité est :",
        'options': {'A': "Supérieur à 0", 'B': "Inférieur à 1", 'C': "Supérieur à 1"},
        'correct_answer': 'C'
    },
    {
        'id': 16,
        'question': "16) Le coût de l'investissement est compris entre :",
        'options': {'A': "150,39 et 147,88", 'B': "152,24 et 148,12", 'C': "149,87 et 146,59"},
        'correct_answer': 'C' 
    },
    {
        'id': 17,
        'question': "17) Quel est le taux interne de rentabilité de cet investissement (TIR) ?",
        'options': {'A': "16,215", 'B': "16,117", 'C': "16,167"},
        'correct_answer': 'B' 
    },
    {
        'id': 18,
        'question': "18) Les dirigeants d'une entreprise hésitent entre deux projets A et B. Quel projet est le plus rentable ? Projet A : Coût de l'investissement : 360000 et Cash flows prévisionnels pendant 5 années : 150000. Projet B : Coût de l'investissement : 390000 et Cash flows prévisionnels pendant 5 années : 130000",
        'options': {'A': "Projet A", 'B': "Projet B", 'C': "Les deux projets sont égaux"},
        'correct_answer': 'A' 
    },
    {
        'id': 19,
        'question': "19) La formule =SI(C2>=10 ; \"Pas de remise\" ; SI(C2>=5 ; \"Remise de 10%\" ; \"Remise de 15%\")) est stockée en C3. La cellule C2 contient la valeur 20. La valeur stockée en C3 sera :",
        'options': {'A': "Pas de remise", 'B': "Remise de 10%", 'C': "Remise de 15%"},
        'correct_answer': 'A' 
    },
    {
        'id': 20,
        'question': "20) La formule =RECHERCHEV(\"Ingénieur\" ; A3:D20 ; 3 ; FAUX) permet de chercher la cellule A22, \"Elle\" permet de réaliser la recherche dans D20 et elle renvoie la valeur stockée en 4ème position :",
        'options': {'A': "Vrai", 'B': "Faux"},
        'correct_answer': 'B' 
    },
    {
        'id': 21,
        'question': "21) La formule =SI(ET(C1<100 ; C2>1) ; \"Achat Conseillé\" ; \"Achat Négocié\") est stockée en C3. La cellule C1 contient la valeur 150 et la cellule C2 contient la valeur 1. La valeur stockée en C3 sera :",
        'options': {'A': "Achat Conseillé", 'B': "Achat Négocié"},
        'correct_answer': 'B' 
    },
    {
        'id': 22,
        'question': "22) La formule =RECHERCHEV(B14 ; B6:C12 ; 2 ; FAUX) permet de rechercher une valeur dans une liste :",
        'options': {'A': "Triée", 'B': "Non triée", 'C': "Triée ou non triée B6 : B12"},
        'correct_answer': 'B' 
    },
    {
        'id': 23,
        'question': "23) En utilisant la fonction SI() pour afficher l'observation (Non admis (Moyenne<5) ; Rattrapage (moyenne >=5 et <10) ; Admis (Moyenne>=10)) selon la moyenne de trois notes B3, C3, et D3, la formule pourrait ressembler à :",
        'options': {'A': "=SI(Moyenne(B3 :D3)<5 ; \"Non Admis\" ; SI (E3<10 ; \"Rattrapage\" ; \"Admis\"))", 'B': "=SI(Moyenne(B3 :D3)<10 ; \"Rattrapage\" ; SI(Moyenne(B3 :D3)>=10 ; \"Admis\" ; \"Non Admis\"))", 'C': "Aucune réponse."},
        'correct_answer': 'A' 
    },
    {
        'id': 24,
        'question': "24) La plage C13 : C20 contient les valeurs 1, 5, 10, 20, 30, 50, 60. Et la plage D13 : D20 contiennent A, B, C, D, A, H, H. La formule =RECHERCHEV(39 ; $C$35:$D$20 ; 2 ; VRAI) :",
        'options': {'A': "E", 'B': "F", 'C': "Une erreur se produit"},
        'correct_answer': 'C' 
    },
    {
        'id': 25,
        'question': "25) Quelle est la formule qui permet de compter le nombre d'étudiants de sexe masculin nés après le 1er janvier 2005 ? Noms en (A2 : A30), Date de naissance en (B2 : B30) et Sexe (F ou M) en (C2 : C30) :",
        'options': {'A': "=NB.SI.ENS(C2:C30 ; \"M\" ; B2:B30 ; \">01/01/2005\")", 'B': "=NB.SI.ENS(B2:B30 ; \">01/01/2005\" ; C2:C30 ; \"M\")", 'C': "=NB.SI.ENS(A2:A30 ; C2:C30 ; \"M\" ; B2:B30 ; \">01/01/2005\")"},
        'correct_answer': 'A' 
    },
    {
        'id': 26,
        'question': "26) Si la cellule A1 contient la valeur 15, la formule : =SI(A1<15 ; SI(A1<10 ; \"A\" ; \"B\") ; SI(A1<16 ; \"C\" ; \"A++\")) renvoie la valeur :",
        'options': {'A': "A", 'B': "C", 'C': "A+"},
        'correct_answer': 'B' 
    },
    {
        'id': 27,
        'question': "27) Dans une boucle \"TantQue\", quand les instructions sont-elles exécutées ?",
        'options': {'A': "Une fois que la condition devient vraie", 'B': "Tant qu'une condition est vraie", 'C': "Tant que la condition est fausse"},
        'correct_answer': 'B'
    },
    {
        'id': 28,
        'question': "28) Que se passe-t-il si la condition dans une boucle \"TantQue\" est toujours vraie ?",
        'options': {'A': "La boucle ne s'exécute pas du tout", 'B': "La boucle s'exécute indéfiniment (boucle infinie)", 'C': "La boucle s'arrête après la première exécution"},
        'correct_answer': 'B'
    },
    {
        'id': 29,
        'question': "29) Dans quel cas une boucle \"Pour\" ne s'exécutera-t-elle jamais ?",
        'options': {'A': "Si la condition initiale est toujours vraie", 'B': "Si la borne de départ est supérieure à la borne de fin", 'C': "Si la boucle n'inclut aucune instruction à exécuter"},
        'correct_answer': 'B'
    },
    {
        'id': 30,
        'question': "30) Quelle est la valeur finale de *somme* après l'exécution de cet algorithme ?\n`somme ← 0`\n`Pour i de 1 à 3 Faire`\n`  somme ← somme + i * 2`\n`FinPour`",
        'options': {'A': "2", 'B': "6", 'C': "12"},
        'correct_answer': 'C' 
    },
    {
        'id': 31,
        'question': "31) Quel est le résultat du pseudocode suivant ?\n`Pour i = 1 à 5`\n`  Si i mod 3 = 0 Alors`\n`    afficher(i, \"est divisible par 3\")`\n`  FinSi`\n`FinPour`",
        'options': {'A': "Il affiche \"1 est divisible par 3\", \"2 est divisible par 3\", \"3 est divisible par 3\"", 'B': "Il affiche \"3 est divisible par 3\"", 'C': "Il n'affiche aucun résultat"},
        'correct_answer': 'B' 
    },
    {
        'id': 32,
        'question': "32) Quel est le résultat de l'exécution suivante ? pour chaque MHT dans [1500, 1200, 500, 2500]\n`Si MHT > 2000 Alors`\n`  break`\n`FinSi`\n`TVA ← MHT * 0.2`\n`TTC ← MHT + TVA`\n`afficher(\"Montant HT: \", MHT, \", Montant TTC: \", TTC)`\n`FinPour`",
        'options': {'A': "Montant HT: 1500, Montant TTC: 1800; Montant HT: 1200, Montant TTC: 1440; Montant HT: 500, Montant TTC: 600", 'B': "Montant HT: 1500, Montant TTC: 1800; Montant HT: 1200, Montant TTC: 1440; Montant HT: 500, Montant TTC: 600; Montant HT: 2500, Montant TTC: 3000", 'C': "Aucun résultat, car 500 est inférieur à 2000."},
        'correct_answer': 'A' 
    }
]