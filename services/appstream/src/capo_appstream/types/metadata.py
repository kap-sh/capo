"""Generated from Smithy shape ``com.amazonaws.appstream#Metadata``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.string

Metadata: TypeAlias = dict[
    "capo_appstream.types.string.String", "capo_appstream.types.string.String"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Metadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Metadata:
    out: Metadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: Metadata) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> Metadata:
    out: Metadata = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
