"""Generated from Smithy shape ``com.amazonaws.iot#AuthInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.action_type
    import capo_iot.types.resources


class AuthInfo(TypedDict, closed=True):
    action_type: NotRequired["capo_iot.types.action_type.ActionType"]
    """<p>The type of action for which the principal is being authorized.</p>"""
    resources: "capo_iot.types.resources.Resources"
    """<p>The resources for which the principal is being authorized to perform the specified action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthInfo) -> dict:
    out: dict = {}
    if "action_type" in value:
        import capo_iot.types.action_type

        out["actionType"] = capo_iot.types.action_type.serialize_json(
            value["action_type"]
        )
    import capo_iot.types.resources

    out["resources"] = capo_iot.types.resources.serialize_json(value["resources"])
    return out


def deserialize_json(data: dict) -> AuthInfo:
    out: AuthInfo = {}  # type: ignore[typeddict-item]
    if data.get("actionType") is not None:
        import capo_iot.types.action_type

        out["action_type"] = capo_iot.types.action_type.deserialize_json(
            data["actionType"]
        )
    if data.get("resources") is not None:
        import capo_iot.types.resources

        out["resources"] = capo_iot.types.resources.deserialize_json(data["resources"])
    else:
        out["resources"] = []
    return out
