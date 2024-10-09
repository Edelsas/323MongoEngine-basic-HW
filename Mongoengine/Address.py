import mongoengine as me

class Address(me.Document):
    zip_code = me.StringField(required=True, max_length=60)
    city = me.StringField(required=True)
    state = me.StringField(required=True)

    def __str__(self):
        return f"Address: {self.city}, {self.state}, ZIP: {self.zip_code}"
