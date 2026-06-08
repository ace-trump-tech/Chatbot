# 🧙‍♂️ LordSlack - 摆烂仙君 AI 聊天机器人框架

这是 LordSlack 项目 - 基于摆烂仙君 (ace-trump-tech) 的定制版本。

## 📌 项目标记

本项目由 AstrBot 衍生而来，经过以下改造：

- ✨ 品牌化改造：将所有标识改为 **摆烂仙君 (ace-trump-tech)**
- 🎨 Logo 更新：创建了新的摆烂仙君主题 Logo
- 🔒 隐私保护：删除了所有个人配置和敏感信息
- 📖 文档更新：编写了详细的中文使用文档
- 🚀 项目重命名：重新命名为 **LordSlack** 

## 📚 文档

- **[完整中文文档](README_CN.md)** - 详细的安装、配置、使用和插件开发指南
- **[快速开始](README.md)** - 3 分钟快速开始
- **[发布前检查清单](PRE_PUSH_CHECKLIST.md)** - 上传到 GitHub 前的清单
- **[贡献指南](CONTRIBUTING.md)** - 如何贡献代码

## 🚀 快速开始

```bash
# 1. 安装依赖
pip install uv && uv sync

# 2. 启动应用
uv run main.py

# 3. 打开浏览器
# http://localhost:6185
# 默认用户名/密码: astrbot/astrbot
```

## 🔐 发布前清理

在上传到 GitHub 前，务必运行清理脚本：

```bash
python cleanup_for_github.py
```

这会自动清理个人数据和敏感信息。详见 [PRE_PUSH_CHECKLIST.md](PRE_PUSH_CHECKLIST.md)

## 📝 项目结构

```
lordslack/
├── README.md                    # 快速开始
├── README_CN.md                 # 完整中文文档
├── PRE_PUSH_CHECKLIST.md        # GitHub 发布清单
├── cleanup_for_github.py        # 清理脚本
├── pyproject.toml               # Python 项目配置
├── astrbot/                     # 核心代码
│   ├── api/                    # 插件 API
│   ├── core/                   # 核心功能
│   ├── dashboard/              # Web UI 后端
│   └── builtin_stars/          # 内置插件
├── dashboard/                   # Vue.js 前端
│   ├── src/                    # 源代码
│   ├── public/                 # 静态资源（包括新 logo）
│   └── package.json            # npm 配置
├── data/                        # 运行时数据（占位符）
│   ├── plugins/                # 用户插件
│   ├── config/                 # 配置目录
│   └── temp/                   # 临时文件
├── tests/                       # 测试
├── docs/                        # 文档
└── .gitignore                   # Git 忽略配置
```

## 🎨 新增 Logo 文件

项目已创建以下 Logo 文件（摆烂仙君主题）：

- `dashboard/public/logo-new.svg` - 完整 Logo
- `dashboard/public/logo-mini.svg` - 迷你 Logo  
- `dashboard/public/favicon-new.svg` - 网站图标
- `dashboard/src/assets/images/banner-new.svg` - 横幅

## ⚠️ 已清理的项目

以下项目中的个人配置已被清理：

- ❌ `data/` - 运行时个人数据（已删除，创建占位符）
- ❌ `configs/` - 个人配置文件（已删除）
- ❌ `.env` - 环境变量（已删除）
- ❌ 所有数据库文件 `*.db`、`*.sqlite` （已删除）

新用户首次运行时这些目录会自动生成。

## 🔄 更新历史

### v1.0.0 (2026-06-08)

- ✨ 首次发布 LordSlack 版本
- 🎨 完全品牌化为摆烂仙君 (ace-trump-tech) 主题
- 🔒 清理个人配置信息，适合开源分享
- 📖 编写详细中文文档
- 🚀 优化项目结构，便于社区使用

## 📞 使用帮助

遇到问题？

1. **查看文档** - [README_CN.md](README_CN.md) 包含常见问题解答
2. **检查日志** - `logs/` 目录中的日志文件
3. **提交 Issue** - 在 GitHub 提交问题

## 📜 许可证

采用 **AGPL-3.0-or-later** 许可证。详见 [LICENSE](LICENSE)

### 关于商业使用

如果您需要在商业项目中使用，请了解 AGPL 许可证的义务，或联系项目维护者。

## 🙏 致谢

- 感谢 [AstrBot](https://github.com/AstrBotDevs/AstrBot) 项目提供的基础代码
- 感谢所有贡献者和社区的支持

## 🌟 下一步

1. **完成 GitHub 发布清单** - 运行 `cleanup_for_github.py`
2. **创建 GitHub 仓库** - 新建仓库
3. **推送代码** - `git push origin main`
4. **设置 README 徽章** - 添加 CI/CD 状态
5. **发布 Release** - 标记版本

---

**感谢使用 LordSlack！如果有帮助，请给个 Star ⭐**
