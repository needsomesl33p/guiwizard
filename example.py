from tkinter import Frame, Widget, Label, Entry, Button, Radiobutton, StringVar
from guiwizard import GUIWizard
from typing import List, Tuple


def left_panel(panel: Frame, radio_foodtime_type: StringVar) -> Tuple[List[Widget], dict]:
    widgets: List[Widget] = []
    widgets.append(Label(panel, text='When do you eat?', name='eatlabel'))
    widgets.append(Radiobutton(
        panel, variable=radio_foodtime_type, text='morning', value='morning'))
    widgets.append(Radiobutton(panel, variable=radio_foodtime_type,
                   text='afternoon', value='afternoon'))
    widgets.append(Entry(panel, width=35, name='result'))
    packing_params = {'eatlabel': {'pady': (0, 20)},
                      'radiobutton': {'pady': (0, 20)},
                      'radiobutton2': {'pady': (0, 50)}
                      }

    return widgets, packing_params


def right_panel(panel: Frame) -> Tuple[List[Widget], dict]:
    widgets: List[Widget] = []
    widgets.append(Label(panel, text='What is your favorite food?'))
    widgets.append(Entry(panel, width=35, name='fav_food'))
    widgets.append(Button(panel, text="Let's eat", command=get_my_fav_food))
    packing_params = {'fav_food': {'pady': (20, 90)}}
    return widgets, packing_params


def get_my_fav_food():
    foodtime = radio_foodtime_type.get()
    fav_food = gui.get_component_from_window('fav_food').get()
    result_entry = gui.get_component(0, 'result')
    result_entry.insert(0, f'I usually eat {fav_food} in {foodtime}.')
    gui.update_ui({'result': {'state': 'readonly'}})


gui = GUIWizard('My Exmaple GUI App', 1000, 760, 20, 20, 500, 450, 'logo.png')
gui.create_panels(2)

radio_foodtime_type = StringVar()
radio_foodtime_type.set('none')

left_widgets, left_widget_params = left_panel(
    gui.panels[0], radio_foodtime_type)
right_widgets, right_widget_params = right_panel(gui.panels[1])

gui.pack_on_panel(left_widgets, left_widget_params)
gui.pack_on_panel(right_widgets, right_widget_params)
gui.pack_on_window()
gui.window.mainloop()
