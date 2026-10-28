"""Generated from Smithy shape ``com.amazonaws.securityhub#ParameterValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.double
    import capo_securityhub.types.integer
    import capo_securityhub.types.integer_list
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.string_list


class ParameterValueIntegerMember(TypedDict, closed=True):
    Integer: "capo_securityhub.types.integer.Integer"


class ParameterValueIntegerListMember(TypedDict, closed=True):
    IntegerList: "capo_securityhub.types.integer_list.IntegerList"


class ParameterValueDoubleMember(TypedDict, closed=True):
    Double: "capo_securityhub.types.double.Double"


class ParameterValueStringMember(TypedDict, closed=True):
    String: "capo_securityhub.types.non_empty_string.NonEmptyString"


class ParameterValueStringListMember(TypedDict, closed=True):
    StringList: "capo_securityhub.types.string_list.StringList"


class ParameterValueBooleanMember(TypedDict, closed=True):
    Boolean: "capo_securityhub.types.boolean.Boolean"


class ParameterValueEnumMember(TypedDict, closed=True):
    Enum: "capo_securityhub.types.non_empty_string.NonEmptyString"


class ParameterValueEnumListMember(TypedDict, closed=True):
    EnumList: "capo_securityhub.types.string_list.StringList"


ParameterValue: TypeAlias = (
    ParameterValueIntegerMember
    | ParameterValueIntegerListMember
    | ParameterValueDoubleMember
    | ParameterValueStringMember
    | ParameterValueStringListMember
    | ParameterValueBooleanMember
    | ParameterValueEnumMember
    | ParameterValueEnumListMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ParameterValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ParameterValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Integer" in value:
        return {"Integer": value["Integer"]}
    elif "IntegerList" in value:
        import capo_securityhub.types.integer_list

        return {
            "IntegerList": capo_securityhub.types.integer_list.serialize_json(
                value["IntegerList"]
            )
        }
    elif "Double" in value:
        return {
            "Double": (
                "NaN"
                if value["Double"] != value["Double"]
                else "Infinity"
                if value["Double"] == float("inf")
                else "-Infinity"
                if value["Double"] == float("-inf")
                else value["Double"]
            )
        }
    elif "String" in value:
        return {"String": value["String"]}
    elif "StringList" in value:
        import capo_securityhub.types.string_list

        return {
            "StringList": capo_securityhub.types.string_list.serialize_json(
                value["StringList"]
            )
        }
    elif "Boolean" in value:
        return {"Boolean": value["Boolean"]}
    elif "Enum" in value:
        return {"Enum": value["Enum"]}
    elif "EnumList" in value:
        import capo_securityhub.types.string_list

        return {
            "EnumList": capo_securityhub.types.string_list.serialize_json(
                value["EnumList"]
            )
        }
    else:
        raise SerializationError("ParameterValue: no variant present")


def deserialize_json(data: dict) -> ParameterValue:
    if data.get("Integer") is not None:
        return {"Integer": data["Integer"]}
    elif data.get("IntegerList") is not None:
        import capo_securityhub.types.integer_list

        return {
            "IntegerList": capo_securityhub.types.integer_list.deserialize_json(
                data["IntegerList"]
            )
        }
    elif data.get("Double") is not None:
        return {"Double": float(data["Double"])}
    elif data.get("String") is not None:
        return {"String": data["String"]}
    elif data.get("StringList") is not None:
        import capo_securityhub.types.string_list

        return {
            "StringList": capo_securityhub.types.string_list.deserialize_json(
                data["StringList"]
            )
        }
    elif data.get("Boolean") is not None:
        return {"Boolean": data["Boolean"]}
    elif data.get("Enum") is not None:
        return {"Enum": data["Enum"]}
    elif data.get("EnumList") is not None:
        import capo_securityhub.types.string_list

        return {
            "EnumList": capo_securityhub.types.string_list.deserialize_json(
                data["EnumList"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ParameterValue: no recognized variant key")
