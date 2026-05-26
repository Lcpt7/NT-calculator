# NT Calculator

一个基于 Python + Flet 开发的移动端数论计算工具，专注于常见数论与密码学相关计算，同时提供基础学习内容。

---

## 功能特性

### 数论计算

目前支持：

- 模运算
- 幂模运算
- 素数判断
- 欧拉函数
- 勒让德符号
- 阶计算
- 原根计算
- 逆元计算

---

## 学习模块

内置基础数论知识介绍，包括：

- 素数
- 欧拉函数
- 原根
- 逆元
- 二次剩余
- 快速幂

适合初学者快速了解相关概念。

---

## 界面特性

- 深色 / 浅色主题切换
- 移动端 UI 设计
- 历史记录功能
- Material Design 风格
- 自定义字体（MiSans）

---

## 技术栈

- Python
- Flet
- Flutter (WebView)
- Material Design

---

## 本地运行

### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动项目

```bash
flet run
```

### Web 运行

```bash
flet run --web
```

---

## 项目结构

```text
NT-Calculator/
│
├── assets/
│   ├── fonts/
│   │   └── MiSans-Regular.ttf
│   │
│   └── icons/
│       └── app_icon.png
│
├── calculator.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 后续计划

- 更多数论算法
- RSA 小工具
- 中国剩余定理
- 椭圆曲线相关功能
- 数学公式渲染
- Android / Windows 打包

---

## 作者

Lcpt7

---

## License

MIT License