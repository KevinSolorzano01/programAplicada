sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)


translations = {"mountain":	"orod", "bread":	"bass", "friend":	"mellon", "horse":	"roch" }
print(translations)
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}

students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

students_in_classes["philosophy"].append("marco")

print(students_in_classes)

students_in_classes["philosophy"].append("5")

print(students_in_classes)


""" se crea un diccionario vacio y se le agregan elementos con sus palabras o numeros claves """


Automoviles= {}
Automoviles["Audi"]=0
print(Automoviles)


Automoviles={"Mercedes":1}
print(Automoviles)

Automoviles = {"ferrari": 9018293, "lambo": 119238}
print(Automoviles)
Automoviles.update({"renauld": 138475, "pontiac": 85739})
print(Automoviles)


oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
oscar_winners.update({"Supporting Actress": "Viola Davis"})
oscar_winners["Best Picture"] = "Moonlight"
oscar_winners["Animated Feature"] = "No te metas con zohan"
print(oscar_winners)

drinks =["espresso","chai","decaf","drip"]
caffeine=[64,40,0,120]
zipped_drinks=zip(drinks,caffeine)
drinks_to_caffeine={key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)
