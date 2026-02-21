

import os
import json

# 自动扫描chapters文件夹里所有的txt文件
if not os.path.exists('chapters'):
    print("❌ 错误：找不到chapters文件夹，请确认脚本放在正确的目录里")
    input("按回车退出")
    exit()

txt_files = [f for f in os.listdir('chapters') if f.lower().endswith('.txt')]

# 生成filelist.json
filelist_data = {"files": txt_files}
with open('filelist.json', 'w', encoding='utf-8') as f:
    json.dump(filelist_data, f, ensure_ascii=False, indent=2)

print(f"✅ 成功生成filelist.json！共找到 {len(txt_files)} 个txt文件")
print("📋 已自动识别的文件：")
for i, file in enumerate(txt_files, 1):
    print(f"  {i}. {file}")
input("\n按回车退出")
