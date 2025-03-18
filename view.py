import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.__bottone_spell = None
        self.frase = None
        self.__menu_modality = None
        self.__menu_lingua = None
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None
        self.lv=None

        # define the UI elements and populate the page



    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here
        self.lv=ft.ListView(expand=1, spacing =10, padding=20, auto_scroll=True)
        self.__menu_lingua= ft.Dropdown(label="Select language", options=[ft.dropdown.Option("english"),ft.dropdown.Option("italian"),ft.dropdown.Option("spanish")],width=self.page.width)
        row1=ft.Row(spacing=0,controls=[ self.__menu_lingua], alignment=ft.MainAxisAlignment.START)
        self.page.add(row1)

        self.__menu_modality=ft.Dropdown(label="Search modality", options=[ft.dropdown.Option("Default"),ft.dropdown.Option("Linear"),ft.dropdown.Option("Dichotomic")],width=200)
        self.frase= ft.TextField(label="Add your sentence here")

        def handleFunction(e):
            self.__controller.handleSpellCheck(self.frase.value, self.__menu_lingua.value, self.__menu_modality.value)

        self.__bottone_spell=ft.ElevatedButton(text="Spell Check", on_click =handleFunction , color ="lightblue")
        row2=ft.Row(controls=[self.__menu_modality,self.frase, self.__bottone_spell],width=self.page.width)
        self.page.add(row2)

        # self.__txtOut=ft.Text(value=f"Fase inserita: {self.__frase.value}")
        # self.page.add(self.__txtOut)

        #self.page.add([])

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
