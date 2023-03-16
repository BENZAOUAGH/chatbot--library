from tkinter import *

from PIL import ImageTk, Image
import re

books = {"python": "Voici les 4 meilleurs livres Python : "
                   "\n p1. Apprenez à programmer en Python " 
                   "\n p2. Machine learning avec Python"
                   "\n p3. Comprendre les bases et maitriser la programmation"
                   "\n p4. Programmer avec Python ",
         "java": "Voici les 4 meilleurs livres java : "
                  "\n j1. Programmer avec Java "
                  "\n j2. Java 11 - Les fondamentaux du langage"
                  "\n j3. Apprendre la Programmation Orientée Objet avec le langage Java"
                  "\n j4. Apprenez à programmer en Java",

         "Programmation Web": "Voici les 4 meilleurs livres Programmation Web: "
                  "\n pw1.Réalisez votre site web avec HTML 5 et CSS3"
                  "\n pw2.Assurance qualité Web"
                  "\n pw3.Développer un site web"
                  "\n pw4.Créer un site web pour les nuls",

         "Data Science": "Voici les 4 meilleurs livres Data Science: "
                  "\n d1.The Elements of Statistical Learning"
                  "\n d2.Python for Data Science Handbook"
                  "\n d3.Introduction to Statistical Learning"
                  "\n d4.Data Science from Scratch : First Principles with Python",

         "Cybersecurity": "Voici les 4 meilleurs livres Cybersecurity: "
                  "\n c1.Cybersecurite et Cyberdefense:Enjeux Strategiques"
                  "\n c2.La Cybersécurité pour les Nuls"
                  "\n c3.Cybersécurité des services informatiques"
                  "\n c4.Tribe of Hackers Blue Team: Tribal Knowledge from the Best in Defensive ",
         }

