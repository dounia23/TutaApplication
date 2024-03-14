from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screen import Screen

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        title_label = MDLabel(
            text="Login or Create Account",
            halign="center",
            font_style="H4",
            size_hint_y=None,
            height=100,
        )
        layout.add_widget(title_label)
        create_account_button = MDRaisedButton(
            text="Create Account",
            size_hint=(None, None),
            width=200,
            height=50,
            pos_hint={"center_x": 0.5},
            on_release=self.on_create_account,
        )
        layout.add_widget(create_account_button)
        self.add_widget(layout)

    def on_create_account(self, instance):
        # Add logic to handle creating a new account
        pass
