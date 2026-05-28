"""精简的启动入口：把 UI 逻辑移到 `ui.py`，此文件仅负责运行应用。"""

import flet as ft

from ui import main


if __name__ == "__main__":
    ft.run(main)
