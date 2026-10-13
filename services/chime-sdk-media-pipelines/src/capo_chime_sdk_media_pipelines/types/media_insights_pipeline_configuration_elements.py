"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineConfigurationElements``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element

MediaInsightsPipelineConfigurationElements: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element.MediaInsightsPipelineConfigurationElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineConfigurationElements) -> list:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaInsightsPipelineConfigurationElements:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element

    out: MediaInsightsPipelineConfigurationElements = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: MediaInsightsPipelineConfigurationElements) -> list[Any]:
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element

    return [
        capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_element.redact_sensitive(
            item
        )
        for item in value
    ]
