"""Generated from Smithy shape ``com.amazonaws.supportauthz#ActionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.actions


class _ActionSet_allActions(TypedDict, closed=True):
    allActions: "None"


class _ActionSet_actions(TypedDict, closed=True):
    actions: "capo_supportauthz.types.actions.Actions"


ActionSet: TypeAlias = _ActionSet_allActions | _ActionSet_actions


# --- restJson1 ser/de ---
def serialize_json(value: ActionSet) -> dict:
    if "allActions" in value:
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
        raise DeserializationError("ActionSet: no recognized variant key")
