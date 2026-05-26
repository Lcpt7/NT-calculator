import flet as ft
import calculator


def main(page: ft.Page):
    page.title = "NTCT"
    page.padding = 0

    page.fonts = {
        "MiSans": "fonts/MiSans-Regular.ttf"
    }

    page.theme = ft.Theme(
        font_family="MiSans"
    )

    page.bgcolor = "#ECECEC"

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    current_function = None
    current_tab = 0

    history_list = []

    is_dark_theme = False

    LIGHT = {
        "page_bg": "#ECECEC",
        "phone_bg": "#F7F7F7",
        "card_bg": "#FFFFFF",
        "title": "#222222",
        "subtitle": "#444444",
        "hint": "#666666",
        "input_bg": "#F5F7FA",
        "input_border": "#E0E0E0",
        "btn_bg": "#F5F7FA",
        "btn_text": "#3A5A8A",
        "accent": "#3A5A8A",
        "result": "#222222",
        "shadow": ft.Colors.BLACK12,
        "divider": "#E8E4DD",
        "hist_bg": "#F5F7FA",
        "hist_text": "#444444",
        "desc_color": "#888888",
    }

    DARK = {
        "page_bg": "#1A1A1A",
        "phone_bg": "#252525",
        "card_bg": "#333333",
        "title": "#F0F0F0",
        "subtitle": "#B0B0B0",
        "hint": "#808080",
        "input_bg": "#404040",
        "input_border": "#555555",
        "btn_bg": "#404040",
        "btn_text": "#E0E0E0",
        "accent": "#7A9CC6",
        "result": "#F0F0F0",
        "shadow": ft.Colors.BLACK38,
        "divider": "#555555",
        "hist_bg": "#404040",
        "hist_text": "#B0B0B0",
        "desc_color": "#AAAAAA",
    }

    colors = DARK if is_dark_theme else LIGHT

    top_card_ref = ft.Ref[ft.Container]()
    function_card_ref = ft.Ref[ft.Container]()
    nav_container_ref = ft.Ref[ft.Container]()
    phone_card_ref = ft.Ref[ft.Container]()

    title_text = ft.Ref[ft.Text]()
    subtitle_text = ft.Ref[ft.Text]()
    hint_text = ft.Ref[ft.Text]()

    functions_config = {

        "素数判断": {
            "params": ["n"],
            "func": calculator.is_prime,
            "type": "bool",
            "desc": "判断 n 是否为素数"
        },

        "幂模运算": {
            "params": ["a", "x", "m"],
            "func": calculator.pow_mod,
            "type": "int",
            "desc": "a^x mod m"
        },

        "勒让德符号": {
            "params": ["a", "p"],
            "func": calculator.legendre_symbol,
            "type": "int",
            "desc": "Legendre 符号 (a|p)"
        },

        "欧拉函数": {
            "params": ["n"],
            "func": calculator.euler_phi,
            "type": "int",
            "desc": "φ(n)"
        },

        "模运算": {
            "params": ["a", "m"],
            "func": calculator.mod,
            "type": "int",
            "desc": "a mod m"
        },

        "阶计算": {
            "params": ["a", "m"],
            "func": calculator.order,
            "type": "int",
            "desc": "ordₘ(a)"
        },

        "原根计算": {
            "params": ["m"],
            "func": calculator.primitive_root,
            "type": "list",
            "desc": "模 m 的所有原根"
        },

        "逆元计算": {
            "params": ["a", "m"],
            "func": calculator.mod_inverse,
            "type": "int",
            "desc": "a⁻¹ mod m"
        },
    }

    learning_content = {

        "素数判断":
            "素数：只能被 1 和自身整除的大于 1 的整数。\n\n"
            "例如：2、3、5、7。\n\n"
            "应用：RSA、大整数分解。",

        "幂模运算":
            "幂模运算：计算 a^x mod m。\n\n"
            "通常采用快速幂算法优化。\n\n"
            "应用：密码学、Diffie-Hellman。",

        "勒让德符号":
            "勒让德符号用于判断二次剩余。\n\n"
            "(a|p)=1 表示 a 是模 p 的二次剩余。",

        "欧拉函数":
            "欧拉函数 φ(n)：1~n 中与 n 互素的整数个数。\n\n"
            "例如 φ(8)=4。",

        "模运算":
            "模运算就是求余数。\n\n"
            "例如：17 mod 5 = 2。",

        "阶计算":
            "元素的阶：满足 a^k ≡ 1 (mod m) 的最小正整数 k。",

        "原根计算":
            "原根：能够生成模 m 所有互素剩余类的数。",

        "逆元计算":
            "逆元：满足 a·b ≡ 1 (mod m) 的 b。\n\n"
            "只有 gcd(a,m)=1 时逆元存在。",
    }

    def apply_theme():

        nonlocal colors

        colors = DARK if is_dark_theme else LIGHT

        page.bgcolor = colors["page_bg"]

        phone_card_ref.current.bgcolor = colors["phone_bg"]

        top_card_ref.current.bgcolor = colors["card_bg"]

        function_card_ref.current.bgcolor = colors["card_bg"]

        nav_container_ref.current.content.bgcolor = colors["card_bg"]

        title_text.current.color = colors["title"]

        subtitle_text.current.color = colors["subtitle"]

        hint_text.current.color = colors["hint"]

        page.update()

    def refresh_view():

        if current_tab == 0:

            if current_function:
                show_calculation_view(current_function)

            else:
                show_home()

        elif current_tab == 1:
            show_learning()

        elif current_tab == 2:
            show_settings()

    def show_home():

        nonlocal current_function

        current_function = None

        hint_text.current.value = "请选择功能"

        apply_theme()

        buttons = []

        for func_name in functions_config:

            btn = ft.Container(

                content=ft.Text(
                    func_name,
                    size=14,
                    weight=ft.FontWeight.W_500,
                    color=colors["btn_text"],
                ),

                width=250,
                height=40,

                border_radius=14,

                bgcolor=colors["btn_bg"],

                alignment=ft.Alignment(0, 0),

                on_click=lambda e, fn=func_name: on_function_click(fn),

                ink=True,
            )

            buttons.append(btn)

        function_card_ref.current.content = ft.Column(
            controls=buttons,
            spacing=8,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        page.update()

    def show_calculation_view(func_name):

        nonlocal current_function

        current_function = func_name

        config = functions_config[func_name]

        hint_text.current.value = "请输入整数"

        apply_theme()

        desc_label = ft.Text(
            value=config["desc"],
            size=13,
            weight=ft.FontWeight.W_400,
            color=colors["desc_color"],
            italic=True,
            text_align=ft.TextAlign.CENTER,
        )

        input_fields = []
        input_controls = []

        for param in config["params"]:

            tf = ft.TextField(

                label=param,

                text_align=ft.TextAlign.CENTER,

                label_style=ft.TextStyle(
                    color=colors["hint"]
                ),

                width=250,
                height=52,

                border_radius=12,

                border_color=colors["input_border"],

                focused_border_color=colors["accent"],

                bgcolor=colors["input_bg"],

                color=colors["title"],

                cursor_color=colors["accent"],

                keyboard_type=ft.KeyboardType.NUMBER,
            )

            input_fields.append(tf)

            input_controls.append(tf)

        result_text = ft.Text(
            value="",
            size=16,
            weight=ft.FontWeight.W_500,
            color=colors["result"],
            text_align=ft.TextAlign.CENTER,
        )

        result_box = ft.Container(

            content=result_text,

            width=270,

            padding=16,

            border_radius=12,

            bgcolor=colors["input_bg"],

            border=ft.Border(
                left=ft.BorderSide(1, colors["input_border"]),
                top=ft.BorderSide(1, colors["input_border"]),
                right=ft.BorderSide(1, colors["input_border"]),
                bottom=ft.BorderSide(1, colors["input_border"]),
            ),

            alignment=ft.Alignment(0, 0),
        )

        def calculate(e):

            try:

                params = [
                    int(f.value.strip())
                    for f in input_fields
                ]

                raw = config["func"](*params)

                ps = ", ".join(map(str, params))

                if config["type"] == "bool":

                    result_value = "是素数" if raw else "不是素数"

                elif config["type"] == "list":

                    result_value = (
                        "无原根"
                        if raw is None
                        else ", ".join(map(str, raw))
                    )

                else:

                    result_value = str(raw)

                result_text.value = f"结果：{result_value}"

                result_text.color = colors["result"]

                history_list.insert(
                    0,
                    f"{func_name}({ps}) = {result_value}"
                )

                if len(history_list) > 20:
                    history_list.pop()

            except Exception as ex:

                result_text.value = f"错误：{ex}"

                result_text.color = "#FF6B6B"

            result_box.update()

        back_btn = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=colors["accent"],
            on_click=lambda e: show_home(),
        )

        calc_btn = ft.Container(

            content=ft.Text(
                "计算",
                size=15,
                weight=ft.FontWeight.W_600,
                color="#FFFFFF",
            ),

            width=250,
            height=44,

            border_radius=14,

            bgcolor=colors["accent"],

            alignment=ft.Alignment(0, 0),

            on_click=calculate,

            ink=True,
        )

        function_card_ref.current.content = ft.Column(

            controls=[

                ft.Row(
                    controls=[back_btn],
                    alignment=ft.MainAxisAlignment.START,
                ),

                desc_label,

                ft.Container(height=4),

                *input_controls,

                ft.Container(height=6),

                calc_btn,

                ft.Container(height=12),

                result_box,
            ],

            spacing=8,

            scroll=ft.ScrollMode.AUTO,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

        page.update()

    def show_learning():

        hint_text.current.value = "学习资料"

        apply_theme()

        controls = []

        back_btn = ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color=colors["accent"],
            on_click=lambda e: show_home(),
        )

        controls.append(
            ft.Row(
                controls=[back_btn],
                alignment=ft.MainAxisAlignment.START,
            )
        )

        for title, content in learning_content.items():

            controls.append(

                ft.Text(
                    title,
                    size=18,
                    weight=ft.FontWeight.BOLD,
                    color=colors["title"],
                )
            )

            controls.append(

                ft.Text(
                    content,
                    size=14,
                    color=colors["subtitle"],
                )
            )

            controls.append(
                ft.Divider(
                    color=colors["divider"]
                )
            )

        function_card_ref.current.content = ft.Column(
            controls=controls,

            spacing=10,

            scroll=ft.ScrollMode.AUTO,
        )

        page.update()

    def show_settings():

        hint_text.current.value = "设置"

        apply_theme()

        def open_history(e):

            history_controls = []

            back_btn = ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=colors["accent"],
                on_click=lambda e: show_settings(),
            )

            history_controls.append(
                ft.Row(
                    controls=[back_btn],
                    alignment=ft.MainAxisAlignment.START,
                )
            )

            history_controls.append(
                ft.Text(
                    "历史记录",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color=colors["title"],
                )
            )

            if history_list:

                for item in history_list:

                    history_controls.append(

                        ft.Text(
                            item,
                            size=14,
                            color=colors["subtitle"],
                        )
                    )

            else:

                history_controls.append(
                    ft.Text(
                        "暂无历史记录",
                        size=14,
                        color=colors["hint"],
                        italic=True,
                    )
                )

            function_card_ref.current.content = ft.Column(
                controls=history_controls,

                spacing=12,

                scroll=ft.ScrollMode.AUTO,
            )

            page.update()

        def open_about(e):

            back_btn = ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                icon_color=colors["accent"],
                on_click=lambda e: show_settings(),
            )

            function_card_ref.current.content = ft.Column(

                controls=[

                    ft.Row(
                        controls=[back_btn],
                        alignment=ft.MainAxisAlignment.START,
                    ),

                    ft.Icon(
                        ft.Icons.INFO_OUTLINE,
                        size=56,
                        color=colors["accent"],
                    ),

                    ft.Text(
                        "NT Calculator",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=colors["title"],
                    ),

                    ft.Text(
                        "版本号 V1.0",
                        size=15,
                        color=colors["subtitle"],
                    ),
                ],

                spacing=16,

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )

            page.update()

        theme_row = ft.Row(

            controls=[

                ft.Text(
                    "切换主题",
                    size=15,
                    weight=ft.FontWeight.W_500,
                    color=colors["title"],
                ),

                ft.Switch(
                    value=is_dark_theme,

                    on_change=lambda e: toggle_theme(
                        e.control.value
                    ),

                    active_color=colors["accent"],
                ),
            ],

            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        history_btn = ft.Container(

            content=ft.Row(

                controls=[

                    ft.Icon(
                        ft.Icons.HISTORY,
                        color=colors["btn_text"],
                    ),

                    ft.Text(
                        "历史记录",
                        size=15,
                        weight=ft.FontWeight.W_500,
                        color=colors["btn_text"],
                    ),
                ],

                spacing=10,
            ),

            padding=12,

            border_radius=14,

            bgcolor=colors["btn_bg"],

            on_click=open_history,

            ink=True,
        )

        about_btn = ft.Container(

            content=ft.Row(

                controls=[

                    ft.Icon(
                        ft.Icons.INFO_OUTLINE,
                        color=colors["btn_text"],
                    ),

                    ft.Text(
                        "关于产品",
                        size=15,
                        weight=ft.FontWeight.W_500,
                        color=colors["btn_text"],
                    ),
                ],

                spacing=10,
            ),

            padding=12,

            border_radius=14,

            bgcolor=colors["btn_bg"],

            on_click=open_about,

            ink=True,
        )

        function_card_ref.current.content = ft.Column(

            controls=[

                theme_row,

                ft.Divider(
                    color=colors["divider"]
                ),

                history_btn,

                about_btn,
            ],

            spacing=14,

            scroll=ft.ScrollMode.AUTO,
        )

        page.update()

    def toggle_theme(dark):

        nonlocal is_dark_theme

        is_dark_theme = dark

        apply_theme()

        refresh_view()

    def on_function_click(fn):
        show_calculation_view(fn)

    def on_nav_change(e):

        nonlocal current_tab

        current_tab = e.control.selected_index

        if current_tab == 0:
            show_home()

        elif current_tab == 1:
            show_learning()

        elif current_tab == 2:
            show_settings()

    top_card = ft.Container(

        ref=top_card_ref,

        width=320,

        padding=ft.Padding(
            left=18,
            right=18,
            top=18,
            bottom=12,
        ),

        border_radius=22,

        bgcolor=colors["card_bg"],

        shadow=ft.BoxShadow(
            blur_radius=16,
            spread_radius=1,
            color=colors["shadow"],
            offset=ft.Offset(0, 4),
        ),

        content=ft.Column(

            controls=[

                ft.Text(
                    ref=title_text,

                    value="数论计算器",

                    size=24,

                    weight=ft.FontWeight.BOLD,

                    color=colors["title"],
                ),

                ft.Text(
                    ref=subtitle_text,

                    value="NT Calculator",

                    size=18,

                    weight=ft.FontWeight.W_600,

                    color=colors["subtitle"],
                ),

                ft.Container(height=4),

                ft.Text(
                    ref=hint_text,

                    value="请选择功能",

                    size=15,

                    color=colors["hint"],
                ),
            ],

            spacing=4,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    function_card = ft.Container(

        ref=function_card_ref,

        width=320,

        height=420,

        padding=16,

        border_radius=22,

        bgcolor=colors["card_bg"],

        shadow=ft.BoxShadow(
            blur_radius=16,
            spread_radius=1,
            color=colors["shadow"],
            offset=ft.Offset(0, 4),
        ),

        content=ft.Column(
            controls=[],
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    nav_bar = ft.NavigationBar(

        bgcolor=colors["card_bg"],

        indicator_color=colors["accent"],

        selected_index=0,

        on_change=on_nav_change,

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

        ref=nav_container_ref,

        width=320,

        border_radius=22,

        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,

        shadow=ft.BoxShadow(
            blur_radius=16,
            spread_radius=1,
            color=colors["shadow"],
            offset=ft.Offset(0, 4),
        ),

        content=nav_bar,
    )

    phone_card = ft.Container(

        ref=phone_card_ref,

        width=360,

        padding=18,

        border_radius=28,

        bgcolor=colors["phone_bg"],

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

    page.add(phone_card)

    apply_theme()

    show_home()


ft.run(main)