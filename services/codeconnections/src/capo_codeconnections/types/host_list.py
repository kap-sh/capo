"""Generated from Smithy shape ``com.amazonaws.codeconnections#HostList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.host

HostList: TypeAlias = list["capo_codeconnections.types.host.Host"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: HostList) -> list:
    import capo_codeconnections.types.host

    out: list = []
    for item in value:
        out.append(capo_codeconnections.types.host.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> HostList:
    import capo_codeconnections.types.host

    out: HostList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codeconnections.types.host.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HostList) -> list:
    import capo_codeconnections.types.host

    out: list = []
    for item in value:
        out.append(capo_codeconnections.types.host.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> HostList:
    import capo_codeconnections.types.host

    out: HostList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codeconnections.types.host.deserialize_cbor(item))
    return out
