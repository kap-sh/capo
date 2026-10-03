"""Generated from Smithy shape ``com.amazonaws.wafv2#ListResourcesForWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.resource_type


class ListResourcesForWebACLRequest(TypedDict, closed=True):
    web_acl_arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL.</p>"""
    resource_type: NotRequired["capo_wafv2.types.resource_type.ResourceType"]
    """<p>Retrieves the web ACLs that are used by the specified resource type. </p> <p>For Amazon CloudFront, don't use this call. Instead, use the CloudFront call <code>ListDistributionsByWebACLId</code>. For information, see <a href="https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_ListDistributionsByWebACLId.html">ListDistributionsByWebACLId</a> in the <i>Amazon CloudFront API Reference</i>. </p> <note> <p>If you don't provide a resource type, the call uses the resource type <code>APPLICATION_LOAD_BALANCER</code>. </p> </note> <p>Default: <code>APPLICATION_LOAD_BALANCER</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesForWebACLRequest) -> dict:
    out: dict = {}
    out["WebACLArn"] = value["web_acl_arn"]
    if "resource_type" in value:
        import capo_wafv2.types.resource_type

        out["ResourceType"] = capo_wafv2.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesForWebACLRequest:
    out: ListResourcesForWebACLRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebACLArn") is not None:
        out["web_acl_arn"] = data["WebACLArn"]
    else:
        raise DeserializationError("ListResourcesForWebACLRequest.web_acl_arn required")
    if data.get("ResourceType") is not None:
        import capo_wafv2.types.resource_type

        out["resource_type"] = capo_wafv2.types.resource_type.deserialize_aws_json_1_1(
            data["ResourceType"]
        )
    return out
