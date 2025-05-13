import customtkinter
from CTkMenuBar import CTkMenuBar, CustomDropdownMenu
from fornecedor import FornecedorApp

root = customtkinter.CTk()
root.geometry("600x200")



menu = CTkMenuBar(root)
button_1 = menu.add_cascade("File")
button_2 = menu.add_cascade("Edit")
button_3 = menu.add_cascade("Settings")
button_4 = menu.add_cascade("About")
instancia = FornecedorApp(root)
minhafun = instancia.cadastro_forn  # Garanta que este método existe na classe
# Dropdown para "File"
dropdown1 = CustomDropdownMenu(button_1)
dropdown1.add_option(option="Open", command=minhafun)
dropdown1.add_option(option="Save")
dropdown1.add_separator()

sub_menu = dropdown1.add_submenu("Export As")
sub_menu.add_option(option=".TXT")
sub_menu.add_option(option=".PDF")

# Dropdown para "Edit"
dropdown2 = CustomDropdownMenu(button_2)
dropdown2.add_option(option="Cut")
dropdown2.add_option(option="Copy")
dropdown2.add_option(option="Paste")

# Dropdown para "Settings"
dropdown3 = CustomDropdownMenu(button_3)
dropdown3.add_option(option="Preferences")
dropdown3.add_option(option="Update")

# Dropdown para "About"
dropdown4 = CustomDropdownMenu(button_4)
dropdown4.add_option(option="Hello World")

root.mainloop()
