"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#FlinkApplicationConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.checkpoint_configuration_description
    import capo_kinesis_analytics_v2.types.job_plan_description
    import capo_kinesis_analytics_v2.types.monitoring_configuration_description
    import capo_kinesis_analytics_v2.types.parallelism_configuration_description


class FlinkApplicationConfigurationDescription(TypedDict, closed=True):
    checkpoint_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.checkpoint_configuration_description.CheckpointConfigurationDescription"
    ]
    """<p>Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.</p>"""
    monitoring_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.monitoring_configuration_description.MonitoringConfigurationDescription"
    ]
    """<p>Describes configuration parameters for Amazon CloudWatch logging for an application.</p>"""
    parallelism_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.parallelism_configuration_description.ParallelismConfigurationDescription"
    ]
    """<p>Describes parameters for how an application executes multiple tasks simultaneously.</p>"""
    job_plan_description: NotRequired[
        "capo_kinesis_analytics_v2.types.job_plan_description.JobPlanDescription"
    ]
    """<p>The job plan for an application. For more information about the job plan, see <a href="https://nightlies.apache.org/flink/flink-docs-release-2.3/internals/job_scheduling.html">Jobs and Scheduling</a> in the <a href="https://nightlies.apache.org/flink/flink-docs-release-2.3/">Apache Flink Documentation</a>. To retrieve the job plan for the application, use the <a>DescribeApplicationRequest$IncludeAdditionalDetails</a> parameter of the <a>DescribeApplication</a> operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlinkApplicationConfigurationDescription) -> dict:
    out: dict = {}
    if "checkpoint_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.checkpoint_configuration_description

        out["CheckpointConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.checkpoint_configuration_description.serialize_aws_json_1_1(
                value["checkpoint_configuration_description"]
            )
        )
    if "monitoring_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.monitoring_configuration_description

        out["MonitoringConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.monitoring_configuration_description.serialize_aws_json_1_1(
                value["monitoring_configuration_description"]
            )
        )
    if "parallelism_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.parallelism_configuration_description

        out["ParallelismConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.parallelism_configuration_description.serialize_aws_json_1_1(
                value["parallelism_configuration_description"]
            )
        )
    if "job_plan_description" in value:
        out["JobPlanDescription"] = value["job_plan_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FlinkApplicationConfigurationDescription:
    out: FlinkApplicationConfigurationDescription = {}  # type: ignore[typeddict-item]
    if data.get("CheckpointConfigurationDescription") is not None:
        import capo_kinesis_analytics_v2.types.checkpoint_configuration_description

        out["checkpoint_configuration_description"] = (
            capo_kinesis_analytics_v2.types.checkpoint_configuration_description.deserialize_aws_json_1_1(
                data["CheckpointConfigurationDescription"]
            )
        )
    if data.get("MonitoringConfigurationDescription") is not None:
        import capo_kinesis_analytics_v2.types.monitoring_configuration_description

        out["monitoring_configuration_description"] = (
            capo_kinesis_analytics_v2.types.monitoring_configuration_description.deserialize_aws_json_1_1(
                data["MonitoringConfigurationDescription"]
            )
        )
    if data.get("ParallelismConfigurationDescription") is not None:
        import capo_kinesis_analytics_v2.types.parallelism_configuration_description

        out["parallelism_configuration_description"] = (
            capo_kinesis_analytics_v2.types.parallelism_configuration_description.deserialize_aws_json_1_1(
                data["ParallelismConfigurationDescription"]
            )
        )
    if data.get("JobPlanDescription") is not None:
        out["job_plan_description"] = data["JobPlanDescription"]
    return out
