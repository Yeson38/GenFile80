#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil
import glob

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample_files")
D_OTH = "09_other"

def fix_ttf():
    """复制系统自带的字体，重命名为 sample.ttf，确保有效"""
    print("[*] 正在修复 TTF ...")
    font_candidates = glob.glob(r"C:\Windows\Fonts\*.ttf")
    
    target_font = None
    # 优先找 Arial 或 Calibri
    for f in font_candidates:
        if "arial.ttf" in f.lower() or "calibri.ttf" in f.lower():
            target_font = f
            break
    if not target_font and font_candidates:
        target_font = font_candidates[0]
        
    if target_font:
        dest = os.path.join(ROOT, D_OTH, "sample.ttf")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy(target_font, dest)
        print(f"  [OK] sample.ttf 修复成功 (来源: {os.path.basename(target_font)})")
    else:
        print("  [失败] 未能找到系统字体文件")

def fix_dxf():
    """生成一个包含真实图形（直线+圆）的 DXF 文件"""
    print("[*] 正在修复 DXF ...")
    dxf_content = (
        "0\nSECTION\n2\nENTITIES\n"
        "0\nLINE\n8\n0\n"          # 新建一条直线
        "10\n0.0\n20\n0.0\n"       # 起点 (0,0)
        "11\n100.0\n21\n100.0\n"   # 终点 (100,100)
        "0\nCIRCLE\n8\n0\n"        # 新建一个圆
        "10\n50.0\n20\n50.0\n"     # 圆心 (50,50)
        "40\n25.0\n"               # 半径 25
        "0\nENDSEC\n0\nEOF\n"
    )
    
    dest = os.path.join(ROOT, D_OTH, "sample.dxf")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="ascii") as f:
        f.write(dxf_content)
    print("  [OK] sample.dxf 修复成功 (已写入直线和圆形)")

if __name__ == "__main__":
    print("=" * 60)
    print("  字体与 DXF 文件修复补丁")
    print(f"  目标目录: {ROOT}")
    print("=" * 60)
    if not os.path.isdir(ROOT):
        print(f"[!] 找不到目录 {ROOT}，请先运行 gen_all.py")
    else:
        fix_ttf()
        fix_dxf()
        print("\n修复完成！请重新双击打开这两个文件进行验证。")