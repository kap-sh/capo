"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#PathElement``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError
from capo_accessanalyzer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_accessanalyzer.types.substring


class PathElementIndexMember(TypedDict, closed=True):
    index: "int"


class PathElementKeyMember(TypedDict, closed=True):
    key: "str"


class PathElementSubstringMember(TypedDict, closed=True):
    substring: "capo_accessanalyzer.types.substring.Substring"


class PathElementValueMember(TypedDict, closed=True):
    value: "str"


PathElement: TypeAlias = (
    PathElementIndexMember
    | PathElementKeyMember
    | PathElementSubstringMember
    | PathElementValueMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PathElement) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PathElement: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "index" in value:
        return {"index": value["index"]}
    elif "key" in value:
        return {"key": value["key"]}
    elif "substring" in value:
        import capo_accessanalyzer.types.substring

        return {
            "substring": capo_accessanalyzer.types.substring.serialize_json(
                value["substring"]
            )
        }
    elif "value" in value:
        return {"value": value["value"]}
    else:
        raise SerializationError("PathElement: no variant present")


def deserialize_json(data: dict) -> PathElement:
    if data.get("index") is not None:
        return {"index": data["index"]}
    elif data.get("key") is not None:
        return {"key": data["key"]}
    elif data.get("substring") is not None:
        import capo_accessanalyzer.types.substring

        return {
            "substring": capo_accessanalyzer.types.substring.deserialize_json(
                data["substring"]
            )
        }
    elif data.get("value") is not None:
        return {"value": data["value"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PathElement: no recognized variant key")
