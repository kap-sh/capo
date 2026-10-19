"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DescribeScheduledQueryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_timestream_query.types.amazon_resource_name


class DescribeScheduledQueryRequest(TypedDict, closed=True):
    scheduled_query_arn: (
        "capo_timestream_query.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the scheduled query.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeScheduledQueryRequest) -> dict:
    out: dict = {}
    out["ScheduledQueryArn"] = value["scheduled_query_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeScheduledQueryRequest:
    out: DescribeScheduledQueryRequest = {}  # type: ignore[typeddict-item]
    if data.get("ScheduledQueryArn") is not None:
        out["scheduled_query_arn"] = data["ScheduledQueryArn"]
    else:
        out["scheduled_query_arn"] = ""
    return out
