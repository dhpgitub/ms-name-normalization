from marshmallow import Schema, fields, ValidationError, validates


class MemberName():
    def __init__(self, name=None, status=None, correlationID=None):
        self.name = name
        self.status = status
        self.correlationID = correlationID


class MemberName_schema(Schema):
    name = fields.String(required=True
                         # ,error_messages={'name':'Name is required field cannot be null'}
                         )
    status = fields.String()
    correlation = fields.String()

    # @validates('name')
    # def validate_name(self, name):
    #     if name is None:
    #         raise ValidationError('Name is required field cannot be null')
