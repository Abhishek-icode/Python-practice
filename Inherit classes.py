# --------------------------INHERIT CLASSES----------------------
class electronic_device:
    monitor = 6
    cpu = 4
    keybord = 7

class pocket_gadget(electronic_device):
    smartphon = 5
    tablate = 6

class phone(pocket_gadget):
    smasung = 5
    iphon = 7

ec = electronic_device()
pg = pocket_gadget()
ph = phone()

print(ph.iphon, "- iphon")
print(ph.tablate, "- tablate")
print(ph.cpu, "- cpu")