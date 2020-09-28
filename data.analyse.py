import pandas as pd
# data titanic inlezen  met pandas
titanic = pd.read_csv("data/titanic.csv")
#data uitprinten
print(titanic)
# eerst 5 rijen van data uitprinten
print(titanic.head(5))
# laatste 5 rijen van data uitprinten
print(titanic.tail(5))
# type van data printen
print(titanic.dtypes)

#file omzetten naar excel
#titanic.to_excel('titanic.xlsx', sheet_name="passengers", index=False)

#twee categorieen vergelijken bv in een kolom of rijen
subset = titanic[["Age" , "Survived"]]
print(subset)

above_40 = titanic[titanic["Age"] > 40]#print(above_40)
# het zoeken van bepaald iets
first_class = titanic[titanic["Pclass"].isin([1 and 2])]

print(first_class)

#loc functie om in een kolom te filteren
adult_names = titanic.loc[titanic["Age"]>35, "Name"]

print(adult_names)
# iloc om specifieke selectie te maken en ze filteren
adult_names = titanic.iloc[0:10,2:5]
print(adult_names)
# aggregate gemiddelde uitprinten
average_ticket_price = titanic["Fare"].mean()
print(average_ticket_price)
median_ticket_price = titanic["Fare"].median()
print(median_ticket_price)

# voor meer gegevens van een data te halen meer details
titanic_stats = titanic.agg({
    "Fare" : ['min' , 'max' , 'mean']
})

print(titanic_stats)

# Split = gegevens delen in verschillende groepen
# Apply = pas een functie to op elke groep
# Combine = voeg gegevens samen in 1 datas tructuur

titanic_stats_prices = titanic.groupby("Sex")["Fare"].mean()
print(titanic_stats_prices)




