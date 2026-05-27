import flet as ft


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


def get_colors(is_dark_theme: bool):
    return DARK if is_dark_theme else LIGHT
