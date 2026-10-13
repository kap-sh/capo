"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaPipeline``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_capture_pipeline
    import capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline
    import capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline
    import capo_chime_sdk_media_pipelines.types.media_stream_pipeline


class MediaPipeline(TypedDict, closed=True):
    media_capture_pipeline: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_capture_pipeline.MediaCapturePipeline"
    ]
    """<p>A pipeline that enables users to capture audio and video.</p>"""
    media_live_connector_pipeline: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline.MediaLiveConnectorPipeline"
    ]
    """<p>The connector pipeline of the media pipeline.</p>"""
    media_concatenation_pipeline: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline.MediaConcatenationPipeline"
    ]
    """<p>The media concatenation pipeline in a media pipeline.</p>"""
    media_insights_pipeline: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_insights_pipeline.MediaInsightsPipeline"
    ]
    """<p>The media insights pipeline of a media pipeline.</p>"""
    media_stream_pipeline: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_stream_pipeline.MediaStreamPipeline"
    ]
    """<p>Designates a media pipeline as a media stream pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaPipeline) -> dict:
    out: dict = {}
    if "media_capture_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_capture_pipeline

        out["MediaCapturePipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_capture_pipeline.serialize_json(
                value["media_capture_pipeline"]
            )
        )
    if "media_live_connector_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline

        out["MediaLiveConnectorPipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline.serialize_json(
                value["media_live_connector_pipeline"]
            )
        )
    if "media_concatenation_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline

        out["MediaConcatenationPipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline.serialize_json(
                value["media_concatenation_pipeline"]
            )
        )
    if "media_insights_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline

        out["MediaInsightsPipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline.serialize_json(
                value["media_insights_pipeline"]
            )
        )
    if "media_stream_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_stream_pipeline

        out["MediaStreamPipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_pipeline.serialize_json(
                value["media_stream_pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaPipeline:
    out: MediaPipeline = {}  # type: ignore[typeddict-item]
    if data.get("MediaCapturePipeline") is not None:
        import capo_chime_sdk_media_pipelines.types.media_capture_pipeline

        out["media_capture_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_capture_pipeline.deserialize_json(
                data["MediaCapturePipeline"]
            )
        )
    if data.get("MediaLiveConnectorPipeline") is not None:
        import capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline

        out["media_live_connector_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline.deserialize_json(
                data["MediaLiveConnectorPipeline"]
            )
        )
    if data.get("MediaConcatenationPipeline") is not None:
        import capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline

        out["media_concatenation_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline.deserialize_json(
                data["MediaConcatenationPipeline"]
            )
        )
    if data.get("MediaInsightsPipeline") is not None:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline

        out["media_insights_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline.deserialize_json(
                data["MediaInsightsPipeline"]
            )
        )
    if data.get("MediaStreamPipeline") is not None:
        import capo_chime_sdk_media_pipelines.types.media_stream_pipeline

        out["media_stream_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_pipeline.deserialize_json(
                data["MediaStreamPipeline"]
            )
        )
    return out


def redact_sensitive(value: MediaPipeline) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_capture_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_capture_pipeline

        out["media_capture_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_capture_pipeline.redact_sensitive(
                value["media_capture_pipeline"]
            )
        )
    if "media_live_connector_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline

        out["media_live_connector_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline.redact_sensitive(
                value["media_live_connector_pipeline"]
            )
        )
    if "media_concatenation_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline

        out["media_concatenation_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_concatenation_pipeline.redact_sensitive(
                value["media_concatenation_pipeline"]
            )
        )
    if "media_insights_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline

        out["media_insights_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline.redact_sensitive(
                value["media_insights_pipeline"]
            )
        )
    if "media_stream_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_stream_pipeline

        out["media_stream_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_pipeline.redact_sensitive(
                value["media_stream_pipeline"]
            )
        )
    return out
