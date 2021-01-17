from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from plyer import filechooser
import txthide
kv = '''
<Root>:
    orientation:"vertical"
    padding:[20,20,20,10]
    spacing:10
    TextInput:
        id:txt_data
    BoxLayout:
        size_hint_y:None
        height:32
        Button:
            size_hint:None,None
            text:"Save"
            size:150,32
            on_release:root.btn_browse_save()
        Button:
            size_hint:None,None

            text:"New"
            size:150,32
            on_release:root.btn_browse_new()
        Button:
            size_hint_x:None
            width:150
            text:"opens"
            on_release:root.btn_browse_click()
'''
Builder.load_string(kv)


class Root(BoxLayout):

    file_opened = None

    def btn_browse_click(self):
        result = filechooser.open_file()
        if result:
            self.file_opened = result[0]
            file = open(self.file_opened)
            data = file.read()
            file.close()
            self.ids.txt_data.text = txthide.whitespaces_to_str(
                data)

        else:
            self.file_opened = None

    def btn_browse_new(self):
        self.ids.txt_data.text = ""
        self.file_opened = None

    def btn_browse_save(self):
        data = txthide.str_to_whitespaces(self.ids.txt_data.text)

        if self.file_opened:

            file = open(self.file_opened, "w")
            file.write(data)
            file.close()
        else:
            result = filechooser.save_file()
            if result:
                self.file_opened = result[0]
                file = open(self.file_opened, "w")
                file.write(data)
                file.close()


class THideApp(App):
    def build(self):
        return Root()


THideApp().run()
