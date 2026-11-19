"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#ExternalSubnetMapping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.external_az
    import capo_cloudhsm_v2.types.subnet_id

ExternalSubnetMapping: TypeAlias = dict[
    "capo_cloudhsm_v2.types.external_az.ExternalAz",
    "capo_cloudhsm_v2.types.subnet_id.SubnetId",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ExternalSubnetMapping) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ExternalSubnetMapping:
    out: ExternalSubnetMapping = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ExternalSubnetMapping) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> ExternalSubnetMapping:
    out: ExternalSubnetMapping = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
