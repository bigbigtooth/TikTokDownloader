<div align="center">
<img src="./static/images/DouK-Downloader.png" alt="DouK-Downloader" height="256" width="256"><br>
<h1>DouK-Downloader</h1>
<p>简体中文 | <a href="README_EN.md">English</a></p>
<a href="https://trendshift.io/repositories/6222" target="_blank"><img src="https://trendshift.io/api/badge/repositories/6222" alt="" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<br>
<img alt="GitHub" src="https://img.shields.io/github/license/JoeanAmier/TikTokDownloader?style=flat-square">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/JoeanAmier/TikTokDownloader?style=flat-square&color=55efc4">
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/JoeanAmier/TikTokDownloader?style=flat-square&color=fda7df">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/JoeanAmier/TikTokDownloader?style=flat-square&color=a29bfe">
<br>
<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.12-b8e994?style=flat-square&logo=python&labelColor=3dc1d3">
<img alt="GitHub release (with filter)" src="https://img.shields.io/github/v/release/JoeanAmier/TikTokDownloader?style=flat-square&color=48dbfb">
<img src="https://img.shields.io/badge/Sourcery-enabled-884898?style=flat-square&color=1890ff" alt="">
<img alt="Static Badge" src="https://img.shields.io/badge/Docker-badc58?style=flat-square&logo=docker">
<img alt="GitHub all releases" src="https://img.shields.io/github/downloads/JoeanAmier/TikTokDownloader/total?style=flat-square&color=ffdd59">
</div>

---

## 📖 项目说明

本项目是基于 [TikTokDownloader](https://github.com/JoeanAmier/TikTokDownloader) 的优化版本，专注于提供**API服务器模式**的增强功能。

> **💡 重要提示**  
> 如果您希望了解完整的 TikTokDownloader 项目功能、详细文档、GUI界面等内容，  
> **强烈建议访问原项目**: 👉 **[https://github.com/JoeanAmier/TikTokDownloader](https://github.com/JoeanAmier/TikTokDownloader)**

### ✨ 本分支特色

- 🚀 **命令行直接启动API服务器** - 无需交互式选择
- ⚙️ **灵活配置参数** - 自定义主机、端口、日志级别
- 🔄 **自动化配置** - 自动接受免责声明并设置默认语言
- 📚 **完整API文档** - 内置Swagger UI和ReDoc
- 🔗 **向后兼容** - 完全支持原有的交互式模式

---

## 🚀 快速开始

### 基础用法

```bash
# 启动默认配置的API服务器 (127.0.0.1:5555)
python main.py --server
```

### 高级用法

```bash
# 自定义主机和端口
python main.py --server --host 0.0.0.0 --port 8080

# 设置日志级别
python main.py --server --log-level debug

# 生产环境部署
python main.py --server --host 0.0.0.0 --port 8000 --log-level warning
```

---

## ⚙️ 命令行参数

```bash
python main.py [选项]
```

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--server` | 启动API服务器模式 | - |
| `--host HOST` | API服务器主机地址 | `127.0.0.1` |
| `--port PORT` | API服务器端口 | `5555` |
| `--log-level` | 日志级别 (`critical`/`error`/`warning`/`info`/`debug`/`trace`) | `info` |
| `-h, --help` | 显示帮助信息 | - |

---

## 📚 API 文档

服务器启动后，可通过以下地址访问API文档：

| 文档类型 | 访问地址 | 说明 |
|----------|----------|------|
| **Swagger UI** | `http://your-host:your-port/docs` | 交互式API文档 |
| **ReDoc** | `http://your-host:your-port/redoc` | 美观的API文档 |

**示例**：如果服务器运行在 `127.0.0.1:8080`
- Swagger UI: http://127.0.0.1:8080/docs
- ReDoc: http://127.0.0.1:8080/redoc

---

## 💡 使用示例

### 1. 查看帮助信息
```bash
python main.py --help
```

### 2. 本地开发
```bash
# 本地测试，调试模式
python main.py --server --log-level debug
```

### 3. 局域网访问
```bash
# 允许局域网内其他设备访问
python main.py --server --host 0.0.0.0 --port 8080
```

### 4. 生产环境
```bash
# 优化日志输出，提升性能
python main.py --server --host 0.0.0.0 --port 8000 --log-level warning
```

---

## ⚠️ 注意事项

- 📁 **首次运行**: 程序会自动创建必要的配置文件
- 🍪 **Cookie配置**: 需要按照原项目说明进行Cookie设置
- 🔒 **安全提醒**: 公网部署时请设置适当的安全措施
- 🔄 **端口占用**: 确保指定端口未被其他程序占用

---

## 🔧 兼容性说明

本优化版本**完全向后兼容**原有功能：

```bash
# 原有的交互式模式仍然可用
python main.py
```

---

## 🆘 故障排除

遇到问题时，请按以下步骤排查：

1. **检查端口占用**
   ```bash
   # Linux/macOS
   lsof -i :5555
   
   # Windows
   netstat -ano | findstr :5555
   ```

2. **查看详细日志**
   ```bash
   python main.py --server --log-level debug
   ```

3. **验证配置文件**
   - 检查Cookie配置是否正确
   - 确认配置文件权限

---

## 📖 更多资源

### 🔗 相关链接

- **原项目地址**: [https://github.com/JoeanAmier/TikTokDownloader](https://github.com/JoeanAmier/TikTokDownloader)
- **详细文档**: 请查看原项目的完整文档
- **GUI版本**: 原项目提供图形界面版本
- **更多功能**: 原项目包含更多采集功能和使用教程

### 🤝 贡献与支持

如果您在使用过程中遇到问题或有改进建议：
1. 优先查看原项目的Issues和文档
2. 对于API服务器模式特有的问题，可以在本项目提Issue

---

<div align="center">

**✨ 感谢使用 DouK-Downloader API 服务器模式！**

如需了解更多功能，请访问 **[原项目](https://github.com/JoeanAmier/TikTokDownloader)** 🚀

</div>
