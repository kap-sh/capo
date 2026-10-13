"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ListMediaInsightsPipelineConfigurationsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary_list
    import capo_chime_sdk_media_pipelines.types.string


class ListMediaInsightsPipelineConfigurationsResponse(TypedDict, closed=True):
    media_insights_pipeline_configurations: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary_list.MediaInsightsPipelineConfigurationSummaryList"
    ]
    """<p>The requested list of media insights pipeline configurations.</p>"""
    next_token: NotRequired["capo_chime_sdk_media_pipelines.types.string.String"]
    """<p>The token used to return the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMediaInsightsPipelineConfigurationsResponse) -> dict:
    out: dict = {}
    if "media_insights_pipeline_configurations" in value:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary_list

        out["MediaInsightsPipelineConfigurations"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary_list.serialize_json(
                value["media_insights_pipeline_configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMediaInsightsPipelineConfigurationsResponse:
    out: ListMediaInsightsPipelineConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("MediaInsightsPipelineConfigurations") is not None:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary_list

        out["media_insights_pipeline_configurations"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary_list.deserialize_json(
                data["MediaInsightsPipelineConfigurations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(
    value: ListMediaInsightsPipelineConfigurationsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_insights_pipeline_configurations" in value:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary_list

        out["media_insights_pipeline_configurations"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_summary_list.redact_sensitive(
                value["media_insights_pipeline_configurations"]
            )
        )
    return out
