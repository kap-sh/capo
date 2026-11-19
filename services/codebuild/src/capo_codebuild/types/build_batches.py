"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildBatches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.build_batch

BuildBatches: TypeAlias = list["capo_codebuild.types.build_batch.BuildBatch"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildBatches) -> list:
    import capo_codebuild.types.build_batch

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_batch.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildBatches:
    import capo_codebuild.types.build_batch

    out: BuildBatches = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build_batch.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildBatches) -> list:
    import capo_codebuild.types.build_batch

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_batch.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> BuildBatches:
    import capo_codebuild.types.build_batch

    out: BuildBatches = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build_batch.deserialize_cbor(item))
    return out
