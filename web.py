import sys
import requests
import pygame

MAP_FILE = 'map.png'

class Map:
    def __init__(self, long, lat, spn, l_params):
        self.longitude = long
        self.latitude = lat
        self.spn = spn
        self.l_params = l_params

    def make_dict(self):
        self.d = {}
        self.d['ll'] = ','.join([str(self.longitude), str(self.latitude)])
        self.d['l'] = self.l_params
        self.d['spn'] = ','.join([str(self.spn), str(self.spn)])
        return self.d


def get_ip(params):
    api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(api_server, params)
    if not response:
        print('Что-то пошло не так', response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit()
    with open(MAP_FILE, 'wb') as file:
        file.write(response.content)


def draw_map():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(MAP_FILE), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


longitude = 56.26108
latitude = 58.007368
spn = 0.001
l_param = 'map'
maps = Map(longitude, latitude, spn, l_param)
get_ip(maps.make_dict())
draw_map()