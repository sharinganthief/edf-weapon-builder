import sys
import tkinter as tk
from decimal import Decimal
from tkinter import ttk
import webbrowser
from text import *
import json

labelwidth = 20
inputwidth = 25


def translateNestedDict(d):
    return {getText(key): (translateNestedDict(value) if isinstance(value, dict) else value) for key, value in
            d.items()}


def getKeyFromValue(d, v):
    # print(v)
    for key, value in d.items():
        if v == value:
            # print(key)
            return key
    return f"{v} not in {d}"


def getpath(nested_dict, value, prepath=()):
    # from https://stackoverflow.com/questions/22162321/search-for-a-value-in-a-nested-dictionary-python
    for k, v in nested_dict.items():
        path = prepath + (k,)
        if v == value: # found value
            return path
        elif hasattr(v, 'items'): # v is a dict
            p = getpath(v, value, path) # recursive call
            if p is not None:
                return p
    return None


def makeLabelClickable(widget, url):
    label = widget.label
    label.configure(fg="blue", underline=True, cursor="hand2")
    label.bind("<Button-1>", lambda e: webbrowser.open(url))


def disableInput(widget):
    widget.input.config(background="grey", state="disabled")


def enableInput(widget):
    if isinstance(widget, SliderWidget):
        widget.input.config(state="normal", background="#F0F0F0")
    else:
        widget.input.config(state="normal", background="white")


def setWidgetValue(widget, value):
    widget.inputVar.set(value)


# class ClickableLabel(tk.Label):
#     def __init__(self, parent, labeltext, labelwidth, url):
#         tk.Label.__init__(self, parent, labeltext=getText(labeltext), justify="left", relief="groove", anchor="w", fg="blue",
#                           underline=True, labelwidth=labelwidth, cursor="hand2")
#         self.bind("<Button-1>", lambda e:webbrowser.open_url(url))




# class ScrollableFrame(ttk.Frame):
#     def __init__(self, parent, *args, **kwargs):
#         tk.Frame.__init__(self, parent)
#         self.frame = tk.Frame(self, width=300, height=300)
#         self.frame.pack(expand=True, fill="both")  # .grid(row=0,column=0)
#         self.canvas = tk.Canvas(self.frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 500, 500))
#         hbar = ttk.Scrollbar(self.frame, orient="horizontal")
#         hbar.pack(side="bottom", fill="x")
#         hbar.config(command=self.canvas.xview)
#         vbar = ttk.Scrollbar(self.frame, orient="vertical")
#         vbar.pack(side="right", fill="y")
#         vbar.config(command=self.canvas.yview)
#         self.canvas.config(width=300, height=300)
#         self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
#         self.canvas.pack(side="left", expand=True, fill="both")
#         self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
#
#         # hscroll = ttk.Scrollbar(self, orient="horizontal")
#         # vscroll = ttk.Scrollbar(self, orient="vertical")
#         #
#         # hscroll.pack(side="bottom", fill="x")
#         # vscroll.pack(side="left", fill="y")
#         # hscroll.config()
#         # self.canvas = tk.Canvas(self, xscrollcommand=hscroll.set, yscrollcommand=vscroll.set)
#         # self.canvas.config(width=300, height=300)
#         # self.frame = tk.Frame(self.canvas)
#         # hscroll.config(command=self.canvas.xview)
#         # vscroll.config(command=self.canvas.yview)
#         # self.canvas.pack(side="top", fill="both", expand=True)
#         #
#         # self.frame.pack(fill="both")
#         # self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

# https://pypi.org/project/tkScrolledFrame/

