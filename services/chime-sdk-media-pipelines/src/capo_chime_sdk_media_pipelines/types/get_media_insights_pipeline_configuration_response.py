"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#GetMediaInsightsPipelineConfigurationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration


class GetMediaInsightsPipelineConfigurationResponse(TypedDict, closed=True):
    media_insights_pipeline_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration.MediaInsightsPipelineConfiguration"
    ]
    """<p>The requested media insights pipeline configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaInsightsPipelineConfigurationResponse) -> dict:
    out: dict = {}
    if "media_insights_pipeline_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration

        out["MediaInsightsPipelineConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration.serialize_json(
                value["media_insights_pipeline_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMediaInsightsPipelineConfigurationResponse:
    out: GetMediaInsightsPipelineConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("MediaInsightsPipelineConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration

        out["media_insights_pipeline_configuration"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration.deserialize_json(
                data["MediaInsightsPipelineConfiguration"]
            )
        )
    return out


def redact_sensitive(
    value: GetMediaInsightsPipelineConfigurationResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_insights_pipeline_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration

        out["media_insights_pipeline_configuration"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration.redact_sensitive(
                value["media_insights_pipeline_configuration"]
            )
        )
    return out
