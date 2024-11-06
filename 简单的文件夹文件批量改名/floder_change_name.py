import os

def rename_png_files(directory, start_number):
    # 获取目录下的所有文件
    files = os.listdir(directory)
    
    # 过滤出所有的PNG文件
    png_files = [f for f in files if f.lower().endswith('.png')]
    
    # 按照文件名排序，确保重命名顺序一致
    png_files.sort()
    
    # 重命名文件
    for i, filename in enumerate(png_files):
        new_name = f"{start_number + i}.png"
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")

# 使用示例
directory = r"D:\a_fantasyui\linux-mtk-ui-resource\resource\resource_1280x720_hmi3.0\main\22000_22999_icon"
start_number = 22000
rename_png_files(directory, start_number)
