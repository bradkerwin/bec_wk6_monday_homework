import requests
import json


def planet_info():
    response = requests.get("https://api.le-systeme-solaire.net/rest/bodies")
    planets = response.json()['bodies']
    planets_only = []
    for planet in planets:
        if planet['isPlanet']:
            planets_only.append(planet)
            name = planet['name'] 
            mass = planet['mass']['massValue'] 
            orbit_period = planet['sideralOrbit'] 
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    return planets_only
planet_info()


def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0
    for planet in planets:
        
        if planet["mass"]:
            mass_value = planet["mass"]["massValue"]
            if mass_value > max_mass:
                max_mass = mass_value
                heaviest_planet = planet
    print(heaviest_planet)

planets = planet_info()
find_heaviest_planet(planets)
