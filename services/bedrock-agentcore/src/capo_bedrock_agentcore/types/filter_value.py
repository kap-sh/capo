"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FilterValue``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.filter_string_value


class FilterValueStringValueMember(TypedDict, closed=True):
    stringValue: "capo_bedrock_agentcore.types.filter_string_value.FilterStringValue"


class FilterValueDoubleValueMember(TypedDict, closed=True):
    doubleValue: "float"


class FilterValueBooleanValueMember(TypedDict, closed=True):
    booleanValue: "bool"


FilterValue: TypeAlias = (
    FilterValueStringValueMember
    | FilterValueDoubleValueMember
    | FilterValueBooleanValueMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FilterValue) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FilterValue: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("FilterValue: no recognized variant key")
