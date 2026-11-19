"""Generated from Smithy shape ``com.amazonaws.fms#InvalidNetworkAclEntriesViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.entry_violations
    import capo_fms.types.length_bounded_string
    import capo_fms.types.resource_id


class InvalidNetworkAclEntriesViolation(TypedDict, closed=True):
    vpc: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The VPC where the violation was found. </p>"""
    subnet: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The subnet that's associated with the network ACL.</p>"""
    subnet_availability_zone: NotRequired[
        "capo_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>The Availability Zone where the network ACL is in use. </p>"""
    current_associated_network_acl: NotRequired["capo_fms.types.resource_id.ResourceId"]
    """<p>The network ACL containing the entry violations. </p>"""
    entry_violations: NotRequired["capo_fms.types.entry_violations.EntryViolations"]
    """<p>Detailed information about the entry violations in the network ACL. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidNetworkAclEntriesViolation) -> dict:
    out: dict = {}
    if "vpc" in value:
        out["Vpc"] = value["vpc"]
    if "subnet" in value:
        out["Subnet"] = value["subnet"]
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "current_associated_network_acl" in value:
        out["CurrentAssociatedNetworkAcl"] = value["current_associated_network_acl"]
    if "entry_violations" in value:
        import capo_fms.types.entry_violations

        out["EntryViolations"] = capo_fms.types.entry_violations.serialize_aws_json_1_1(
            value["entry_violations"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidNetworkAclEntriesViolation:
    out: InvalidNetworkAclEntriesViolation = {}  # type: ignore[typeddict-item]
    if data.get("Vpc") is not None:
        out["vpc"] = data["Vpc"]
    if data.get("Subnet") is not None:
        out["subnet"] = data["Subnet"]
    if data.get("SubnetAvailabilityZone") is not None:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if data.get("CurrentAssociatedNetworkAcl") is not None:
        out["current_associated_network_acl"] = data["CurrentAssociatedNetworkAcl"]
    if data.get("EntryViolations") is not None:
        import capo_fms.types.entry_violations

        out["entry_violations"] = (
            capo_fms.types.entry_violations.deserialize_aws_json_1_1(
                data["EntryViolations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InvalidNetworkAclEntriesViolation) -> dict:
    out: dict = {}
    if "vpc" in value:
        out["Vpc"] = value["vpc"]
    if "subnet" in value:
        out["Subnet"] = value["subnet"]
    if "subnet_availability_zone" in value:
        out["SubnetAvailabilityZone"] = value["subnet_availability_zone"]
    if "current_associated_network_acl" in value:
        out["CurrentAssociatedNetworkAcl"] = value["current_associated_network_acl"]
    if "entry_violations" in value:
        import capo_fms.types.entry_violations

        out["EntryViolations"] = capo_fms.types.entry_violations.serialize_cbor(
            value["entry_violations"]
        )
    return out


def deserialize_cbor(data: dict) -> InvalidNetworkAclEntriesViolation:
    out: InvalidNetworkAclEntriesViolation = {}  # type: ignore[typeddict-item]
    if data.get("Vpc") is not None:
        out["vpc"] = data["Vpc"]
    if data.get("Subnet") is not None:
        out["subnet"] = data["Subnet"]
    if data.get("SubnetAvailabilityZone") is not None:
        out["subnet_availability_zone"] = data["SubnetAvailabilityZone"]
    if data.get("CurrentAssociatedNetworkAcl") is not None:
        out["current_associated_network_acl"] = data["CurrentAssociatedNetworkAcl"]
    if data.get("EntryViolations") is not None:
        import capo_fms.types.entry_violations

        out["entry_violations"] = capo_fms.types.entry_violations.deserialize_cbor(
            data["EntryViolations"]
        )
    return out
