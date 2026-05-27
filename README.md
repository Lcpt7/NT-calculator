# NT Calculator

当前版本：V1.1

一个基于 Python + Flet 开发的数论计算器，提供常见数论函数计算、基础学习资料、历史记录和明暗主题切换。

## 功能特性

### 数论计算

目前支持：

- 素数判断
- 幂模运算
- 勒让德符号
- 欧拉函数
- 模运算
- 阶计算
- 原根计算
- 逆元计算

### 学习模块

内置基础数论知识介绍，包括：

- 素数
- 幂模运算
- 勒让德符号
- 欧拉函数
- 模运算
- 阶
- 原根
- 逆元

### 界面功能

- 移动端风格 UI
- 浅色 / 深色主题切换
- 历史记录
- 输入校验和大数限制
- 自定义字体 MiSans

## V1.1 更新

- 拆分原本较长的 `ui.py`，将 UI 相关代码整理到 `app_ui/` 包中。
- 修复 README 和 UI 文案的编码显示问题。
- 优化 UI 代码结构，分离主题、内容配置、输入校验和视图逻辑。
- 保留 `ui.py` 作为兼容入口，`main.py` 无需修改导入方式。

## 技术栈

- Python
- Flet
- Material Design 风格组件

## 本地运行

### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动项目

```bash
python main.py
```

也可以使用 Flet 命令运行：

```bash
flet run
```

### Web 运行

```bash
flet run --web
```

## 项目结构

```text
NT-Calculator/
├── app_ui/
│   ├── __init__.py
│   ├── content.py
│   ├── theme.py
│   ├── validation.py
│   └── views.py
├── assets/
│   ├── fonts/
│   │   └── MiSans-Regular.ttf
│   └── icons/
│       └── app_icon.png
├── calculator.py
├── main.py
├── ui.py
├── requirements.txt
├── runtime.txt
└── README.md
```

## 模块说明

- `main.py`：应用启动入口。
- `ui.py`：兼容入口，导出 `app_ui.main`。
- `app_ui/views.py`：Flet 页面布局和交互逻辑。
- `app_ui/content.py`：计算功能配置和学习内容。
- `app_ui/theme.py`：浅色 / 深色主题颜色配置。
- `app_ui/validation.py`：输入校验和参数解析。
- `calculator.py`：数论计算核心函数。

## 后续计划

- 增加更多数论算法
- RSA 小工具
- 中国剩余定理
- 椭圆曲线相关功能
- 数学公式渲染
- Android / Windows 打包

## 作者

Lcpt7

## License

MIT License
