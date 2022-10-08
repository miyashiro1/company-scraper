import json
import csv
from creating_file import create_file

create_file()

with open('data.json') as f:
    data = json.load(f)

# Create a csv files
with open('freework.csv', 'a', encoding="utf-8") as new_file:
    fieldnames = ['name', 'presentation', 'année de création', 'Chiffre d’affaires', 'Collaborateurs',
                  'siége', 'Activité', 'website', 'twitter', 'facebook', 'linkedin', 'skills']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=';')
    csv_writer.writeheader()

    for i in data['hydra:member']:
        r = ''
        lista_skills =[]
        try:
            name = i['name']
            print(name)
            presentation = i['description']
            creation = i['creationYear']
            revenue = i['annualRevenue']
            Collaborateurs = i["size"]["label"]
            location = i['location']['label']
            activity = i["businessActivity"]["name"]
            website = i["websiteUrl"]
            twitter = i["twitterUrl"]
            facebook = i["facebookUrl"]
            linkedin = i["linkedInUrl"]
            for s in i['skills']:
                lista_skills.append(s['name'])
        except:
            continue

        skill = ', '.join(lista_skills)

        csv_writer.writerow({'name': name, 'presentation': presentation, 'année de création': creation,
                             'Chiffre d’affaires': revenue, 'Collaborateurs': Collaborateurs, 'siége': location,
                             'Activité': activity, 'website': website, 'twitter': twitter, 'facebook': facebook,
                             'linkedin': linkedin, 'skills': skill})



