def toggleOrientation(kwargs):
    node = kwargs['node']
    parm_name = kwargs['parm'].name()

    horizontal = node.parm("horizontalToggle")
    vertical = node.parm("verticalToggle")

    if parm_name == "horizontalToggle":
        vertical.set(0 if horizontal.eval() else 1)
    elif parm_name == "verticalToggle":
        horizontal.set(0 if vertical.eval() else 1)
