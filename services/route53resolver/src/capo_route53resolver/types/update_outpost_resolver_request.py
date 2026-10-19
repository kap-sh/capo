"""Generated from Smithy shape ``com.amazonaws.route53resolver#UpdateOutpostResolverRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.instance_count
    import capo_route53resolver.types.outpost_instance_type
    import capo_route53resolver.types.outpost_resolver_name
    import capo_route53resolver.types.resource_id


class UpdateOutpostResolverRequest(TypedDict, closed=True):
    id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>A unique string that identifies Resolver on an Outpost.</p>"""
    name: NotRequired[
        "capo_route53resolver.types.outpost_resolver_name.OutpostResolverName"
    ]
    """<p>Name of the Resolver on the Outpost.</p>"""
    instance_count: NotRequired[
        "capo_route53resolver.types.instance_count.InstanceCount"
    ]
    """<p>The Amazon EC2 instance count for a Resolver on the Outpost.</p>"""
    preferred_instance_type: NotRequired[
        "capo_route53resolver.types.outpost_instance_type.OutpostInstanceType"
    ]
    """<p> Amazon EC2 instance type. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateOutpostResolverRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    if "preferred_instance_type" in value:
        out["PreferredInstanceType"] = value["preferred_instance_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateOutpostResolverRequest:
    out: UpdateOutpostResolverRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("InstanceCount") is not None:
        out["instance_count"] = data["InstanceCount"]
    if data.get("PreferredInstanceType") is not None:
        out["preferred_instance_type"] = data["PreferredInstanceType"]
    return out
