"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#StreamingConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.boolean
    import capo_chime_sdk_voice.types.data_retention_in_hours
    import capo_chime_sdk_voice.types.media_insights_configuration
    import capo_chime_sdk_voice.types.streaming_notification_target_list


class StreamingConfiguration(TypedDict, closed=True):
    data_retention_in_hours: (
        "capo_chime_sdk_voice.types.data_retention_in_hours.DataRetentionInHours"
    )
    """<p>The amount of time, in hours, to the Kinesis data.</p>"""
    disabled: "capo_chime_sdk_voice.types.boolean.Boolean"
    """<p>When true, streaming to Kinesis is off.</p>"""
    streaming_notification_targets: NotRequired[
        "capo_chime_sdk_voice.types.streaming_notification_target_list.StreamingNotificationTargetList"
    ]
    """<p>The streaming notification targets.</p>"""
    media_insights_configuration: NotRequired[
        "capo_chime_sdk_voice.types.media_insights_configuration.MediaInsightsConfiguration"
    ]
    """<p>The call analytics configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamingConfiguration) -> dict:
    out: dict = {}
    out["DataRetentionInHours"] = value["data_retention_in_hours"]
    out["Disabled"] = value["disabled"]
    if "streaming_notification_targets" in value:
        import capo_chime_sdk_voice.types.streaming_notification_target_list

        out["StreamingNotificationTargets"] = (
            capo_chime_sdk_voice.types.streaming_notification_target_list.serialize_json(
                value["streaming_notification_targets"]
            )
        )
    if "media_insights_configuration" in value:
        import capo_chime_sdk_voice.types.media_insights_configuration

        out["MediaInsightsConfiguration"] = (
            capo_chime_sdk_voice.types.media_insights_configuration.serialize_json(
                value["media_insights_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> StreamingConfiguration:
    out: StreamingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DataRetentionInHours") is not None:
        out["data_retention_in_hours"] = data["DataRetentionInHours"]
    else:
        out["data_retention_in_hours"] = 0
    if data.get("Disabled") is not None:
        out["disabled"] = data["Disabled"]
    else:
        out["disabled"] = False
    if data.get("StreamingNotificationTargets") is not None:
        import capo_chime_sdk_voice.types.streaming_notification_target_list

        out["streaming_notification_targets"] = (
            capo_chime_sdk_voice.types.streaming_notification_target_list.deserialize_json(
                data["StreamingNotificationTargets"]
            )
        )
    if data.get("MediaInsightsConfiguration") is not None:
        import capo_chime_sdk_voice.types.media_insights_configuration

        out["media_insights_configuration"] = (
            capo_chime_sdk_voice.types.media_insights_configuration.deserialize_json(
                data["MediaInsightsConfiguration"]
            )
        )
    return out


def redact_sensitive(value: StreamingConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_insights_configuration" in value:
        import capo_chime_sdk_voice.types.media_insights_configuration

        out["media_insights_configuration"] = (
            capo_chime_sdk_voice.types.media_insights_configuration.redact_sensitive(
                value["media_insights_configuration"]
            )
        )
    return out
