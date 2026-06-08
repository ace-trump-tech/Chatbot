# 🔒 GitHub 发布前检查清单 - LordSlack

在将 LordSlack 项目推送到 GitHub 之前，请按照此清单进行操作，确保不会泄露个人配置和敏感信息。

## ✅ 必做项

### 1️⃣ 清理个人数据

```bash
# 删除或备份以下目录（包含个人配置）
rm -rf data/
rm -rf configs/

# 新建空目录供用户初始化
mkdir -p data/plugins data/config data/temp
```

### 2️⃣ 验证 .gitignore

确保以下项已在 `.gitignore` 中：

```
# Data files
data/
data_v2.db
data_v3.db
data_v4.db
*.db
*.sqlite

# Config files
configs/
config.yaml
cmd_config.json

# User-specific files
.venv
.vscode
.idea
logs/
temp/
```

**检查命令**：
```bash
git status
```

确保上面的文件/目录不会出现在输出中。

### 3️⃣ 删除环境变量和 secrets

检查以下文件是否包含敏感信息：

- [ ] `.env` 文件（不应该提交）
- [ ] `.github/workflows/*.yml` - 检查是否有硬编码的密钥（应使用 `${{ secrets.* }}` ）
- [ ] 代码文件中是否有 API Keys
- [ ] 配置文件中是否有用户名/密码

**检查命令**：
```bash
grep -r "api_key\|apiKey\|API_KEY\|password\|token" --include="*.py" --include="*.js" --include="*.json"
```

### 4️⃣ 清理个人信息

检查并删除以下内容：

- [ ] 代码注释中的个人信息（姓名、邮箱、电话等）
- [ ] 提交历史中的个人邮箱（如需，可使用 `git filter-branch`）
- [ ] 文档中的个人联系方式
- [ ] 本地开发的临时注释和调试代码

### 5️⃣ 验证 git 历史

```bash
# 查看最近的提交
git log --oneline -20

# 检查是否有不希望公开的提交
git log --all --pretty=format:"%h %s" | grep -i "personal\|secret\|key\|password"
```

### 6️⃣ 清理大文件（可选）

LordSlack 项目本身不应该有很大的文件，但可检查：

```bash
# 查找超过 10MB 的文件
find . -size +10M -type f | grep -v ".git"
```

### 7️⃣ 验证 LICENSE 和 CONTRIBUTING

- [ ] `LICENSE` 文件存在且内容正确（AGPL-3.0）
- [ ] `CONTRIBUTING.md` 存在并有清晰的贡献指南
- [ ] `CODE_OF_CONDUCT.md` 存在（可选）

### 8️⃣ 更新项目元数据

确保以下文件已针对 LordSlack 更新：

- [ ] `pyproject.toml` - 项目名称、描述、关键词
- [ ] `package.json` (dashboard) - 项目名称和描述
- [ ] `README.md` - 项目简介和快速开始
- [ ] `README_CN.md` - 中文完整文档

### 9️⃣ 验证 Dashboard 构建

```bash
cd dashboard
npm install
npm run build

# 检查是否有错误
echo $?
```

### 🔟 最终检查

```bash
# 运行完整的 git 检查
git status              # 应该是干净的
git log -1              # 查看最后一次提交
git remote -v           # 确认远程地址正确
```

---

## 🚀 准备发布

### 1. 创建 .gitignore 验证脚本

创建文件 `scripts/pre-push-check.sh`：

```bash
#!/bin/bash

echo "检查敏感文件..."

# 检查是否有未被 .gitignore 的数据文件
if [ -d "data" ] && [ -f "data/.gitkeep" ]; then
    echo "❌ 错误: data/ 目录不应该被提交"
    exit 1
fi

# 检查是否有 .env 文件
if [ -f ".env" ]; then
    echo "❌ 错误: .env 文件不应该被提交"
    exit 1
fi

echo "✅ 检查通过!"
exit 0
```

运行：
```bash
chmod +x scripts/pre-push-check.sh
./scripts/pre-push-check.sh
```

### 2. 提交到 GitHub

```bash
# 添加所有文件（确保 .gitignore 生效）
git add -A

# 检查提交内容
git status

# 提交
git commit -m "chore: prepare LordSlack for GitHub release"

# 推送
git push origin main
```

### 3. 验证 GitHub 上的内容

推送后，在 GitHub 网页上检查：

- [ ] 没有看到 `data/` 目录
- [ ] 没有看到 `.env` 或其他敏感文件
- [ ] `README.md` 能正常显示
- [ ] 所有文档文件都在

---

## ⚠️ 常见错误

### 错误1: 已经提交了敏感数据

如果数据已经被提交，使用 `git filter-branch` 清理历史：

```bash
# 从整个历史中删除文件
git filter-branch --tree-filter 'rm -rf data' HEAD

# 强制推送（仅在确定的情况下，会改写历史）
git push origin main --force
```

### 错误2: 忘记更新 .gitignore

```bash
# 从 git 缓存中移除
git rm --cached data/ -r
git rm --cached *.db -r

# 再次提交
git add .gitignore
git commit -m "fix: update .gitignore to exclude data files"
```

### 错误3: 无法推送

确保：
- 有正确的权限
- 不是在受保护的分支上
- 没有推送冲突

```bash
git push --set-upstream origin main
```

---

## 📋 最终清单

在执行 `git push` 前，确认所有项都已完成：

- [ ] ✅ `data/` 目录已删除或备份
- [ ] ✅ `.gitignore` 已更新
- [ ] ✅ 没有硬编码的 API Keys
- [ ] ✅ 没有个人邮箱或联系方式
- [ ] ✅ 项目名称已更新为 LordSlack
- [ ] ✅ README 已更新
- [ ] ✅ 版本号已设置（pyproject.toml）
- [ ] ✅ Dashboard 能正常构建
- [ ] ✅ 运行 `git status` 确认没有意外文件
- [ ] ✅ LICENSE 文件存在

---

## ✨ 发布后建议

推送到 GitHub 后：

1. **设置 README 徽章** - 添加 CI/CD 状态、许可证等
2. **启用 GitHub Pages** - 发布文档
3. **配置 Branch Protection** - 保护 main 分支
4. **添加 Topics** - 帮助用户发现项目
5. **编写 Releases** - 描述版本变化

---

**准备好了？安全地发布你的 LordSlack 项目吧！** 🚀
