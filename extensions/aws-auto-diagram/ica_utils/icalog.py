import inkex

LOGFILE = True

def debug(var):
    if LOGFILE:
        with open("/tmp/aws-auto-diagram.log", "a") as text_file:
            text_file.write(str(var))
            text_file.write("\n")
    else:
        inkex.errormsg((var))

