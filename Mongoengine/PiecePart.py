import mongoengine as me

class PiecePart(me.Document):
    part_name = me.StringField(required=True, max_length=16)
    part_description = me.StringField(required=True, max_length=80)
    vendor_number = me.ReferenceField('Vendor', required=True)

    def __str__(self):
        return f"Piece name: {self.part_name}, Part description: {self.part_description}, Vendor: {self.vendor_number}"
