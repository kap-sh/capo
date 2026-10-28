"""Generated from Smithy shape ``com.amazonaws.supportauthz#ActionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError, SerializationError
from capo_supportauthz.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_supportauthz.types.actions


class ActionSetAllActionsMember(TypedDict, closed=True):
    allActions: "None"


class ActionSetActionsMember(TypedDict, closed=True):
    actions: "capo_supportauthz.types.actions.Actions"


ActionSet: TypeAlias = (
    ActionSetAllActionsMember | ActionSetActionsMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ActionSet) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ActionSet: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "allActions" in value:
        return {"allActions": {}}
    elif "actions" in value:
        import capo_supportauthz.types.actions

        return {
            "actions": capo_supportauthz.types.actions.serialize_json(value["actions"])
        }
    else:
        raise SerializationError("ActionSet: no variant present")


def deserialize_json(data: dict) -> ActionSet:
    if data.get("allActions") is not None:
        return {"allActions": None}
    elif data.get("actions") is not None:
        import capo_supportauthz.types.actions

        return {
            "actions": capo_supportauthz.types.actions.deserialize_json(data["actions"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ActionSet: no recognized variant key")
