"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationEc2Instance``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.sensitive_string
    import capo_guardduty.types.string
    import capo_guardduty.types.timestamp


class InvestigationEc2Instance(TypedDict, closed=True):
    instance_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the instance.</p>"""
    instance_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The instance type.</p>"""
    instance_state: NotRequired["capo_guardduty.types.string.String"]
    """<p>The state of the instance.</p>"""
    availability_zone: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Availability Zone of the instance.</p>"""
    private_ip_address: NotRequired[
        "capo_guardduty.types.sensitive_string.SensitiveString"
    ]
    """<p>The private IP address of the instance.</p>"""
    public_ip: NotRequired["capo_guardduty.types.string.String"]
    """<p>The public IP address of the instance.</p>"""
    vpc_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the VPC in which the instance runs.</p>"""
    subnet_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the subnet in which the instance runs.</p>"""
    image_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the Amazon Machine Image (AMI) that was used to launch the instance.</p>"""
    launched_at: NotRequired["capo_guardduty.types.timestamp.Timestamp"]
    """<p>The timestamp at which the instance was launched.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationEc2Instance) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "instance_state" in value:
        out["instanceState"] = value["instance_state"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "private_ip_address" in value:
        out["privateIpAddress"] = value["private_ip_address"]
    if "public_ip" in value:
        out["publicIp"] = value["public_ip"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "image_id" in value:
        out["imageId"] = value["image_id"]
    if "launched_at" in value:
        import capo_guardduty.types.timestamp

        out["launchedAt"] = capo_guardduty.types.timestamp.serialize_json(
            value["launched_at"]
        )
    return out


def deserialize_json(data: dict) -> InvestigationEc2Instance:
    out: InvestigationEc2Instance = {}  # type: ignore[typeddict-item]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("instanceState") is not None:
        out["instance_state"] = data["instanceState"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("privateIpAddress") is not None:
        out["private_ip_address"] = data["privateIpAddress"]
    if data.get("publicIp") is not None:
        out["public_ip"] = data["publicIp"]
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    if data.get("imageId") is not None:
        out["image_id"] = data["imageId"]
    if data.get("launchedAt") is not None:
        import capo_guardduty.types.timestamp

        out["launched_at"] = capo_guardduty.types.timestamp.deserialize_json(
            data["launchedAt"]
        )
    return out


def redact_sensitive(value: InvestigationEc2Instance) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "private_ip_address" in value:
        out["private_ip_address"] = "*** Sensitive Data Redacted ***"
    return out
