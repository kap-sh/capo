"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#AppInstanceBot``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.chime_arn
    import capo_chime_sdk_identity.types.configuration
    import capo_chime_sdk_identity.types.metadata
    import capo_chime_sdk_identity.types.resource_name
    import capo_chime_sdk_identity.types.timestamp


class AppInstanceBot(TypedDict, closed=True):
    app_instance_bot_arn: NotRequired[
        "capo_chime_sdk_identity.types.chime_arn.ChimeArn"
    ]
    """<p>The ARN of the AppInstanceBot.</p>"""
    name: NotRequired["capo_chime_sdk_identity.types.resource_name.ResourceName"]
    """<p>The name of the AppInstanceBot.</p>"""
    configuration: NotRequired[
        "capo_chime_sdk_identity.types.configuration.Configuration"
    ]
    """<p>The data processing instructions for an AppInstanceBot.</p>"""
    created_timestamp: NotRequired["capo_chime_sdk_identity.types.timestamp.Timestamp"]
    """<p>The time at which the <code>AppInstanceBot</code> was created.</p>"""
    last_updated_timestamp: NotRequired[
        "capo_chime_sdk_identity.types.timestamp.Timestamp"
    ]
    """<p>The time at which the <code>AppInstanceBot</code> was last updated.</p>"""
    metadata: NotRequired["capo_chime_sdk_identity.types.metadata.Metadata"]
    """<p>The metadata for an AppInstanceBot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppInstanceBot) -> dict:
    out: dict = {}
    if "app_instance_bot_arn" in value:
        out["AppInstanceBotArn"] = value["app_instance_bot_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "configuration" in value:
        import capo_chime_sdk_identity.types.configuration

        out["Configuration"] = (
            capo_chime_sdk_identity.types.configuration.serialize_json(
                value["configuration"]
            )
        )
    if "created_timestamp" in value:
        import capo_chime_sdk_identity.types.timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_identity.types.timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_chime_sdk_identity.types.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_chime_sdk_identity.types.timestamp.serialize_json(
                value["last_updated_timestamp"]
            )
        )
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> AppInstanceBot:
    out: AppInstanceBot = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceBotArn") is not None:
        out["app_instance_bot_arn"] = data["AppInstanceBotArn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Configuration") is not None:
        import capo_chime_sdk_identity.types.configuration

        out["configuration"] = (
            capo_chime_sdk_identity.types.configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_identity.types.timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_identity.types.timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_chime_sdk_identity.types.timestamp

        out["last_updated_timestamp"] = (
            capo_chime_sdk_identity.types.timestamp.deserialize_json(
                data["LastUpdatedTimestamp"]
            )
        )
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    return out


def redact_sensitive(value: AppInstanceBot) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "metadata" in value:
        out["metadata"] = "*** Sensitive Data Redacted ***"
    return out
