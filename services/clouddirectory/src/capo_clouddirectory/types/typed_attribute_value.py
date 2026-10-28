"""Generated from Smithy shape ``com.amazonaws.clouddirectory#TypedAttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError, SerializationError
from capo_clouddirectory.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_clouddirectory.types.binary_attribute_value
    import capo_clouddirectory.types.boolean_attribute_value
    import capo_clouddirectory.types.datetime_attribute_value
    import capo_clouddirectory.types.number_attribute_value
    import capo_clouddirectory.types.string_attribute_value


class TypedAttributeValueStringValueMember(TypedDict, closed=True):
    StringValue: "capo_clouddirectory.types.string_attribute_value.StringAttributeValue"


class TypedAttributeValueBinaryValueMember(TypedDict, closed=True):
    BinaryValue: "capo_clouddirectory.types.binary_attribute_value.BinaryAttributeValue"


class TypedAttributeValueBooleanValueMember(TypedDict, closed=True):
    BooleanValue: (
        "capo_clouddirectory.types.boolean_attribute_value.BooleanAttributeValue"
    )


class TypedAttributeValueNumberValueMember(TypedDict, closed=True):
    NumberValue: "capo_clouddirectory.types.number_attribute_value.NumberAttributeValue"


class TypedAttributeValueDatetimeValueMember(TypedDict, closed=True):
    DatetimeValue: (
        "capo_clouddirectory.types.datetime_attribute_value.DatetimeAttributeValue"
    )


TypedAttributeValue: TypeAlias = (
    TypedAttributeValueStringValueMember
    | TypedAttributeValueBinaryValueMember
    | TypedAttributeValueBooleanValueMember
    | TypedAttributeValueNumberValueMember
    | TypedAttributeValueDatetimeValueMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TypedAttributeValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TypedAttributeValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    elif "BinaryValue" in value:
        import capo_clouddirectory.types.binary_attribute_value

        return {
            "BinaryValue": capo_clouddirectory.types.binary_attribute_value.serialize_json(
                value["BinaryValue"]
            )
        }
    elif "BooleanValue" in value:
        return {"BooleanValue": value["BooleanValue"]}
    elif "NumberValue" in value:
        return {"NumberValue": value["NumberValue"]}
    elif "DatetimeValue" in value:
        import capo_clouddirectory.types.datetime_attribute_value

        return {
            "DatetimeValue": capo_clouddirectory.types.datetime_attribute_value.serialize_json(
                value["DatetimeValue"]
            )
        }
    else:
        raise SerializationError("TypedAttributeValue: no variant present")


def deserialize_json(data: dict) -> TypedAttributeValue:
    if data.get("StringValue") is not None:
        return {"StringValue": data["StringValue"]}
    elif data.get("BinaryValue") is not None:
        import capo_clouddirectory.types.binary_attribute_value

        return {
            "BinaryValue": capo_clouddirectory.types.binary_attribute_value.deserialize_json(
                data["BinaryValue"]
            )
        }
    elif data.get("BooleanValue") is not None:
        return {"BooleanValue": data["BooleanValue"]}
    elif data.get("NumberValue") is not None:
        return {"NumberValue": data["NumberValue"]}
    elif data.get("DatetimeValue") is not None:
        import capo_clouddirectory.types.datetime_attribute_value

        return {
            "DatetimeValue": capo_clouddirectory.types.datetime_attribute_value.deserialize_json(
                data["DatetimeValue"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TypedAttributeValue: no recognized variant key")
