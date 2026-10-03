"""Generated from Smithy shape ``com.amazonaws.kinesis#EnhancedMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.metrics_name_list


class EnhancedMetrics(TypedDict, closed=True):
    shard_level_metrics: NotRequired[
        "capo_kinesis.types.metrics_name_list.MetricsNameList"
    ]
    """<p>List of shard-level metrics.</p> <p>The following are the valid shard-level metrics. The value "<code>ALL</code>" enhances every metric.</p> <ul> <li> <p> <code>IncomingBytes</code> </p> </li> <li> <p> <code>IncomingRecords</code> </p> </li> <li> <p> <code>OutgoingBytes</code> </p> </li> <li> <p> <code>OutgoingRecords</code> </p> </li> <li> <p> <code>WriteProvisionedThroughputExceeded</code> </p> </li> <li> <p> <code>ReadProvisionedThroughputExceeded</code> </p> </li> <li> <p> <code>IteratorAgeMilliseconds</code> </p> </li> <li> <p> <code>ALL</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/kinesis/latest/dev/monitoring-with-cloudwatch.html">Monitoring the Amazon Kinesis Data Streams Service with Amazon CloudWatch</a> in the <i>Amazon Kinesis Data Streams Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnhancedMetrics) -> dict:
    out: dict = {}
    if "shard_level_metrics" in value:
        import capo_kinesis.types.metrics_name_list

        out["ShardLevelMetrics"] = (
            capo_kinesis.types.metrics_name_list.serialize_aws_json_1_1(
                value["shard_level_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnhancedMetrics:
    out: EnhancedMetrics = {}  # type: ignore[typeddict-item]
    if data.get("ShardLevelMetrics") is not None:
        import capo_kinesis.types.metrics_name_list

        out["shard_level_metrics"] = (
            capo_kinesis.types.metrics_name_list.deserialize_aws_json_1_1(
                data["ShardLevelMetrics"]
            )
        )
    return out
