"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateMonitoringScheduleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.monitoring_schedule_config
    import capo_sagemaker.types.monitoring_schedule_name
    import capo_sagemaker.types.tag_list


class CreateMonitoringScheduleRequest(TypedDict, closed=True):
    monitoring_schedule_name: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_name.MonitoringScheduleName"
    ]
    """<p>The name of the monitoring schedule. The name must be unique within an Amazon Web Services Region within an Amazon Web Services account.</p>"""
    monitoring_schedule_config: NotRequired[
        "capo_sagemaker.types.monitoring_schedule_config.MonitoringScheduleConfig"
    ]
    """<p>The configuration object that specifies the monitoring schedule and defines the monitoring job.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>(Optional) An array of key-value pairs. For more information, see <a href=" https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-whatURL">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMonitoringScheduleRequest) -> dict:
    out: dict = {}
    if "monitoring_schedule_name" in value:
        out["MonitoringScheduleName"] = value["monitoring_schedule_name"]
    if "monitoring_schedule_config" in value:
        import capo_sagemaker.types.monitoring_schedule_config

        out["MonitoringScheduleConfig"] = (
            capo_sagemaker.types.monitoring_schedule_config.serialize_aws_json_1_1(
                value["monitoring_schedule_config"]
            )
        )
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMonitoringScheduleRequest:
    out: CreateMonitoringScheduleRequest = {}  # type: ignore[typeddict-item]
    if data.get("MonitoringScheduleName") is not None:
        out["monitoring_schedule_name"] = data["MonitoringScheduleName"]
    if data.get("MonitoringScheduleConfig") is not None:
        import capo_sagemaker.types.monitoring_schedule_config

        out["monitoring_schedule_config"] = (
            capo_sagemaker.types.monitoring_schedule_config.deserialize_aws_json_1_1(
                data["MonitoringScheduleConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
