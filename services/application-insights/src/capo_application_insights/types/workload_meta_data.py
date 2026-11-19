"""Generated from Smithy shape ``com.amazonaws.applicationinsights#WorkloadMetaData``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_insights.types.meta_data_key
    import capo_application_insights.types.meta_data_value

WorkloadMetaData: TypeAlias = dict[
    "capo_application_insights.types.meta_data_key.MetaDataKey",
    "capo_application_insights.types.meta_data_value.MetaDataValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: WorkloadMetaData) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkloadMetaData:
    out: WorkloadMetaData = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: WorkloadMetaData) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_cbor(data: dict) -> WorkloadMetaData:
    out: WorkloadMetaData = {}
    for key, value in data.items():
        if value is None:
            continue
        out[key] = value
    return out
