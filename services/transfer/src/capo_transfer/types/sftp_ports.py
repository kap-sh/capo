"""Generated from Smithy shape ``com.amazonaws.transfer#SftpPorts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.sftp_port_with_options

SftpPorts: TypeAlias = list[
    "capo_transfer.types.sftp_port_with_options.SftpPortWithOptions"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SftpPorts) -> list:
    import capo_transfer.types.sftp_port_with_options

    out: list = []
    for item in value:
        out.append(
            capo_transfer.types.sftp_port_with_options.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SftpPorts:
    import capo_transfer.types.sftp_port_with_options

    out: SftpPorts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transfer.types.sftp_port_with_options.deserialize_aws_json_1_1(item)
        )
    return out
