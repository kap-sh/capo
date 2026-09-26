"""Generated from Smithy shape ``com.amazonaws.supportauthz#Permit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.action_set
    import capo_supportauthz.types.conditions
    import capo_supportauthz.types.resource_set


class Permit(TypedDict, closed=True):
    actions: "capo_supportauthz.types.action_set.ActionSet"
    """<p>The set of actions that the support operator is authorized to perform.</p>"""
    resources: "capo_supportauthz.types.resource_set.ResourceSet"
    """<p>The set of resources that the support operator is authorized to act upon.</p>"""
    conditions: NotRequired["capo_supportauthz.types.conditions.Conditions"]
    """<p>The time-window conditions that constrain when the permit is valid. Maximum of 2 conditions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Permit) -> dict:
    out: dict = {}
    import capo_supportauthz.types.action_set

    out["actions"] = capo_supportauthz.types.action_set.serialize_json(value["actions"])
    import capo_supportauthz.types.resource_set

    out["resources"] = capo_supportauthz.types.resource_set.serialize_json(
        value["resources"]
    )
    if "conditions" in value:
        import capo_supportauthz.types.conditions

        out["conditions"] = capo_supportauthz.types.conditions.serialize_json(
            value["conditions"]
        )
    return out


def deserialize_json(data: dict) -> Permit:
    out: Permit = {}  # type: ignore[typeddict-item]
    if data.get("actions") is not None:
        import capo_supportauthz.types.action_set

        out["actions"] = capo_supportauthz.types.action_set.deserialize_json(
            data["actions"]
        )
    else:
        raise DeserializationError("Permit.actions required")
    if data.get("resources") is not None:
        import capo_supportauthz.types.resource_set

        out["resources"] = capo_supportauthz.types.resource_set.deserialize_json(
            data["resources"]
        )
    else:
        raise DeserializationError("Permit.resources required")
    if data.get("conditions") is not None:
        import capo_supportauthz.types.conditions

        out["conditions"] = capo_supportauthz.types.conditions.deserialize_json(
            data["conditions"]
        )
    return out
