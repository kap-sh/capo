"""Generated from Smithy shape ``com.amazonaws.timestreamquery#QuerySpatialCoverageMax``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name
    import capo_timestream_query.types.double
    import capo_timestream_query.types.partition_key_list


class QuerySpatialCoverageMax(TypedDict, closed=True):
    value: "capo_timestream_query.types.double.Double"
    """<p>The maximum ratio of spatial coverage.</p>"""
    table_arn: NotRequired[
        "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the table with the most sub-optimal spatial pruning.</p>"""
    partition_key: NotRequired[
        "capo_timestream_query.types.partition_key_list.PartitionKeyList"
    ]
    """<p>The partition key used for partitioning, which can be a default <code>measure_name</code> or a <a href="https://docs.aws.amazon.com/timestream/latest/developerguide/customer-defined-partition-keys.html">customer defined partition key</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QuerySpatialCoverageMax) -> dict:
    out: dict = {}
    out["Value"] = (
        "NaN"
        if value.get("value", 0) != value.get("value", 0)
        else "Infinity"
        if value.get("value", 0) == float("inf")
        else "-Infinity"
        if value.get("value", 0) == float("-inf")
        else value.get("value", 0)
    )
    if "table_arn" in value:
        out["TableArn"] = value["table_arn"]
    if "partition_key" in value:
        import capo_timestream_query.types.partition_key_list

        out["PartitionKey"] = (
            capo_timestream_query.types.partition_key_list.serialize_aws_json_1_0(
                value["partition_key"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> QuerySpatialCoverageMax:
    out: QuerySpatialCoverageMax = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    else:
        out["value"] = 0
    if data.get("TableArn") is not None:
        out["table_arn"] = data["TableArn"]
    if data.get("PartitionKey") is not None:
        import capo_timestream_query.types.partition_key_list

        out["partition_key"] = (
            capo_timestream_query.types.partition_key_list.deserialize_aws_json_1_0(
                data["PartitionKey"]
            )
        )
    return out
