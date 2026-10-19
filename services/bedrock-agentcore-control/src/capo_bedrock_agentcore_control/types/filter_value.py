"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FilterValue``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember


class _FilterValue_stringValue(TypedDict, closed=True):
    stringValue: "str"


class _FilterValue_doubleValue(TypedDict, closed=True):
    doubleValue: "float"


class _FilterValue_booleanValue(TypedDict, closed=True):
    booleanValue: "bool"


FilterValue: TypeAlias = (
    _FilterValue_stringValue
    | _FilterValue_doubleValue
    | _FilterValue_booleanValue
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FilterValue) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"FilterValue: cannot serialize unknown variant {value.name!r}"
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
    else:
        raise SerializationError("FilterValue: no variant present")


def deserialize_json(data: dict) -> FilterValue:
    if data.get("stringValue") is not None:
        return {"stringValue": data["stringValue"]}
    elif data.get("doubleValue") is not None:
        return {"doubleValue": float(data["doubleValue"])}
    elif data.get("booleanValue") is not None:
        return {"booleanValue": data["booleanValue"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("FilterValue: no recognized variant key")
