import mongoengine as me
import logging
from menu_definitions import (
    menu_main, add_select, delete_select, list_select,
    select_select, update_select, yes_no
)
from Vendor import Vendor
from PiecePart import PiecePart
from Address import Address

me.connect(host="mongodb+srv://edelsas:Nightwing2204@cecs-323-fall-2024.am0tq.mongodb.net/?retryWrites=true&w=majority&appName=CECS-323-Fall-2024")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    while True:
        choice = menu_main.menu_prompt()
        if choice == "Add PiecePart":
            add_piece_part()
        elif choice == "Add Vendor":
            add_vendor()
        elif choice == "Add Address":
            add_address()
        elif choice == "List PieceParts":
            list_piece_parts()
        elif choice == "List Vendors":
            list_vendors()
        elif choice == "Update Vendor":
            update_vendor()
        elif choice == "Delete PiecePart":
            delete_piece_part()
        elif choice == "Delete Vendor":
            delete_vendor()
        elif choice == "Quit":
            break


def add_piece_part():
    part_name = input("Enter part name: ")
    part_desc = input("Enter part description: ")
    vendor_number = input("Enter vendor number: ")

    vendor = Vendor.objects(vendor_number=vendor_number).first()
    if not vendor:
        print(f"Error: Vendor with number {vendor_number} does not exist.")
        return

    piece_part = PiecePart(part_name=part_name, part_description=part_desc, vendor_number=vendor)

    piece_part.save()
    print("Piece part added successfully!")


def add_address():
    zip_code = input("Enter zip code: ")
    city = input("Enter city: ")
    state = input("Enter state: ")

    address = Address(zip_code=zip_code, city=city, state=state)

    address.save()
    print(f"Address added successfully with ID: {address.id}")


def add_vendor():
    vendor_name = input("Enter vendor name: ")
    address_id = input("Enter address ID: ")

    address = Address.objects(id=address_id).first()
    if not address:
        print(f"Error: Address with ID {address_id} does not exist.")
        return

    vendor_number = Vendor.objects.count() + 1

    vendor = Vendor(vendor_name=vendor_name, address_id=address, vendor_number=vendor_number)
    vendor.save()
    print(f"Vendor added successfully with vendor number: {vendor.vendor_number}")


def list_piece_parts():
    piece_parts = PiecePart.objects()
    for part in piece_parts:
        print(f"Part ID: {part.id}, Name: {part.part_name}, Description: {part.part_description}, Vendor: {part.vendor_number}")


def list_vendors():
    vendors = Vendor.objects()
    for vendor in vendors:
        print(vendor)


def update_vendor():
    vendor_number = input("Enter vendor number: ")
    new_vendor_name = input("Enter new vendor name: ")

    vendor = Vendor.objects(vendor_number=vendor_number).first()
    if vendor:
        vendor.vendor_name = new_vendor_name
        vendor.save()
        print("Vendor updated successfully!")
    else:
        print("Vendor not found.")


def delete_piece_part():
    part_id = input("Enter part ID: ")

    piece_part = PiecePart.objects(id=part_id).first()
    if piece_part:
        piece_part.delete()
        print("Piece part deleted successfully!")
    else:
        print("Piece part not found.")


def delete_vendor():
    vendor_number = input("Enter vendor number: ")

    vendor = Vendor.objects(vendor_number=vendor_number).first()
    if vendor:
        vendor.delete()
        print("Vendor deleted successfully!")
    else:
        print("Vendor not found.")


if __name__ == "__main__":
    main()
