# 🧙‍♂️ LordSlack - 摆烂仙君 AI 聊天机器人

> **[中文文档](README_CN.md)** | [English](README_EN.md)

一个基于摆烂仙君 (ace-trump-tech) 打造的开源多平台 AI 聊天机器人框架。

## ⚡ 快速开始

\\ash
# 克隆项目
git clone https://github.com/your-username/lordslack.git
cd lordslack

# 安装依赖
pip install uv && uv sync

# 启动应用
uv run main.py
\
🌐 访问 **http://localhost:6185** | 默认账户：astrbot / astrbot

## ✨ 特性

- 🤖 多 LLM 支持（OpenAI、Claude、Gemini 等）
- 🌐 多平台集成（QQ、微信、Telegram 等）
- 🧠 Agent 和知识库
- 📦 1000+ 社区插件
- 🎨 现代化 Web 仪表板

## 📖 文档

**[👉 点击查看完整中文文档](README_CN.md)**

包含：
- 安装和配置指南
- 平台接入说明
- 插件开发教程
- 常见问题解答

## 🐳 Docker 启动

\\ash
docker run -d \
  --name lordslack \
  -p 6185:6185 \
  -v ./data:/lordslack/data \
  soulter/astrbot:latest
\
## 📋 需求

- Python 3.12+
- Node.js 20+（可选）

## 🔐 安全提示

修改默认密码、保护 API Keys、启用 HTTPS、定期备份

详见 [README_CN.md](README_CN.md#安全建议)

## 📜 许可

AGPL-3.0-or-later

## 🤝 贡献

欢迎 Fork、提交 Issue 和 Pull Request！

---

**更多详情：[📖 中文文档](README_CN.md)**
