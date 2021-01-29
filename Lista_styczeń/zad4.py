def memory (gb):
    bt = gb * 1000000000
    return ( bt / 1024 / 1024 / 1024)

gb = float(input("Podaj rozmiar w GB:"))
print("Realna pojemność:","{:.3f}".format(memory(gb)),"GB")
