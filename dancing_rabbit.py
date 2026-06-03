import pygame
import math
import sys

# 初始化 Pygame
pygame.init()

# 屏幕设置
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dancing Rabbit")

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)
LIGHT_PINK = (255, 218, 224)

# 时钟和帧率
clock = pygame.time.Clock()
FPS = 60

class DancingRabbit:
    """可以跳舞的兔子类"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 30
        self.animation_time = 0
        self.dance_moves = [
            {"name": "jump", "duration": 15},
            {"name": "spin", "duration": 20},
            {"name": "wiggle", "duration": 15},
            {"name": "hop", "duration": 10}
        ]
        self.current_move_index = 0
        self.move_time = 0
        
    def update(self):
        """更新兔子的动画"""
        self.animation_time += 1
        self.move_time += 1
        
        # 获取当前舞蹈动作
        current_move = self.dance_moves[self.current_move_index]
        
        # 如果当前舞蹈动作完成，切换到下一个
        if self.move_time >= current_move["duration"]:
            self.move_time = 0
            self.current_move_index = (self.current_move_index + 1) % len(self.dance_moves)
    
    def draw(self, surface):
        """绘制兔子"""
        current_move = self.dance_moves[self.current_move_index]
        progress = self.move_time / current_move["duration"]
        
        if current_move["name"] == "jump":
            self._draw_jumping_rabbit(surface, progress)
        elif current_move["name"] == "spin":
            self._draw_spinning_rabbit(surface, progress)
        elif current_move["name"] == "wiggle":
            self._draw_wiggling_rabbit(surface, progress)
        elif current_move["name"] == "hop":
            self._draw_hopping_rabbit(surface, progress)
    
    def _draw_jumping_rabbit(self, surface, progress):
        """绘制跳跃的兔子"""
        # 使用正弦波实现跳跃动画
        jump_height = math.sin(progress * math.pi) * 50
        current_y = self.y - jump_height
        
        # 绘制身体
        pygame.draw.ellipse(surface, PINK, (self.x - self.size, current_y - self.size, self.size * 2, self.size * 2.5))
        
        # 绘制头部
        pygame.draw.circle(surface, PINK, (int(self.x), int(current_y - self.size * 2)), self.size)
        
        # 绘制眼睛
        pygame.draw.circle(surface, BLACK, (int(self.x - 8), int(current_y - self.size * 2 - 5)), 3)
        pygame.draw.circle(surface, BLACK, (int(self.x + 8), int(current_y - self.size * 2 - 5)), 3)
        
        # 绘制鼻子
        pygame.draw.circle(surface, BLACK, (int(self.x), int(current_y - self.size * 2 + 3)), 2)
        
        # 绘制长耳朵
        ear_offset = math.sin(progress * math.pi * 2) * 5
        pygame.draw.line(surface, PINK, 
                        (int(self.x - 10), int(current_y - self.size * 2 - 10)), 
                        (int(self.x - 10 + ear_offset), int(current_y - self.size * 2 - 40)), 8)
        pygame.draw.line(surface, PINK, 
                        (int(self.x + 10), int(current_y - self.size * 2 - 10)), 
                        (int(self.x + 10 - ear_offset), int(current_y - self.size * 2 - 40)), 8)
        
        # 绘制腿
        leg_offset = abs(math.sin(progress * math.pi)) * 10
        pygame.draw.line(surface, PINK, (int(self.x - 12), int(current_y + self.size)), 
                        (int(self.x - 12), int(current_y + self.size + 15 - leg_offset)), 5)
        pygame.draw.line(surface, PINK, (int(self.x + 12), int(current_y + self.size)), 
                        (int(self.x + 12), int(current_y + self.size + 15 - leg_offset)), 5)
    
    def _draw_spinning_rabbit(self, surface, progress):
        """绘制旋转的兔子"""
        angle = progress * math.pi * 2
        
        # 使用旋转变换
        # 这里简化处理，使用基础形状绘制
        body_x = self.x + math.cos(angle) * 10
        body_y = self.y + math.sin(angle) * 10
        
        # 绘制身体
        pygame.draw.ellipse(surface, PINK, (self.x - self.size, self.y - self.size, self.size * 2, self.size * 2.5))
        
        # 绘制头部（旋转）
        head_x = self.x + math.cos(angle) * self.size * 1.5
        head_y = self.y - self.size * 2 + math.sin(angle) * self.size
        pygame.draw.circle(surface, PINK, (int(head_x), int(head_y)), self.size)
        
        # 绘制眼睛
        pygame.draw.circle(surface, BLACK, (int(head_x - 8), int(head_y - 5)), 3)
        pygame.draw.circle(surface, BLACK, (int(head_x + 8), int(head_y - 5)), 3)
        
        # 绘制旋转的耳朵
        ear_length = 30
        ear1_x = int(self.x + math.cos(angle + math.pi/4) * ear_length)
        ear1_y = int(self.y - self.size * 2 + math.sin(angle + math.pi/4) * ear_length)
        pygame.draw.line(surface, PINK, (int(self.x), int(self.y - self.size * 2)), (ear1_x, ear1_y), 6)
    
    def _draw_wiggling_rabbit(self, surface, progress):
        """绘制摇晃的兔子"""
        wiggle_offset = math.sin(progress * math.pi * 4) * 10
        current_x = self.x + wiggle_offset
        
        # 绘制身体
        pygame.draw.ellipse(surface, PINK, (current_x - self.size, self.y - self.size, self.size * 2, self.size * 2.5))
        
        # 绘制头部
        pygame.draw.circle(surface, PINK, (int(current_x), int(self.y - self.size * 2)), self.size)
        
        # 绘制眼睛
        pygame.draw.circle(surface, BLACK, (int(current_x - 8), int(self.y - self.size * 2 - 5)), 3)
        pygame.draw.circle(surface, BLACK, (int(current_x + 8), int(self.y - self.size * 2 - 5)), 3)
        
        # 绘制鼻子
        pygame.draw.circle(surface, BLACK, (int(current_x), int(self.y - self.size * 2 + 3)), 2)
        
        # 绘制摇晃的耳朵
        ear_wiggle = math.sin(progress * math.pi * 6) * 8
        pygame.draw.line(surface, PINK, 
                        (int(current_x - 10), int(self.y - self.size * 2 - 10)), 
                        (int(current_x - 10 + ear_wiggle), int(self.y - self.size * 2 - 40)), 8)
        pygame.draw.line(surface, PINK, 
                        (int(current_x + 10), int(self.y - self.size * 2 - 10)), 
                        (int(current_x + 10 - ear_wiggle), int(self.y - self.size * 2 - 40)), 8)
    
    def _draw_hopping_rabbit(self, surface, progress):
        """绘制原地蹦跳的兔子"""
        # 多次跳跃
        hop_count = 3
        hop_progress = (progress * hop_count) % 1.0
        hop_height = math.sin(hop_progress * math.pi) * 30
        current_y = self.y - hop_height
        
        # 绘制身体
        pygame.draw.ellipse(surface, PINK, (self.x - self.size, current_y - self.size, self.size * 2, self.size * 2.5))
        
        # 绘制头部
        pygame.draw.circle(surface, PINK, (int(self.x), int(current_y - self.size * 2)), self.size)
        
        # 绘制眼睛
        pygame.draw.circle(surface, BLACK, (int(self.x - 8), int(current_y - self.size * 2 - 5)), 3)
        pygame.draw.circle(surface, BLACK, (int(self.x + 8), int(current_y - self.size * 2 - 5)), 3)
        
        # 绘制鼻子
        pygame.draw.circle(surface, BLACK, (int(self.x), int(current_y - self.size * 2 + 3)), 2)
        
        # 绘制竖立的耳朵
        pygame.draw.line(surface, PINK, 
                        (int(self.x - 10), int(current_y - self.size * 2 - 10)), 
                        (int(self.x - 10), int(current_y - self.size * 2 - 40)), 8)
        pygame.draw.line(surface, PINK, 
                        (int(self.x + 10), int(current_y - self.size * 2 - 10)), 
                        (int(self.x + 10), int(current_y - self.size * 2 - 40)), 8)
        
        # 绘制腿
        pygame.draw.line(surface, PINK, (int(self.x - 12), int(current_y + self.size)), 
                        (int(self.x - 12), int(current_y + self.size + 15)), 5)
        pygame.draw.line(surface, PINK, (int(self.x + 12), int(current_y + self.size)), 
                        (int(self.x + 12), int(current_y + self.size + 15)), 5)


def main():
    """主程序"""
    rabbit = DancingRabbit(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # 更新
        rabbit.update()
        
        # 绘制
        screen.fill(WHITE)
        
        # 绘制舞台背景
        pygame.draw.circle(screen, LIGHT_PINK, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 150)
        
        # 绘制兔子
        rabbit.draw(screen)
        
        # 绘制提示文本
        font = pygame.font.Font(None, 24)
        text = font.render("Press ESC to exit", True, BLACK)
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
