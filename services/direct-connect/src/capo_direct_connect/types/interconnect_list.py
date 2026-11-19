"""Generated from Smithy shape ``com.amazonaws.directconnect#InterconnectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_direct_connect.types.interconnect

InterconnectList: TypeAlias = list[
    "capo_direct_connect.types.interconnect.Interconnect"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InterconnectList) -> list:
    import capo_direct_connect.types.interconnect

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.interconnect.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> InterconnectList:
    import capo_direct_connect.types.interconnect

    out: InterconnectList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_direct_connect.types.interconnect.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InterconnectList) -> list:
    import capo_direct_connect.types.interconnect

    out: list = []
    for item in value:
        out.append(capo_direct_connect.types.interconnect.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> InterconnectList:
    import capo_direct_connect.types.interconnect

    out: InterconnectList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_direct_connect.types.interconnect.deserialize_cbor(item))
    return out
