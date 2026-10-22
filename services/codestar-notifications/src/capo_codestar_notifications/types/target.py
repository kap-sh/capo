"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#Target``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codestar_notifications.types.target_address
    import capo_codestar_notifications.types.target_type


class Target(TypedDict, closed=True):
    target_type: NotRequired["capo_codestar_notifications.types.target_type.TargetType"]
    """<p>The target type. Can be an Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client.</p> <ul> <li> <p> Amazon Q Developer in chat applications topics are specified as <code>SNS</code>.</p> </li> <li> <p> Amazon Q Developer in chat applications clients are specified as <code>AWSChatbotSlack</code>.</p> </li> <li> <p> Amazon Q Developer in chat applications clients for Microsoft Teams are specified as <code>AWSChatbotMicrosoftTeams</code>.</p> </li> </ul>"""
    target_address: NotRequired[
        "capo_codestar_notifications.types.target_address.TargetAddress"
    ]
    """<p>The Amazon Resource Name (ARN) of the Amazon Q Developer in chat applications topic or Amazon Q Developer in chat applications client.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Target) -> dict:
    out: dict = {}
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    if "target_address" in value:
        out["TargetAddress"] = value["target_address"]
    return out


def deserialize_json(data: dict) -> Target:
    out: Target = {}  # type: ignore[typeddict-item]
    if data.get("TargetType") is not None:
        out["target_type"] = data["TargetType"]
    if data.get("TargetAddress") is not None:
        out["target_address"] = data["TargetAddress"]
    return out


def redact_sensitive(value: Target) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "target_address" in value:
        out["target_address"] = "*** Sensitive Data Redacted ***"
    return out
