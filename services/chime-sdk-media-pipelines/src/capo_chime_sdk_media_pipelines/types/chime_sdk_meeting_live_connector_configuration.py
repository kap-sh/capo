"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ChimeSdkMeetingLiveConnectorConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration
    import capo_chime_sdk_media_pipelines.types.live_connector_mux_type
    import capo_chime_sdk_media_pipelines.types.source_configuration


class ChimeSdkMeetingLiveConnectorConfiguration(TypedDict, closed=True):
    arn: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The configuration object's Chime SDK meeting ARN.</p>"""
    mux_type: "capo_chime_sdk_media_pipelines.types.live_connector_mux_type.LiveConnectorMuxType"
    """<p>The configuration object's multiplex type.</p>"""
    composited_video: NotRequired[
        "capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.CompositedVideoArtifactsConfiguration"
    ]
    """<p>The media pipeline's composited video.</p>"""
    source_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.source_configuration.SourceConfiguration"
    ]
    """<p>The source configuration settings of the media pipeline's configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChimeSdkMeetingLiveConnectorConfiguration) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_chime_sdk_media_pipelines.types.live_connector_mux_type

    out["MuxType"] = (
        capo_chime_sdk_media_pipelines.types.live_connector_mux_type.serialize_json(
            value["mux_type"]
        )
    )
    if "composited_video" in value:
        import capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration

        out["CompositedVideo"] = (
            capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.serialize_json(
                value["composited_video"]
            )
        )
    if "source_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.source_configuration

        out["SourceConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChimeSdkMeetingLiveConnectorConfiguration:
    out: ChimeSdkMeetingLiveConnectorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError(
            "ChimeSdkMeetingLiveConnectorConfiguration.arn required"
        )
    if data.get("MuxType") is not None:
        import capo_chime_sdk_media_pipelines.types.live_connector_mux_type

        out["mux_type"] = (
            capo_chime_sdk_media_pipelines.types.live_connector_mux_type.deserialize_json(
                data["MuxType"]
            )
        )
    else:
        raise DeserializationError(
            "ChimeSdkMeetingLiveConnectorConfiguration.mux_type required"
        )
    if data.get("CompositedVideo") is not None:
        import capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration

        out["composited_video"] = (
            capo_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.deserialize_json(
                data["CompositedVideo"]
            )
        )
    if data.get("SourceConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.source_configuration

        out["source_configuration"] = (
            capo_chime_sdk_media_pipelines.types.source_configuration.deserialize_json(
                data["SourceConfiguration"]
            )
        )
    return out


def redact_sensitive(
    value: ChimeSdkMeetingLiveConnectorConfiguration,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "arn" in value:
        out["arn"] = "*** Sensitive Data Redacted ***"
    if "source_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.source_configuration

        out["source_configuration"] = (
            capo_chime_sdk_media_pipelines.types.source_configuration.redact_sensitive(
                value["source_configuration"]
            )
        )
    return out
