"""Generated from Smithy shape ``com.amazonaws.shield#ProtectionGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.protected_resource_type
    import capo_shield.types.protection_group_aggregation
    import capo_shield.types.protection_group_id
    import capo_shield.types.protection_group_members
    import capo_shield.types.protection_group_pattern
    import capo_shield.types.resource_arn


class ProtectionGroup(TypedDict, closed=True):
    protection_group_id: "capo_shield.types.protection_group_id.ProtectionGroupId"
    """<p>The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it. </p>"""
    aggregation: (
        "capo_shield.types.protection_group_aggregation.ProtectionGroupAggregation"
    )
    """<p>Defines how Shield combines resource data for the group in order to detect, mitigate, and report events.</p> <ul> <li> <p>Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.</p> </li> <li> <p>Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.</p> </li> <li> <p>Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront distributions and origin resources for CloudFront distributions.</p> </li> </ul>"""
    pattern: "capo_shield.types.protection_group_pattern.ProtectionGroupPattern"
    """<p>The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource ARNs (Amazon Resource Names), or include all resources of a specified resource type.</p>"""
    resource_type: NotRequired[
        "capo_shield.types.protected_resource_type.ProtectedResourceType"
    ]
    """<p>The resource type to include in the protection group. All protected resources of this type are included in the protection group. You must set this when you set <code>Pattern</code> to <code>BY_RESOURCE_TYPE</code> and you must not set it for any other <code>Pattern</code> setting. </p>"""
    members: "capo_shield.types.protection_group_members.ProtectionGroupMembers"
    """<p>The ARNs (Amazon Resource Names) of the resources to include in the protection group. You must set this when you set <code>Pattern</code> to <code>ARBITRARY</code> and you must not set it for any other <code>Pattern</code> setting. </p>"""
    protection_group_arn: NotRequired["capo_shield.types.resource_arn.ResourceArn"]
    """<p>The ARN (Amazon Resource Name) of the protection group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectionGroup) -> dict:
    out: dict = {}
    out["ProtectionGroupId"] = value["protection_group_id"]
    import capo_shield.types.protection_group_aggregation

    out["Aggregation"] = (
        capo_shield.types.protection_group_aggregation.serialize_aws_json_1_1(
            value["aggregation"]
        )
    )
    import capo_shield.types.protection_group_pattern

    out["Pattern"] = capo_shield.types.protection_group_pattern.serialize_aws_json_1_1(
        value["pattern"]
    )
    if "resource_type" in value:
        import capo_shield.types.protected_resource_type

        out["ResourceType"] = (
            capo_shield.types.protected_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    import capo_shield.types.protection_group_members

    out["Members"] = capo_shield.types.protection_group_members.serialize_aws_json_1_1(
        value["members"]
    )
    if "protection_group_arn" in value:
        out["ProtectionGroupArn"] = value["protection_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectionGroup:
    out: ProtectionGroup = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionGroupId") is not None:
        out["protection_group_id"] = data["ProtectionGroupId"]
    else:
        out["protection_group_id"] = ""
    if data.get("Aggregation") is not None:
        import capo_shield.types.protection_group_aggregation

        out["aggregation"] = (
            capo_shield.types.protection_group_aggregation.deserialize_aws_json_1_1(
                data["Aggregation"]
            )
        )
    else:
        import typing

        out["aggregation"] = typing.cast(
            "capo_shield.types.protection_group_aggregation.ProtectionGroupAggregation",
            "",
        )
    if data.get("Pattern") is not None:
        import capo_shield.types.protection_group_pattern

        out["pattern"] = (
            capo_shield.types.protection_group_pattern.deserialize_aws_json_1_1(
                data["Pattern"]
            )
        )
    else:
        import typing

        out["pattern"] = typing.cast(
            "capo_shield.types.protection_group_pattern.ProtectionGroupPattern", ""
        )
    if data.get("ResourceType") is not None:
        import capo_shield.types.protected_resource_type

        out["resource_type"] = (
            capo_shield.types.protected_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if data.get("Members") is not None:
        import capo_shield.types.protection_group_members

        out["members"] = (
            capo_shield.types.protection_group_members.deserialize_aws_json_1_1(
                data["Members"]
            )
        )
    else:
        out["members"] = []
    if data.get("ProtectionGroupArn") is not None:
        out["protection_group_arn"] = data["ProtectionGroupArn"]
    return out
