import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from tkinter import Tk
from interface import Loc

# Fonction pour traiter le numéro de téléphone
def process_phone_number(phone_number, update_map_callback):
    pepnumber = phonenumbers.parse(phone_number, None)
    location = geocoder.description_for_number(pepnumber, "en")
    print(f"Location: {location}")

    service_pro = phonenumbers.parse(phone_number)
    service_provider = carrier.name_for_number(service_pro, "en")
    print(f"Service Provider: {service_provider}")

    # Utilisation de OpenCage pour obtenir la géolocalisation
    key = '6b72761fdfe2475db9294e91865f17d9'  # Remplacez par votre clé API OpenCage
    geocoder_api = OpenCageGeocode(key)
    query = str(location)
    results = geocoder_api.geocode(query)

    if results:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print(f"Latitude: {lat}, Longitude: {lng}")

        # Création d'une carte avec folium
        myMap = folium.Map(location=[lat, lng], zoom_start=4)
        folium.Marker([lat, lng], popup=location).add_to(myMap)

        # Sauvegarde de la carte dans un fichier HTML temporaire
        map_html = "location.html"
        myMap.save(map_html)
        print("Map saved as location.html")

        # Mise à jour de la carte dans l'interface
        update_map_callback(map_html)
    else:
        print("No results found for the given location query.")

def main():
    root = Tk()

    # Fonction pour gérer le numéro de téléphone entré dans l'interface
    def handle_phone_number(phone_number):
        print(f"Phone number entered in interface: {phone_number}")
        process_phone_number(phone_number, obj.update_map)

    # Création de l'objet Loc et passage de la fonction callback
    obj = Loc(root, handle_phone_number)
    root.mainloop()

if __name__ == "__main__":
    main()
