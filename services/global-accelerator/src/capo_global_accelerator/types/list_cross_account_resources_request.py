"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#ListCrossAccountResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.aws_account_id
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.max_results


class ListCrossAccountResourcesRequest(TypedDict, closed=True):
    accelerator_arn: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of an accelerator in a cross-account attachment.</p>"""
    resource_owner_aws_account_id: (
        "capo_global_accelerator.types.aws_account_id.AwsAccountId"
    )
    """<p>The account ID of a resource owner in a cross-account attachment.</p>"""
    max_results: NotRequired["capo_global_accelerator.types.max_results.MaxResults"]
    """<p>The number of cross-account resource objects that you want to return with this call. The default value is 10.</p>"""
    next_token: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCrossAccountResourcesRequest) -> dict:
    out: dict = {}
    if "accelerator_arn" in value:
        out["AcceleratorArn"] = value["accelerator_arn"]
    out["ResourceOwnerAwsAccountId"] = value["resource_owner_aws_account_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCrossAccountResourcesRequest:
    out: ListCrossAccountResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("AcceleratorArn") is not None:
        out["accelerator_arn"] = data["AcceleratorArn"]
    if data.get("ResourceOwnerAwsAccountId") is not None:
        out["resource_owner_aws_account_id"] = data["ResourceOwnerAwsAccountId"]
    else:
        out["resource_owner_aws_account_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
