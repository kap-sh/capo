"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#UpdateMediaInsightsPipelineConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements
    import capo_chime_sdk_media_pipelines.types.non_empty_string
    import capo_chime_sdk_media_pipelines.types.real_time_alert_configuration


class UpdateMediaInsightsPipelineConfigurationRequest(TypedDict, closed=True):
    identifier: "capo_chime_sdk_media_pipelines.types.non_empty_string.NonEmptyString"
    """<p>The unique identifier for the resource to be updated. Valid values include the name and ARN of the media insights pipeline configuration.</p>"""
    resource_access_role_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The ARN of the role used by the service to access Amazon Web Services resources.</p>"""
    real_time_alert_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.real_time_alert_configuration.RealTimeAlertConfiguration"
    ]
    """<p>The configuration settings for real-time alerts for the media insights pipeline.</p>"""
    elements: "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.MediaInsightsPipelineConfigurationElements"
    """<p>The elements in the request, such as a processor for Amazon Transcribe or a sink for a Kinesis Data Stream..</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMediaInsightsPipelineConfigurationRequest) -> dict:
    out: dict = {}
    out["ResourceAccessRoleArn"] = value["resource_access_role_arn"]
    if "real_time_alert_configuration" in value:
        import capo_chime_sdk_media_pipelines.types.real_time_alert_configuration

        out["RealTimeAlertConfiguration"] = (
            capo_chime_sdk_media_pipelines.types.real_time_alert_configuration.serialize_json(
                value["real_time_alert_configuration"]
            )
        )
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements

    out["Elements"] = (
        capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.serialize_json(
            value["elements"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateMediaInsightsPipelineConfigurationRequest:
    out: UpdateMediaInsightsPipelineConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceAccessRoleArn") is not None:
        out["resource_access_role_arn"] = data["ResourceAccessRoleArn"]
    else:
        raise DeserializationError(
            "UpdateMediaInsightsPipelineConfigurationRequest.resource_access_role_arn required"
        )
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
    else:
        raise DeserializationError(
            "UpdateMediaInsightsPipelineConfigurationRequest.elements required"
        )
    return out


def redact_sensitive(
    value: UpdateMediaInsightsPipelineConfigurationRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
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
