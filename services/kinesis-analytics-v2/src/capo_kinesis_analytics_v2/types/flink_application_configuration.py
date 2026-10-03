"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#FlinkApplicationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.checkpoint_configuration
    import capo_kinesis_analytics_v2.types.monitoring_configuration
    import capo_kinesis_analytics_v2.types.parallelism_configuration


class FlinkApplicationConfiguration(TypedDict, closed=True):
    checkpoint_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.checkpoint_configuration.CheckpointConfiguration"
    ]
    """<p>Describes an application's checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance. For more information, see <a href="https://nightlies.apache.org/flink/flink-docs-release-2.3/docs/dev/datastream/fault-tolerance/checkpointing/#enabling-and-configuring-checkpointing"> Checkpoints for Fault Tolerance</a> in the <a href="https://nightlies.apache.org/flink/flink-docs-release-2.3/">Apache Flink Documentation</a>. </p>"""
    monitoring_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>Describes configuration parameters for Amazon CloudWatch logging for an application.</p>"""
    parallelism_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.parallelism_configuration.ParallelismConfiguration"
    ]
    """<p>Describes parameters for how an application executes multiple tasks simultaneously.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlinkApplicationConfiguration) -> dict:
    out: dict = {}
    if "checkpoint_configuration" in value:
        import capo_kinesis_analytics_v2.types.checkpoint_configuration

        out["CheckpointConfiguration"] = (
            capo_kinesis_analytics_v2.types.checkpoint_configuration.serialize_aws_json_1_1(
                value["checkpoint_configuration"]
            )
        )
    if "monitoring_configuration" in value:
        import capo_kinesis_analytics_v2.types.monitoring_configuration

        out["MonitoringConfiguration"] = (
            capo_kinesis_analytics_v2.types.monitoring_configuration.serialize_aws_json_1_1(
                value["monitoring_configuration"]
            )
        )
    if "parallelism_configuration" in value:
        import capo_kinesis_analytics_v2.types.parallelism_configuration

        out["ParallelismConfiguration"] = (
            capo_kinesis_analytics_v2.types.parallelism_configuration.serialize_aws_json_1_1(
                value["parallelism_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FlinkApplicationConfiguration:
    out: FlinkApplicationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CheckpointConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.checkpoint_configuration

        out["checkpoint_configuration"] = (
            capo_kinesis_analytics_v2.types.checkpoint_configuration.deserialize_aws_json_1_1(
                data["CheckpointConfiguration"]
            )
        )
    if data.get("MonitoringConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.monitoring_configuration

        out["monitoring_configuration"] = (
            capo_kinesis_analytics_v2.types.monitoring_configuration.deserialize_aws_json_1_1(
                data["MonitoringConfiguration"]
            )
        )
    if data.get("ParallelismConfiguration") is not None:
        import capo_kinesis_analytics_v2.types.parallelism_configuration

        out["parallelism_configuration"] = (
            capo_kinesis_analytics_v2.types.parallelism_configuration.deserialize_aws_json_1_1(
                data["ParallelismConfiguration"]
            )
        )
    return out
