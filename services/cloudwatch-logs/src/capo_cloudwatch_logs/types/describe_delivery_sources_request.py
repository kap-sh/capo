"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeDeliverySourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.filter_resource_arns
    import capo_cloudwatch_logs.types.next_token


class DescribeDeliverySourcesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]
    limit: NotRequired["capo_cloudwatch_logs.types.describe_limit.DescribeLimit"]
    """<p>Optionally specify the maximum number of delivery sources to return in the response.</p>"""
    resource_arns: NotRequired[
        "capo_cloudwatch_logs.types.filter_resource_arns.FilterResourceArns"
    ]
    """<p>An array of Amazon Resource Names (ARNs) that filters the results to delivery sources associated with any specified ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDeliverySourcesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "resource_arns" in value:
        import capo_cloudwatch_logs.types.filter_resource_arns

        out["resourceArns"] = (
            capo_cloudwatch_logs.types.filter_resource_arns.serialize_aws_json_1_1(
                value["resource_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDeliverySourcesRequest:
    out: DescribeDeliverySourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("limit") is not None:
        out["limit"] = data["limit"]
    if data.get("resourceArns") is not None:
        import capo_cloudwatch_logs.types.filter_resource_arns

        out["resource_arns"] = (
            capo_cloudwatch_logs.types.filter_resource_arns.deserialize_aws_json_1_1(
                data["resourceArns"]
            )
        )
    return out
