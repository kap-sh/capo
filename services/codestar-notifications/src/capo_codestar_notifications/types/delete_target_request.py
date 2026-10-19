"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#DeleteTargetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.force_unsubscribe_all
    import capo_codestar_notifications.types.target_address


class DeleteTargetRequest(TypedDict, closed=True):
    target_address: "capo_codestar_notifications.types.target_address.TargetAddress"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client to delete.</p>"""
    force_unsubscribe_all: NotRequired[
        "capo_codestar_notifications.types.force_unsubscribe_all.ForceUnsubscribeAll"
    ]
    """<p>A Boolean value that can be used to delete all associations with this Amazon Q Developer in chat applications topic. The default value is FALSE. If set to TRUE, all associations between that target and every notification rule in your Amazon Web Services account are deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteTargetRequest) -> dict:
    out: dict = {}
    out["TargetAddress"] = value["target_address"]
    if "force_unsubscribe_all" in value:
        out["ForceUnsubscribeAll"] = value["force_unsubscribe_all"]
    return out


def deserialize_json(data: dict) -> DeleteTargetRequest:
    out: DeleteTargetRequest = {}  # type: ignore[typeddict-item]
    if data.get("TargetAddress") is not None:
        out["target_address"] = data["TargetAddress"]
    else:
        out["target_address"] = ""
    if data.get("ForceUnsubscribeAll") is not None:
        out["force_unsubscribe_all"] = data["ForceUnsubscribeAll"]
    return out


def redact_sensitive(value: DeleteTargetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_address" in value:
        out["target_address"] = "*** Sensitive Data Redacted ***"
    return out
