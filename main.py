from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window, WindowBase
from kivymd.uix.button import MDFillRoundFlatButton
from widgets import InfoContent, MemberRow


Window.softinput_mode = 'below_target'

bg_color = [0.26, 0.40, 0.55, 1]


class FlatButton(MDFillRoundFlatButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = bg_color
        self.line_color = bg_color


class Owe(MDApp):
    """Основной класс приложения"""

    md_bg_color = bg_color
    title = "Сколько должен"
    by_who = 'by anb76ru'
    version = "version 0.0.1"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_file('owe.kv')
        self.part_list_widgets = {}
        self.part_list = {}
        self.hint_text = "Расчет не производился"
        self.info_dialog = MDDialog(
            title="Как работать с приложением:\n",
            type='custom',
            content_cls=InfoContent(),
            buttons=[
                FlatButton(text="CLOSE", on_release=self.close_info)
            ]
        )

    def build(self):
        return self.screen

    def on_start(self):
        self.screen.ids.result.add_widget(MDLabel(
            text=self.hint_text,
            halign="center",
            font_style='H6'
        ))

    @staticmethod
    def close_app():
        """Закрыть приложение"""

        Owe().get_running_app().stop()
        WindowBase().close()

    def show_info(self):
        """Показать информацию"""

        info_text_list = [
            '\n1. На вкладке "Участники"',
            'ввести количество участников',
            '2. Нажать кнопку',
            '"Создать таблицу"',
            '3. Ввести имена',
            'и сумму затрат ',
            'для каждого участника',
            '4. Нажать Рассчитать',
            'После нажатия рассчитать,',
            'приложение переключится',
            'на вкладку "Расчет"',
            'Кнопки "Добавить" и "Удалить"',
            'соответственно добавляют',
            'и удаляют одну строку',
            'для заполнения данных'

        ]

        self.info_dialog.content_cls.ids.info_content.clear_widgets()
        for line in info_text_list:
            widget = MDLabel(
                text=line,
                halign="center",
                font_style='Caption',
                size_hint_y=None

            )
            self.info_dialog.content_cls.ids.info_content.add_widget(widget)
        self.info_dialog.open()

    def close_info(self, inst):
        """Закрыть окно с информацией"""

        self.info_dialog.dismiss()

    def get_count_participant(self):
        """Получить количество участников"""

        if self.screen.ids.participant_count.text:
            count = int(self.screen.ids.participant_count.text)
        elif len(self.part_list_widgets):
            count = len(self.part_list_widgets)
        else:
            count = 0
        return count

    def add_row(self):
        row_color = (0.98, 0.98, 0.98, 1)
        widget = MemberRow(color=row_color, text=str(len(self.part_list_widgets) + 1))
        self.part_list_widgets[f'user_{len(self.part_list_widgets) + 1}'] = widget
        self.screen.ids.table_list.add_widget(widget)

    def remove_row(self):
        if self.part_list_widgets:
            widget = self.part_list_widgets.pop(f'user_{len(self.part_list_widgets)}')
            self.screen.ids.table_list.remove_widget(widget)

    def create_table_to_add_data(self):
        """Создать таблицу для заполнения данных"""
        from kivymd.uix.textfield import MDTextField

        self.screen.ids.table_list.clear_widgets()
        participant_count = self.get_count_participant()
        if participant_count <= 0 or participant_count >= 100:
            return
        for i in range(1, participant_count+1):
            row_color = (0.98, 0.98, 0.98, 1)
            #widget = MDTextField(text='123123')
            widget = MemberRow(color=row_color, text=str(i)+'widget')
            self.part_list_widgets[f'user_{i}'] = widget
            self.screen.ids.table_list.add_widget(widget)


if __name__ == '__main__':
    Owe().run()
