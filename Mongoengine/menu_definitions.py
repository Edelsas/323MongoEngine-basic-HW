from Menu import Menu

# Main menu
menu_main = Menu(
    "Main Menu",
    "Please select an option: ",
    [
        ("Add PiecePart", "Add PiecePart"),
        ("Add Vendor", "Add Vendor"),
        ("Add Address", "Add Address"),
        ("List PieceParts", "List PieceParts"),
        ("List Vendors", "List Vendors"),
        ("Update Vendor", "Update Vendor"),
        ("Delete PiecePart", "Delete PiecePart"),
        ("Delete Vendor", "Delete Vendor"),
        ("Quit", "Quit")
    ]
)

# Selection menu for adding entries
add_select = Menu(
    "Add Menu",
    "What would you like to add? ",
    [
        ("Add PiecePart", "Add PiecePart"),
        ("Add Vendor", "Add Vendor"),
        ("Back to Main Menu", "Back")
    ]
)

# Selection menu for deleting entries
delete_select = Menu(
    "Delete Menu",
    "What would you like to delete? ",
    [
        ("Delete PiecePart", "Delete PiecePart"),
        ("Delete Vendor", "Delete Vendor"),
        ("Back to Main Menu", "Back")
    ]
)

# Selection menu for listing entries
list_select = Menu(
    "List Menu",
    "What would you like to list? ",
    [
        ("List PieceParts", "List PieceParts"),
        ("List Vendors", "List Vendors"),
        ("Back to Main Menu", "Back")
    ]
)

# Selection menu for updating entries
update_select = Menu(
    "Update Menu",
    "What would you like to update? ",
    [
        ("Update Vendor", "Update Vendor"),
        ("Back to Main Menu", "Back")
    ]
)

# Select menu (for choosing between options like PiecePart or Vendor)
select_select = Menu(
    "Select Menu",
    "Please select an option: ",
    [
        ("Select PiecePart", "Select PiecePart"),
        ("Select Vendor", "Select Vendor"),
        ("Back to Main Menu", "Back")
    ]
)

# Yes/No confirmation menu
yes_no = Menu(
    "Confirm",
    "Are you sure? ",
    [
        ("Yes", "Yes"),
        ("No", "No")
    ]
)
