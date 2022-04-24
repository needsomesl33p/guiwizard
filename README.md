# GUIWizard
Defines a tkinter window and frames/panels to make the GUI development more transparent and easier.      Think in panels and design your application according to them. Tear down your GUI to panels and put the widgets on them.

## Defining the panels

### Left panel

Each panel can be described by a function:

```python
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
```

We need to provide a parent component, which is a panel or `Frame` and other variables to the GUI as parameters. Then we start adding `Widgets` to a list and defining the belonging parameters.

We have to refer to the components with their names.

Give a name to a component:

`widgets.append(Label(panel, text='When do you eat?', name='eatlabel'))`

Link it with parameters:

`{'eatlabel': {'pady': (0, 20)}...`

If you do not name the components, you can still refer to them with the following names for example:

`radiobutton`

`radiobutton1`

`...`

### Right panel

```python
def right_panel(panel: Frame) -> Tuple[List[Widget], dict]:
    widgets: List[Widget] = []
    widgets.append(Label(panel, text='What is you favorite food?'))
    widgets.append(Entry(panel, width=35, name='fav_food'))
    widgets.append(Button(panel, text="Let's eat", command=get_my_fav_food))
    packing_params = {'fav_food': {'pady': (20, 90)}}
    return widgets, packing_params
```

After we defined the panels we can add more logic to our application:

```python
def get_my_fav_food():
    foodtime = radio_foodtime_type.get()
    fav_food = gui.get_component_from_window('fav_food').get()
    result_entry = gui.get_component(0, 'result')
    result_entry.insert(0, f'I usually eat {fav_food} in {foodtime}.')
    gui.update_ui({'result': {'state': 'readonly'}})
```

We can get a component by calling GUIWizard methods:
 - get_component_from_window()
 - get_component()

This system is more practical when you have a massive amount of Widgets on your window and you use the grid packing system. It is easy to lost in the rows and columns, plus you need to calculate and align them. 

With this technique you organise your `Widgets` by panels and names. Tearing down a complex GUI makes the whole picture transparent and development could be easier. 

## Creating the window, panels and put them together

```python
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
```

## Try it out

`python3 example.py`

The created GUI with GUIWizard:

![GUI](https://raw.githubusercontent.com/needsomesl33p/guiwizard/master/images/init.png)

After some interaction:

![Wizard](https://raw.githubusercontent.com/needsomesl33p/guiwizard/master/images/after.png)

### Tested on

`Python 3.9.10`

### Requirements

`tkinter`


