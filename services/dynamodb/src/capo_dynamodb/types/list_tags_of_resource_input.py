"""Generated from Smithy shape ``com.amazonaws.dynamodb#ListTagsOfResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.next_token_string
    import capo_dynamodb.types.resource_arn_string


class ListTagsOfResourceInput(TypedDict, closed=True):
    resource_arn: "capo_dynamodb.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon DynamoDB resource with tags to be listed. This value is an Amazon Resource Name (ARN).</p>"""
    next_token: NotRequired["capo_dynamodb.types.next_token_string.NextTokenString"]
    """<p>An optional string that, if supplied, must be copied from the output of a previous call to ListTagOfResource. When provided in this manner, this API fetches the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsOfResourceInput) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsOfResourceInput:
    out: ListTagsOfResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
