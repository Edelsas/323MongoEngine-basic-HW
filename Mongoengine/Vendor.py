import mongoengine as me

class Vendor(me.Document):
    vendor_number = me.IntField(required=True, unique=True)
    vendor_name = me.StringField(required=True, max_length=80)
    address_id = me.ReferenceField('Address', required=True)
    piece_parts = me.ListField(me.ReferenceField('PiecePart'))

    def __str__(self):
        return f"Vendor name: {self.vendor_name}, Address: {self.address_id}"
