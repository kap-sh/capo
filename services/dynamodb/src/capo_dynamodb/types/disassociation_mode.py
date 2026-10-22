"""Generated from Smithy shape ``com.amazonaws.dynamodb#DisassociationMode``."""

from typing import Literal, TypeAlias, cast

"""<p>Specifies how pending replication is handled before a replica is disassociated. <code>WAIT_FOR_REPLICATION</code> is the only supported value.</p>"""
DisassociationMode: TypeAlias = Literal["WAIT_FOR_REPLICATION",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociationMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DisassociationMode:
    return cast(DisassociationMode, data)
