# 📦 GenFile80

> 一键在 Windows 下生成 80+ 种真实、可正常打开的示例文件。

在开发过程中，我们经常需要测试上传、杀毒、解析或下载功能，却常常苦于找不到各种格式的测试文件。
本项目旨在彻底解决这一痛点！**不仅生成的格式齐全，更保证每一个文件都有真实内容，能被对应的软件正常打开。**

## ✨ 核心特性

- 📁 **80+ 种格式全覆盖**：涵盖文档、表格、图片、音视频、压缩包、代码、字体、3D模型等。
- 💯 **100% 真实有效**：拒绝 0 字节假文件。`.ttf` 能预览，`.dxf` 有图形，`.docx` 排版正常。
- 🛡️ **全自动 COM 无弹窗**：通过 `DispatchEx` 调用本机 Office 生成 `.doc/.ppt/.xls`，彻底禁用弹窗，防止卡死。
- 🔧 **外部工具智能探测**：自动寻找并调用 `ffmpeg`、`7-Zip`、`WinRAR`、`Calibre` 等工具生成音视频和专有压缩包。
- 🧹 **智能清理机制**：运行前自动检测旧样本文件，询问并一键清理，防止文件冲突和数据库表重复报错。
- 📊 **生成报告一览无余**：执行结束后，分类列出成功、跳过、失败的格式及具体原因，绝不糊弄。

## 🚀 快速开始

### 1. 安装依赖

确保您已安装 Python 3.7+，然后在终端运行：

```bash
pip install python-docx openpyxl python-pptx Pillow reportlab odfpy EbookLib fonttools pycdlib py7zr pywin32
```

### 2. 一键生成

将 `gen.py` 保存到本地，在终端中运行：

```bash
python gen.py
```

按照提示确认清理旧文件后，所有样本文件将生成在 `sample_files/` 目录中。

## 🛠️ 环境增强（可选）

为了生成 **mp3/mp4/flac** 等媒体文件、**7z** 压缩包、**mobi/azw3** 电子书，请确保以下工具已安装且路径已加入系统环境变量 `PATH`：
- [FFmpeg](https://ffmpeg.org/download.html) （音视频）
- [7-Zip](https://www.7-zip.org/) （7z 压缩包，亦可生成）
- [WinRAR](https://www.win-rar.com/) （rar 压缩包）
- [Calibre](https://calibre-ebook.com/) （mobi/azw3 电子书）
