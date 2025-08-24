# Simple Advance Multi Compiler 
# Package Manager Build System
# What Need?
# Make an Package Manager
# Complete Ckg And Add Support System For Librarys
# Add Support To Mingw and GNU Compilers

import json

compiler = "gnu_compiler"
exec(f"import {compiler} as compiler")
#import gnu_compiler as compiler

with open("test.json","r") as fp:
    cfg = json.load(fp)

def prepareConfig(config: dict):
    for target in config:
        if target.get("lang") == None:
            target["lang"] = "cpp"
        if target.get("includes") == None:
            target["includes"] = []
        if target.get("libs") == None:
            target["libs"] = []
        for source in target["source"]:
            if source.startswith("json:"):
                with open(source.split(":")[1],"r") as fp:
                    target["source"] = [*target["source"],*json.load(fp)]
                target["source"].remove(source)
        for source in target["includes"]:
            if source.startswith("json:"):
                with open(source.split(":")[1],"r") as fp:
                    target["includes"] = [*target["includes"],*json.load(fp)]
                target["includes"].remove(source)
        for source in target["libs"]:
            if source.startswith("json:"):
                with open(source.split(":")[1],"r") as fp:
                    target["libs"] = [*target["libs"],*json.load(fp)]
                target["libs"].remove(source)
    return config

def runConfig(config: dict):
    print("Building...")
    for target in config:
        if target["type"] == "object":
            compiler.compile_object(
                target["source"][0],
                target["output"],
                {
                    "include":target["includes"],
                    "lib":target["libs"],
                    "lang":target["lang"]
                }
            )
        elif target["type"] == "exe":
            compiler.compile_execute(
                target["source"],
                target["output"],
                {
                    "include":target["includes"],
                    "lib":target["libs"],
                    "lang":target["lang"]
                }
            )


runConfig(
    prepareConfig(
        cfg
    )
)