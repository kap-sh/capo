"""Generated from Smithy shape ``com.amazonaws.wafregional#AssociateWebACLRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.resource_arn
    import capo_waf_regional.types.resource_id


class AssociateWebACLRequest(TypedDict, closed=True):
    web_acl_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>A unique identifier (ID) for the web ACL. </p>"""
    resource_arn: "capo_waf_regional.types.resource_arn.ResourceArn"
    """<p>The ARN (Amazon Resource Name) of the resource to be protected, either an application load balancer or Amazon API Gateway stage. </p> <p>The ARN should be in one of the following formats:</p> <ul> <li> <p>For an Application Load Balancer: <code>arn:aws:elasticloadbalancing:<i>region</i>:<i>account-id</i>:loadbalancer/app/<i>load-balancer-name</i>/<i>load-balancer-id</i> </code> </p> </li> <li> <p>For an Amazon API Gateway stage: <code>arn:aws:apigateway:<i>region</i>::/restapis/<i>api-id</i>/stages/<i>stage-name</i> </code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateWebACLRequest) -> dict:
    out: dict = {}
    out["WebACLId"] = value["web_acl_id"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateWebACLRequest:
    out: AssociateWebACLRequest = {}  # type: ignore[typeddict-item]
    if data.get("WebACLId") is not None:
        out["web_acl_id"] = data["WebACLId"]
    else:
        out["web_acl_id"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
