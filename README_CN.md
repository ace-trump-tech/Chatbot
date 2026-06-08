# 🧙‍♂️ LordSlack - 摆烂仙君 AI 聊天机器人平台

## 项目简介

**LordSlack** 是一个基于 **摆烂仙君** (ace-trump-tech) 打造的开源多平台 AI 聊天机器人框架。它是 AstrBot 项目的定制版本，经过品牌化改造和优化，专门为 DIY 爱好者和开发者设计。

支持多种即时通讯平台的集成，提供可靠、可扩展的对话 AI 基础设施。无论是构建个人 AI 助手、智能客服、自动化工具还是知识库应用，LordSlack 都能帮您快速构建生产级 AI 应用。

### ✨ 核心特性

- **🤖 多 LLM 支持**：支持 OpenAI、Anthropic、Google Gemini、阿里云百炼、Coze 等多种 AI 模型
- **🌐 多平台集成**：QQ、微信、企业微信、飞书、钉钉、Telegram、Slack 等
- **🧠 高级功能**：多模态对话、Agent 智能体、MCP 协议、技能系统、知识库、人设管理、上下文压缩
- **📦 丰富插件**：1000+ 社区插件，一键安装扩展功能
- **🎨 Web 仪表板**：现代化 Vue.js 界面，方便配置和管理
- **📱 跨平台**：支持 Windows、macOS、Linux 和 Docker 部署
- **💯 完全开源**：AGPL-3.0 许可证，可自由修改和使用

---

## 🚀 快速开始

### 系统要求

- **Python 3.12+**（推荐 3.12）
- **Node.js 20+** 和 **npm 10+**（用于前端 Dashboard）
- **Git** 版本控制

### 1️⃣ 克隆项目

```bash
git clone https://github.com/your-username/lordslack.git
cd lordslack
```

### 2️⃣ 安装依赖

**第一步：安装 UV 包管理器**

```bash
pip install uv
```

**第二步：安装 Python 依赖**

```bash
uv sync
```

⏱️ 这一步需要 6-7 分钟，**请勿中断**。

### 3️⃣ 创建必要目录

```bash
mkdir -p data/plugins data/config data/temp
```

### 4️⃣ 启动应用

```bash
uv run main.py
```

✅ 应用会在约 3 秒内启动，开放 WebUI 地址：

**🌐 http://localhost:6185**

默认登录凭证：
- 用户名：`astrbot`
- 密码：`astrbot`

---

## 📊 Dashboard 前端配置（可选）

如果要在开发环境中运行前端热更新：

```bash
cd dashboard
npm install      # 第一次运行，需要 2-3 分钟
npm run dev      # 启动开发服务器
```

🌐 Dashboard 会运行在：**http://localhost:3000**

### 生产构建

```bash
cd dashboard
npm run build    # 构建优化后的生产版本
```

构建后的文件在 `dashboard/dist/` 目录中。

---

## 🐳 Docker 部署

### 方式一：Docker 直接运行

```bash
docker run -d \
  --name lordslack \
  -p 6185:6185 \
  -v ./data:/lordslack/data \
  soulter/astrbot:latest
```

### 方式二：Docker Compose

```bash
docker-compose up -d
```

默认会暴露以下端口：
- `6185` - Web UI
- `6195` - WeChat
- `6199` - QQ Bot
- 其他平台端口（根据配置）

---

## ⚙️ 配置说明

### 1. 首次启动配置

首次启动后，访问 `http://localhost:6185`，进行以下配置：

#### 🔑 配置 LLM 服务商

在 **Settings → LLM 服务商** 中选择并配置：

- **OpenAI**: 填入 API Key
- **Anthropic Claude**: 配置 API Key
- **Google Gemini**: 配置 API Key  
- **阿里云百炼**: 配置 API Key
- **Coze**: 配置 Bot ID 等参数

#### 🤖 配置即时通讯平台

在 **Settings → 平台配置** 中配置您要接入的平台：

**QQ 平台**:
- 选择 OneBot 或 NapCat 方案
- 配置 Bot 的 QQ 号和 Token

**微信平台**:
- 配置微信公众号的 AppID 和 AppSecret
- 配置服务器地址和回调 Token

**企业微信**:
- 配置企业 ID、应用 ID、应用 Secret

**Telegram**:
- 输入 Bot Token
- 配置代理（可选）

#### 🧠 配置 Agent 和技能

在 **Plugins → Agent** 中启用 Agent 功能，或在 **Skills** 中安装扩展插件。

### 2. 数据存储

所有配置和数据存储在 `data/` 目录：

- `data/config.yaml` - 主配置文件（启动后生成）
- `data/data_v4.db` - SQLite 数据库（用户数据、消息记录等）
- `data/plugins/` - 用户安装的第三方插件
- `data/knowledge_base/` - 知识库文件

### 3. 日志文件

运行日志保存在 `logs/` 目录，便于调试。

---

## 🔌 插件开发

### 创建简单插件

在 `data/plugins/` 中创建新文件夹：

```
data/plugins/my_plugin/
├── __init__.py
└── metadata.yaml
```

**metadata.yaml 示例**：

```yaml
metadata:
  name: "my_plugin"
  version: "1.0.0"
  author: "Your Name"
  description: "My awesome plugin"
  plugin_type: "message_handler"
```

