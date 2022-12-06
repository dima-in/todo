from datetime import datetime


def add_event(ev_inst):
    event_list.append(event_inst)


def show_list_event(ev_inst):
    for item in event_list:
        print(event_list.index(item) + 1, 'событие :', item.text, item.date, item.cond)


def make_done(index, event_list) -> None:
    event_list.pop(index)


class EventTodo:
    def __init__(self,  text, date, cond):

        self.text = text
        self.date = date
        self.cond = cond


event_cond = False
event_list = list()
event_text = None
while event_text != 'q':

    event_date = datetime.now()
    event_text = input('текст события: ')
    if event_text != 'q':
        event_inst = EventTodo(event_text, event_date, event_cond)
        add_event(event_inst)

show_list_event(event_list)
index = int(input('чтобы удалить введите номер события'))
make_done(index -1, event_list)
show_list_event(event_list)

if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
