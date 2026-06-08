
# 🧙‍♂️ LordSlack - 摆烂仙君 AI 聊天机器人

> **[中文文档](README_CN.md)** | [English](README_EN.md) | [问题反馈](https://github.com/ace-trump-tech/Chatbot/issues)

**LordSlack** 是一个开箱即用的多平台 AI 聊天机器人框架，基于 **摆烂仙君 (ace-trump-tech)** 深度定制。无论你想搭建个人助手、智能客服、还是自动化工具，都能在 10 分钟内完成部署。

---

## 📌 目录

- [✨ 特性](#-特性)
- [📋 系统要求](#-系统要求)
- [🚀 快速部署（5 分钟上手）](#-快速部署5-分钟上手)
  - [1. 环境准备](#1-环境准备)
  - [2. 获取代码](#2-获取代码)
  - [3. 安装依赖](#3-安装依赖)
  - [4. 启动服务](#4-启动服务)
- [🧠 配置 AI 模型](#-配置-ai-模型)
  - [支持 OpenAI / 豆包 / Claude / Gemini 等](#支持-openapi--豆包--claude--gemini-等)
  - [以豆包（火山引擎）为例](#以豆包火山引擎为例)
- [🤖 接入聊天平台](#-接入聊天平台)
  - [QQ 群机器人（NapCat）](#qq-群机器人napcat)
  - [微信 / 企业微信 / Telegram](#微信--企业微信--telegram)
- [🎨 Web 管理面板](#-web-管理面板)
- [🐳 Docker 部署（推荐生产）](#-docker-部署推荐生产)
- [🧩 插件与扩展](#-插件与扩展)
- [🔐 安全建议](#-安全建议)
- [❓ 常见问题（FAQ）](#-常见问题faq)
- [📜 开源协议](#-开源协议)

---

## ✨ 特性

- 🤖 **多模型支持**：OpenAI、Anthropic、Gemini、豆包、阿里云百炼、Coze……  
- 🌐 **多平台接入**：QQ、微信、企业微信、飞书、钉钉、Telegram、Slack  
- 🧠 **高级功能**：多模态对话、Agent 智能体、私有知识库、人格设定、上下文压缩  
- 📦 **海量插件**：1000+ 社区插件，一键安装，功能无限扩展  
- 🎨 **现代化仪表板**：Vue.js 管理界面，配置、日志、用户管理全在浏览器  
- 💯 **完全开源**：AGPL-3.0 许可，可商用（需遵守协议）  

---

## 📋 系统要求

| 组件       | 最低版本          | 推荐版本      |
|------------|------------------|---------------|
| Python     | 3.10              | 3.12+          |
| Node.js    | 18.0 (仅构建前端) | 20.0 (可选)    |
| 操作系统   | Windows / macOS / Linux | Ubuntu 22.04 / Windows 11 |
| 网络       | 可访问 GitHub & AI 服务商 | 稳定公网（如需微信/QQ） |

---

## 🚀 快速部署（5 分钟上手）

### 1. 环境准备

- **安装 Python 3.12**（推荐从 [python.org](https://python.org) 下载）
- **安装 Git**（[git-scm.com](https://git-scm.com)）
- **安装 UV 包管理器**（更快更稳定）：
  ```bash
  pip install uv
  ```

### 2. 获取代码

```bash
git clone https://github.com/ace-trump-tech/Chatbot.git lordslack
cd lordslack
```

> 💡 如果你已经下载了 ZIP 压缩包，解压后进入文件夹即可。

### 3. 安装依赖

```bash
# 使用 UV 一键安装所有依赖（推荐）
uv sync

# 或者使用传统 pip（较慢）
pip install -r requirements.txt
```

> ⏱️ 首次安装需要 3-5 分钟，请耐心等待。

### 4. 启动服务

```bash
uv run main.py
```

当控制台出现类似以下信息时，说明启动成功：

```
✨ LordSlack v4.25.5 WebUI is ready
   ➜  Local: http://localhost:6185
   ➜  Username: astrbot
   ➜  Password: astrbot
```

**立即访问** `http://localhost:6185` 打开 Web 管理面板。

> ⚠️ **首次登录后请立即修改默认密码！**  
> 路径：WebUI → 右上角头像 → 修改密码。

---

## 🧠 配置 AI 模型

LordSlack 支持几乎所有主流 LLM API。你只需要提供 **API Key** 和 **Base URL**。

### 支持 OpenAI / 豆包 / Claude / Gemini 等

| 模型提供商 | API Base URL（示例）                    | 说明                         |
|------------|------------------------------------------|------------------------------|
| OpenAI     | `https://api.openai.com/v1`              | 需要 `sk-xxx` 格式的 key     |
| 豆包       | `https://ark.cn-beijing.volces.com/api/v3` | 火山引擎豆包                 |
| Claude     | `https://api.anthropic.com/v1`           | 需要 API key                 |
| Gemini     | `https://generativelanguage.googleapis.com` | 需从 Google AI Studio 获取 |

### 以豆包（火山引擎）为例

如果你想使用**免费额度**的豆包模型（每月 50 万 tokens），按以下步骤操作：

1. **注册火山引擎** → 完成实名认证（个人即可）
2. **开通豆包服务**：
   - 进入 [火山方舟控制台](https://console.volcengine.com/ark/region:ark+cn-beijing/model)
   - 找到 `Doubao-lite-32k` 模型，点击「开通服务」
3. **创建 API Key**：
   - 左侧菜单「API Key 管理」→「创建 API Key」
   - 名称任意，权限选择「读/写」
   - 复制生成的 `apikey-xxxxxx` 字符串
4. **在 LordSlack 中添加模型**：
   - 登录 WebUI（http://localhost:6185）
   - 进入「模型提供商」→「新增提供商」
   - 选择 **OpenAI (通用)**
   - 填写：
     - API Key：粘贴刚才的 `apikey-xxxxxx`
     - API Base URL：`https://ark.cn-beijing.volces.com/api/v3`
   - 点击「获取模型列表」→ 选择 `doubao-lite-32k` → 添加并设为默认
5. **测试**：打开「聊天测试」页面，发送一条消息，如果正常回复则配置成功。

> 📘 详细豆包接入文档：[官方指南](https://www.volcengine.com/docs/82379)

---

## 🤖 接入聊天平台

### QQ 群机器人（NapCat）

LordSlack 通过 **NapCatQQ**（个人版）或 **QQ 官方机器人**（企业版）连接 QQ。

#### 使用 NapCat（推荐个人用户）

1. **下载 NapCatQQ**：[GitHub Releases](https://github.com/NapNeko/NapCatQQ/releases)
   - Windows 用户选择 `napcat.win.x64.exe`
2. **运行 NapCat**，用你的**小号 QQ**扫码登录
3. 登录后 NapCat 会显示正向 WebSocket 地址，默认为 `ws://127.0.0.1:3001`
4. **在 LordSlack 中配置**：
   - WebUI →「平台配置」→「新增平台」→ 选择 **NapCat**
   - 填入 WebSocket 地址，保存
5. **重启 LordSlack**，然后在 QQ 群里 @机器人 即可对话

#### 使用 QQ 官方机器人（稳定、合规）

1. 前往 [QQ 开放平台](https://q.qq.com) 注册开发者，创建机器人应用
2. 获得 `AppID` 和 `AppSecret`
3. 在 LordSlack 平台配置中选择「QQ 官方机器人」，填入上述信息
4. 按开放平台要求配置事件回调地址（LordSlack 会自动提供）

> ⚠️ 注意：个人使用 NapCat 时请遵守腾讯协议，建议使用专用小号。

### 微信 / 企业微信 / Telegram

- **微信公众号**：需要在公众号后台配置服务器 URL 和 Token。
- **企业微信**：创建自建应用，获取 `CorpID`、`AgentID`、`Secret`。
- **Telegram**：通过 `@BotFather` 创建机器人，获得 Token，在 LordSlack 中填入即可。

配置入口均在 WebUI →「平台配置」→「新增平台」，选择对应平台后按提示填写。

---

## 🎨 Web 管理面板

LordSlack 提供一个现代化的管理界面，功能包括：

- 对话模型切换
- 多平台状态监控
- 插件安装/卸载
- 知识库上传（PDF、TXT、Markdown）
- 人设管理
- 对话日志查看

**访问地址**：`http://你的服务器IP:6185`

---

## 🐳 Docker 部署（推荐生产）

如果你有 Docker 环境，可以使用官方镜像快速部署：

```bash
docker run -d \
  --name lordslack \
  -p 6185:6185 \
  -v ./lordslack_data:/lordslack/data \
  soulter/astrbot:latest
```

使用 Docker Compose（更灵活）：

```yaml
version: '3.8'
services:
  lordslack:
    image: soulter/astrbot:latest
    container_name: lordslack
    ports:
      - "6185:6185"
    volumes:
      - ./data:/lordslack/data
    restart: unless-stopped
```

启动：`docker-compose up -d`

---

## 🧩 插件与扩展

LordSlack 拥有强大的插件系统，你可以：

- **一键安装社区插件**：WebUI →「插件商店」
- **开发自己的插件**：参考 [插件开发文档](README_CN.md#插件开发)

示例插件结构：

```
data/plugins/my_plugin/
├── __init__.py
└── metadata.yaml
```

`__init__.py` 内容：

```python
from astrbot.api.star import Star
from astrbot.api.message import MessageChain

class MyPlugin(Star):
    def on_message(self, message: MessageChain):
        if "hello" in str(message).lower():
            return "Hi there!"
```

---

## 🔐 安全建议

- ✅ **修改默认密码**：首次登录后立即更改 `astrbot/astrbot` 默认密码
- ✅ **使用环境变量**：不要在代码中硬编码 API Key，推荐用 `data/secrets.yaml` 或环境变量
- ✅ **启用 HTTPS**：生产环境请使用 Nginx 反代并配置 SSL 证书
- ✅ **限制端口暴露**：不要将 6185 端口直接暴露在公网，可通过防火墙限制访问 IP
- ✅ **定期备份**：备份 `data/` 目录（包含配置、数据库、知识库）

---

## ❓ 常见问题（FAQ）

### Q1: 启动时提示 `ModuleNotFoundError: No module named 'astrbot'`

**A**: 你没有在正确的虚拟环境中运行。请使用 `uv run main.py` 而不是 `python main.py`。

### Q2: WebUI 显示“无法获取模型列表”

**A**: 常见原因：
- API Key 错误或未开通模型服务
- Base URL 填写不正确（注意末尾是否有 `/v1` 或 `/v3`）
- 网络无法访问 API 地址（可尝试在「高级配置」中设置代理）

### Q3: QQ 机器人无法回复消息

**A**: 
- 确认 NapCat 已成功登录 QQ 且 WebSocket 地址正确
- 检查 LordSlack 中该平台是否已启用
- 查看日志 `logs/` 目录中的错误信息

### Q4: 如何重置 WebUI 密码？

**A**: 停止 LordSlack，删除 `data/data_v4.db` 文件，然后重启，密码会恢复为默认的 `astrbot`。

### Q5: 如何更新 LordSlack 到最新版？

**A**:
```bash
git pull
uv sync
uv run main.py
```

### Q6: 支持 GPT-4o、Claude 3.5 等最新模型吗？

**A**: 支持。只要提供商 API 兼容 OpenAI 格式，均可通过「OpenAI（通用）」模式接入。

---

## 📜 开源协议

本项目采用 **AGPL-3.0-or-later** 许可证。  
你可以自由使用、修改、分发，但**必须公开源代码**（若网络提供服务）。  
商用请联系作者获取其他授权选项。

---

## 🤝 贡献与支持

- 🐛 **报告 Bug**：请在 GitHub Issues 中详细描述
- 💡 **建议新功能**：同样在 Issues 中提出
- 🔧 **提交代码**：Fork 项目 → 修改 → Pull Request
- 💬 **讨论交流**：GitHub Discussions

**项目主页**：[https://github.com/ace-trump-tech/Chatbot](https://github.com/ace-trump-tech/Chatbot)

**祝你使用愉快，摆烂修仙！** 🧙‍♂️

---

> 如果本文档未能解决你的问题，欢迎提 Issue，我们会尽快补充。
```

这样修改后的 README 内容更加丰富，详细到每一步，并且包含了豆包配置、QQ 接入、Docker 部署、常见问题等，完全能满足“教会从头部署”的需求。你可以直接复制保存为 `README.md` 并推送到 GitHub。
