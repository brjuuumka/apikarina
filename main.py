
import os
import sys
import pygame
import requests


def ll(x, y):
    return '{0}, {1}'.format(x, y)


class MapParams(object):
    def __init__(self):
        self.lat = 55.364880
        self.lon = 50.606852
        self.zoom = 17
        self.type = 'map'

    # def ll(self):
        # return ll(self.lon, self.lat)


def load_map(mp):
    map_requests = 'https://static-maps.yandex.ru/1.x/?ll={lon},{lat}&z={z}&l={type}'.format(lon=mp.lon,
                                                                                             lat=mp.lat,
                                                                                             z=mp.zoom,
                                                                                             type=mp.type)
    response = requests.get(map_requests)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_requests)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = 'map.png'
    try:
        with open(map_file, 'wb') as file:
            file.write(response.content)
    except IOError as ex:
        print('Ошибка')
        sys.exit(2)

    return map_file
=======
import pygame
import requests
import sys
import os


class MapsParams:
    def __init__(self):
        self.lat = 0  # Центр карты
        self.lon = 0  # Широта x
        self.zoom = 17.6  # Увеличение
        self.type = "map"  # Тип карты

    def ll(self):
        return self.lon, self.lat, self.zoom


# https://static-maps.yandex.ru/1.x/?azimuth=0.15&ll=50.607,55.3647&z=17&l=map

def load_map(lat, lon, zoom, type):
     map_request = f"https://static-maps.yandex.ru/1.x/?ll={lat},{lon}&z={zoom}&l={type}"
     response = requests.get(map_request)
     if not response:
         print("Ошибка выполнения запроса")
         print(map_request)
         print("Http статус:", response.status_code)
         sys.exit(1)

    map_file = "map.png"
    try:
        pass
    except IOError as error:
        print(error)
>>>>>>> origin/master


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
<<<<<<< HEAD
    mp = MapParams()

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            break

        map_file = load_map(mp)
        screen.blit(pygame.image.load(map_file), (0, 0))
=======
    mp = MapsParams()

    running = True
    while running:

        screen.blit()
>>>>>>> origin/master
        pygame.display.flip()

    pygame.quit()
    os.remove(map_file)


if __name__ == '__main__':
    main()
