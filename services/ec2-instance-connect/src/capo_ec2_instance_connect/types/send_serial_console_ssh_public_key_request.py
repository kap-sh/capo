"""Generated from Smithy shape ``com.amazonaws.ec2instanceconnect#SendSerialConsoleSSHPublicKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ec2_instance_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ec2_instance_connect.types.instance_id
    import capo_ec2_instance_connect.types.serial_port
    import capo_ec2_instance_connect.types.ssh_public_key


class SendSerialConsoleSSHPublicKeyRequest(TypedDict, closed=True):
    instance_id: "capo_ec2_instance_connect.types.instance_id.InstanceId"
    """<p>The ID of the EC2 instance.</p>"""
    serial_port: "capo_ec2_instance_connect.types.serial_port.SerialPort"
    """<p>The serial port of the EC2 instance. Currently only port 0 is supported.</p> <p>Default: 0</p>"""
    ssh_public_key: "capo_ec2_instance_connect.types.ssh_public_key.SSHPublicKey"
    """<p>The public key material. To use the public key, you must have the matching private key. For information about the supported key formats and lengths, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html#how-to-generate-your-own-key-and-import-it-to-aws">Requirements for key pairs</a> in the <i>Amazon EC2 User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendSerialConsoleSSHPublicKeyRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["SerialPort"] = value.get("serial_port", 0)
    out["SSHPublicKey"] = value["ssh_public_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SendSerialConsoleSSHPublicKeyRequest:
    out: SendSerialConsoleSSHPublicKeyRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "SendSerialConsoleSSHPublicKeyRequest.instance_id required"
        )
    if data.get("SerialPort") is not None:
        out["serial_port"] = data["SerialPort"]
    else:
        out["serial_port"] = 0
    if data.get("SSHPublicKey") is not None:
        out["ssh_public_key"] = data["SSHPublicKey"]
    else:
        raise DeserializationError(
            "SendSerialConsoleSSHPublicKeyRequest.ssh_public_key required"
        )
    return out
