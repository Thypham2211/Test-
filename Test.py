import random

def zahlenraten():
    print("Willkommen zum Zahlenraten-Spiel!")
    geheime_zahl = random.randint(1, 100)  # Zufällige Zahl zwischen 1 und 100
    versuche = 0

    while True:
        try:
            tipp = int(input("Gib eine Zahl zwischen 1 und 100 ein: "))
            versuche += 1

            if tipp < 1 or tipp > 100:
                print("Die Zahl muss zwischen 1 und 100 liegen!")
                continue

            if tipp < geheime_zahl:
                print("Zu niedrig! Versuch es nochmal.")
            elif tipp > geheime_zahl:
                print("Zu hoch! Versuch es nochmal.")
            else:
                print(f"Glückwunsch! Du hast die Zahl {geheime_zahl} nach {versuche} Versuchen erraten.")
                break

        except ValueError:
            print("Bitte gib eine gültige Zahl ein.")

if __name__ == "__main__":
    zahlenraten()

