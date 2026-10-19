"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ActionIdentifier``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.action_id
    import capo_verifiedpermissions.types.action_type


class ActionIdentifier(TypedDict, closed=True):
    action_type: "capo_verifiedpermissions.types.action_type.ActionType"
    """<p>The type of an action.</p>"""
    action_id: "capo_verifiedpermissions.types.action_id.ActionId"
    """<p>The ID of an action.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionIdentifier) -> dict:
    out: dict = {}
    out["actionType"] = value["action_type"]
    out["actionId"] = value["action_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ActionIdentifier:
    out: ActionIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("actionType") is not None:
        out["action_type"] = data["actionType"]
    else:
        out["action_type"] = ""
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    else:
        out["action_id"] = ""
    return out


def redact_sensitive(value: ActionIdentifier) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "action_type" in value:
        out["action_type"] = "*** Sensitive Data Redacted ***"
    if "action_id" in value:
        out["action_id"] = "*** Sensitive Data Redacted ***"
    return out
