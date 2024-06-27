import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

def run_game():

# 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建Play按钮
    play_button = Button(ai_settings,screen,"Play")

    ship = Ship(ai_settings,screen)   # 创建Ship实例
    alien = Alien(ai_settings,screen)  # 创建Alien实例
    stats = GameStats(ai_settings) # 创建一个用于存储游戏统计信息的实例
    bullets = Group() #创建一个用于存储子弹的数组
    aliens = Group() # 创建一个外星人编组
    gf.create_fleet(ai_settings,screen,ship,aliens)# 创建外星人群

# 开始游戏的主循环
    while True:
    # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        if stats.game_active:
            # 监视飞船位置更新
            ship.update()
            # 子弹控制
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            # 更新外星人的位置
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)
run_game()