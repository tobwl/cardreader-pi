from PIL import Image, ImageDraw, ImageFont
import settings
import importlib

WIDTH = 250
HEIGHT = 122

def render_sprite(sprite, pixel_size, offset_x, offset_y, draw):
    for y, row in enumerate(sprite):
        for x, char in enumerate(row):
            if char == "X":
                draw.rectangle(
                    (offset_x + x*pixel_size,
                    offset_y + y*pixel_size,
                    offset_x + (x+1)*pixel_size - 1,
                    offset_y + (y+1)*pixel_size - 1),
                    fill=0
                )
                
def render_wifi(bars, draw):
    x = 225
    y = 10
    for i in range(4):
        height = (i + 1) * 2
        if i < bars:
            draw.rectangle((x, y - height, x + 2, y), fill=0)
        else:
            draw.rectangle((x, y - height, x + 2, y), outline=0)
        x += 4

def render_screen(stats, config):
    importlib.reload(sprites)
    
    image = Image.new("1", (WIDTH, HEIGHT), 255)
    draw = ImageDraw.Draw(image)

    font_small = ImageFont.truetype(
        config['font'], 10
    )
    font_title = ImageFont.truetype(
        config["font_bold"], 10
    )
    
    # Top section
    draw.line((10, 12, 239, 12), fill=0)

    # WiFi bars
    render_wifi(stats['wifi'], draw)
        
    # System Info
    draw.text((10, 0), "UP", font=font_title, fill=0)
    draw.text((30, 0), f"{stats['uptime']}", font=font_small, fill=0)
    
    
    # Bottom section
    draw.line((10, 110, 239, 110), fill=0)
    
    # System Info 2
    draw.text((10, 109), "BUSY" if stats['busy'] else "FREE", font=font_title, fill=0)

    return image