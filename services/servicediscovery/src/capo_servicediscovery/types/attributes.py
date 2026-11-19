"""Generated from Smithy shape ``com.amazonaws.servicediscovery#Attributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_servicediscovery.types.attr_key
    import capo_servicediscovery.types.attr_value

Attributes: TypeAlias = dict[
    "capo_servicediscovery.types.attr_key.AttrKey",
    "capo_servicediscovery.types.attr_value.AttrValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Attributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Attributes:
    out: Attributes = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: Attributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> Attributes:
    out: Attributes = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
