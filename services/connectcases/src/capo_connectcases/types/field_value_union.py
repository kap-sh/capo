"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldValueUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.empty_field_value


class _FieldValueUnion_stringValue(TypedDict, closed=True):
    stringValue: "str"


class _FieldValueUnion_doubleValue(TypedDict, closed=True):
    doubleValue: "float"


class _FieldValueUnion_booleanValue(TypedDict, closed=True):
    booleanValue: "bool"


class _FieldValueUnion_emptyValue(TypedDict, closed=True):
    emptyValue: "capo_connectcases.types.empty_field_value.EmptyFieldValue"


class _FieldValueUnion_userArnValue(TypedDict, closed=True):
    userArnValue: "str"


FieldValueUnion: TypeAlias = (
    _FieldValueUnion_stringValue
    | _FieldValueUnion_doubleValue
    | _FieldValueUnion_booleanValue
    | _FieldValueUnion_emptyValue
    | _FieldValueUnion_userArnValue
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FieldValueUnion) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"FieldValueUnion: cannot serialize unknown variant {value.name!r}"
        )
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "doubleValue" in value:
        return {
            "doubleValue": (
                "NaN"
                if value["doubleValue"] != value["doubleValue"]
                else "Infinity"
                if value["doubleValue"] == float("inf")
                else "-Infinity"
                if value["doubleValue"] == float("-inf")
                else value["doubleValue"]
            )
        }
    elif "booleanValue" in value:
        return {"booleanValue": value["booleanValue"]}
    elif "emptyValue" in value:
        import capo_connectcases.types.empty_field_value

        return {
            "emptyValue": capo_connectcases.types.empty_field_value.serialize_json(
                value["emptyValue"]
            )
        }
    elif "userArnValue" in value:
        return {"userArnValue": value["userArnValue"]}
    else:
        raise SerializationError("FieldValueUnion: no variant present")


def deserialize_json(data: dict) -> FieldValueUnion:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("doubleValue") is not None:
        return {"doubleValue": float(data["doubleValue"])}
    elif data.get("booleanValue") is not None:
        return {"booleanValue": data["booleanValue"]}
    elif data.get("emptyValue") is not None:
        import capo_connectcases.types.empty_field_value

        return {
            "emptyValue": capo_connectcases.types.empty_field_value.deserialize_json(
                data["emptyValue"]
            )
        }
    elif data.get("userArnValue") is not None:
        return {"userArnValue": data["userArnValue"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("FieldValueUnion: no recognized variant key")
