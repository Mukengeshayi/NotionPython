# list
plateformes_sociales = ["Facebook", "Instagram", "Snapchat", "Twitter"]
print (plateformes_sociales)
plateformes_sociales[2]='lindkind'
print (plateformes_sociales)
plateformes_sociales.append("tiktok")
print (plateformes_sociales)
plateformes_sociales.remove("tiktok")
print (plateformes_sociales)

# dictionnaire
nouvelle_campagne = {
"responsable_de_campagne": "Jeanne d'Arc",
"nom_de_campagne": "Campagne nous aimons les chiens",
"date_de_début": "01/01/2020",
"influenceurs_importants": ["@MonAmourDeChien", "@MeilleuresFriandisesPourChiens"]
}
print(nouvelle_campagne)
print(nouvelle_campagne["date_de_début"])

# Ajouter les elements dans un dictionnaire vide
taux_de_conversion = dict()
taux_de_conversion['facebook'] = 3.4
taux_de_conversion['instagram'] = 1.2
print(taux_de_conversion)
print(taux_de_conversion['facebook'])
