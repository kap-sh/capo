"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#AssociateHostedZoneInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53globalresolver.types.hosted_zone_id
    import capo_route53globalresolver.types.resource_arn
    import capo_route53globalresolver.types.resource_name


class AssociateHostedZoneInput(TypedDict, closed=True):
    hosted_zone_id: "capo_route53globalresolver.types.hosted_zone_id.HostedZoneId"
    """<p>The ID of the Route 53 private hosted zone to associate with the Route 53 Global Resolver resource.</p>"""
    resource_arn: "capo_route53globalresolver.types.resource_arn.ResourceArn"
    """<p>An Amazon Resource Name (ARN) of the Route 53 Global Resolver the private hosted zone will be associated to.</p>"""
    name: "capo_route53globalresolver.types.resource_name.ResourceName"
    """<p>Name for the private hosted zone association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateHostedZoneInput) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> AssociateHostedZoneInput:
    out: AssociateHostedZoneInput = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
