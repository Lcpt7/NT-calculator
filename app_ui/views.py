import flet as ft

from .content import FUNCTIONS_CONFIG, LEARNING_CONTENT
from .theme import get_colors
from .validation import validate_and_parse


class NumberTheoryApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.current_function = None
        self.current_tab = 0
        self.history_list = []
        self.is_dark_theme = False
        self.colors = get_colors(self.is_dark_theme)

        self.top_card_ref = ft.Ref[ft.Container]()
        self.function_card_ref = ft.Ref[ft.Container]()
        self.nav_container_ref = ft.Ref[ft.Container]()
        self.phone_card_ref = ft.Ref[ft.Container]()
        self.title_text = ft.Ref[ft.Text]()
        self.subtitle_text = ft.Ref[ft.Text]()
        self.hint_text = ft.Ref[ft.Text]()

    def run(self):
        self.configure_page()
        self.page.add(self.build_layout())
        self.apply_theme()
        self.show_home()

    def configure_page(self):
        self.page.title = "NTCT"
        self.page.padding = 0
        self.page.fonts = {"MiSans": "MiSans-Regular.ttf"}
        self.page.theme = ft.Theme(font_family="MiSans")
        self.page.bgcolor = self.colors["page_bg"]
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def apply_theme(self):
        self.colors = get_colors(self.is_dark_theme)
        self.page.bgcolor = self.colors["page_bg"]
        self.phone_card_ref.current.bgcolor = self.colors["phone_bg"]
        self.top_card_ref.current.bgcolor = self.colors["card_bg"]
        self.function_card_ref.current.bgcolor = self.colors["card_bg"]
        self.nav_container_ref.current.content.bgcolor = self.colors["card_bg"]
        self.title_text.current.color = self.colors["title"]
        self.subtitle_text.current.color = self.colors["subtitle"]
        self.hint_text.current.color = self.colors["hint"]
        self.page.update()

    def refresh_view(self):
        if self.current_tab == 0:
            if self.current_function:
                self.show_calculation_view(self.current_function)
            else:
                self.show_home()
        elif self.current_tab == 1:
            self.show_learning()
        elif self.current_tab == 2:
            self.show_settings()

    def show_home(self):
        self.current_function = None
        self.hint_text.current.value = "请选择功能"
        self.apply_theme()

        buttons = [self.build_function_button(func_name) for func_name in FUNCTIONS_CONFIG]
        self.function_card_ref.current.content = ft.Column(
            controls=buttons,
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.page.update()

    def show_calculation_view(self, func_name):
        self.current_function = func_name
        config = FUNCTIONS_CONFIG[func_name]
        self.hint_text.current.value = "请输入整数"
        self.apply_theme()

        desc_label = ft.Text(
            value=config["desc"],
            size=13,
            weight=ft.FontWeight.W_400,
            color=self.colors["desc_color"],
            italic=True,
            text_align=ft.TextAlign.CENTER,
        )
        input_fields = [self.build_input_field(param) for param in config["params"]]
        result_text = ft.Text(
            value="",
            size=16,
            weight=ft.FontWeight.W_500,
            color=self.colors["result"],
            text_align=ft.TextAlign.CENTER,
        )
        result_box = self.build_result_box(result_text)

        def calculate(_):
            ok, parsed_or_msg = validate_and_parse(input_fields, config["params"], func_name)
            if not ok:
                self.show_error(result_text, result_box, parsed_or_msg)
                return

            params = parsed_or_msg
            try:
                raw = config["func"](*params)
            except ValueError as exc:
                self.show_error(result_text, result_box, exc)
                return
            except Exception:
                self.show_error(result_text, result_box, "计算出错，请检查输入或稍后重试")
                return

            result_value = self.format_result(raw, config["type"])
            result_text.value = f"结果：{result_value}"
            result_text.color = self.colors["result"]

            params_text = ", ".join(map(str, params))
            self.history_list.insert(0, f"{func_name}({params_text}) = {result_value}")
            if len(self.history_list) > 20:
                self.history_list.pop()
            result_box.update()

        back_btn = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=self.colors["accent"],
            on_click=lambda _: self.show_home(),
        )
        calc_btn = ft.Container(
            content=ft.Text("计算", size=15, weight=ft.FontWeight.W_600, color="#FFFFFF"),
            width=250,
            height=44,
            border_radius=14,
            bgcolor=self.colors["accent"],
            alignment=ft.Alignment(0, 0),
            on_click=calculate,
            ink=True,
        )

        self.function_card_ref.current.content = ft.Column(
            controls=[
                ft.Row(controls=[back_btn], alignment=ft.MainAxisAlignment.START),
                desc_label,
                ft.Container(height=4),
                *input_fields,
                ft.Container(height=6),
                calc_btn,
                ft.Container(height=12),
                result_box,
            ],
            spacing=8,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.page.update()

    def show_learning(self):
        self.hint_text.current.value = "学习资料"
        self.apply_theme()

        controls = []
        for title, content in LEARNING_CONTENT.items():
            controls.append(ft.Text(title, size=18, weight=ft.FontWeight.BOLD, color=self.colors["title"]))
            controls.append(ft.Text(content, size=14, color=self.colors["subtitle"]))
            controls.append(ft.Divider(color=self.colors["divider"]))

        self.function_card_ref.current.content = ft.Column(
            controls=controls,
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
        )
        self.page.update()

    def show_settings(self):
        self.hint_text.current.value = "设置"
        self.apply_theme()

        theme_row = ft.Row(
            controls=[
                ft.Text("切换主题", size=15, weight=ft.FontWeight.W_500, color=self.colors["title"]),
                ft.Switch(
                    value=self.is_dark_theme,
                    on_change=lambda e: self.toggle_theme(e.control.value),
                    active_color=self.colors["accent"],
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        history_btn = self.build_settings_button(
            ft.Icons.HISTORY,
            "历史记录",
            self.open_history,
        )
        about_btn = self.build_settings_button(
            ft.Icons.INFO_OUTLINE,
            "关于产品",
            self.open_about,
        )

        self.function_card_ref.current.content = ft.Column(
            controls=[theme_row, ft.Divider(color=self.colors["divider"]), history_btn, about_btn],
            spacing=14,
            scroll=ft.ScrollMode.AUTO,
        )
        self.page.update()

    def open_history(self, _):
        history_controls = [
            ft.Row(controls=[self.build_back_to_settings_button()], alignment=ft.MainAxisAlignment.START),
            ft.Text("历史记录", size=20, weight=ft.FontWeight.BOLD, color=self.colors["title"]),
        ]

        if self.history_list:
            history_controls.extend(
                ft.Text(item, size=14, color=self.colors["subtitle"]) for item in self.history_list
            )
        else:
            history_controls.append(ft.Text("暂无历史记录", size=14, color=self.colors["hint"], italic=True))

        self.function_card_ref.current.content = ft.Column(
            controls=history_controls,
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
        )
        self.page.update()

    def open_about(self, _):
        self.function_card_ref.current.content = ft.Column(
            controls=[
                ft.Row(controls=[self.build_back_to_settings_button()], alignment=ft.MainAxisAlignment.START),
                ft.Icon(ft.Icons.INFO_OUTLINE, size=56, color=self.colors["accent"]),
                ft.Text("NT Calculator", size=22, weight=ft.FontWeight.BOLD, color=self.colors["title"]),
                ft.Text("版本号 V1.1", size=15, color=self.colors["subtitle"]),
            ],
            spacing=16,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.page.update()

    def toggle_theme(self, dark):
        self.is_dark_theme = dark
        self.apply_theme()
        self.refresh_view()

    def on_nav_change(self, event):
        self.current_tab = event.control.selected_index
        if self.current_tab == 0:
            self.show_home()
        elif self.current_tab == 1:
            self.show_learning()
        elif self.current_tab == 2:
            self.show_settings()

    def build_layout(self):
        top_card = ft.Container(
            ref=self.top_card_ref,
            width=320,
            padding=ft.Padding(left=18, right=18, top=18, bottom=12),
            border_radius=22,
            bgcolor=self.colors["card_bg"],
            shadow=self.build_shadow(),
            content=ft.Column(
                controls=[
                    ft.Text(
                        ref=self.title_text,
                        value="数论计算器",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color=self.colors["title"],
                    ),
                    ft.Text(
                        ref=self.subtitle_text,
                        value="NT Calculator",
                        size=18,
                        weight=ft.FontWeight.W_600,
                        color=self.colors["subtitle"],
                    ),
                    ft.Container(height=4),
                    ft.Text(ref=self.hint_text, value="请选择功能", size=15, color=self.colors["hint"]),
                ],
                spacing=4,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        function_card = ft.Container(
            ref=self.function_card_ref,
            width=320,
            height=420,
            padding=16,
            border_radius=22,
            bgcolor=self.colors["card_bg"],
            shadow=self.build_shadow(),
            content=ft.Column(
                controls=[],
                scroll=ft.ScrollMode.AUTO,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
        nav_bar = ft.NavigationBar(
            bgcolor=self.colors["card_bg"],
            indicator_color=self.colors["accent"],
            selected_index=0,
            on_change=self.on_nav_change,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.HOME_OUTLINED,
                    selected_icon=ft.Icons.HOME,
                    label="首页",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.MENU_BOOK_OUTLINED,
                    selected_icon=ft.Icons.MENU_BOOK,
                    label="学习",
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.SETTINGS_OUTLINED,
                    selected_icon=ft.Icons.SETTINGS,
                    label="设置",
                ),
            ],
        )
        nav_container = ft.Container(
            ref=self.nav_container_ref,
            width=320,
            border_radius=22,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            shadow=self.build_shadow(),
            content=nav_bar,
        )

        return ft.Container(
            ref=self.phone_card_ref,
            width=360,
            padding=18,
            border_radius=28,
            bgcolor=self.colors["phone_bg"],
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=20,
                color=ft.Colors.BLACK12,
                offset=ft.Offset(0, 6),
            ),
            content=ft.Column(
                controls=[
                    top_card,
                    ft.Container(height=10),
                    function_card,
                    ft.Container(height=10),
                    nav_container,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def build_function_button(self, func_name):
        return ft.Container(
            content=ft.Text(
                func_name,
                size=14,
                weight=ft.FontWeight.W_500,
                color=self.colors["btn_text"],
            ),
            width=250,
            height=40,
            border_radius=14,
            bgcolor=self.colors["btn_bg"],
            alignment=ft.Alignment(0, 0),
            on_click=lambda _, name=func_name: self.show_calculation_view(name),
            ink=True,
        )

    def build_input_field(self, param):
        return ft.TextField(
            label=param,
            text_align=ft.TextAlign.CENTER,
            label_style=ft.TextStyle(color=self.colors["hint"]),
            width=250,
            height=52,
            border_radius=12,
            border_color=self.colors["input_border"],
            focused_border_color=self.colors["accent"],
            bgcolor=self.colors["input_bg"],
            color=self.colors["title"],
            cursor_color=self.colors["accent"],
            keyboard_type=ft.KeyboardType.NUMBER,
        )

    def build_result_box(self, result_text):
        return ft.Container(
            content=result_text,
            width=270,
            padding=16,
            border_radius=12,
            bgcolor=self.colors["input_bg"],
            border=ft.Border(
                left=ft.BorderSide(1, self.colors["input_border"]),
                top=ft.BorderSide(1, self.colors["input_border"]),
                right=ft.BorderSide(1, self.colors["input_border"]),
                bottom=ft.BorderSide(1, self.colors["input_border"]),
            ),
            alignment=ft.Alignment(0, 0),
        )

    def build_settings_button(self, icon, label, on_click):
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(icon, color=self.colors["btn_text"]),
                    ft.Text(label, size=15, weight=ft.FontWeight.W_500, color=self.colors["btn_text"]),
                ],
                spacing=10,
            ),
            padding=12,
            border_radius=14,
            bgcolor=self.colors["btn_bg"],
            on_click=on_click,
            ink=True,
        )

    def build_back_to_settings_button(self):
        return ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=self.colors["accent"],
            on_click=lambda _: self.show_settings(),
        )

    def build_shadow(self):
        return ft.BoxShadow(
            blur_radius=16,
            spread_radius=1,
            color=self.colors["shadow"],
            offset=ft.Offset(0, 4),
        )

    def show_error(self, result_text, result_box, message):
        result_text.value = f"错误：{message}"
        result_text.color = "#FF6B6B"
        result_box.update()

    @staticmethod
    def format_result(raw, result_type):
        if result_type == "bool":
            return "是素数" if raw else "不是素数"
        if result_type == "list":
            return "无原根" if raw is None else ", ".join(map(str, raw))
        return str(raw)


def main(page: ft.Page):
    NumberTheoryApp(page).run()
