"""Generated from Smithy shape ``com.amazonaws.route53profiles#AssociateResourceToProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53profiles.types.arn
    import capo_route53profiles.types.name
    import capo_route53profiles.types.resource_id
    import capo_route53profiles.types.resource_properties


class AssociateResourceToProfileRequest(TypedDict, closed=True):
    profile_id: "capo_route53profiles.types.resource_id.ResourceId"
    """<p> ID of the Profile. </p>"""
    resource_arn: "capo_route53profiles.types.arn.Arn"
    """<p> Amazon resource number, ARN, of the DNS resource. </p>"""
    name: "capo_route53profiles.types.name.Name"
    """<p> Name for the resource association. </p>"""
    resource_properties: NotRequired[
        "capo_route53profiles.types.resource_properties.ResourceProperties"
    ]
    """<p> If you are adding a DNS Firewall rule group, include also a priority. The priority indicates the processing order for the rule groups, starting with the priority assinged the lowest value. </p> <p>The allowed values for priority are between 100 and 9900.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateResourceToProfileRequest) -> dict:
    out: dict = {}
    out["ProfileId"] = value["profile_id"]
    out["ResourceArn"] = value["resource_arn"]
    out["Name"] = value["name"]
    if "resource_properties" in value:
        out["ResourceProperties"] = value["resource_properties"]
    return out


def deserialize_json(data: dict) -> AssociateResourceToProfileRequest:
    out: AssociateResourceToProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProfileId") is not None:
        out["profile_id"] = data["ProfileId"]
    else:
        out["profile_id"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ResourceProperties") is not None:
        out["resource_properties"] = data["ResourceProperties"]
    return out
