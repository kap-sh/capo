"""Generated from Smithy shape ``com.amazonaws.bedrock#RatingScaleItemValue``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember


class _RatingScaleItemValue_stringValue(TypedDict, closed=True):
    stringValue: "str"


class _RatingScaleItemValue_floatValue(TypedDict, closed=True):
    floatValue: "float"


RatingScaleItemValue: TypeAlias = (
    _RatingScaleItemValue_stringValue
    | _RatingScaleItemValue_floatValue
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RatingScaleItemValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RatingScaleItemValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "stringValue" in value:
        return {"stringValue": value["stringValue"]}
    elif "floatValue" in value:
        return {
            "floatValue": (
                "NaN"
                if value["floatValue"] != value["floatValue"]
                else "Infinity"
                if value["floatValue"] == float("inf")
                else "-Infinity"
                if value["floatValue"] == float("-inf")
                else value["floatValue"]
            )
        }
    else:
        raise SerializationError("RatingScaleItemValue: no variant present")


def deserialize_json(data: dict) -> RatingScaleItemValue:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("floatValue") is not None:
        return {"floatValue": float(data["floatValue"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RatingScaleItemValue: no recognized variant key")
