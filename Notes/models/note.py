from datetime import datetime
import controllers.counter as counter


class Note:

    def __init__(self, id=str(counter.counter()), title="Название", body="Заметка",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    
    def set_id(note):
        note.id = str(counter.counter())

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'Название: ' + note.title + '\n' + 'Описание: ' + note.body + '\n' + 'Дата публикации: ' + note.date