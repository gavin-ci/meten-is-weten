
answer = input("Is de kaas geel?")
if answer == "ja":
        answer = input("Zitten er gaten in?")
        if answer == "ja":
                answer = input("Is de kaas belachelijk duur?")
                if answer == "nee":
                        print("Leerdammer")
                elif answer == "ja":
                        print("Emmenthaler")
        elif answer == "nee":
                answer = input("Is de kaas hard als steen?")
                if answer == "ja":
                    print("Parnigiano Reggiano")
                elif answer == "nee":
                    print("Goudse Kaas")
                

elif answer == "nee":
        answer = input("Heeft de kaas blauwe schimmels?")
        if answer == "ja":
                answer = input("Heeft de kaas een korst?")
                if answer == "nee":
                    print("Fourne d'Ambert")
                elif answer == "ja":
                    print("Bleu de Rochbaron")
        elif answer == "nee":
                answer = input("Heeft de kaas een korst?")
                if answer == "ja":
                    print("Camembert")
                elif answer == "nee":
                    print("Mozzarella")
        