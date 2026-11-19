"""Generated from Smithy shape ``com.amazonaws.fms#PreviousProtocolsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.previous_list_version
    import capo_fms.types.protocols_list

PreviousProtocolsList: TypeAlias = dict[
    "capo_fms.types.previous_list_version.PreviousListVersion",
    "capo_fms.types.protocols_list.ProtocolsList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PreviousProtocolsList) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fms.types.protocols_list

        out[key] = capo_fms.types.protocols_list.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> PreviousProtocolsList:
    out: PreviousProtocolsList = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_fms.types.protocols_list

        out[key] = capo_fms.types.protocols_list.deserialize_aws_json_1_1(value)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: PreviousProtocolsList) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fms.types.protocols_list

        out[key] = capo_fms.types.protocols_list.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> PreviousProtocolsList:
    out: PreviousProtocolsList = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_fms.types.protocols_list

        out[key] = capo_fms.types.protocols_list.deserialize_cbor(value)
    return out
