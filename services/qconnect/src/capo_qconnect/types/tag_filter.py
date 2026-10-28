"""Generated from Smithy shape ``com.amazonaws.qconnect#TagFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.and_conditions
    import capo_qconnect.types.or_conditions
    import capo_qconnect.types.tag_condition


class TagFilterTagConditionMember(TypedDict, closed=True):
    tagCondition: "capo_qconnect.types.tag_condition.TagCondition"


class TagFilterAndConditionsMember(TypedDict, closed=True):
    andConditions: "capo_qconnect.types.and_conditions.AndConditions"


class TagFilterOrConditionsMember(TypedDict, closed=True):
    orConditions: "capo_qconnect.types.or_conditions.OrConditions"


TagFilter: TypeAlias = (
    TagFilterTagConditionMember
    | TagFilterAndConditionsMember
    | TagFilterOrConditionsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: TagFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TagFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "tagCondition" in value:
        import capo_qconnect.types.tag_condition

        return {
            "tagCondition": capo_qconnect.types.tag_condition.serialize_json(
                value["tagCondition"]
            )
        }
    elif "andConditions" in value:
        import capo_qconnect.types.and_conditions

        return {
            "andConditions": capo_qconnect.types.and_conditions.serialize_json(
                value["andConditions"]
            )
        }
    elif "orConditions" in value:
        import capo_qconnect.types.or_conditions

        return {
            "orConditions": capo_qconnect.types.or_conditions.serialize_json(
                value["orConditions"]
            )
        }
    else:
        raise SerializationError("TagFilter: no variant present")


def deserialize_json(data: dict) -> TagFilter:
    if data.get("tagCondition") is not None:
        import capo_qconnect.types.tag_condition

        return {
            "tagCondition": capo_qconnect.types.tag_condition.deserialize_json(
                data["tagCondition"]
            )
        }
    elif data.get("andConditions") is not None:
        import capo_qconnect.types.and_conditions

        return {
            "andConditions": capo_qconnect.types.and_conditions.deserialize_json(
                data["andConditions"]
            )
        }
    elif data.get("orConditions") is not None:
        import capo_qconnect.types.or_conditions

        return {
            "orConditions": capo_qconnect.types.or_conditions.deserialize_json(
                data["orConditions"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TagFilter: no recognized variant key")
