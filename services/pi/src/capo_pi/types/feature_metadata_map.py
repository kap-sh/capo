"""Generated from Smithy shape ``com.amazonaws.pi#FeatureMetadataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.feature_metadata
    import capo_pi.types.string

FeatureMetadataMap: TypeAlias = dict[
    "capo_pi.types.string.String", "capo_pi.types.feature_metadata.FeatureMetadata"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: FeatureMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pi.types.feature_metadata

        out[key] = capo_pi.types.feature_metadata.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> FeatureMetadataMap:
    out: FeatureMetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_pi.types.feature_metadata

        out[key] = capo_pi.types.feature_metadata.deserialize_aws_json_1_1(value)
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: FeatureMetadataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pi.types.feature_metadata

        out[key] = capo_pi.types.feature_metadata.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> FeatureMetadataMap:
    out: FeatureMetadataMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_pi.types.feature_metadata

        out[key] = capo_pi.types.feature_metadata.deserialize_cbor(value)
    return out
