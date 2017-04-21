import gi
from gi.repository import Gtk
gi.require_version('Gtk', '3.0')


class Handler:
    def onDeleteWindow(self, *args):
        print "onDeleteWindow"
        Gtk.main_quit(*args)

    def change_value(self, *args):
        self.value = max(min(args[2], 100), 10)
        print self.value

    def value_change(self, *args):
        pass


builder = Gtk.Builder()
builder.add_from_file("ui.glade")
builder.connect_signals(Handler())
window = builder.get_object("window1")

window.show_all()
Gtk.main()
