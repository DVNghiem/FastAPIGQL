from marshmallow import Schema, RAISE, fields, validate

class RegisterSchema(Schema):
    class Meta:
        unknow = RAISE
    username = fields.String(required=True, validate=validate.Length(min=5))
    password = fields.String(required=True, validate=validate.Length(min=2))

    avatar = fields.String(required=False)
    fullName = fields.String(required=False)

class LoginSchema(Schema):
    class Meta:
        unknow = RAISE
    username = fields.String(required=True)
    password = fields.String(required=True)
