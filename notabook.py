#!/usr/bin/env python


import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class OpenDocument():

    def __init__(self):
        self.path = ''
        self.toSaver = False
        self.textViewer = None

class App:

    def __init__(self):
        self.documents = []
        self.documentActif = None
        
        interface = gtk.Builder()
        interface.add_from_file('notabook.glade')
        window = Gtk.Window()
        window.set_title("My app")
        window.set_default_size(300,300)
        window.set_position(Gtk.WindowPosition.CENTER)
        window.connect("destroy", self.destroy)
        
        button = Gtk.Button("Hi !")
        button.connect_after("clicked", self.button_clicked)
        window.add(button)
        
        window.show_all()

    def destroy(self, window):
        Gtk.main_quit()

    def button_clicked(self, button):
        print("touched !")

def main():
    app = App()
    Gtk.main()

if __name__ == '__main__':
    main()
