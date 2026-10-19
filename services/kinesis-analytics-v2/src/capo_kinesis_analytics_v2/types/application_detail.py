"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_configuration_description
    import capo_kinesis_analytics_v2.types.application_description
    import capo_kinesis_analytics_v2.types.application_maintenance_configuration_description
    import capo_kinesis_analytics_v2.types.application_mode
    import capo_kinesis_analytics_v2.types.application_name
    import capo_kinesis_analytics_v2.types.application_status
    import capo_kinesis_analytics_v2.types.application_version_id
    import capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions
    import capo_kinesis_analytics_v2.types.conditional_token
    import capo_kinesis_analytics_v2.types.resource_arn
    import capo_kinesis_analytics_v2.types.role_arn
    import capo_kinesis_analytics_v2.types.runtime_environment
    import capo_kinesis_analytics_v2.types.timestamp


class ApplicationDetail(TypedDict, closed=True):
    application_arn: "capo_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The ARN of the application.</p>"""
    application_description: NotRequired[
        "capo_kinesis_analytics_v2.types.application_description.ApplicationDescription"
    ]
    """<p>The description of the application.</p>"""
    application_name: "capo_kinesis_analytics_v2.types.application_name.ApplicationName"
    """<p>The name of the application.</p>"""
    runtime_environment: (
        "capo_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment"
    )
    """<p>The runtime environment for the application.</p>"""
    service_execution_role: NotRequired[
        "capo_kinesis_analytics_v2.types.role_arn.RoleARN"
    ]
    """<p>Specifies the IAM role that the application uses to access external resources.</p>"""
    application_status: (
        "capo_kinesis_analytics_v2.types.application_status.ApplicationStatus"
    )
    """<p>The status of the application.</p>"""
    application_version_id: (
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>Provides the current application version. Managed Service for Apache Flink updates the <code>ApplicationVersionId</code> each time you update the application.</p>"""
    create_timestamp: NotRequired["capo_kinesis_analytics_v2.types.timestamp.Timestamp"]
    """<p>The current timestamp when the application was created.</p>"""
    last_update_timestamp: NotRequired[
        "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    ]
    """<p>The current timestamp when the application was last updated.</p>"""
    application_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.application_configuration_description.ApplicationConfigurationDescription"
    ]
    """<p>Describes details about the application code and starting parameters for a Managed Service for Apache Flink application.</p>"""
    cloud_watch_logging_option_descriptions: NotRequired[
        "capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.CloudWatchLoggingOptionDescriptions"
    ]
    """<p>Describes the application Amazon CloudWatch logging options.</p>"""
    application_maintenance_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.application_maintenance_configuration_description.ApplicationMaintenanceConfigurationDescription"
    ]
    """<p>The details of the maintenance configuration for the application.</p>"""
    application_version_updated_from: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The previous application version before the latest application update. <a>RollbackApplication</a> reverts the application to this version.</p>"""
    application_version_rolled_back_from: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>If you reverted the application using <a>RollbackApplication</a>, the application version when <code>RollbackApplication</code> was called.</p>"""
    application_version_create_timestamp: NotRequired[
        "capo_kinesis_analytics_v2.types.timestamp.Timestamp"
    ]
    """<p>The timestamp that indicates when the application version was created.</p>"""
    conditional_token: NotRequired[
        "capo_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
    ]
    """<p>A value you use to implement strong concurrency for application updates.</p>"""
    application_version_rolled_back_to: NotRequired[
        "capo_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The version to which you want to roll back the application.</p>"""
    application_mode: NotRequired[
        "capo_kinesis_analytics_v2.types.application_mode.ApplicationMode"
    ]
    """<p>To create a Managed Service for Apache Flink Studio notebook, you must set the mode to <code>INTERACTIVE</code>. However, for a Managed Service for Apache Flink application, the mode is optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationDetail) -> dict:
    out: dict = {}
    out["ApplicationARN"] = value["application_arn"]
    if "application_description" in value:
        out["ApplicationDescription"] = value["application_description"]
    out["ApplicationName"] = value["application_name"]
    import capo_kinesis_analytics_v2.types.runtime_environment

    out["RuntimeEnvironment"] = (
        capo_kinesis_analytics_v2.types.runtime_environment.serialize_aws_json_1_1(
            value["runtime_environment"]
        )
    )
    if "service_execution_role" in value:
        out["ServiceExecutionRole"] = value["service_execution_role"]
    import capo_kinesis_analytics_v2.types.application_status

    out["ApplicationStatus"] = (
        capo_kinesis_analytics_v2.types.application_status.serialize_aws_json_1_1(
            value["application_status"]
        )
    )
    out["ApplicationVersionId"] = value["application_version_id"]
    if "create_timestamp" in value:
        import capo_kinesis_analytics_v2.types.timestamp

        out["CreateTimestamp"] = (
            capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["create_timestamp"]
            )
        )
    if "last_update_timestamp" in value:
        import capo_kinesis_analytics_v2.types.timestamp

        out["LastUpdateTimestamp"] = (
            capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["last_update_timestamp"]
            )
        )
    if "application_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.application_configuration_description

        out["ApplicationConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.application_configuration_description.serialize_aws_json_1_1(
                value["application_configuration_description"]
            )
        )
    if "cloud_watch_logging_option_descriptions" in value:
        import capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions

        out["CloudWatchLoggingOptionDescriptions"] = (
            capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.serialize_aws_json_1_1(
                value["cloud_watch_logging_option_descriptions"]
            )
        )
    if "application_maintenance_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.application_maintenance_configuration_description

        out["ApplicationMaintenanceConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.application_maintenance_configuration_description.serialize_aws_json_1_1(
                value["application_maintenance_configuration_description"]
            )
        )
    if "application_version_updated_from" in value:
        out["ApplicationVersionUpdatedFrom"] = value["application_version_updated_from"]
    if "application_version_rolled_back_from" in value:
        out["ApplicationVersionRolledBackFrom"] = value[
            "application_version_rolled_back_from"
        ]
    if "application_version_create_timestamp" in value:
        import capo_kinesis_analytics_v2.types.timestamp

        out["ApplicationVersionCreateTimestamp"] = (
            capo_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["application_version_create_timestamp"]
            )
        )
    if "conditional_token" in value:
        out["ConditionalToken"] = value["conditional_token"]
    if "application_version_rolled_back_to" in value:
        out["ApplicationVersionRolledBackTo"] = value[
            "application_version_rolled_back_to"
        ]
    if "application_mode" in value:
        import capo_kinesis_analytics_v2.types.application_mode

        out["ApplicationMode"] = (
            capo_kinesis_analytics_v2.types.application_mode.serialize_aws_json_1_1(
                value["application_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationDetail:
    out: ApplicationDetail = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationARN") is not None:
        out["application_arn"] = data["ApplicationARN"]
    else:
        out["application_arn"] = ""
    if data.get("ApplicationDescription") is not None:
        out["application_description"] = data["ApplicationDescription"]
    if data.get("ApplicationName") is not None:
        out["application_name"] = data["ApplicationName"]
    else:
        out["application_name"] = ""
    if data.get("RuntimeEnvironment") is not None:
        import capo_kinesis_analytics_v2.types.runtime_environment

        out["runtime_environment"] = (
            capo_kinesis_analytics_v2.types.runtime_environment.deserialize_aws_json_1_1(
                data["RuntimeEnvironment"]
            )
        )
    else:
        import typing

        out["runtime_environment"] = typing.cast(
            "capo_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment", ""
        )
    if data.get("ServiceExecutionRole") is not None:
        out["service_execution_role"] = data["ServiceExecutionRole"]
    if data.get("ApplicationStatus") is not None:
        import capo_kinesis_analytics_v2.types.application_status

        out["application_status"] = (
            capo_kinesis_analytics_v2.types.application_status.deserialize_aws_json_1_1(
                data["ApplicationStatus"]
            )
        )
    else:
        import typing

        out["application_status"] = typing.cast(
            "capo_kinesis_analytics_v2.types.application_status.ApplicationStatus", ""
        )
    if data.get("ApplicationVersionId") is not None:
        out["application_version_id"] = data["ApplicationVersionId"]
    else:
        out["application_version_id"] = 0
    if data.get("CreateTimestamp") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["create_timestamp"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["CreateTimestamp"]
            )
        )
    if data.get("LastUpdateTimestamp") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["last_update_timestamp"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdateTimestamp"]
            )
        )
    if data.get("ApplicationConfigurationDescription") is not None:
        import capo_kinesis_analytics_v2.types.application_configuration_description

        out["application_configuration_description"] = (
            capo_kinesis_analytics_v2.types.application_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationConfigurationDescription"]
            )
        )
    if data.get("CloudWatchLoggingOptionDescriptions") is not None:
        import capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions

        out["cloud_watch_logging_option_descriptions"] = (
            capo_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptionDescriptions"]
            )
        )
    if data.get("ApplicationMaintenanceConfigurationDescription") is not None:
        import capo_kinesis_analytics_v2.types.application_maintenance_configuration_description

        out["application_maintenance_configuration_description"] = (
            capo_kinesis_analytics_v2.types.application_maintenance_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationMaintenanceConfigurationDescription"]
            )
        )
    if data.get("ApplicationVersionUpdatedFrom") is not None:
        out["application_version_updated_from"] = data["ApplicationVersionUpdatedFrom"]
    if data.get("ApplicationVersionRolledBackFrom") is not None:
        out["application_version_rolled_back_from"] = data[
            "ApplicationVersionRolledBackFrom"
        ]
    if data.get("ApplicationVersionCreateTimestamp") is not None:
        import capo_kinesis_analytics_v2.types.timestamp

        out["application_version_create_timestamp"] = (
            capo_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["ApplicationVersionCreateTimestamp"]
            )
        )
    if data.get("ConditionalToken") is not None:
        out["conditional_token"] = data["ConditionalToken"]
    if data.get("ApplicationVersionRolledBackTo") is not None:
        out["application_version_rolled_back_to"] = data[
            "ApplicationVersionRolledBackTo"
        ]
    if data.get("ApplicationMode") is not None:
        import capo_kinesis_analytics_v2.types.application_mode

        out["application_mode"] = (
            capo_kinesis_analytics_v2.types.application_mode.deserialize_aws_json_1_1(
                data["ApplicationMode"]
            )
        )
    return out
