"""Generated from Smithy shape ``com.amazonaws.connectcases#TagFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.tag_value


class TagFilterEqualToMember(TypedDict, closed=True):
    equalTo: "capo_connectcases.types.tag_value.TagValue"


TagFilter: TypeAlias = TagFilterEqualToMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: TagFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TagFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "equalTo" in value:
        import capo_connectcases.types.tag_value

        return {
            "equalTo": capo_connectcases.types.tag_value.serialize_json(
                value["equalTo"]
            )
        }
    else:
        raise SerializationError("TagFilter: no variant present")


def deserialize_json(data: dict) -> TagFilter:
    if data.get("equalTo") is not None:
        import capo_connectcases.types.tag_value

        return {
            "equalTo": capo_connectcases.types.tag_value.deserialize_json(
                data["equalTo"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TagFilter: no recognized variant key")
