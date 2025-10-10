def switchPointNode(kwargs, myHda):
    numBooks = myHda.parm("numBooks")
    parm = myHda.parm("st")
    
    if numBooks.eval() > 1:
        parm.set(0)
    else:
        parm.set(1)