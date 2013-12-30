from Registry import Registry

def getControlSet(reg_sys):
    try:
        select = reg_sys.open("Select")
        current = select.value("Current").value()
        controlsetnum = "ControlSet00%d" % (current)
        return controlsetnum

    except Registry.RegistryKeyNotFoundException as e:
        pass