"""Generated from Smithy shape ``com.amazonaws.codepipeline#ArtifactStoreMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.artifact_store
    import capo_codepipeline.types.aws_region_name

ArtifactStoreMap: TypeAlias = dict[
    "capo_codepipeline.types.aws_region_name.AWSRegionName",
    "capo_codepipeline.types.artifact_store.ArtifactStore",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ArtifactStoreMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codepipeline.types.artifact_store

        out[key] = capo_codepipeline.types.artifact_store.serialize_aws_json_1_1(value)
    return out


def deserialize_aws_json_1_1(data: dict) -> ArtifactStoreMap:
    out: ArtifactStoreMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_codepipeline.types.artifact_store

        out[key] = capo_codepipeline.types.artifact_store.deserialize_aws_json_1_1(
            value
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: ArtifactStoreMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_codepipeline.types.artifact_store

        out[key] = capo_codepipeline.types.artifact_store.serialize_cbor(value)
    return out


def deserialize_cbor(data: dict) -> ArtifactStoreMap:
    out: ArtifactStoreMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_codepipeline.types.artifact_store

        out[key] = capo_codepipeline.types.artifact_store.deserialize_cbor(value)
    return out