library= {"p1": ['p1.png',"Apprenez à programmer en Python","Auteur:Vincent Le Goff","Edition:2éme édition","Prix:32€","Résumé : \nVous n'y connaissez rien en programmation et\n vous souhaitez apprendre un langage clair et intuitif ?\n Python est fait pour vous ! Vous découvrirez dans ce livre,\n conçu pour les débutants, tout ce dont vous avez besoin pour programmer,\n des bases à la bibliothèque standard, en passant par la programmation orientée objet et\n l'acquisition d'outils avancés ou\n professionnels pour devenir plus efficace."],
          "p2": ['p2.png', "Le machine learning avec Python", "Auteur:Andreas C.Müeller,Sarah Guido", "Edition: edi8 , 2018", "prix:39€ ","Résumé : \n Ce livre sur le Machine Learning avec le langage Python permet aux lecteurs \nnovices ou étudiants de disposer des connaissances théoriques nécessaires\n pour une compréhension approfondie du Machine Learning et d'appréhender les outils\n techniques utiles pour mettre en pratique les concepts étudiés"],
          "p3": ['p3.png',"Comprendre les bases et maitriser la programmation","Auteur:Bill Lubanovic","Edition:De Boeck Supérieur, 2022","Prix:34,90€","Résumé : \nVous découvrez Python et vous voulez progresser dans la maitrise de ce langage ? \nCet ouvrage de base est fait pour vous. Vous comprendrez tous les concepts inconrtournables \net vous apprendrez à les mettre en pratique en vous exerçant avec \nles nombreux exercices proposés."],
          "p4": ['p4.png',"Apprenez à Programmer avec Python","Auteur:Gérard Swinnen","Edition:3éme édition","Prix:39€","Résumé : \n Original et stimulant, cet ouvrage aborde au travers \nd'exemples attrayants et concrets tous les fondamentaux de la programmation. \nL'auteur a choisi Python, langage moderne et élégant,\n aussi performant pour le développement d'applications web complexes\n que pour la réalisation de scripts système ou l'analyse de fichiers XML."],

          "d1": ['d1.png',"The Elements of Statistical Learning","Auteur:Patrick Viafore","Edition:2éme édition","Prix:$61.27","Résumé : \nCe livre décrit les idées importantes dans ces domaines \ndans un cadre conceptuel commun. Bien que l'approche soit statistique, \nl'accent est mis sur les concepts plutôt que sur les mathématiques.\n De nombreux exemples sont donnés avec une utilisation libérale des graphiques en couleur.\n Il devrait être une ressource précieuse pour les statisticiens et \ntoute personne intéressée par l'exploration de données dans le domaine scientifique ou industriel."],
          "d2": ['d2.png', "Python for Data Science Handbook", "Auteur:Andreas C.Müeller,Sarah Guido", "Edition: 1ére édition", "prix:$57.78","Résumé : \n Pour de nombreux chercheurs, Python est un outil essentiel en raison \nde ses bibliothèques pour stocker, manipuler et obtenir un aperçu des données.\n Ce livre décrit toutes les ressources dont vous pouvez disposer pour mettre en oeuvre vos applications : \nIPython, NumPy, Pandas, Matplotlib, Scikit-Learn et d'autres outils associés."],
          "d3": ['d3.png',"Introduction to Statistical Learning","Auteur:Gareth James ,Daniela Witten , Trevor Hastie , Robert Tibshirani ","Edition:2éme édition","Prix:$65.46","Résumé : \n CE LIVRE est pour ceux qui ne possèdent pas \nde solides connaissances en mathématiques (enfin, limitée). \nIl se positionne comme une excellente introduction à la méthodologie de\n l’apprentissage statistique avec R. À mon avis,\n il sera difficile de trouver des livres\n de Data Science (avec R) qui font mieux."],
          "d4": ['d4.png',"Data Science from Scratch : First Principles with Python","Auteur:Joel Grus ","Edition:2éme édition","Prix:$34.94","Résumé : \n Un livre de data science en python qui explique comment implémenter \ndes algorithmes à partir de zéro (Oui zéro). Il couvre une variété de domaines, \ndont le deep learning, les statistiques, le NLP et bien d’autres encore."],

          "j1": ['j1.png', "Programmer avec Java", "Auteur:Ben Evans, David Flanagan ", "Edition:1éme édition","Prix:$39.36","Résumé : \n  Il contient tout ce que vous attendez des éditions \n précédentes - syntaxe, exemples et une excellente référence.\n Les nouvelles fonctionnalités de Java 8+ sont mises \n en évidence. De nombreux concepts, comme la collecte \n des déchets, sont également couverts."],
          "j2": ['j2.png', "Java 11 - Les fondamentaux du langage", "Auteur:Thierry RICHARD Thi ","Edition: 1ére édition", "prix:$87.79 ","Résumé : \n  Le livre vous accompagne notamment dans la découverte\n de Java SE, Eclipse et MySQL, la programmation \n orientée objet et les différentes API Java."],
          "j3": ['j3.png', "Apprendre la Programmation Orientée Objet avec le langage Java","Auteur:Luc GERVAIS ", "Edition:3éme édition","Prix:$102.55","Résumé : \nVous y trouverez des exercices concrets et \n corrigés pour vous exercer sur ce paradigme. "],
          "j4": ['j4.png', "Apprenez à programmer en Java", "Auteur:Cyrille Herby","Edition:3éme édition", "Prix:$34.94","Résumé : \n Cet ouvrage destiné aux debutants vous tiendra par \n la main pour vous accompagner dans la découverte des fondamentaux du langage Java"],

          "pw1": ['pw1.png', "Réalisez votre site web avec HTML 5 et CSS3", "Auteur:Mathieu Nebra", "Edition:3éme édition","Prix:28€","Résumé : \nVous rêvez d'apprendre à créer des sites web mais vous \n avez peur que ce soit compliqué car vous débutez ? \n Ce cours est fait pour vous ! Conçu pour les débutants, il \n vous permettra de découvrir HTML5 et CSS3,\n les dernières technologies en matière de création de sites web."],
          "pw2": ['pw2.png', "Assurance qualité Web", "Auteur:Élie Sloïm, Laurent Denis ","Edition: 3ére édition", "prix:36€","Résumé : \n En apparence, c’est une petite évolution, mais \n sur le fond c’est un changement majeur : le livre\n s’appelle maintenant assurance qualité web, car\n  il pose les bases d’un métier, d’une activité de\n  management, d’un ensemble de compétences que les\n professionnels du web doivent maîtriser."],
          "pw3": ['pw3.png', "Développer un site web", "Auteur:NIXON ROBIN ","Edition:4éme édition", "Prix:33,50€  ","Résumé : \n Au premier rang des meilleurs livres sur le Web!\n Construisez des sites web interactifs, pilotés par\n les données avec la puissante combinaison des\n technologies en source ouverte et des normes du Web\n, même si vous n'avez que des connaissances de base\n du HTML. Vous abordez la programmation web dynamique à\n l'aide des technologies de base d'aujourd'hui. "],
          "pw4": ['pw4.png', "Créer un site web pour les nuls", "Auteur:David A. Crowder", "Edition:10éme édition","Prix:4,95€","Résumé : \n Ce livre vous dit tout ce que vous devez savoir pour\n créer votre propre site Internet, du simple \n serveur FTP à l'intérieur de votre bureau jusqu'à \n la mise en service de serveurs Web virtuels\n accessibles du monde entier"],

          "c1": ['c1.png', "Cybersecurite et Cyberdefense:Enjeux Strategiques", "Auteur:ann Salamon", "Edition:1éme édition","Prix:$47.37","Résumé : \n S’adressant à un panel de publics divers, cet ouvrage\n balaie un large panorama de sujets structurants\n liés à la sécurité numérique. Prenant comme \n point de départ la compréhension du cyberespace,"],
          "c2": ['c2.png', "La Cybersécurité pour les Nuls", "Auteur:Joseph Steinberg","Edition: 1ére édition", "prix:$33.96 ","Résumé : \n Toutes les clés pour protéger\n vos données sur Internet\nLa cybersécurité consiste à se protéger d'attaques \n venant de cybercriminels. Ces hackers ont \n pour but d'utiliser vos données afin \n de pirater des brevets, des comptes bancaires, et \n de détourner toutes sortes d'informations personnelles ou secrètes."],
          "c3": ['c3.png', "Cybersécurité des services informatiques", "Auteur:Patrice Dignan , Jérôme Parra, Jean-Pierre Souvanne","Edition:1éme édition", "Prix:$44.33 ","Résumé : \n  S'adressant à un panel de publics divers, \n cet ouvrage balaie un large panorama de sujets \n structurants liés à la sécurité numérique. Prenant \n comme point de départ la compréhension \n du cyberespace, il en décrit quelques propriétés \n importantes : tendances, enjeux, caractéristiques <<topologiques>>,\n acteurs en présence. Il évoque la question de la \n souveraineté numérique, en tentant \n d'en donner des clés de compréhension."],
          "c4": ['c4.png', "Tribe of Hackers Blue Team: Tribal Knowledge from the Best in Defensive ", "Auteur:Marcus J. Carey , Jennifer Jin", "Edition:1éme édition","Prix:$17.43","Résumé : \nL’équipe Tribe of Hackers est de retour. Ce\n nouveau guide regorge d’informations sur les problèmes \n de l’équipe bleue des plus grands noms de la cybersécurité.\n À l’intérieur, des dizaines des plus grands spécialistes de la \n sécurité de la Blue Team au monde vous montrent comment \n renforcer les systèmes contre les violations et les attaques\n  réelles et simulées. "],
          }



