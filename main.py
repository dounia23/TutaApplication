from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

class TutaAbsolutaApp(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()

        # Create the main screen
        main_screen = Screen(name="main")
        layout = BoxLayout(orientation="vertical")
        title_label = MDLabel(
            text="Welcome to Tuta Absoluta Application",
            halign="center",
            font_style="H4",
            theme_text_color="Custom",
            text_color=[0, 0.7, 0, 1],
            size_hint_y=None,
            height=dp(80),
        )
        layout.add_widget(title_label)
        image = Image(source="Images/welcome.jpg", size_hint=(1, 2))
        layout.add_widget(image)
        get_started_button = MDRaisedButton(
            text="Get Started",
            size_hint=(None, None),
            width=dp(200),
            height=dp(50),
            pos_hint={"center_x": 0.5},
            on_release=self.on_get_started,
        )
        layout.add_widget(get_started_button)
        main_screen.add_widget(layout)
        self.screen_manager.add_widget(main_screen)

        # Create the login screen
        login_screen = Screen(name="login")
        login_layout = BoxLayout(orientation="vertical")
        login_title_label = MDLabel(
            text="Login or Create Account",
            halign="center",
            font_style="H4",
            size_hint_y=None,
            height=dp(80),
        )
        login_layout.add_widget(login_title_label)
        login_screen.add_widget(login_layout)
        self.screen_manager.add_widget(login_screen)

        return self.screen_manager

    def on_get_started(self, instance):
        self.screen_manager.current = "login"

TutaAbsolutaApp().run()
