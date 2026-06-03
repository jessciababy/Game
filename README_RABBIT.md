# Dancing Rabbit 🐰

一个可爱的跳舞兔子小游戏，使用 Python 和 Pygame 实现。

## 功能特性

- 🐰 **可爱的兔子角色** - 粉色的兔子设计
- 💃 **多种舞蹈动作**：
  - **跳跃 (Jump)** - 兔子向上跳跃，耳朵摇晃
  - **旋转 (Spin)** - 兔子旋转身体
  - **摇晃 (Wiggle)** - 兔子左右摇晃身体
  - **蹦跳 (Hop)** - 连续蹦跳动作

- 🎨 **流畅的动画** - 使用正弦波函数实现平滑的运动
- ⌨️ **简单的控制** - 按 ESC 键退出

## 安装要求

- Python 3.6+
- Pygame

## 安装依赖

```bash
pip install pygame
```

## 运行程序

```bash
python dancing_rabbit.py
```

## 游戏说明

1. 运行程序后，窗口中会出现一只粉色的兔子
2. 兔子会自动循环表演四种舞蹈动作
3. 按 `ESC` 键退出游戏

## 代码结构

- `DancingRabbit` 类 - 管理兔子的动画和状态
  - `update()` - 更新动画帧
  - `draw()` - 绘制兔子
  - `_draw_jumping_rabbit()` - 绘制跳跃动作
  - `_draw_spinning_rabbit()` - 绘制旋转动作
  - `_draw_wiggling_rabbit()` - 绘制摇晃动作
  - `_draw_hopping_rabbit()` - 绘制蹦跳动作

## 可自定义选项

编辑 `dancing_rabbit.py` 可以修改：

- `SCREEN_WIDTH` 和 `SCREEN_HEIGHT` - 窗口大小
- `PINK`、`LIGHT_PINK` 等颜色 - 兔子和背景颜色
- `FPS` - 帧率（默认 60）
- `dance_moves` 列表 - 添加或修改舞蹈动作

## 扩展想法

- 🎵 添加背景音乐和音效
- 🎮 添加键盘控制让用户控制兔子
- 🌈 添加更多颜色和主题
- 👥 添加多只兔子
- 🎯 转换为完整的游戏，添加得分机制

享受你的舞蹈兔子！🐰💃
