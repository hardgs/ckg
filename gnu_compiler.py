import os

def compile_object(source,dest,options):
    cmd = ""
    if options["lang"] == "c":
        cmd += "gcc -c "
    else:
        cmd += "g++ -c "
    cmd = cmd + source + " -o " + dest
    # Add Includes
    for inc in options["include"]:
        cmd = cmd + " -I" + inc
    for lib in options["lib"]:
        cmd = cmd + lib
    print("RUN: ",cmd)
    os.system(cmd)

def compile_execute(sources,dest,options):
    cmd = ""
    if options["lang"] == "c":
        cmd += "gcc "
    else:
        cmd += "g++ "
    for source in sources:
        cmd = cmd + source
    cmd += " -o " + dest
    # Add Includes
    for inc in options["include"]:
        cmd = cmd + " -I" + inc
    for lib in options["lib"]:
        cmd = cmd + lib
    print("RUN: ",cmd)
    os.system(cmd)