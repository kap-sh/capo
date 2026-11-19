"""Generated from Smithy shape ``com.amazonaws.gamelift#ServerProcessList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.server_process

ServerProcessList: TypeAlias = list["capo_gamelift.types.server_process.ServerProcess"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServerProcessList) -> list:
    import capo_gamelift.types.server_process

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.server_process.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ServerProcessList:
    import capo_gamelift.types.server_process

    out: ServerProcessList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.server_process.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServerProcessList) -> list:
    import capo_gamelift.types.server_process

    out: list = []
    for item in value:
        out.append(capo_gamelift.types.server_process.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ServerProcessList:
    import capo_gamelift.types.server_process

    out: ServerProcessList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gamelift.types.server_process.deserialize_cbor(item))
    return out
