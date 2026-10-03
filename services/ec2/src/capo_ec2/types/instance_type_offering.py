"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeOffering``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_type
    import capo_ec2.types.location
    import capo_ec2.types.location_type


class InstanceTypeOffering(TypedDict, closed=True):
    instance_type: NotRequired["capo_ec2.types.instance_type.InstanceType"]
    """<p>The instance type. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">Instance types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    location_type: NotRequired["capo_ec2.types.location_type.LocationType"]
    """<p>The location type.</p>"""
    location: NotRequired["capo_ec2.types.location.Location"]
    """<p>The identifier for the location. This depends on the location type. For example, if the location type is <code>region</code>, the location is the Region code (for example, <code>us-east-2</code>.)</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceTypeOffering, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_type" in value:
        import capo_ec2.types.instance_type

        capo_ec2.types.instance_type.serialize_ec2_query(
            value["instance_type"], pairs, f"{key_prefix}InstanceType"
        )
    if "location_type" in value:
        import capo_ec2.types.location_type

        capo_ec2.types.location_type.serialize_ec2_query(
            value["location_type"], pairs, f"{key_prefix}LocationType"
        )
    if "location" in value:
        pairs.append((f"{key_prefix}Location", str(value["location"])))


def deserialize_ec2_query(el: Element) -> InstanceTypeOffering:
    out: InstanceTypeOffering = {}  # type: ignore[typeddict-item]
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        import capo_ec2.types.instance_type

        out["instance_type"] = capo_ec2.types.instance_type.deserialize_ec2_query(
            child_instance_type
        )
    child_location_type = el.find("locationType")
    if child_location_type is not None:
        import capo_ec2.types.location_type

        out["location_type"] = capo_ec2.types.location_type.deserialize_ec2_query(
            child_location_type
        )
    child_location = el.find("location")
    if child_location is not None:
        out["location"] = str(child_location.text or "")
    return out
