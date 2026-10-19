"""Generated from Smithy shape ``com.amazonaws.shield#CreateProtectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.protection_name
    import capo_shield.types.resource_arn
    import capo_shield.types.tag_list


class CreateProtectionRequest(TypedDict, closed=True):
    name: "capo_shield.types.protection_name.ProtectionName"
    """<p>Friendly name for the <code>Protection</code> you are creating.</p>"""
    resource_arn: "capo_shield.types.resource_arn.ResourceArn"
    """<p>The ARN (Amazon Resource Name) of the resource to be protected.</p> <p>The ARN should be in one of the following formats:</p> <ul> <li> <p>For an Application Load Balancer: <code>arn:aws:elasticloadbalancing:<i>region</i>:<i>account-id</i>:loadbalancer/app/<i>load-balancer-name</i>/<i>load-balancer-id</i> </code> </p> </li> <li> <p>For an Elastic Load Balancer (Classic Load Balancer): <code>arn:aws:elasticloadbalancing:<i>region</i>:<i>account-id</i>:loadbalancer/<i>load-balancer-name</i> </code> </p> </li> <li> <p>For an Amazon CloudFront distribution: <code>arn:aws:cloudfront::<i>account-id</i>:distribution/<i>distribution-id</i> </code> </p> </li> <li> <p>For an Global Accelerator standard accelerator: <code>arn:aws:globalaccelerator::<i>account-id</i>:accelerator/<i>accelerator-id</i> </code> </p> </li> <li> <p>For Amazon Route 53: <code>arn:aws:route53:::hostedzone/<i>hosted-zone-id</i> </code> </p> </li> <li> <p>For an Elastic IP address: <code>arn:aws:ec2:<i>region</i>:<i>account-id</i>:eip-allocation/<i>allocation-id</i> </code> </p> </li> </ul>"""
    tags: NotRequired["capo_shield.types.tag_list.TagList"]
    """<p>One or more tag key-value pairs for the <a>Protection</a> object that is created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProtectionRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ResourceArn"] = value["resource_arn"]
    if "tags" in value:
        import capo_shield.types.tag_list

        out["Tags"] = capo_shield.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProtectionRequest:
    out: CreateProtectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_shield.types.tag_list

        out["tags"] = capo_shield.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
