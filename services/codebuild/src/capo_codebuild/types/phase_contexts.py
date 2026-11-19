"""Generated from Smithy shape ``com.amazonaws.codebuild#PhaseContexts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.phase_context

PhaseContexts: TypeAlias = list["capo_codebuild.types.phase_context.PhaseContext"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PhaseContexts) -> list:
    import capo_codebuild.types.phase_context

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.phase_context.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PhaseContexts:
    import capo_codebuild.types.phase_context

    out: PhaseContexts = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.phase_context.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PhaseContexts) -> list:
    import capo_codebuild.types.phase_context

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.phase_context.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> PhaseContexts:
    import capo_codebuild.types.phase_context

    out: PhaseContexts = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.phase_context.deserialize_cbor(item))
    return out
