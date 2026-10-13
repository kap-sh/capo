"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineConfigurationSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.guid_string
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string


class MediaInsightsPipelineConfigurationSummary(TypedDict, closed=True):
    media_insights_pipeline_configuration_name: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string.MediaInsightsPipelineConfigurationNameString"
    ]
    """<p>The name of the media insights pipeline configuration.</p>"""
    media_insights_pipeline_configuration_id: NotRequired[
        "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    ]
    """<p>The ID of the media insights pipeline configuration.</p>"""
    media_insights_pipeline_configuration_arn: NotRequired[
        "capo_chime_sdk_media_pipelines.types.arn.Arn"
    ]
    """<p>The ARN of the media insights pipeline configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineConfigurationSummary) -> dict:
    out: dict = {}
    if "media_insights_pipeline_configuration_name" in value:
        out["MediaInsightsPipelineConfigurationName"] = value[
            "media_insights_pipeline_configuration_name"
        ]
    if "media_insights_pipeline_configuration_id" in value:
        out["MediaInsightsPipelineConfigurationId"] = value[
            "media_insights_pipeline_configuration_id"
        ]
    if "media_insights_pipeline_configuration_arn" in value:
        out["MediaInsightsPipelineConfigurationArn"] = value[
            "media_insights_pipeline_configuration_arn"
        ]
    return out


def deserialize_json(data: dict) -> MediaInsightsPipelineConfigurationSummary:
    out: MediaInsightsPipelineConfigurationSummary = {}  # type: ignore[typeddict-item]
    if data.get("MediaInsightsPipelineConfigurationName") is not None:
        out["media_insights_pipeline_configuration_name"] = data[
            "MediaInsightsPipelineConfigurationName"
        ]
    if data.get("MediaInsightsPipelineConfigurationId") is not None:
        out["media_insights_pipeline_configuration_id"] = data[
            "MediaInsightsPipelineConfigurationId"
        ]
    if data.get("MediaInsightsPipelineConfigurationArn") is not None:
        out["media_insights_pipeline_configuration_arn"] = data[
            "MediaInsightsPipelineConfigurationArn"
        ]
    return out


def redact_sensitive(
    value: MediaInsightsPipelineConfigurationSummary,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_insights_pipeline_configuration_arn" in value:
        out["media_insights_pipeline_configuration_arn"] = (
            "*** Sensitive Data Redacted ***"
        )
    return out