def response(request):
    answer = []
    for key in books.keys():
        if re.search(key, request, re.IGNORECASE):
            answer.append(books.get(key))

    if answer:
        return "\n".join(answer)

    return "Bienvenue dans votre librairie en ligne qui vous propose \n les meilleurs livres en Informatique! \nVoici la liste des domaines qu on propose: \n {Python,Data science,programmation web,Java,Cybersécurité}\n Lequel vous desiriez ?"




class Window:
    def __init__(self, master):
        self.frame = None
        self.entry_msg = None
        self.text_cons = None
        label=Label(master, text="Welcome to your Library!")
        label.pack()
        self.master = master
        subframe = self.createTopFrame(master)
        subframe.pack(expand=FALSE, fill=BOTH, side=TOP)

        left_frame = self.createLeftFrame(master)
        left_frame.pack(expand=True, fill=BOTH, side=LEFT)

        self.right_frame = self.createRightFrame(master)
        self.right_frame.pack(expand=True, fill=BOTH, side=LEFT)

    def createLeftFrame(self, master):
        left_frame = Frame(master)
        self.text_cons = Text(left_frame,
                              width=20,
                              height=2,
                              bg="chocolate",
                              fg="#EAECEE",
                              font="Helvetica 14",
                              padx=5, pady=5)

        self.text_cons.place(relheight=1, relwidth=1)

        label_bottom = Label(left_frame,
                             bg="sandybrown",
                             height=80)

        label_bottom.place(relwidth=1,
                           rely=0.825)

        self.entry_msg = Entry(label_bottom,
                               bg="sienna",
                               fg="#EAECEE",
                               font="Helvetica 13")

        # place the given widget
        # into the gui window
        self.entry_msg.place(relwidth=0.74,
                             relheight=0.06,
                             rely=0.008,
                             relx=0.011)

        self.entry_msg.focus()

        # create a Send Button
        button_msg = Button(label_bottom,
                            text="Send",
                            font="Helvetica 14 bold",
                            width=20,
                            bg="sandybrown",
                            command=lambda: self.sendButton(self.entry_msg.get()))

        button_msg.place(relx=0.77,
                         rely=0.008,
                         relheight=0.06,
                         relwidth=0.22)

        self.text_cons.config(cursor="arrow")

        # create a scroll bar
        scrollbar = Scrollbar(self.text_cons)

        # place the scroll bar
        # into the gui window
        scrollbar.place(relheight=1, relx=0.974)

        scrollbar.config(command=self.text_cons.yview)

        self.text_cons.config(state=DISABLED)
        return left_frame

    def createRightFrame(self, master):
        self.right_frame = Frame(master, background="peachpuff")
        self.frame = Frame(self.right_frame )
        self.frame.pack(expand=True, fill=BOTH, side=TOP)
        return self.right_frame

    def createTopFrame(self, master):
        subframe = Frame(master, height=120)
        global my_img
        # Load the image
        image = Image.open('livres.png')
        # Resize the image in the given (width, height)
        img = image.resize((1500, 120))
        my_img = ImageTk.PhotoImage(img)
        my_label = Label(subframe, image=my_img)
        my_label.pack(side=BOTTOM, fill=BOTH, anchor=CENTER)
        return subframe

    def sendButton(self, msg):
        if msg.lower() in library.keys():
            book = library.get(msg)
            self.frame.pack_forget()
            self.frame = Frame(self.right_frame)
            self.frame.pack(expand=True, fill=BOTH, side=TOP, padx=10, pady=10)
            global img
            img = ImageTk.PhotoImage(Image.open(book[0]))

            Label(self.frame, image=img, padx=5, pady=5).grid(row=1, column=3, rowspan=3, columnspan=4, sticky="nsew")
            l1 = Label(self.frame, text=(book[1]), font="Helvetica 16 bold",padx=5, pady=5)
            l2 = Label(self.frame, text=(book[2]), font="Helvetica 16 bold", padx=5, pady=5)
            l3 = Label(self.frame, text=(book[3]), font="Helvetica 16 bold", padx=5, pady=5)
            l4 = Label(self.frame, text=(book[4]), bg='moccasin', fg='#f00', font="Helvetica 16 bold", padx=5, pady=5)
            l5 = Label(self.frame, text=(book[5]), bg='moccasin', fg='black', font="Helvetica 10 bold", padx=5, pady=5)
            l1.grid(row=7, column=5, sticky="nsew")
            l2.grid(row=9, column=5, sticky="nsew")
            l3.grid(row=11, column=5, sticky="nsew")
            l4.grid(row=13, column=5, sticky="nsew")
            l5.grid(row=3, column=7, sticky="nsew")
        else:
            answer = response(msg)
            self.text_cons.config(state=NORMAL)
            self.text_cons.insert(END, "Bot -> " + answer + "\n\n")

            self.text_cons.config(state=DISABLED)
            self.text_cons.see(END)

        self.entry_msg.delete(0,END)

root = Tk()
root.geometry('1000x1000')

window = Window(root)
root.mainloop()