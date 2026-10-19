"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#SendSSHPublicKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ec2_instance_connect.types.availability_zone
    import capo_ec2_instance_connect.types.instance_id
    import capo_ec2_instance_connect.types.instance_os_user
    import capo_ec2_instance_connect.types.ssh_public_key


class SendSSHPublicKeyRequest(TypedDict, closed=True):
    instance_id: "capo_ec2_instance_connect.types.instance_id.InstanceId"
    """<p>The ID of the EC2 instance.</p>"""
    instance_os_user: "capo_ec2_instance_connect.types.instance_os_user.InstanceOSUser"
    """<p>The OS user on the EC2 instance for whom the key can be used to authenticate.</p>"""
    ssh_public_key: "capo_ec2_instance_connect.types.ssh_public_key.SSHPublicKey"
    """<p>The public key material. To use the public key, you must have the matching private key.</p>"""
    availability_zone: NotRequired[
        "capo_ec2_instance_connect.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone in which the EC2 instance was launched.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendSSHPublicKeyRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["InstanceOSUser"] = value["instance_os_user"]
    out["SSHPublicKey"] = value["ssh_public_key"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SendSSHPublicKeyRequest:
    out: SendSSHPublicKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    if data.get("InstanceOSUser") is not None:
        out["instance_os_user"] = data["InstanceOSUser"]
    else:
        out["instance_os_user"] = ""
    if data.get("SSHPublicKey") is not None:
        out["ssh_public_key"] = data["SSHPublicKey"]
    else:
        out["ssh_public_key"] = ""
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    return out
