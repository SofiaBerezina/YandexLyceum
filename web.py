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

    def increase(self):
        if 0.001 <= self.spn <= 0.01:
            self.spn -= 0.001
        elif 0.01 <= self.spn <= 0.1:
            self.spn -= 0.01
        elif 0.1 <= self.spn <= 1:
            self.spn -= 0.1
        elif 1 <= self.spn <= 10:
            self.spn -= 1
        elif 20 <= self.spn <= 90:
            self.spn -= 10

    def decrease(self):
        if 0.001 <= self.spn <= 0.01:
            self.spn += 0.001
        elif 0.01 <= self.spn <= 0.1:
            self.spn += 0.01
        elif 0.1 <= self.spn <= 1:
            self.spn += 0.1
        elif 1 <= self.spn <= 10:
            self.spn += 1
        elif 10 <= self.spn <= 80:
            self.spn += 10

    def update(self, key):
        if key == pygame.K_PAGEUP:
            self.increase()
        elif key == pygame.K_PAGEDOWN:
            self.decrease()


def get_ip(params):
    api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(api_server, params)
    if not response:
        print('Что-то пошло не так', response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit()
    with open(MAP_FILE, 'ab') as file:
        file.write(response.content)


def draw_map(map):
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    screen.blit(pygame.image.load(MAP_FILE), (0, 0))
    pygame.display.flip()
    r = True
    while r:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                map.update(event.key)
                get_ip(map.make_dict())
        screen.blit(pygame.image.load(MAP_FILE), (0, 0))
        pygame.display.flip()

    pygame.quit()


longitude = 56.26108
latitude = 58.007368
spn = 0.001
l_param = 'map'
maps = Map(longitude, latitude, spn, l_param)
get_ip(maps.make_dict())
draw_map(maps)