"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorSinkConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration
    import capo_chime_sdk_media_pipelines.types.live_connector_sink_type


class LiveConnectorSinkConfiguration(TypedDict, closed=True):
    sink_type: "capo_chime_sdk_media_pipelines.types.live_connector_sink_type.LiveConnectorSinkType"
    """<p>The sink configuration's sink type.</p>"""
    rtmp_configuration: "capo_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration.LiveConnectorRTMPConfiguration"
    """<p>The sink configuration's RTMP configuration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LiveConnectorSinkConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.live_connector_sink_type

    out["SinkType"] = (
        capo_chime_sdk_media_pipelines.types.live_connector_sink_type.serialize_json(
            value["sink_type"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration

    out["RTMPConfiguration"] = (
        capo_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration.serialize_json(
            value["rtmp_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> LiveConnectorSinkConfiguration:
    out: LiveConnectorSinkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("SinkType") is not None:
        import capo_chime_sdk_media_pipelines.types.live_connector_sink_type

        out["sink_type"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_sink_type.deserialize_json(
                data["SinkType"]
            )
        )
    else:
        import typing

        out["sink_type"] = typing.cast(
            "capo_chime_sdk_media_pipelines.types.live_connector_sink_type.LiveConnectorSinkType",
            "",
        )
    if data.get("RTMPConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration

        out["rtmp_configuration"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration.deserialize_json(
                data["RTMPConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "LiveConnectorSinkConfiguration.rtmp_configuration required"
        )
    return out


def redact_sensitive(value: LiveConnectorSinkConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "rtmp_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration

        out["rtmp_configuration"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration.redact_sensitive(
                value["rtmp_configuration"]
            )
        )
    return out
