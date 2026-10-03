"""Generated from Smithy shape ``com.amazonaws.ec2#SpotPlacement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.placement_group_name
    import capo_ec2.types.string
    import capo_ec2.types.tenancy


class SpotPlacement(TypedDict, closed=True):
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone. For example, <code>us-east-2a</code>.</p> <p>[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, "<code>us-east-2a</code>, <code>us-east-2b</code>".</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""
    group_name: NotRequired["capo_ec2.types.placement_group_name.PlacementGroupName"]
    """<p>The name of the placement group.</p>"""
    tenancy: NotRequired["capo_ec2.types.tenancy.Tenancy"]
    """<p>The tenancy of the instance (if the instance is running in a VPC). An instance with a tenancy of <code>dedicated</code> runs on single-tenant hardware. The <code>host</code> tenancy is not supported for Spot Instances.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone. For example, <code>use2-az1</code>.</p> <p>[Spot Fleet only] To specify multiple Availability Zones, separate them using commas; for example, "<code>use2-az1</code>, <code>use2-bz1</code>".</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified in the request, but not both.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotPlacement, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "group_name" in value:
        pairs.append((f"{key_prefix}GroupName", str(value["group_name"])))
    if "tenancy" in value:
        import capo_ec2.types.tenancy

        capo_ec2.types.tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{key_prefix}Tenancy"
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )


def deserialize_ec2_query(el: Element) -> SpotPlacement:
    out: SpotPlacement = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_group_name = el.find("groupName")
    if child_group_name is not None:
        out["group_name"] = str(child_group_name.text or "")
    child_tenancy = el.find("tenancy")
    if child_tenancy is not None:
        import capo_ec2.types.tenancy

        out["tenancy"] = capo_ec2.types.tenancy.deserialize_ec2_query(child_tenancy)
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    return out
