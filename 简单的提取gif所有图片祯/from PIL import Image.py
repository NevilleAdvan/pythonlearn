from PIL import Image
import os

def get_gif_info(gif_path):
    # 打开GIF文件
    gif = Image.open(gif_path)
    
    # 获取GIF基本信息
    info = {
        "format": gif.format,
        "mode": gif.mode,
        "size": gif.size,
        "is_animated": getattr(gif, "is_animated", False),
        "n_frames": getattr(gif, "n_frames", 1),
        "duration": gif.info.get("duration", 0)
    }
    
    return info

def extract_and_resize_frames_from_gif(gif_path, output_directory, target_size, start_number):
    # 打开GIF文件
    gif = Image.open(gif_path)
    
    # 确保输出目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # 提取并保存每一帧
    frame_number = 0
    while True:
        try:
            # 设置当前帧
            gif.seek(frame_number)
        except EOFError:
            # 如果到达文件末尾，退出循环
            break
        
        # 复制当前帧并调整大小
        frame = gif.copy()
        frame = frame.resize(target_size, Image.LANCZOS)
        
        # 生成新的文件名
        new_name = f"{start_number + frame_number}.png"
        
        # 保存当前帧为PNG文件
        frame.save(os.path.join(output_directory, new_name), 'PNG')
        
        frame_number += 1

    print(f"Extracted and resized {frame_number} frames from {gif_path} to {output_directory}")

# 使用示例
gif_path = r"D:\test\need.gif"
output_directory = r"D:\test\frames"
target_size = (800, 480)
start_number = 25000

# 获取并打印GIF信息
gif_info = get_gif_info(gif_path)
print("GIF Information:")
for key, value in gif_info.items():
    print(f"{key}: {value}")

# 提取并保存帧
extract_and_resize_frames_from_gif(gif_path, output_directory, target_size, start_number)