"""Generated from Smithy shape ``com.amazonaws.workspaces#ProtocolList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.protocol

ProtocolList: TypeAlias = list["capo_workspaces.types.protocol.Protocol"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtocolList) -> list:
    import capo_workspaces.types.protocol

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.protocol.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProtocolList:
    import capo_workspaces.types.protocol

    out: ProtocolList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.protocol.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProtocolList) -> list:
    import capo_workspaces.types.protocol

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.protocol.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProtocolList:
    import capo_workspaces.types.protocol

    out: ProtocolList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workspaces.types.protocol.deserialize_cbor(item))
    return out
