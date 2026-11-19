"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildBatchPhases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.build_batch_phase

BuildBatchPhases: TypeAlias = list[
    "capo_codebuild.types.build_batch_phase.BuildBatchPhase"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildBatchPhases) -> list:
    import capo_codebuild.types.build_batch_phase

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_batch_phase.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BuildBatchPhases:
    import capo_codebuild.types.build_batch_phase

    out: BuildBatchPhases = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.build_batch_phase.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildBatchPhases) -> list:
    import capo_codebuild.types.build_batch_phase

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.build_batch_phase.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> BuildBatchPhases:
    import capo_codebuild.types.build_batch_phase

    out: BuildBatchPhases = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.build_batch_phase.deserialize_cbor(item))
    return out
