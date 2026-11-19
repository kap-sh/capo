"""Generated from Smithy shape ``com.amazonaws.fms#PartialMatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.partial_match

PartialMatches: TypeAlias = list["capo_fms.types.partial_match.PartialMatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartialMatches) -> list:
    import capo_fms.types.partial_match

    out: list = []
    for item in value:
        out.append(capo_fms.types.partial_match.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PartialMatches:
    import capo_fms.types.partial_match

    out: PartialMatches = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.partial_match.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PartialMatches) -> list:
    import capo_fms.types.partial_match

    out: list = []
    for item in value:
        out.append(capo_fms.types.partial_match.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PartialMatches:
    import capo_fms.types.partial_match

    out: PartialMatches = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.partial_match.deserialize_cbor(item))
    return out