**__init__.py 示例**：

```python
from astrbot.api.star import Star
from astrbot.api.message import MessageChain

class MyPlugin(Star):
    def on_message(self, message: MessageChain):
        if "hello" in str(message).lower():
            return "Hi there!"
        return None
```

### 使用官方插件系统

LordSlack 提供了一套完整的插件 API：

```python
from astrbot.api.star import Star
from astrbot.api.message import MessageChain, Message

class MyAwesomePlugin(Star):
    async def on_message(self, message: MessageChain) -> None:
        # 处理消息
        pass
    
    async def on_command(self, command: str, args: list) -> None:
        # 处理命令
        pass
```

详见 `astrbot/api/` 中的 API 文档。

---

## 🛠️ 代码检查和格式化

项目使用 **Ruff** 进行代码检查和格式化。

### 检查代码样式

```bash
uv run ruff check .
```

### 自动格式化

```bash
uv run ruff format .
```

### Pre-commit 钩子（可选）

安装 pre-commit 自动在提交前检查代码：

```bash
pip install pre-commit
pre-commit install
```

之后每次提交都会自动运行 ruff 检查。

---

## 📚 项目结构

```
lordslack/
├── main.py                 # 应用入口
├── astrbot/               # 核心代码
│   ├── api/              # 插件 API
│   ├── core/             # 核心功能
│   ├── dashboard/        # Web UI 后端
│   ├── builtin_stars/    # 内置插件
│   └── utils/            # 工具函数
├── dashboard/             # Vue.js 前端
│   ├── src/              # 源代码
│   ├── public/           # 静态资源（包括 logo）
│   └── dist/             # 构建输出
├── data/                  # 运行时数据
│   ├── config.yaml       # 配置文件
│   ├── data_v4.db        # 数据库
│   ├── plugins/          # 用户插件
│   └── knowledge_base/   # 知识库
├── tests/                 # 测试文件
├── docs/                  # 文档
├── k8s/                   # Kubernetes 配置
├── .github/              # GitHub 工作流
└── requirements.txt      # 依赖列表
```

---

## 🔐 安全建议

在部署到生产环境前，请注意：

1. **修改默认密码**：首次运行后立即修改默认 WebUI 登录密码
2. **保护 API Keys**：不要在代码中硬编码 API 密钥，使用环境变量或配置文件
3. **启用 HTTPS**：在生产环境中配置 SSL 证书
4. **防火墙配置**：限制 WebUI 端口的访问权限
5. **备份数据**：定期备份 `data/` 目录

---

## 📖 常见问题

### Q1: 如何重置密码？

在 `data/` 目录中删除 `data_v4.db` 文件，然后重启应用，会重新初始化为默认账户。

### Q2: 如何接入 QQ 机器人？

需要先准备 QQ 机器人框架（如 OneBot 或 NapCat），然后在 LordSlack 中配置连接。

### Q3: 如何实现私有知识库？

在 **Dashboard → 知识库** 中上传文档（PDF、TXT、Markdown 等），系统会自动进行向量化和索引。

### Q4: 如何扩展功能？

通过编写插件扩展功能。详见本文档的 **插件开发** 部分。

### Q5: 性能优化建议？

- 使用 `uv run` 而不是 `python` 运行以获得更好的依赖管理
- 配置合理的 LLM 超时时间
- 定期清理过期日志和临时文件
- 在 Docker 中运行以获得更好的资源隔离

---

## 🐛 问题报告

遇到问题？请：

1. 检查 `logs/` 目录的错误日志
2. 查看 GitHub Issues 是否已有相关问题
3. 提交详细的 Issue 报告，包括：
   - 错误消息和堆栈跟踪
   - 系统环境信息（OS、Python 版本等）
   - 重现问题的步骤

---

## 📜 许可证

本项目采用 **AGPL-3.0-or-later** 许可证。详见 [LICENSE](LICENSE) 文件。

### 商业使用

如果需要用于商业用途，请了解 AGPL 许可证的义务，或联系项目维护者了解其他许可选项。

---

## 🤝 贡献指南

欢迎贡献代码、报告 Bug、提出建议！

1. **Fork** 本项目
2. 创建功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开 Pull Request

### 代码规范

- 使用 `uv run ruff format .` 格式化代码
- 使用 `uv run ruff check .` 检查代码
- 编写清晰的提交信息
- 遵循 Conventional Commits 规范

---

## 📞 联系方式

- **项目主页**：[GitHub - LordSlack](https://github.com/your-username/lordslack)
- **问题反馈**：使用 GitHub Issues
- **讨论交流**：GitHub Discussions

---

## 🙏 致谢

- 感谢 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 项目提供的基础代码
- 感谢所有贡献者和社区用户的支持

---

## 📝 更新日志

### v1.0.0 (2026-06-08)

- ✨ 首次发布 LordSlack 版本
- 🎨 完全品牌化为摆烂仙君 (ace-trump-tech) 主题
- 🔒 清理个人配置信息，适合开源分享
- 📖 添加详细的中文使用文档

详见 [CHANGELOG.md](CHANGELOG.md)（如有）

---

**祝您使用愉快！如有任何问题，欢迎反馈。** 🎉
