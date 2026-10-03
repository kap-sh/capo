"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceBlockDeviceMappingSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ebs_instance_block_device_specification
    import capo_ec2.types.string


class InstanceBlockDeviceMappingSpecification(TypedDict, closed=True):
    device_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The device name. For available device names, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html">Device names for volumes</a>.</p>"""
    ebs: NotRequired[
        "capo_ec2.types.ebs_instance_block_device_specification.EbsInstanceBlockDeviceSpecification"
    ]
    """<p>Parameters used to automatically set up EBS volumes when the instance is launched.</p>"""
    virtual_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The virtual device name.</p>"""
    no_device: NotRequired["capo_ec2.types.string.String"]
    """<p>Suppresses the specified device included in the block device mapping.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceBlockDeviceMappingSpecification,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "device_name" in value:
        pairs.append((f"{key_prefix}DeviceName", str(value["device_name"])))
    if "ebs" in value:
        import capo_ec2.types.ebs_instance_block_device_specification

        capo_ec2.types.ebs_instance_block_device_specification.serialize_ec2_query(
            value["ebs"], pairs, f"{key_prefix}Ebs"
        )
    if "virtual_name" in value:
        pairs.append((f"{key_prefix}VirtualName", str(value["virtual_name"])))
    if "no_device" in value:
        pairs.append((f"{key_prefix}NoDevice", str(value["no_device"])))


def deserialize_ec2_query(el: Element) -> InstanceBlockDeviceMappingSpecification:
    out: InstanceBlockDeviceMappingSpecification = {}  # type: ignore[typeddict-item]
    child_device_name = el.find("deviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    child_ebs = el.find("ebs")
    if child_ebs is not None:
        import capo_ec2.types.ebs_instance_block_device_specification

        out["ebs"] = (
            capo_ec2.types.ebs_instance_block_device_specification.deserialize_ec2_query(
                child_ebs
            )
        )
    child_virtual_name = el.find("virtualName")
    if child_virtual_name is not None:
        out["virtual_name"] = str(child_virtual_name.text or "")
    child_no_device = el.find("noDevice")
    if child_no_device is not None:
        out["no_device"] = str(child_no_device.text or "")
    return out
