"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_cloud_watch_logs_log_group_details


class AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails(
    TypedDict, closed=True
):
    cloud_watch_logs_log_group: NotRequired[
        "capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_cloud_watch_logs_log_group_details.AwsStepFunctionStateMachineLoggingConfigurationDestinationsCloudWatchLogsLogGroupDetails"
    ]
    """<p> An object describing a CloudWatch Logs log group. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html"> Amazon Web Services::Logs::LogGroup</a> in the <i>CloudFormation User Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails,
) -> dict:
    out: dict = {}
    if "cloud_watch_logs_log_group" in value:
        import capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_cloud_watch_logs_log_group_details

        out["CloudWatchLogsLogGroup"] = (
            capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_cloud_watch_logs_log_group_details.serialize_json(
                value["cloud_watch_logs_log_group"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails:
    out: AwsStepFunctionStateMachineLoggingConfigurationDestinationsDetails = {}  # type: ignore[typeddict-item]
    if data.get("CloudWatchLogsLogGroup") is not None:
        import capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_cloud_watch_logs_log_group_details

        out["cloud_watch_logs_log_group"] = (
            capo_securityhub.types.aws_step_function_state_machine_logging_configuration_destinations_cloud_watch_logs_log_group_details.deserialize_json(
                data["CloudWatchLogsLogGroup"]
            )
        )
    return out
