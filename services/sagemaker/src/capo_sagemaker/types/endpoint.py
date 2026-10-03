"""Generated from Smithy shape ``com.amazonaws.sagemaker#Endpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.data_capture_config_summary
    import capo_sagemaker.types.endpoint_arn
    import capo_sagemaker.types.endpoint_config_name
    import capo_sagemaker.types.endpoint_name
    import capo_sagemaker.types.endpoint_status
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.monitoring_schedule_list
    import capo_sagemaker.types.production_variant_summary_list
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.timestamp


class Endpoint(TypedDict, closed=True):
    endpoint_name: NotRequired["capo_sagemaker.types.endpoint_name.EndpointName"]
    """<p>The name of the endpoint.</p>"""
    endpoint_arn: NotRequired["capo_sagemaker.types.endpoint_arn.EndpointArn"]
    """<p>The Amazon Resource Name (ARN) of the endpoint.</p>"""
    endpoint_config_name: NotRequired[
        "capo_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    """<p>The endpoint configuration associated with the endpoint.</p>"""
    production_variants: NotRequired[
        "capo_sagemaker.types.production_variant_summary_list.ProductionVariantSummaryList"
    ]
    """<p>A list of the production variants hosted on the endpoint. Each production variant is a model.</p>"""
    data_capture_config: NotRequired[
        "capo_sagemaker.types.data_capture_config_summary.DataCaptureConfigSummary"
    ]
    endpoint_status: NotRequired["capo_sagemaker.types.endpoint_status.EndpointStatus"]
    """<p>The status of the endpoint.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the endpoint failed, the reason it failed.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time that the endpoint was created.</p>"""
    last_modified_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The last time the endpoint was modified.</p>"""
    monitoring_schedules: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_list.MonitoringScheduleList"
    ]
    """<p>A list of monitoring schedules for the endpoint. For information about model monitoring, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html">Amazon SageMaker Model Monitor</a>.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>A list of the tags associated with the endpoint. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""
    shadow_production_variants: NotRequired[
        "capo_sagemaker.types.production_variant_summary_list.ProductionVariantSummaryList"
    ]
    """<p>A list of the shadow variants hosted on the endpoint. Each shadow variant is a model in shadow mode with production traffic replicated from the production variant.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Endpoint) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "endpoint_arn" in value:
        out["EndpointArn"] = value["endpoint_arn"]
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
    if "production_variants" in value:
        import capo_sagemaker.types.production_variant_summary_list

        out["ProductionVariants"] = (
            capo_sagemaker.types.production_variant_summary_list.serialize_aws_json_1_1(
                value["production_variants"]
            )
        )
    if "data_capture_config" in value:
        import capo_sagemaker.types.data_capture_config_summary

        out["DataCaptureConfig"] = (
            capo_sagemaker.types.data_capture_config_summary.serialize_aws_json_1_1(
                value["data_capture_config"]
            )
        )
    if "endpoint_status" in value:
        import capo_sagemaker.types.endpoint_status

        out["EndpointStatus"] = (
            capo_sagemaker.types.endpoint_status.serialize_aws_json_1_1(
                value["endpoint_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_time"]
        )
    if "monitoring_schedules" in value:
        import capo_sagemaker.types.monitoring_schedule_list

        out["MonitoringSchedules"] = (
            capo_sagemaker.types.monitoring_schedule_list.serialize_aws_json_1_1(
                value["monitoring_schedules"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "shadow_production_variants" in value:
        import capo_sagemaker.types.production_variant_summary_list

        out["ShadowProductionVariants"] = (
            capo_sagemaker.types.production_variant_summary_list.serialize_aws_json_1_1(
                value["shadow_production_variants"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Endpoint:
    out: Endpoint = {}  # type: ignore[typeddict-item]
    if data.get("EndpointName") is not None:
        out["endpoint_name"] = data["EndpointName"]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    if data.get("EndpointConfigName") is not None:
        out["endpoint_config_name"] = data["EndpointConfigName"]
    if data.get("ProductionVariants") is not None:
        import capo_sagemaker.types.production_variant_summary_list

        out["production_variants"] = (
            capo_sagemaker.types.production_variant_summary_list.deserialize_aws_json_1_1(
                data["ProductionVariants"]
            )
        )
    if data.get("DataCaptureConfig") is not None:
        import capo_sagemaker.types.data_capture_config_summary

        out["data_capture_config"] = (
            capo_sagemaker.types.data_capture_config_summary.deserialize_aws_json_1_1(
                data["DataCaptureConfig"]
            )
        )
    if data.get("EndpointStatus") is not None:
        import capo_sagemaker.types.endpoint_status

        out["endpoint_status"] = (
            capo_sagemaker.types.endpoint_status.deserialize_aws_json_1_1(
                data["EndpointStatus"]
            )
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if data.get("LastModifiedTime") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if data.get("MonitoringSchedules") is not None:
        import capo_sagemaker.types.monitoring_schedule_list

        out["monitoring_schedules"] = (
            capo_sagemaker.types.monitoring_schedule_list.deserialize_aws_json_1_1(
                data["MonitoringSchedules"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ShadowProductionVariants") is not None:
        import capo_sagemaker.types.production_variant_summary_list

        out["shadow_production_variants"] = (
            capo_sagemaker.types.production_variant_summary_list.deserialize_aws_json_1_1(
                data["ShadowProductionVariants"]
            )
        )
    return out
