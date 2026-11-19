"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Hsms``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.hsm

Hsms: TypeAlias = list["capo_cloudhsm_v2.types.hsm.Hsm"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Hsms) -> list:
    import capo_cloudhsm_v2.types.hsm

    out: list = []
    for item in value:
        out.append(capo_cloudhsm_v2.types.hsm.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Hsms:
    import capo_cloudhsm_v2.types.hsm

    out: Hsms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudhsm_v2.types.hsm.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Hsms) -> list:
    import capo_cloudhsm_v2.types.hsm

    out: list = []
    for item in value:
        out.append(capo_cloudhsm_v2.types.hsm.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Hsms:
    import capo_cloudhsm_v2.types.hsm

    out: Hsms = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudhsm_v2.types.hsm.deserialize_cbor(item))
    return out
