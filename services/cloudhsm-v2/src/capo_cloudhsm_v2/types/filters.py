"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Filters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.field
    import capo_cloudhsm_v2.types.strings

Filters: TypeAlias = dict[
    "capo_cloudhsm_v2.types.field.Field", "capo_cloudhsm_v2.types.strings.Strings"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Filters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_cloudhsm_v2.types.strings

        out[key] = capo_cloudhsm_v2.types.strings.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> Filters:
    out: Filters = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_cloudhsm_v2.types.strings

        out[key] = capo_cloudhsm_v2.types.strings.deserialize_aws_json_1_1(value)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: Filters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_cloudhsm_v2.types.strings

        out[key] = capo_cloudhsm_v2.types.strings.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> Filters:
    out: Filters = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_cloudhsm_v2.types.strings

        out[key] = capo_cloudhsm_v2.types.strings.deserialize_cbor(value)
    return out
