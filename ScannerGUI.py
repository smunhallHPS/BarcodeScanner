"""
Builds GUI for scanning barcode
"""

from breezypythongui import EasyFrame

class ScannerGUI(EasyFrame):
    """GUI for the client app."""

    COLOR = "#FFFFFF"

    def __init__(self):
        """Initialize the frame and widgets."""
        EasyFrame.__init__(self, title="Phone Book", background=ScannerGUI.COLOR)
        # Add the labels, fields, and button
        self.label = self.addLabel(text="Please scan your ID",
                                         row=0, column=0,
                                         columnspan=2,
                                         background=ScannerGUI.COLOR)
        self.txtFld = self.addTextField(text="", row=1,
                                        column=0, rowspan=1,
                                        columnspan=2, width=20)
        self.addBtn = self.addButton(row=1, column=2,
                                     text="Add",
                                     command=self.add,
                                     state="normal")

    def add(self):
        """Adds a name and number to the phone book."""

        # self.txtFld["text"] = text entered


def main():
    """Instantiate and pop up the window."""
    ScannerGUI().mainloop()


if __name__ == "__main__":
    main()
