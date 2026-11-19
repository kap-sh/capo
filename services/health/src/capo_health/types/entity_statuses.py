"""Generated from Smithy shape ``com.amazonaws.health#entityStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.count
    import capo_health.types.entity_status_code

entityStatuses: TypeAlias = dict[
    "capo_health.types.entity_status_code.entityStatusCode",
    "capo_health.types.count.count",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: entityStatuses) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_health.types.entity_status_code

        out[capo_health.types.entity_status_code.serialize_aws_json_1_1(key)] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> entityStatuses:
    out: entityStatuses = {}
    for key, value in data.items():
        import capo_health.types.entity_status_code

        if value is None:
            continue
        out[capo_health.types.entity_status_code.deserialize_aws_json_1_1(key)] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: entityStatuses) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_health.types.entity_status_code

        out[capo_health.types.entity_status_code.serialize_cbor(key)] = value
    return out


def deserialize_cbor(data: dict) -> entityStatuses:
    out: entityStatuses = {}
    for key, value in data.items():
        import capo_health.types.entity_status_code

        if value is None:
            continue
        out[capo_health.types.entity_status_code.deserialize_cbor(key)] = value
    return out
