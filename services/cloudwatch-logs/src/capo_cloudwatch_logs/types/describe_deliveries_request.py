"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDeliveriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_source_names
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.next_token


class DescribeDeliveriesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>Optionally specify the maximum number of deliveries to return in the response.</p>"""
    delivery_source_names: NotRequired[
        "capo_cloudwatch_logs.types.delivery_source_names.DeliverySourceNames"
    ]
    """<p>An array of delivery source names that filters the results to deliveries associated with any specified delivery source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveriesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "delivery_source_names" in value:
        import capo_cloudwatch_logs.types.delivery_source_names

        out["deliverySourceNames"] = (
            capo_cloudwatch_logs.types.delivery_source_names.serialize_aws_json_1_1(
                value["delivery_source_names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveriesRequest:
    out: DescribeDeliveriesRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("deliverySourceNames") is not None:
        import capo_cloudwatch_logs.types.delivery_source_names

        out["delivery_source_names"] = (
            capo_cloudwatch_logs.types.delivery_source_names.deserialize_aws_json_1_1(
                data["deliverySourceNames"]
            )
        )
    return out
