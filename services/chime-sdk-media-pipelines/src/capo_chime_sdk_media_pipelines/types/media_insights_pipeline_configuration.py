"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaInsightsPipelineConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.guid_string
    import capo_chime_sdk_media_pipelines.types.iso8601_timestamp
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string
    import capo_chime_sdk_media_pipelines.types.real_time_alert_configuration


class MediaInsightsPipelineConfiguration(TypedDict, closed=True):
    media_insights_pipeline_configuration_name: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string.MediaInsightsPipelineConfigurationNameString"
    ]
    """<p>The name of the configuration.</p>"""
    media_insights_pipeline_configuration_arn: NotRequired[
        "capo_chime_sdk_media_pipelines.types.arn.Arn"
    ]
    """<p>The ARN of the configuration.</p>"""
    resource_access_role_arn: NotRequired[
        "capo_chime_sdk_media_pipelines.types.arn.Arn"
    ]
    """<p>The ARN of the role used by the service to access Amazon Web Services resources.</p>"""
    real_time_alert_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.real_time_alert_configuration.RealTimeAlertConfiguration"
    ]
    """<p>Lists the rules that trigger a real-time alert.</p>"""
    elements: NotRequired[
        "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.MediaInsightsPipelineConfigurationElements"
    ]
    """<p>The elements in the configuration.</p>"""
    media_insights_pipeline_configuration_id: NotRequired[
        "capo_chime_sdk_media_pipelines.types.guid_string.GuidString"
    ]
    """<p>The ID of the configuration.</p>"""
    created_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the configuration was created.</p>"""
    updated_timestamp: NotRequired[
        "capo_chime_sdk_media_pipelines.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time at which the configuration was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaInsightsPipelineConfiguration) -> dict:
    out: dict = {}
    if "media_insights_pipeline_configuration_name" in value:
        out["MediaInsightsPipelineConfigurationName"] = value[
            "media_insights_pipeline_configuration_name"
        ]
    if "media_insights_pipeline_configuration_arn" in value:
        out["MediaInsightsPipelineConfigurationArn"] = value[
            "media_insights_pipeline_configuration_arn"
        ]
    if "resource_access_role_arn" in value:
        out["ResourceAccessRoleArn"] = value["resource_access_role_arn"]
    if "real_time_alert_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.real_time_alert_configuration

        out["RealTimeAlertConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.real_time_alert_configuration.serialize_json(
                value["real_time_alert_configuration"]
            )
        )
    if "elements" in value:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements

        out["Elements"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.serialize_json(
                value["elements"]
            )
        )
    if "media_insights_pipeline_configuration_id" in value:
        out["MediaInsightsPipelineConfigurationId"] = value[
            "media_insights_pipeline_configuration_id"
        ]
    if "created_timestamp" in value:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["CreatedTimestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["created_timestamp"]
            )
        )
    if "updated_timestamp" in value:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["UpdatedTimestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.serialize_json(
                value["updated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> MediaInsightsPipelineConfiguration:
    out: MediaInsightsPipelineConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("MediaInsightsPipelineConfigurationName") is not None:
        out["media_insights_pipeline_configuration_name"] = data[
            "MediaInsightsPipelineConfigurationName"
        ]
    if data.get("MediaInsightsPipelineConfigurationArn") is not None:
        out["media_insights_pipeline_configuration_arn"] = data[
            "MediaInsightsPipelineConfigurationArn"
        ]
    if data.get("ResourceAccessRoleArn") is not None:
        out["resource_access_role_arn"] = data["ResourceAccessRoleArn"]
    if data.get("RealTimeAlertConfiguration") is not None:
        import capo_chime_sdk_media_pipelines.types.real_time_alert_configuration

        out["real_time_alert_configuration"] = (
            capo_chime_sdk_media_pipelines.types.real_time_alert_configuration.deserialize_json(
                data["RealTimeAlertConfiguration"]
            )
        )
    if data.get("Elements") is not None:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements

        out["elements"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.deserialize_json(
                data["Elements"]
            )
        )
    if data.get("MediaInsightsPipelineConfigurationId") is not None:
        out["media_insights_pipeline_configuration_id"] = data[
            "MediaInsightsPipelineConfigurationId"
        ]
    if data.get("CreatedTimestamp") is not None:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["created_timestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if data.get("UpdatedTimestamp") is not None:
        import capo_chime_sdk_media_pipelines.types.iso8601_timestamp

        out["updated_timestamp"] = (
            capo_chime_sdk_media_pipelines.types.iso8601_timestamp.deserialize_json(
                data["UpdatedTimestamp"]
            )
        )
    return out


def redact_sensitive(value: MediaInsightsPipelineConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "media_insights_pipeline_configuration_arn" in value:
        out["media_insights_pipeline_configuration_arn"] = (
            "*** Sensitive Data Redacted ***"
        )
    if "resource_access_role_arn" in value:
        out["resource_access_role_arn"] = "*** Sensitive Data Redacted ***"
    if "elements" in value:
        import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements

        out["elements"] = (
            capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.redact_sensitive(
                value["elements"]
            )
        )
    return out
