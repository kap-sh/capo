"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDeliveryDestinationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.delivery_destination_names
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.next_token


class DescribeDeliveryDestinationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>Optionally specify the maximum number of delivery destinations to return in the response.</p>"""
    names: NotRequired[
        "capo_cloudwatch_logs.types.delivery_destination_names.DeliveryDestinationNames"
    ]
    """<p>An array of delivery destination names that filters the results to delivery destinations with any specified name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliveryDestinationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "names" in value:
        import capo_cloudwatch_logs.types.delivery_destination_names

        out["names"] = (
            capo_cloudwatch_logs.types.delivery_destination_names.serialize_aws_json_1_1(
                value["names"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliveryDestinationsRequest:
    out: DescribeDeliveryDestinationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("names") is not None:
        import capo_cloudwatch_logs.types.delivery_destination_names

        out["names"] = (
            capo_cloudwatch_logs.types.delivery_destination_names.deserialize_aws_json_1_1(
                data["names"]
            )
        )
    return out
