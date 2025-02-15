import subprocess
import os

# 遍历当前目录及其子目录中的所有 MP4 文件
for root, dirs, files in os.walk(".\\工业级别端到端实战教程\\第三章"):
    for file in files:
        if file.endswith(".mp4") and file.startswith("3-"):
            file_path = os.path.join(root, file)

            analyze_command = ["recover_mp4.exe", file_path, "--analyze"]
            analyze_output = subprocess.run(analyze_command, capture_output=True, text=True)
            
            suggested_command = analyze_output.stdout.strip().split("\n")[-1].split()
            suggested_command[-1] = f"{file_path[:-4]}_recovered.mp4"
            recover_command = ["recover_mp4.exe", file_path, "result.h264", "result.aac", "--lav"]
            subprocess.run(recover_command)
            
            subprocess.run(suggested_command)