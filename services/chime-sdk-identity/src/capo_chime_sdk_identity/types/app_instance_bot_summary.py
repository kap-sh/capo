"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceBotSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.resource_name


class AppInstanceBotSummary(TypedDict, closed=True):
    app_instance_bot_arn: NotRequired[
        "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the AppInstanceBot.</p>"""
    name: NotRequired["capo_chime_sdk_identity.types.resource_name.ResourceName"]
    """<p>The name of the AppInstanceBox.</p>"""
    metadata: NotRequired["capo_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The metadata of the AppInstanceBot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceBotSummary) -> dict:
    out: dict = {}
    if "app_instance_bot_arn" in value:
        out["AppInstanceBotArn"] = value["app_instance_bot_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> AppInstanceBotSummary:
    out: AppInstanceBotSummary = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceBotArn") is not None:
        out["app_instance_bot_arn"] = data["AppInstanceBotArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    return out


def redact_sensitive(value: AppInstanceBotSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
