"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaInsightsPipelineConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.arn
    import capo_chime_sdk_media_pipelines.types.client_request_token
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements
    import capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string
    import capo_chime_sdk_media_pipelines.types.real_time_alert_configuration
    import capo_chime_sdk_media_pipelines.types.tag_list


class CreateMediaInsightsPipelineConfigurationRequest(TypedDict, closed=True):
    media_insights_pipeline_configuration_name: "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_name_string.MediaInsightsPipelineConfigurationNameString"
    """<p>The name of the media insights pipeline configuration.</p>"""
    resource_access_role_arn: "capo_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The ARN of the role used by the service to access Amazon Web Services resources, including <code>Transcribe</code> and <code>Transcribe Call Analytics</code>, on the caller’s behalf.</p>"""
    real_time_alert_configuration: NotRequired[
        "capo_chime_sdk_media_pipelines.types.real_time_alert_configuration.RealTimeAlertConfiguration"
    ]
    """<p>The configuration settings for the real-time alerts in a media insights pipeline configuration.</p>"""
    elements: "capo_chime_sdk_media_pipelines.types.media_insights_pipeline_configuration_elements.MediaInsightsPipelineConfigurationElements"
    """<p>The elements in the request, such as a processor for Amazon Transcribe or a sink for a Kinesis Data Stream.</p>"""
    tags: NotRequired["capo_chime_sdk_media_pipelines.types.tag_list.TagList"]
    """<p>The tags assigned to the media insights pipeline configuration.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The unique identifier for the media insights pipeline configuration request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaInsightsPipelineConfigurationRequest) -> dict:
    out: dict = {}
    out["MediaInsightsPipelineConfigurationName"] = value[
        "media_insights_pipeline_configuration_name"
    ]
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
    if "tags" in value:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["Tags"] = capo_chime_sdk_media_pipelines.types.tag_list.serialize_json(
            value["tags"]
        )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateMediaInsightsPipelineConfigurationRequest:
    out: CreateMediaInsightsPipelineConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("MediaInsightsPipelineConfigurationName") is not None:
        out["media_insights_pipeline_configuration_name"] = data[
            "MediaInsightsPipelineConfigurationName"
        ]
    else:
        out["media_insights_pipeline_configuration_name"] = ""
    if data.get("ResourceAccessRoleArn") is not None:
        out["resource_access_role_arn"] = data["ResourceAccessRoleArn"]
    else:
        out["resource_access_role_arn"] = ""
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
        out["elements"] = []
    if data.get("Tags") is not None:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["tags"] = capo_chime_sdk_media_pipelines.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out


def redact_sensitive(
    value: CreateMediaInsightsPipelineConfigurationRequest,
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
    if "client_request_token" in value:
        out["client_request_token"] = "*** Sensitive Data Redacted ***"
    return out
