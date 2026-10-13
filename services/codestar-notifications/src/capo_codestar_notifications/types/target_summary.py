"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#TargetSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.target_address
    import capo_codestar_notifications.types.target_status
    import capo_codestar_notifications.types.target_type


class TargetSummary(TypedDict, closed=True):
    target_address: NotRequired[
        "capo_codestar_notifications.types.target_address.TargetAddress"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client.</p>"""
    target_type: NotRequired["capo_codestar_notifications.types.target_type.TargetType"]
    """<p>The type of the target (for example, <code>SNS</code>).</p> <ul> <li> <p>Amazon Q Developer in chat applications topics are specified as <code>SNS</code>.</p> </li> <li> <p>Amazon Q Developer in chat applications clients are specified as <code>AWSChatbotSlack</code>.</p> </li> </ul>"""
    target_status: NotRequired[
        "capo_codestar_notifications.types.target_status.TargetStatus"
    ]
    """<p>The status of the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummary) -> dict:
    out: dict = {}
    if "target_address" in value:
        out["TargetAddress"] = value["target_address"]
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    if "target_status" in value:
        import capo_codestar_notifications.types.target_status

        out["TargetStatus"] = (
            capo_codestar_notifications.types.target_status.serialize_json(
                value["target_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> TargetSummary:
    out: TargetSummary = {}  # type: ignore[typeddict-item]
    if data.get("TargetAddress") is not None:
        out["target_address"] = data["TargetAddress"]
    if data.get("TargetType") is not None:
        out["target_type"] = data["TargetType"]
    if data.get("TargetStatus") is not None:
        import capo_codestar_notifications.types.target_status

        out["target_status"] = (
            capo_codestar_notifications.types.target_status.deserialize_json(
                data["TargetStatus"]
            )
        )
    return out


def redact_sensitive(value: TargetSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_address" in value:
        out["target_address"] = "*** Sensitive Data Redacted ***"
    return out
