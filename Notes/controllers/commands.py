import repositoties.fileRepository as repo
import models.note

def show(txt):
    array_notes = repo.read_file()

    if array_notes:
        if txt == "all":
            print("ЖУРНАЛ ЗАМЕТОК:")
            for note in array_notes:
                print(models.note.Note.map_note(note))

        elif txt == "ID":
            for note in array_notes:
                print("ID: ", note.id)
            id = input("\nВведите id заметки: ")
            flag = True
            for note in array_notes:
                if id == note.id:
                    print(models.note.Note.map_note(note))
                    flag = False
            if flag:
                print("Нет такого ID")

        elif txt == "date":
            date = input("Введите дату в формате: dd.mm.yyyy: ")
            flag = True
            for note in array_notes:
                date_note = str(note.date)
                if date == date_note[:10]:
                    print(models.note.Note.map_note(note))
                    flag = False
            if flag:
                print("Нет такой даты")
        else:
            print("Журнал заметок пустой!")

def change_note():
    id = input("Введите ID изменяемой заметки: ")
    array_notes = repo.read_file()
    flag = False
    array_notes_new = []
    for note in array_notes:
        if id == note.id:
            note.title = input("Измените  заголовок:\n")
            note.body = input("Измените  описание:\n")
            models.note.Note.set_date(note)
            flag = True
        array_notes_new.append(note)

    if flag:
        repo.write_file(array_notes_new, 'a')
        print("Заметка с id: ", id, " успешно изменена!")
    else:
        print("Нет такого id")

def add_note():
    title = input("Введите заголовок заметки:\n")
    body = input("Введите описание заметки:\n")
    newNote = models.note.Note(title=title, body=body)
    array_notes = repo.read_file()
    for currentNode in array_notes:
        if newNote.id == currentNode.id:
            models.note.Note.set_id(newNote)
    array_notes.append(newNote)
    repo.write_file(array_notes, 'a')
    print("Заметка добавлена в журнал!")

def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = repo.read_file()
    flag = False

    for note in array_notes:
        if id == note.id:
            array_notes.remove(note)
            flag = True

    if flag:
        repo.write_file(array_notes, 'a')
        print("Заметка с id: ", id, " успешно удалена!")
    else:
        print("нет такого id")