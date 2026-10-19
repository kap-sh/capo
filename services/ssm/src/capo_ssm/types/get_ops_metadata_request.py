"""Generated from Smithy shape ``com.amazonaws.ssm#GetOpsMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.get_ops_metadata_max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.ops_metadata_arn


class GetOpsMetadataRequest(TypedDict, closed=True):
    ops_metadata_arn: "capo_ssm.types.ops_metadata_arn.OpsMetadataArn"
    """<p>The Amazon Resource Name (ARN) of an OpsMetadata Object to view.</p>"""
    max_results: NotRequired[
        "capo_ssm.types.get_ops_metadata_max_results.GetOpsMetadataMaxResults"
    ]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>A token to start the list. Use this token to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpsMetadataRequest) -> dict:
    out: dict = {}
    out["OpsMetadataArn"] = value["ops_metadata_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpsMetadataRequest:
    out: GetOpsMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("OpsMetadataArn") is not None:
        out["ops_metadata_arn"] = data["OpsMetadataArn"]
    else:
        out["ops_metadata_arn"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
