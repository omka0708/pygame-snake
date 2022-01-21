from pygame.mixer import Sound, init
init()
sounds = {
    'menu_1': Sound("sound/menu_1.wav"),
    'menu_2': Sound("sound/menu_2.wav"),
    'apple': Sound("sound/apple.wav"),
    'emerald': Sound("sound/emerald.wav"),
    'win': Sound("sound/win.wav"),
    'lose_1': Sound("sound/lose_1.wav"),
    'lose_2': Sound("sound/lose_2.wav")
}
for sound in sounds.values():
    sound.set_volume(0.2)
