def convert(buchstaben):  # Buchstaben werden in Zahlen convertiert, damit man sie einfacher vergleichen kann
    if buchstaben == "Ä":
        erg = 0
    elif buchstaben == "ä":
        erg = 0
    elif buchstaben == "Ö":
        erg = 14
    elif buchstaben == "ö":
        erg = 14
    elif buchstaben == "Ü":
        erg = 20
    elif buchstaben == "ü":
        erg = 20
    elif buchstaben == "ß":
        erg = 18
    elif 64 < ord(buchstaben) < 91:  # wenn es Großbuchstaben sind
        erg = ord(buchstaben) - 65
    else:  # wenn es Kleinbuchstaben sind
        nummer_buchstabe = ord(buchstaben)
        erg = nummer_buchstabe - 97

    return erg  # das Ergebnis des Buchstabens wird zurückgegeben
