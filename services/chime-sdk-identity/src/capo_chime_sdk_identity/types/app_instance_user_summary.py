"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceUserSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.user_name


class AppInstanceUserSummary(TypedDict, closed=True):
    app_instance_user_arn: NotRequired[
        "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the <code>AppInstanceUser</code>.</p>"""
    name: NotRequired["capo_chime_sdk_identity.types.user_name.UserName"]
    """<p>The name of an <code>AppInstanceUser</code>.</p>"""
    metadata: NotRequired["capo_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The metadata of the <code>AppInstanceUser</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceUserSummary) -> dict:
    out: dict = {}
    if "app_instance_user_arn" in value:
        out["AppInstanceUserArn"] = value["app_instance_user_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> AppInstanceUserSummary:
    out: AppInstanceUserSummary = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceUserArn") is not None:
        out["app_instance_user_arn"] = data["AppInstanceUserArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    return out


def redact_sensitive(value: AppInstanceUserSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
