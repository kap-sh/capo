"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaLiveConnectorPipelineResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline


class CreateMediaLiveConnectorPipelineResponse(TypedDict, closed=True):
    media_live_connector_pipeline: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline.MediaLiveConnectorPipeline"
    ]
    """<p>The new media live connector pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaLiveConnectorPipelineResponse) -> dict:
    out: dict = {}
    if "media_live_connector_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline

        out["MediaLiveConnectorPipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline.serialize_json(
                value["media_live_connector_pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMediaLiveConnectorPipelineResponse:
    out: CreateMediaLiveConnectorPipelineResponse = {}  # type: ignore[typeddict-item]
    if data.get("MediaLiveConnectorPipeline") is not None:
        import capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline

        out["media_live_connector_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline.deserialize_json(
                data["MediaLiveConnectorPipeline"]
            )
        )
    return out


def redact_sensitive(value: CreateMediaLiveConnectorPipelineResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_live_connector_pipeline" in value:
        import capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline

        out["media_live_connector_pipeline"] = (
            capo_chime_sdk_media_pipelines.types.media_live_connector_pipeline.redact_sensitive(
                value["media_live_connector_pipeline"]
            )
        )
    return out
