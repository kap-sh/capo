"""Generated from Smithy shape ``com.amazonaws.shield#ListResourcesInProtectionGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.resource_arn_list
    import capo_shield.types.token


class ListResourcesInProtectionGroupResponse(TypedDict, closed=True):
    resource_arns: "capo_shield.types.resource_arn_list.ResourceArnList"
    """<p>The Amazon Resource Names (ARNs) of the resources that are included in the protection group.</p>"""
    next_token: NotRequired["capo_shield.types.token.Token"]
    """<p>When you request a list of objects from Shield Advanced, if the response does not include all of the remaining available objects, Shield Advanced includes a <code>NextToken</code> value in the response. You can retrieve the next batch of objects by requesting the list again and providing the token that was returned by the prior call in your request. </p> <p>You can indicate the maximum number of objects that you want Shield Advanced to return for a single call with the <code>MaxResults</code> setting. Shield Advanced will not return more than <code>MaxResults</code> objects, but may return fewer, even if more objects are still available.</p> <p>Whenever more objects remain that Shield Advanced has not yet returned to you, the response will include a <code>NextToken</code> value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesInProtectionGroupResponse) -> dict:
    out: dict = {}
    import capo_shield.types.resource_arn_list

    out["ResourceArns"] = capo_shield.types.resource_arn_list.serialize_aws_json_1_1(
        value["resource_arns"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesInProtectionGroupResponse:
    out: ListResourcesInProtectionGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArns") is not None:
        import capo_shield.types.resource_arn_list

        out["resource_arns"] = (
            capo_shield.types.resource_arn_list.deserialize_aws_json_1_1(
                data["ResourceArns"]
            )
        )
    else:
        out["resource_arns"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
