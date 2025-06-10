<div align="center">
<img src="./static/images/DouK-Downloader.png" alt="DouK-Downloader" height="256" width="256"><br>
<h1>DouK-Downloader(Fork)</h1>
<p><a href="README.md">简体中文</a> | English</p>
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

## 📖 Project Description

This project is an optimized version based on [TikTokDownloader](https://github.com/JoeanAmier/TikTokDownloader), focusing on enhanced **API server mode** functionality.

> **💡 Important Notice**  
> If you want to learn about the complete TikTokDownloader project features, detailed documentation, GUI interface, etc.,  
> **we strongly recommend visiting the original project**: 👉 **[https://github.com/JoeanAmier/TikTokDownloader](https://github.com/JoeanAmier/TikTokDownloader)**

### ✨ Branch Features

- 🚀 **Direct Command Line API Server Launch** - No interactive selection required
- ⚙️ **Flexible Configuration Parameters** - Customize host, port, log level
- 🔄 **Automated Configuration** - Automatically accept disclaimer and set default language
- 📚 **Complete API Documentation** - Built-in Swagger UI and ReDoc
- 🔗 **Backward Compatibility** - Fully supports original interactive mode

---

## 🚀 Quick Start

### Basic Usage

```bash
# Start API server with default configuration (127.0.0.1:5555)
python main.py --server
```

### Advanced Usage

```bash
# Custom host and port
python main.py --server --host 0.0.0.0 --port 8080

# Set log level
python main.py --server --log-level debug

# Production deployment
python main.py --server --host 0.0.0.0 --port 8000 --log-level warning
```

---

## ⚙️ Command Line Arguments

```bash
python main.py [options]
```

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--server` | Start API server mode | - |
| `--host HOST` | API server host address | `127.0.0.1` |
| `--port PORT` | API server port | `5555` |
| `--log-level` | Log level (`critical`/`error`/`warning`/`info`/`debug`/`trace`) | `info` |
| `-h, --help` | Show help information | - |

---

## 📚 API Documentation

After the server starts, you can access API documentation through the following addresses:

| Document Type | Access URL | Description |
|---------------|------------|-------------|
| **Swagger UI** | `http://your-host:your-port/docs` | Interactive API documentation |
| **ReDoc** | `http://your-host:your-port/redoc` | Beautiful API documentation |

**Example**: If the server runs on `127.0.0.1:8080`
- Swagger UI: http://127.0.0.1:8080/docs
- ReDoc: http://127.0.0.1:8080/redoc

---

## 💡 Usage Examples

### 1. View Help Information
```bash
python main.py --help
```

### 2. Local Development
```bash
# Local testing, debug mode
python main.py --server --log-level debug
```

### 3. LAN Access
```bash
# Allow access from other devices on the LAN
python main.py --server --host 0.0.0.0 --port 8080
```

### 4. Production Environment
```bash
# Optimize log output, improve performance
python main.py --server --host 0.0.0.0 --port 8000 --log-level warning
```

---

## ⚠️ Important Notes

- 📁 **First Run**: The program will automatically create necessary configuration files
- 🍪 **Cookie Configuration**: Cookie setup is required according to the original project instructions
- 🔒 **Security Reminder**: Please set appropriate security measures when deploying on public networks
- 🔄 **Port Conflicts**: Ensure the specified port is not occupied by other programs

---

## 🔧 Compatibility Notes

This optimized version is **fully backward compatible** with original functionality:

```bash
# Original interactive mode is still available
python main.py
```

---

## 🆘 Troubleshooting

When encountering issues, please follow these troubleshooting steps:

1. **Check Port Usage**
   ```bash
   # Linux/macOS
   lsof -i :5555
   
   # Windows
   netstat -ano | findstr :5555
   ```

2. **View Detailed Logs**
   ```bash
   python main.py --server --log-level debug
   ```

3. **Verify Configuration Files**
   - Check if Cookie configuration is correct
   - Confirm configuration file permissions

---

## 📖 More Resources

### 🔗 Related Links

- **Original Project**: [https://github.com/JoeanAmier/TikTokDownloader](https://github.com/JoeanAmier/TikTokDownloader)
- **Detailed Documentation**: Please refer to the complete documentation of the original project
- **GUI Version**: The original project provides a graphical interface version
- **More Features**: The original project includes more collection features and usage tutorials

### 🤝 Contribution & Support

If you encounter problems or have suggestions for improvement during use:
1. Prioritize checking the Issues and documentation of the original project
2. For issues specific to API server mode, you can submit Issues in this project

---

<div align="center">

**✨ Thank you for using DouK-Downloader API Server Mode!**

For more features, please visit the **[Original Project](https://github.com/JoeanAmier/TikTokDownloader)** 🚀

</div>
