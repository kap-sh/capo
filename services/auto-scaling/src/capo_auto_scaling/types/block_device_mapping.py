"""Generated from Smithy shape ``com.amazonaws.autoscaling#BlockDeviceMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.ebs
    import capo_auto_scaling.types.no_device
    import capo_auto_scaling.types.xml_string_max_len255


class BlockDeviceMapping(TypedDict, closed=True):
    virtual_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the instance store volume (virtual device) to attach to an instance at launch. The name must be in the form ephemeral<i>X</i> where <i>X</i> is a number starting from zero (0), for example, <code>ephemeral0</code>.</p>"""
    device_name: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The device name assigned to the volume (for example, <code>/dev/sdh</code> or <code>xvdh</code>). For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/device_naming.html">Device naming on Linux instances</a> in the <i>Amazon EC2 User Guide</i>.</p> <note> <p>To define a block device mapping, set the device name and exactly one of the following properties: <code>Ebs</code>, <code>NoDevice</code>, or <code>VirtualName</code>.</p> </note>"""
    ebs: NotRequired["capo_auto_scaling.types.ebs.Ebs"]
    """<p>Information to attach an EBS volume to an instance at launch.</p>"""
    no_device: NotRequired["capo_auto_scaling.types.no_device.NoDevice"]
    """<p>Setting this value to <code>true</code> prevents a volume that is included in the block device mapping of the AMI from being mapped to the specified device name at launch.</p> <p>If <code>NoDevice</code> is <code>true</code> for the root device, instances might fail the EC2 health check. In that case, Amazon EC2 Auto Scaling launches replacement instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BlockDeviceMapping, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "virtual_name" in value:
        pairs.append((f"{key_prefix}VirtualName", str(value["virtual_name"])))
    if "device_name" in value:
        pairs.append((f"{key_prefix}DeviceName", str(value["device_name"])))
    if "ebs" in value:
        import capo_auto_scaling.types.ebs

        capo_auto_scaling.types.ebs.serialize_query(
            value["ebs"], pairs, f"{key_prefix}Ebs"
        )
    if "no_device" in value:
        pairs.append(
            (f"{key_prefix}NoDevice", "true" if value["no_device"] else "false")
        )


def deserialize_query(el: Element) -> BlockDeviceMapping:
    out: BlockDeviceMapping = {}  # type: ignore[typeddict-item]
    child_virtual_name = el.find("VirtualName")
    if child_virtual_name is not None:
        out["virtual_name"] = str(child_virtual_name.text or "")
    child_device_name = el.find("DeviceName")
    if child_device_name is not None:
        out["device_name"] = str(child_device_name.text or "")
    child_ebs = el.find("Ebs")
    if child_ebs is not None:
        import capo_auto_scaling.types.ebs

        out["ebs"] = capo_auto_scaling.types.ebs.deserialize_query(child_ebs)
    child_no_device = el.find("NoDevice")
    if child_no_device is not None:
        out["no_device"] = (child_no_device.text or "").lower() == "true"
    return out
