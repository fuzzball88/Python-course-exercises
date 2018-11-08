class Switch:
    """Switcher-class, returns a Boolean."""
    __mode = False

    def get_mode(self):
        return self.__mode

    def switch_mode(self):
        if self.__mode == False:
            self.__mode = True
        else:
            self.__mode = False

Lamp = Switch()

print(Lamp.get_mode())
Lamp.switch_mode()
print(Lamp.get_mode())
