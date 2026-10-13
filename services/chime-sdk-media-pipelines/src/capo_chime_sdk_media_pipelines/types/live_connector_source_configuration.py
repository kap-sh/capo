"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorSourceConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_live_connector_configuration
    import capo_chime_sdk_media_pipelines.types.live_connector_source_type


class LiveConnectorSourceConfiguration(TypedDict, closed=True):
    source_type: "capo_chime_sdk_media_pipelines.types.live_connector_source_type.LiveConnectorSourceType"
    """<p>The source configuration's media source type.</p>"""
    chime_sdk_meeting_live_connector_configuration: "capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_live_connector_configuration.ChimeSdkMeetingLiveConnectorConfiguration"
    """<p>The configuration settings of the connector pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LiveConnectorSourceConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.live_connector_source_type

    out["SourceType"] = (
        capo_chime_sdk_media_pipelines.types.live_connector_source_type.serialize_json(
            value["source_type"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_live_connector_configuration

    out["ChimeSdkMeetingLiveConnectorConfiguration"] = (
        capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_live_connector_configuration.serialize_json(
            value["chime_sdk_meeting_live_connector_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> LiveConnectorSourceConfiguration:
    out: LiveConnectorSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SourceType") is not None:
        import capo_chime_sdk_media_pipelines.types.live_connector_source_type

        out["source_type"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_source_type.deserialize_json(
                data["SourceType"]
            )
        )
    else:
        raise DeserializationError(
            "LiveConnectorSourceConfiguration.source_type required"
        )
    if data.get("ChimeSdkMeetingLiveConnectorConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_live_connector_configuration

        out["chime_sdk_meeting_live_connector_configuration"] = (
            capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_live_connector_configuration.deserialize_json(
                data["ChimeSdkMeetingLiveConnectorConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "LiveConnectorSourceConfiguration.chime_sdk_meeting_live_connector_configuration required"
        )
    return out


def redact_sensitive(value: LiveConnectorSourceConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "chime_sdk_meeting_live_connector_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_live_connector_configuration

        out["chime_sdk_meeting_live_connector_configuration"] = (
            capo_chime_sdk_media_pipelines.types.chime_sdk_meeting_live_connector_configuration.redact_sensitive(
                value["chime_sdk_meeting_live_connector_configuration"]
            )
        )
    return out