class ScrolledFrame(tk.Frame):
    """Scrollable Frame widget.

    Use display_widget() to set the interior widget. For example,
    to display a Label with the text "Hello, world!", you can say:

        sf = ScrolledFrame(self)
        sf.pack()
        sf.display_widget(Label, text="Hello, world!")

    The constructor accepts the usual Tkinter keyword arguments, plus
    a handful of its own:

      scrollbars (str; default: "both")
        Which scrollbars to provide.
        Must be one of "vertical", "horizontal," "both", or "neither".

      use_ttk (bool; default: False)
        Whether to use ttk widgets if available.
        The default is to use standard Tk widgets. This setting has
        no effect if ttk is not available on your system.
    """

    def __init__(self, master=None, **kw):
        """Return a new scrollable frame widget."""

        tk.Frame.__init__(self, master)

        # Hold these names for the interior widget
        self._interior = None
        self._interior_id = None

        # Whether to fit the interior widget's width to the canvas
        self._fit_width = False

        # Which scrollbars to provide
        if "scrollbars" in kw:
            scrollbars = kw["scrollbars"]
            del kw["scrollbars"]

            if not scrollbars:
                scrollbars = self._DEFAULT_SCROLLBARS
            elif not scrollbars in self._VALID_SCROLLBARS:
                raise ValueError("scrollbars parameter must be one of "
                                 "'vertical', 'horizontal', 'both', or "
                                 "'neither'")
        else:
            scrollbars = self._DEFAULT_SCROLLBARS

        # Whether to use ttk widgets if available
        if "use_ttk" in kw:
            if ttk and kw["use_ttk"]:
                Scrollbar = ttk.Scrollbar
            else:
                Scrollbar = tk.Scrollbar
            del kw["use_ttk"]
        else:
            Scrollbar = tk.Scrollbar

        # Default to a 1px sunken border
        if not "borderwidth" in kw:
            kw["borderwidth"] = 1
        if not "relief" in kw:
            kw["relief"] = "sunken"

        # Set up the grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Canvas to hold the interior widget
        c = self._canvas = tk.Canvas(self,
                                     borderwidth=0,
                                     highlightthickness=0,
                                     takefocus=0)

        # Enable scrolling when the canvas has the focus
        self.bind_arrow_keys(c)
        self.bind_scroll_wheel(c)

        # Call _resize_interior() when the canvas widget is updated
        c.bind("<Configure>", self._resize_interior)

        # Scrollbars
        xs = self._x_scrollbar = Scrollbar(self,
                                           orient="horizontal",
                                           command=c.xview)
        ys = self._y_scrollbar = Scrollbar(self,
                                           orient="vertical",
                                           command=c.yview)
        c.configure(xscrollcommand=xs.set, yscrollcommand=ys.set)

        # Lay out our widgets
        c.grid(row=0, column=0, sticky="nsew")
        if scrollbars == "vertical" or scrollbars == "both":
            ys.grid(row=0, column=1, sticky="ns")
        if scrollbars == "horizontal" or scrollbars == "both":
            xs.grid(row=1, column=0, sticky="we")

        # Forward these to the canvas widget
        self.bind = c.bind
        self.focus_set = c.focus_set
        self.unbind = c.unbind
        self.xview = c.xview
        self.xview_moveto = c.xview_moveto
        self.yview = c.yview
        self.yview_moveto = c.yview_moveto

        # Process our remaining configuration options
        self.configure(**kw)

    def __setitem__(self, key, value):
        """Configure resources of a widget."""

        if key in self._CANVAS_KEYS:
            # Forward these to the canvas widget
            self._canvas.configure(**{key: value})

        else:
            # Handle everything else normally
            tk.Frame.configure(self, **{key: value})

    # ------------------------------------------------------------------------

    def bind_arrow_keys(self, widget):
        """Bind the specified widget's arrow key events to the canvas."""

        widget.bind("<Up>",
                    lambda event: self._canvas.yview_scroll(-1, "units"))

        widget.bind("<Down>",
                    lambda event: self._canvas.yview_scroll(1, "units"))

        widget.bind("<Left>",
                    lambda event: self._canvas.xview_scroll(-1, "units"))

        widget.bind("<Right>",
                    lambda event: self._canvas.xview_scroll(1, "units"))

    def bind_scroll_wheel(self, widget):
        """Bind the specified widget's mouse scroll event to the canvas."""

        widget.bind("<MouseWheel>", self._scroll_canvas)
        widget.bind("<Button-4>", self._scroll_canvas)
        widget.bind("<Button-5>", self._scroll_canvas)

    def cget(self, key):
        """Return the resource value for a KEY given as string."""

        if key in self._CANVAS_KEYS:
            return self._canvas.cget(key)

        else:
            return tk.Frame.cget(self, key)

    # Also override this alias for cget()
    __getitem__ = cget

    def configure(self, cnf=None, **kw):
        """Configure resources of a widget."""

        # This is overridden so we can use our custom __setitem__()
        # to pass certain options directly to the canvas.
        if cnf:
            for key in cnf:
                self[key] = cnf[key]

        for key in kw:
            self[key] = kw[key]

    # Also override this alias for configure()
    config = configure

    def display_widget(self, widget_class, fit_width=False, **kw):
        """Create and display a new widget.

        If fit_width == True, the interior widget will be stretched as
        needed to fit the width of the frame.

        Keyword arguments are passed to the widget_class constructor.

        Returns the new widget.
        """

        # Blank the canvas
        self.erase()

        # Set width fitting
        self._fit_width = fit_width

        # Set the new interior widget
        self._interior = widget_class(self._canvas, **kw)

        # Add the interior widget to the canvas, and save its widget ID
        # for use in _resize_interior()
        self._interior_id = self._canvas.create_window(0, 0,
                                                       anchor="nw",
                                                       window=self._interior)

        # Call _update_scroll_region() when the interior widget is resized
        self._interior.bind("<Configure>", self._update_scroll_region)

        # Fit the interior widget to the canvas if requested
        # We don't need to check fit_width here since _resize_interior()
        # already does.
        self._resize_interior()

        # Scroll to the top-left corner of the canvas
        self.scroll_to_top()

        return self._interior

    def erase(self):
        """Erase the displayed widget."""

        # Clear the canvas
        self._canvas.delete("all")

        # Delete the interior widget
        del self._interior
        del self._interior_id

        # Save these names
        self._interior = None
        self._interior_id = None

        # Reset width fitting
        self._fit_width = False

    def scroll_to_top(self):
        """Scroll to the top-left corner of the canvas."""

        self._canvas.xview_moveto(0)
        self._canvas.yview_moveto(0)

    # ------------------------------------------------------------------------

    def _resize_interior(self, event=None):
        """Resize the interior widget to fit the canvas."""

        if self._fit_width and self._interior_id:
            # The current width of the canvas
            canvas_width = self._canvas.winfo_width()

            # The interior widget's requested width
            requested_width = self._interior.winfo_reqwidth()

            if requested_width != canvas_width:
                # Resize the interior widget
                new_width = max(canvas_width, requested_width)
                self._canvas.itemconfigure(self._interior_id, width=new_width)

    def _scroll_canvas(self, event):
        """Scroll the canvas."""

        c = self._canvas

        if sys.platform.startswith("darwin"):
            # macOS
            c.yview_scroll(-1 * event.delta, "units")

        elif event.num == 4:
            # Unix - scroll up
            c.yview_scroll(-1, "units")

        elif event.num == 5:
            # Unix - scroll down
            c.yview_scroll(1, "units")

        else:
            # Windows
            c.yview_scroll(-1 * (event.delta // 120), "units")

    def _update_scroll_region(self, event):
        """Update the scroll region when the interior widget is resized."""

        # The interior widget's requested width and height
        req_width = self._interior.winfo_reqwidth()
        req_height = self._interior.winfo_reqheight()

        # Set the scroll region to fit the interior widget
        self._canvas.configure(scrollregion=(0, 0, req_width, req_height))

    # ------------------------------------------------------------------------

    # Keys for configure() to forward to the canvas widget
    _CANVAS_KEYS = "width", "height", "takefocus"

    # Scrollbar-related configuration
    _DEFAULT_SCROLLBARS = "both"
    _VALID_SCROLLBARS = "vertical", "horizontal", "both", "neither"


class BigTextWidget(tk.Frame):
    def __init__(self, parent, labeltext, tooltip="", width=30, height=5):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.label = tk.Label(self, text=getText(labeltext), width=labelwidth, justify="left", relief="groove", anchor="w")
        # self.inputVar = tk.StringVar(self, "")
        if tooltip != "":
            self.tooltip = ToolTip(self.label, text=getText(tooltip))
            newText=self.label.cget("text")+"⍰"
            self.label.configure(underline=True, text=newText)
        self.input = tk.Text(self, width=width, height=height)

        self.label.grid(row=0, column=0)
        self.input.grid(row=0, column=1)
        # self.button2 = tk.Button(self, text="disable", command=lambda: disableInput(self))
        # self.button = tk.Button(self, text="enable", command=lambda: enableInput(self))
        # self.button.grid(row=0, column=2)
        # self.button2.grid(row=0, column=4)

    def value(self):
        return self.input.get()

    def setValue(self, value):
        self.input.delete(1.0, "end")
        self.input.insert("end", value)
        # self.inputVar.set(value)


class CheckBoxWidget(tk.Frame):
    def __init__(self, parent, labeltext, uncheckedValue, checkedValue, labelwidth=labelwidth, tooltip="", link=""):
        tk.Frame.__init__(self, parent)
        self.uncheckedValue = uncheckedValue
        self.checkedValue = checkedValue
        self.uncheckedType = type(uncheckedValue)
        self.checkedType = type(checkedValue)

        self.label = tk.Label(self, text=getText(labeltext), width=labelwidth+18, justify="left", relief="groove", anchor="w")
        if tooltip != "":
            self.tooltip = ToolTip(self.label, text=getText(tooltip))
            newText=self.label.cget("text")+"⍰"
            self.label.configure(underline=True, text=newText)
        if link !="":
            makeLabelClickable(self, link)
        self.input = tk.StringVar(self, uncheckedValue)
        self.checkBox = tk.Checkbutton(self, variable=self.input, offvalue=uncheckedValue, onvalue=checkedValue)
        self.label.grid(row=0, column=0)
        self.checkBox.grid(row=0, column=1)

    def value(self):
        # print(self.input.get(), self.uncheckedValue, self.checkedValue)
        if self.input.get() == str(self.uncheckedValue) or self.input.get() == self.uncheckedValue:
            return self.uncheckedType(self.input.get())
        if self.input.get() == str(self.checkedValue) or self.input.get() == self.checkedValue:
            return self.checkedType(self.input.get())


    def setValue(self, v):
        if v == self.uncheckedValue:
            self.input.set(v)
        elif v == self.checkedValue:
            self.input.set(v)
        else: raise ValueError("Checkbox widget was attempted to be set to a value it does not encompass")


class FreeInputWidget(tk.Frame):
    def __init__(self, parent, labeltext, inputType, restrictPositive=False, initialValue="", tooltip="", link=""):
        tk.Frame.__init__(self, parent)
        self.inputType = inputType

        def validateFloat(newValue):
            try:
                newValue = float(newValue)
                if restrictPositive:
                    return True and newValue >= 0
                else: return True
            except:
                return False

        def validateInt(newValue):
            try:
                newValue = int(newValue)
                if restrictPositive:
                    return True and newValue >= 0
                else: return True
            except:
                return False

        if inputType == float:  # float
            # self.inputVar = tk.DoubleVar(self, 0.0)
            if initialValue != "":
                self.inputVar = tk.StringVar(self, initialValue)
            else:
                self.inputVar = tk.StringVar(self, "0.0")
            validate = self.register(validateFloat)
        elif inputType == int:  # int
            # self.inputVar = tk.IntVar(self, 0)
            if initialValue != "":
                self.inputVar = tk.StringVar(self, initialValue)
            else:
                self.inputVar = tk.StringVar(self, "0")
            validate = self.register(validateInt)
        else:  # string
            self.inputVar = tk.StringVar(self, initialValue)
            validate = lambda: True


        self.parent = parent
        self.label = tk.Label(self, text=getText(labeltext), width=labelwidth, justify="left", relief="groove", anchor="w")
        if tooltip != "":
            self.tooltip = ToolTip(self.label, text=getText(tooltip))
            newText=self.label.cget("text")+"⍰"
            self.label.configure(underline=True, text=newText)
        if link !="":
            makeLabelClickable(self, link)
        self.input = tk.Entry(self, textvariable=self.inputVar, width=inputwidth, validate="key", validatecommand=(validate, "%P"), )

        self.label.grid(row=0, column=0)
        self.input.grid(row=0, column=1)
        # self.button2 = tk.Button(self, text="disable", command=lambda: disableInput(self))
        # self.button = tk.Button(self, text="enable", command=lambda: enableInput(self))
        # self.button.grid(row=0, column=2)
        # self.button2.grid(row=0, column=4)

    def value(self):
        return self.inputType(self.inputVar.get())

    def setValue(self, value):
        self.inputVar.set(value)


class DropDownWidget(tk.Frame):
    def __init__(self, parent, labeltext, options, command="", tooltip="", link="", translate=True):
        if not isinstance(options, dict):
            # print(options)
            raise TypeError("DropDownWidgets take dictionaries of the choices and the values they represent as keys and values")


        tk.Frame.__init__(self, parent)
        # self.optionType = optionType
        if translate:
            self.options = {getText(key): value for key, value in options.items()}
        else:
            self.options = options
        self.optionKeys = list(self.options.keys())
        self.optionValues = list(self.options.values())
        self.dropDownDisplayed = tk.StringVar(self, self.optionKeys[0])

        self.label = tk.Label(self, text=getText(labeltext), width=labelwidth, justify="left", relief="groove", anchor="w")
        if tooltip != "":
            self.tooltip = ToolTip(self.label, text=getText(tooltip))
            newText=self.label.cget("text")+"⍰"
            self.label.configure(underline=True, text=newText)
        if link !="":
            makeLabelClickable(self, link)
        self.input = tk.OptionMenu(self, self.dropDownDisplayed, *list(self.options.keys()), command=command)  # , command=self.updateValue)
        self.input.config(width=inputwidth-7)
        self.label.grid(row=0, column=0)
        self.input.grid(row=0, column=1)


    def updateValue(self, something):
        self.inputVar.set(self.options[self.dropDownDisplayed.get()])

    def replaceOptionMenu(self, options, command, *args):
        self.options = {getText(key): value for key, value in options.items()}
        self.input.grid_forget()
        self.dropDownDisplayed.set(list(self.options.keys())[0])
        self.input = tk.OptionMenu(self, self.dropDownDisplayed, *list(self.options.keys()), command=command)
        self.input.config(width=inputwidth - 7)
        self.input.grid(row=0, column=2)

    def replaceOptionMenuNoCmd(self, options):
        self.options = {getText(key): value for key, value in options.items()}
        self.input.grid_forget()
        self.dropDownDisplayed.set(list(self.options.keys())[0])
        self.input = tk.OptionMenu(self, self.dropDownDisplayed, *list(self.options.keys()))
        self.input.config(width=inputwidth - 7)
        self.input.grid(row=0, column=2)

    def value(self):
        return self.options[self.dropDownDisplayed.get()]
        # return self.optionType(self.options[self.dropDownDisplayed.get()])

    def setValue(self, value):
        if value in self.options.values():
            self.dropDownDisplayed.set(getKeyFromValue(self.options, value))
        else:
            pass
            # print(f"{value} not in drop down options")
        #     self.dropDownDisplayed.set(value)


class MultiDropDownWidget(tk.LabelFrame):
    def __init__(self, parent, label, options, isChild=False):
        tk.LabelFrame.__init__(self, parent, text=label)
        # self.originalOptions = {getText(key): value for key, value in options.items()}
        self.originalOptions = translateNestedDict(options)
        if isChild is False:
            self.root = self
        else:
            self.root = self

        if isinstance(options, dict):
            if isinstance(list(options.values())[0], dict):
                # self.options = {getText(key): key for key in options.keys()}
                self.options = {key: key for key in self.originalOptions.keys()}
                self.hasChild = True
            else:
                self.options = {key: value for key, value in self.originalOptions.items()}
                # self.options = {getText(key): value for key, value in options.items()}
                self.hasChild = False

        else:
            raise TypeError("DropDownWidgets take dictionaries of the choices and the values they represent as keys and values")

        self.widgets = []
        self.widgetValues = []
        self.valueLabel = FreeInputWidget(self, "Value", str)
        self.baseChoice =  DropDownWidget(self.root, "Choice", self.options,
                                                         command=lambda x: self.reconstructChildren(1), translate=False)
        self.widgets.append(self.baseChoice)
        self.baseChoice.pack()
        self.constructChildren(1)
        # self.constructChildren(oOptions=self.originalOptions[getText(self.baseChoice.value())])
        self.valueLabel.pack()
        self.valueLabel.input.config(state="readonly")
        # disableInput(self.valueLabel)

    def constructChildren(self, *args, oOptions="", widgetList=""):
        options = oOptions
        while True:
            b = False
            if isinstance(options, dict):
                if isinstance(list(options.values())[0], dict):
                    childoptions = {key: key for key in options.keys()}
                    command = self.reconstructChildren
                    child = DropDownWidget(self.root, "Choice", childoptions,
                                           command=lambda x: self.reconstructChildren(len(self.widgets)-1), translate=False)
                    self.root.widgets.append(child)
                    child.pack()
                    options = options[child.value()]
                else:
                    b = True
                    childoptions = options
                    child = DropDownWidget(self.root, "Choice", childoptions, command=self.updateValueLabel, translate=False)
                    self.root.widgets.append(child)
                    child.pack()
            else:
                pass
            if b is True:
                break
            else:
                pass
                # options = options[child.value()]
        self.updateValueLabel()

    def updateValueLabel(self, *args):
        self.valueLabel.setValue(self.widgets[len(self.widgets)-1].value())
        self.valueLabel.pack_forget()
        self.valueLabel.pack()

    def reconstructChildren(self, index):
        self.destroyChildren(index)
        self.constructChildren(index)

    def destroyChildren(self, index, *args):
        for child in self.widgets[index:]:
            # print(f"{child.value()} destroyed")
            child.pack_forget()
            self.widgets.pop(self.widgets.index(child))
            child.destroy()

    def constructChildren(self, index):
        options = self.originalOptions
        for i in range(index):
            options = options[self.widgets[i].dropDownDisplayed.get()]
        i += 2
        while isinstance(options, dict):
            if isinstance(options[list(options.keys())[0]], dict):
                childOptions = {key: key for key in options.keys()}
                child = DropDownWidget(self, "Sub-category", childOptions, command=lambda x, i=i: self.reconstructChildren(i), translate=False)
                options = options[child.dropDownDisplayed.get()]
                self.widgets.append(child)
                child.pack()
                i+=1
            else:
                childOptions = {key: value for key, value in options.items()}
                child = DropDownWidget(self, "Choose value", childOptions, command=self.updateValueLabel, translate=False)
                # options = options[child.dropDownDisplayed.get()]
                self.widgets.append(child)
                child.pack()
                self.updateValueLabel()
                break

    def disableInput(self, *args):
        for w in self.widgets:
            disableInput(w)

    def enableInput(self, *args):
        for w in self.widgets:
            enableInput(w)

    def value(self):
        # try:
        #     return self.widgets[-1].value()
        # except:
        #     print("aaa")
        #     print(self.widgets[-1].dropDownDisplayed.get())
        #     return self.widgets[-1].value()
        if self.valueLabel.value() != "0":
            return self.valueLabel.value()
        else:
            return 0

    def setValue(self, v):
        valuePath = getpath(self.originalOptions, v)
        if valuePath is not None:
            self.baseChoice.dropDownDisplayed.set(valuePath[0])
            self.reconstructChildren(1)
            i = 1
            for widget in self.widgets[1:]:
                widget.dropDownDisplayed.set(valuePath[i])
                i += 1
        self.valueLabel.setValue(v)


class SliderWidget(tk.Frame):
    def __init__(self, parent, labeltext, min, max, resolution=0, initialValue="", tooltip="", link=""):
        if initialValue == "":
            initialValue = (min + max) / 2
        if resolution == 0:
            resolution = (max - min) / 100
        tk.Frame.__init__(self, parent)
        # self.inputVar = tk.DoubleVar(self, (min + max) / 2)
        # print(self.inputVar.get())
        self.inputVar = tk.DoubleVar(self, initialValue)
        self.input = tk.Scale(self, variable=self.inputVar, from_=min, to=max, orient="horizontal", resolution=resolution, length=inputwidth*6, command=self.updateValue) #, command=self.updateValue)
        self.input.set(initialValue)
        self.label = tk.Label(self, text=getText(labeltext), width=labelwidth, justify="left", relief="groove", anchor="w")
        self.label.grid(row=0, column=0)

        if tooltip != "":
            self.tooltip = ToolTip(self.label, text=getText(tooltip))
            newText=self.label.cget("text")+"⍰"
            self.label.configure(underline=True, text=newText)
        if link !="":
            makeLabelClickable(self, link)

        self.input.grid(row=0, column=1)

        self.v = initialValue


    # def updateValue(self, *args, **kwargs):
        # self.inputVar.set(self.input.get()
        # print(self.inputVar)
    def updateValue(self, *args):
        self.v = self.input.get()

    def value(self):
        return float(self.v)
        # return self.input.get()
        #return self.inputVar.get()

    def setValue(self, value):
        self.v = value
        self.input.set(value)


class SpinBoxWidget(tk.Frame):
    def __init__(self, parent, labeltext, min, max, tooltip="", initialValue=0):
        tk.Frame.__init__(self, parent)
        self.inputVar = tk.IntVar(self, initialValue)
        self.input = tk.Spinbox(self, from_=min, to=max, textvariable=self.inputVar)
        self.label = tk.Label(self, text=getText(labeltext), width=labelwidth+2
                              , justify="left", relief="groove", anchor="w")
        if tooltip != "":
            self.tooltip = ToolTip(self.label, text=getText(tooltip))
            newText=self.label.cget("text")+"⍰"
            self.label.configure(underline=True, text=newText)
        self.label.grid(row=0, column=0)
        self.input.grid(row=0, column=1)
        # self.button = tk.Button(self, text="enable", command=enableInput(self))
        # self.button2 = tk.Button(self, text="disable", command=disableInput(self))
        # self.button.grid(row=0, column=2)
        # self.button2.grid(row=0, column=4)


    def value(self):
        return self.inputVar.get()

    def setValue(self):
        self.inputVar.set()


class ToolTip(object):
    # from https://github.com/slightlynybbled/tk_tools
    """
    Add a tooltip to any widget.::
        entry = tk.Entry(root)
        entry.grid()
        # createst a tooltip
        tk_tools.ToolTip(entry, 'enter a value between 1 and 10')
    :param widget: the widget on which to hover
    :param text: the text to display
    :param time: the time to display the text, in milliseconds
    """

    def __init__(self, widget, text: str = 'widget info', time: int = 4000000):
        self._widget = widget
        self._text = text
        self._time = time

        self._widget.bind("<Enter>",
                          lambda _: self._widget.after(500, self._enter()))
        self._widget.bind("<Leave>", self._close)

        self._tw = None

    def _enter(self, event=None):
        x, y, cx, cy = self._widget.bbox("insert")
        x += self._widget.winfo_rootx() + 25
        y += self._widget.winfo_rooty() + 20

        # creates a toplevel window
        self._tw = tk.Toplevel(self._widget)

        # Leaves only the label and removes the app window
        self._tw.wm_overrideredirect(True)
        self._tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self._tw, text=self._text, justify='left',
                         background='#FFFFDD', relief='solid', borderwidth=1,
                         font="TkDefaultFont") #("arial", "11", "normal"))

        label.pack(ipadx=1)

        if self._time:
            self._tw.after(self._time, self._tw.destroy)

    def _close(self, event=None):
        if self._tw:
            self._tw.destroy()


# from https://github.com/slightlynybbled/tk_tools/blob/master/tk_tools/canvas.py
class Graph(ttk.Frame):
    """
    Tkinter native graph (pretty basic, but doesn't require heavy install).::
        graph = tk_tools.Graph(
            parent=root,
            x_min=-1.0,
            x_max=1.0,
            y_min=0.0,
            y_max=2.0,
            x_tick=0.2,
            y_tick=0.2,
            width=500,
            height=400
        )
        graph.grid(row=0, column=0)
        # create an initial line
        line_0 = [(x/10, x/10) for x in range(10)]
        graph.plot_line(line_0)
    :param parent: the parent frame
    :param x_min: the x minimum
    :param x_max: the x maximum
    :param y_min: the y minimum
    :param y_max: the y maximum
    :param x_tick: the 'tick' on the x-axis
    :param y_tick: the 'tick' on the y-axis
    :param options: additional valid tkinter.canvas options
    """
    def __init__(self, parent, x_min: float, x_max: float,
                 y_min: float, y_max: float,
                 x_tick: float, y_tick: float,
                 **options):
        self._parent = parent
        super().__init__(self._parent, **options)

        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0)

        self.w = float(self.canvas.config('width')[4])
        self.h = float(self.canvas.config('height')[4])
        self.x_min = x_min
        self.x_max = x_max
        self.x_tick = x_tick
        self.y_min = y_min
        self.y_max = y_max
        self.y_tick = y_tick
        self.px_x = (self.w - 100) / ((x_max - x_min) / x_tick)
        self.px_y = (self.h - 100) / ((y_max - y_min) / y_tick)

        self.draw_axes()

    def draw_axes(self):
        """
        Removes all existing series and re-draws the axes.
        :return: None
        """
        self.canvas.delete('all')
        rect = 50, 50, self.w - 50, self.h - 50

        self.canvas.create_rectangle(rect, outline="black")

        for x in self.frange(0, self.x_max - self.x_min + 1, self.x_tick):
            value = Decimal(self.x_min + x)
            if self.x_min <= value <= self.x_max:
                x_step = (self.px_x * x) / self.x_tick
                coord = 50 + x_step, self.h - 50, 50 + x_step, self.h - 45
                self.canvas.create_line(coord, fill="black")
                coord = 50 + x_step, self.h - 40

                label = round(Decimal(self.x_min + x), 1)
                self.canvas.create_text(coord, fill="black", text=label)

        for y in self.frange(0, self.y_max - self.y_min + 1, self.y_tick):
            value = Decimal(self.y_max - y)

            if self.y_min <= value <= self.y_max:
                y_step = (self.px_y * y) / self.y_tick
                coord = 45, 50 + y_step, 50, 50 + y_step
                self.canvas.create_line(coord, fill="black")
                coord = 35, 50 + y_step

                label = round(value, 1)
                self.canvas.create_text(coord, fill="black", text=label)

    def plot_point(self, x, y, visible=True, color='black', size=5):
        """
        Places a single point on the grid
        :param x: the x coordinate
        :param y: the y coordinate
        :param visible: True if the individual point should be visible
        :param color: the color of the point
        :param size: the point size in pixels
        :return: The absolute coordinates as a tuple
        """
        xp = (self.px_x * (x - self.x_min)) / self.x_tick
        yp = (self.px_y * (self.y_max - y)) / self.y_tick
        coord = 50 + xp, 50 + yp

        if visible:
            # divide down to an appropriate size
            size = int(size/2) if int(size/2) > 1 else 1
            x, y = coord

            self.canvas.create_oval(
                x-size, y-size,
                x+size, y+size,
                fill=color
            )

        return coord

    def plot_line(self, points: list, color='black', point_visibility=False):
        """
        Plot a line of points
        :param points: a list of tuples, each tuple containing an (x, y) point
        :param color: the color of the line
        :param point_visibility: True if the points \
        should be individually visible
        :return: None
        """
        last_point = ()
        for point in points:
            this_point = self.plot_point(point[0], point[1],
                                         color=color, visible=point_visibility)
            textPoint = (this_point[0], this_point[1] - 10)
            self.canvas.create_text(textPoint, fill="blue", text=f"{round(point[1])}")

            if last_point:
                self.canvas.create_line(last_point + this_point, fill=color)
            last_point = this_point
            # print last_point

    @staticmethod
    def frange(start, stop, step, digits_to_round=3):
        """
        Works like range for doubles
        :param start: starting value
        :param stop: ending value
        :param step: the increment_value
        :param digits_to_round: the digits to which to round \
        (makes floating-point numbers much easier to work with)
        :return: generator
        """
        while start < stop:
            yield round(start, digits_to_round)
            start += step




