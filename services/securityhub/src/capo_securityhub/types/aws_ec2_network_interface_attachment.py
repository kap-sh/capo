"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2NetworkInterfaceAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsEc2NetworkInterfaceAttachment(TypedDict, closed=True):
    attach_time: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the attachment initiated.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    attachment_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the network interface attachment</p>"""
    delete_on_termination: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Indicates whether the network interface is deleted when the instance is terminated.</p>"""
    device_index: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>The device index of the network interface attachment on the instance.</p>"""
    instance_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the instance.</p>"""
    instance_owner_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Amazon Web Services account ID of the owner of the instance.</p>"""
    status: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The attachment state.</p> <p>Valid values: <code>attaching</code> | <code>attached</code> | <code>detaching</code> | <code>detached</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2NetworkInterfaceAttachment) -> dict:
    out: dict = {}
    if "attach_time" in value:
        out["AttachTime"] = value["attach_time"]
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "delete_on_termination" in value:
        out["DeleteOnTermination"] = value["delete_on_termination"]
    if "device_index" in value:
        out["DeviceIndex"] = value["device_index"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "instance_owner_id" in value:
        out["InstanceOwnerId"] = value["instance_owner_id"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_json(data: dict) -> AwsEc2NetworkInterfaceAttachment:
    out: AwsEc2NetworkInterfaceAttachment = {}  # type: ignore[typeddict-item]
    if data.get("AttachTime") is not None:
        out["attach_time"] = data["AttachTime"]
    if data.get("AttachmentId") is not None:
        out["attachment_id"] = data["AttachmentId"]
    if data.get("DeleteOnTermination") is not None:
        out["delete_on_termination"] = data["DeleteOnTermination"]
    if data.get("DeviceIndex") is not None:
        out["device_index"] = data["DeviceIndex"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("InstanceOwnerId") is not None:
        out["instance_owner_id"] = data["InstanceOwnerId"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    return out
