"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_configuration_update
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_option_updates
    import capo_kinesis_analytics_v2.types.conditional_token
    import capo_kinesis_analytics_v2.types.role_arn
    import capo_kinesis_analytics_v2.types.run_configuration_update
    import capo_kinesis_analytics_v2.types.runtime_environment


class UpdateApplicationRequest(TypedDict, closed=True):
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of the application to update.</p>"""
    current_application_version_id: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The current application version ID. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>.You can retrieve the application version ID using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>"""
    application_configuration_update: NotRequired[
        "capo_kinesis_analytics_v2.types.application_configuration_update.ApplicationConfigurationUpdate"
    ]
    """<p>Describes application configuration updates.</p>"""
    service_execution_role_update: NotRequired[
        "capo_kinesis_analytics_v2.types.role_arn.RoleARN"
    ]
    """<p>Describes updates to the service execution role.</p>"""
    run_configuration_update: NotRequired[
        "capo_kinesis_analytics_v2.types.run_configuration_update.RunConfigurationUpdate"
    ]
    """<p>Describes updates to the application's starting parameters.</p>"""
    cloud_watch_logging_option_updates: NotRequired[
        "capo_kinesis_analytics_v2.types.cloud_watch_logging_option_updates.CloudWatchLoggingOptionUpdates"
    ]
    """<p>Describes application Amazon CloudWatch logging option updates. You can only update existing CloudWatch logging options with this action. To add a new CloudWatch logging option, use <a>AddApplicationCloudWatchLoggingOption</a>.</p>"""
    conditional_token: NotRequired[
        "capo_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
    ]
    """<p>A value you use to implement strong concurrency for application updates. You must provide the <code>CurrentApplicationVersionId</code> or the <code>ConditionalToken</code>. You get the application's current <code>ConditionalToken</code> using <a>DescribeApplication</a>. For better concurrency support, use the <code>ConditionalToken</code> parameter instead of <code>CurrentApplicationVersionId</code>.</p>"""
    runtime_environment_update: NotRequired[
        "capo_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment"
    ]
    """<p>Updates the Managed Service for Apache Flink runtime environment used to run your code. To avoid issues you must:</p> <ul> <li> <p>Ensure your new jar and dependencies are compatible with the new runtime selected.</p> </li> <li> <p>Ensure your new code's state is compatible with the snapshot from which your application will start</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    out["ApplicationName"] = value["application_name"]
    if "current_application_version_id" in value:
        out["CurrentApplicationVersionId"] = value["current_application_version_id"]
    if "application_configuration_update" in value:
        import capo_kinesis_analytics_v2.types.application_configuration_update

        out["ApplicationConfigurationUpdate"] = (
            capo_kinesis_analytics_v2.types.application_configuration_update.serialize_aws_json_1_1(
                value["application_configuration_update"]
            )
        )
    if "service_execution_role_update" in value:
        out["ServiceExecutionRoleUpdate"] = value["service_execution_role_update"]
    if "run_configuration_update" in value:
        import capo_kinesis_analytics_v2.types.run_configuration_update

        out["RunConfigurationUpdate"] = (
            capo_kinesis_analytics_v2.types.run_configuration_update.serialize_aws_json_1_1(
                value["run_configuration_update"]
            )
        )
    if "cloud_watch_logging_option_updates" in value:
        import capo_kinesis_analytics_v2.types.cloud_watch_logging_option_updates

        out["CloudWatchLoggingOptionUpdates"] = (
            capo_kinesis_analytics_v2.types.cloud_watch_logging_option_updates.serialize_aws_json_1_1(
                value["cloud_watch_logging_option_updates"]
            )
        )
    if "conditional_token" in value:
        out["ConditionalToken"] = value["conditional_token"]
    if "runtime_environment_update" in value:
        import capo_kinesis_analytics_v2.types.runtime_environment

        out["RuntimeEnvironmentUpdate"] = (
            capo_kinesis_analytics_v2.types.runtime_environment.serialize_aws_json_1_1(
                value["runtime_environment_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("CurrentApplicationVersionId") is not None:
        out["current_application_version_id"] = data["CurrentApplicationVersionId"]
    if data.get("ApplicationConfigurationUpdate") is not None:
        import capo_kinesis_analytics_v2.types.application_configuration_update

        out["application_configuration_update"] = (
            capo_kinesis_analytics_v2.types.application_configuration_update.deserialize_aws_json_1_1(
                data["ApplicationConfigurationUpdate"]
            )
        )
    if data.get("ServiceExecutionRoleUpdate") is not None:
        out["service_execution_role_update"] = data["ServiceExecutionRoleUpdate"]
    if data.get("RunConfigurationUpdate") is not None:
        import capo_kinesis_analytics_v2.types.run_configuration_update

        out["run_configuration_update"] = (
            capo_kinesis_analytics_v2.types.run_configuration_update.deserialize_aws_json_1_1(
                data["RunConfigurationUpdate"]
            )
        )
    if data.get("CloudWatchLoggingOptionUpdates") is not None:
        import capo_kinesis_analytics_v2.types.cloud_watch_logging_option_updates

        out["cloud_watch_logging_option_updates"] = (
            capo_kinesis_analytics_v2.types.cloud_watch_logging_option_updates.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptionUpdates"]
            )
        )
    if data.get("ConditionalToken") is not None:
        out["conditional_token"] = data["ConditionalToken"]
    if data.get("RuntimeEnvironmentUpdate") is not None:
        import capo_kinesis_analytics_v2.types.runtime_environment

        out["runtime_environment_update"] = (
            capo_kinesis_analytics_v2.types.runtime_environment.deserialize_aws_json_1_1(
                data["RuntimeEnvironmentUpdate"]
            )
        )
    return out
