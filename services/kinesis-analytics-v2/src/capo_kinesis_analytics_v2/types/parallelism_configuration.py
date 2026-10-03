"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ParallelismConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.boolean_object
    import capo_kinesis_analytics_v2.types.configuration_type
    import capo_kinesis_analytics_v2.types.parallelism
    import capo_kinesis_analytics_v2.types.parallelism_per_kpu


class ParallelismConfiguration(TypedDict, closed=True):
    configuration_type: (
        "capo_kinesis_analytics_v2.types.configuration_type.ConfigurationType"
    )
    """<p>Describes whether the application uses the default parallelism for the Managed Service for Apache Flink service. You must set this property to <code>CUSTOM</code> in order to change your application's <code>AutoScalingEnabled</code>, <code>Parallelism</code>, or <code>ParallelismPerKPU</code> properties.</p>"""
    parallelism: NotRequired["capo_kinesis_analytics_v2.types.parallelism.Parallelism"]
    """<p>Describes the initial number of parallel tasks that a Managed Service for Apache Flink application can perform. If <code>AutoScalingEnabled</code> is set to True, Managed Service for Apache Flink increases the <code>CurrentParallelism</code> value in response to application load. The service can increase the <code>CurrentParallelism</code> value up to the maximum parallelism, which is <code>ParalellismPerKPU</code> times the maximum KPUs for the application. The maximum KPUs for an application is 64 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the <code>CurrentParallelism</code> value down to the <code>Parallelism</code> setting.</p>"""
    parallelism_per_kpu: NotRequired[
        "capo_kinesis_analytics_v2.types.parallelism_per_kpu.ParallelismPerKPU"
    ]
    """<p>Describes the number of parallel tasks that a Managed Service for Apache Flink application can perform per Kinesis Processing Unit (KPU) used by the application. For more information about KPUs, see <a href="http://aws.amazon.com/kinesis/data-analytics/pricing/">Amazon Managed Service for Apache Flink Pricing</a>.</p>"""
    auto_scaling_enabled: NotRequired[
        "capo_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    ]
    """<p>Describes whether the Managed Service for Apache Flink service can increase the parallelism of the application in response to increased throughput.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParallelismConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.configuration_type

    out["ConfigurationType"] = (
        capo_kinesis_analytics_v2.types.configuration_type.serialize_aws_json_1_1(
            value["configuration_type"]
        )
    )
    if "parallelism" in value:
        out["Parallelism"] = value["parallelism"]
    if "parallelism_per_kpu" in value:
        out["ParallelismPerKPU"] = value["parallelism_per_kpu"]
    if "auto_scaling_enabled" in value:
        out["AutoScalingEnabled"] = value["auto_scaling_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ParallelismConfiguration:
    out: ParallelismConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationType") is not None:
        import capo_kinesis_analytics_v2.types.configuration_type

        out["configuration_type"] = (
            capo_kinesis_analytics_v2.types.configuration_type.deserialize_aws_json_1_1(
                data["ConfigurationType"]
            )
        )
    else:
        raise DeserializationError(
            "ParallelismConfiguration.configuration_type required"
        )
    if data.get("Parallelism") is not None:
        out["parallelism"] = data["Parallelism"]
    if data.get("ParallelismPerKPU") is not None:
        out["parallelism_per_kpu"] = data["ParallelismPerKPU"]
    if data.get("AutoScalingEnabled") is not None:
        out["auto_scaling_enabled"] = data["AutoScalingEnabled"]
    return out
