"""Generated from Smithy shape ``com.amazonaws.xray#AnnotationValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_xray.errors import DeserializationError, SerializationError
from capo_xray.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_xray.types.nullable_boolean
    import capo_xray.types.nullable_double
    import capo_xray.types.string


class AnnotationValueNumberValueMember(TypedDict, closed=True):
    NumberValue: "capo_xray.types.nullable_double.NullableDouble"


class AnnotationValueBooleanValueMember(TypedDict, closed=True):
    BooleanValue: "capo_xray.types.nullable_boolean.NullableBoolean"


class AnnotationValueStringValueMember(TypedDict, closed=True):
    StringValue: "capo_xray.types.string.String"


AnnotationValue: TypeAlias = (
    AnnotationValueNumberValueMember
    | AnnotationValueBooleanValueMember
    | AnnotationValueStringValueMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AnnotationValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
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
    elif "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    else:
        raise SerializationError("AnnotationValue: no variant present")


def deserialize_json(data: dict) -> AnnotationValue:
    if data.get("NumberValue") is not None:
        return {"NumberValue": float(data["NumberValue"])}
    elif data.get("BooleanValue") is not None:
        return {"BooleanValue": data["BooleanValue"]}
    elif data.get("StringValue") is not None:
        return {"StringValue": data["StringValue"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AnnotationValue: no recognized variant key")
