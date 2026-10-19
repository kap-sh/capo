"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DescribeIndexPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.describe_index_policies_log_group_identifiers
    import capo_cloudwatch_logs.types.next_token


class DescribeIndexPoliciesRequest(TypedDict, closed=True):
    log_group_identifiers: "capo_cloudwatch_logs.types.describe_index_policies_log_group_identifiers.DescribeIndexPoliciesLogGroupIdentifiers"
    """<p>An array containing the name or ARN of the log group that you want to retrieve field index policies for.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeIndexPoliciesRequest) -> dict:
    out: dict = {}
    import capo_cloudwatch_logs.types.describe_index_policies_log_group_identifiers

    out["logGroupIdentifiers"] = (
        capo_cloudwatch_logs.types.describe_index_policies_log_group_identifiers.serialize_aws_json_1_1(
            value["log_group_identifiers"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeIndexPoliciesRequest:
    out: DescribeIndexPoliciesRequest = {}  # type: ignore[typeddict-item]
    if data.get("logGroupIdentifiers") is not None:
        import capo_cloudwatch_logs.types.describe_index_policies_log_group_identifiers

        out["log_group_identifiers"] = (
            capo_cloudwatch_logs.types.describe_index_policies_log_group_identifiers.deserialize_aws_json_1_1(
                data["logGroupIdentifiers"]
            )
        )
    else:
        out["log_group_identifiers"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
