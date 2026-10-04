"""Generated from Smithy shape ``com.amazonaws.transfer#SftpPortWithOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.communication_mode
    import capo_transfer.types.sftp_port


class SftpPortWithOptions(TypedDict, closed=True):
    sftp_port: "capo_transfer.types.sftp_port.SftpPort"
    """<p>The port on which the Transfer Family server listens for SFTP connections. Specify any integer from 2000 to 65535, or 22. This value is required for each entry in the <code>SftpPorts</code> list.</p>"""
    communication_mode: NotRequired[
        "capo_transfer.types.communication_mode.CommunicationMode"
    ]
    """<p>Determines whether the server or the client sends data first when a client establishes an SFTP connection on this port. Valid values are <code>SERVER_TALK_FIRST</code> and <code>CLIENT_TALK_FIRST</code>. For a description of each mode, see the <code>SftpPorts</code> property. This value is optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SftpPortWithOptions) -> dict:
    out: dict = {}
    out["SftpPort"] = value["sftp_port"]
    if "communication_mode" in value:
        import capo_transfer.types.communication_mode

        out["CommunicationMode"] = (
            capo_transfer.types.communication_mode.serialize_aws_json_1_1(
                value["communication_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SftpPortWithOptions:
    out: SftpPortWithOptions = {}  # type: ignore[typeddict-item]
    if data.get("SftpPort") is not None:
        out["sftp_port"] = data["SftpPort"]
    else:
        raise DeserializationError("SftpPortWithOptions.sftp_port required")
    if data.get("CommunicationMode") is not None:
        import capo_transfer.types.communication_mode

        out["communication_mode"] = (
            capo_transfer.types.communication_mode.deserialize_aws_json_1_1(
                data["CommunicationMode"]
            )
        )
    return out
