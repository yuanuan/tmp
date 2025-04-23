def split_file(file_path, chunk_size):
    """
    将大文件分割成多个小文件
    :param file_path: 大文件路径
    :param chunk_size: 每个小文件的大小（字节）
    """
    part_num = 1  # 分割文件的编号
    with open(file_path, 'rb') as f:
        while True:
            # 读取指定大小的数据
            chunk = f.read(chunk_size)
            if not chunk:
                break  # 文件读取完毕

            # 写入小文件
            part_file = f"{file_path}.part{part_num}"
            with open(part_file, 'wb') as part:
                part.write(chunk)

            print(f"Created: {part_file}")
            part_num += 1

# 示例：将文件分割为 1MB 的小文件
split_file("model_motr_final.pth", 24 * 1024 * 1024)  # 1MB