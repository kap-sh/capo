"""Generated from Smithy shape ``com.amazonaws.fms#ComplianceViolatorMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string

ComplianceViolatorMetadata: TypeAlias = dict[
    "capo_fms.types.length_bounded_string.LengthBoundedString",
    "capo_fms.types.length_bounded_string.LengthBoundedString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ComplianceViolatorMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ComplianceViolatorMetadata:
    out: ComplianceViolatorMetadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ComplianceViolatorMetadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> ComplianceViolatorMetadata:
    out: ComplianceViolatorMetadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
