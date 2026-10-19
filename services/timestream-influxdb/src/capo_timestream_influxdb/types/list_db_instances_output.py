"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ListDbInstancesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_instance_summary_list
    import capo_timestream_influxdb.types.next_token


class ListDbInstancesOutput(TypedDict, closed=True):
    items: (
        "capo_timestream_influxdb.types.db_instance_summary_list.DbInstanceSummaryList"
    )
    """<p>A list of Timestream for InfluxDB DB instance summaries.</p>"""
    next_token: NotRequired["capo_timestream_influxdb.types.next_token.NextToken"]
    """<p>Token from a previous call of the operation. When this value is provided, the service returns results from where the previous response left off.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbInstancesOutput) -> dict:
    out: dict = {}
    import capo_timestream_influxdb.types.db_instance_summary_list

    out["items"] = (
        capo_timestream_influxdb.types.db_instance_summary_list.serialize_aws_json_1_0(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbInstancesOutput:
    out: ListDbInstancesOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_timestream_influxdb.types.db_instance_summary_list

        out["items"] = (
            capo_timestream_influxdb.types.db_instance_summary_list.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
