
import sys
import os
cwd = os.getcwd()
pagesDir=cwd+"/userPages"
import importlib
sys.path.insert(1, pagesDir)
pageFiles= sorted([f for f in os.listdir(pagesDir) if os.path.isfile(os.path.join(pagesDir, f)) and "page" in f])
# print("found files in:",pagesDir)
# print(pageFiles)
# print("titles...")
print([x.title() for x in pageFiles])
modules=[]
modules += [importlib.import_module(p[:-3]) for p in pageFiles]
__all__ = [getattr(m,p.title()[:-3]) for m,p in zip(modules,pageFiles)]

print("userPages:\n",__all__)
