"""Generated from Smithy shape ``com.amazonaws.appconfig#AttributeValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_appconfig.errors import DeserializationError, SerializationError
from capo_appconfig.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_appconfig.types.attribute_string
    import capo_appconfig.types.boolean
    import capo_appconfig.types.double
    import capo_appconfig.types.number_list
    import capo_appconfig.types.string_list


class AttributeValueStringValueMember(TypedDict, closed=True):
    StringValue: "capo_appconfig.types.attribute_string.AttributeString"


class AttributeValueNumberValueMember(TypedDict, closed=True):
    NumberValue: "capo_appconfig.types.double.Double"


class AttributeValueBooleanValueMember(TypedDict, closed=True):
    BooleanValue: "capo_appconfig.types.boolean.Boolean"


class AttributeValueStringArrayMember(TypedDict, closed=True):
    StringArray: "capo_appconfig.types.string_list.StringList"


class AttributeValueNumberArrayMember(TypedDict, closed=True):
    NumberArray: "capo_appconfig.types.number_list.NumberList"


AttributeValue: TypeAlias = (
    AttributeValueStringValueMember
    | AttributeValueNumberValueMember
    | AttributeValueBooleanValueMember
    | AttributeValueStringArrayMember
    | AttributeValueNumberArrayMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AttributeValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AttributeValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    elif "NumberValue" in value:
        return {
            "NumberValue": (
                "NaN"
                if value["NumberValue"] != value["NumberValue"]
                else "Infinity"
                if value["NumberValue"] == float("inf")
                else "-Infinity"
                if value["NumberValue"] == float("-inf")
                else value["NumberValue"]
            )
        }
    elif "BooleanValue" in value:
        return {"BooleanValue": value["BooleanValue"]}
    elif "StringArray" in value:
        import capo_appconfig.types.string_list

        return {
            "StringArray": capo_appconfig.types.string_list.serialize_json(
                value["StringArray"]
            )
        }
    elif "NumberArray" in value:
        import capo_appconfig.types.number_list

        return {
            "NumberArray": capo_appconfig.types.number_list.serialize_json(
                value["NumberArray"]
            )
        }
    else:
        raise SerializationError("AttributeValue: no variant present")


def deserialize_json(data: dict) -> AttributeValue:
    if data.get("StringValue") is not None:
        return {"StringValue": data["StringValue"]}
    elif data.get("NumberValue") is not None:
        return {"NumberValue": float(data["NumberValue"])}
    elif data.get("BooleanValue") is not None:
        return {"BooleanValue": data["BooleanValue"]}
    elif data.get("StringArray") is not None:
        import capo_appconfig.types.string_list

        return {
            "StringArray": capo_appconfig.types.string_list.deserialize_json(
                data["StringArray"]
            )
        }
    elif data.get("NumberArray") is not None:
        import capo_appconfig.types.number_list

        return {
            "NumberArray": capo_appconfig.types.number_list.deserialize_json(
                data["NumberArray"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AttributeValue: no recognized variant key")
