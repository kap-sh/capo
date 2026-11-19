"""Generated from Smithy shape ``com.amazonaws.codebuild#SandboxSessionPhases``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.sandbox_session_phase

SandboxSessionPhases: TypeAlias = list[
    "capo_codebuild.types.sandbox_session_phase.SandboxSessionPhase"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SandboxSessionPhases) -> list:
    import capo_codebuild.types.sandbox_session_phase

    out: list = []
    for item in value:
        out.append(
            capo_codebuild.types.sandbox_session_phase.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SandboxSessionPhases:
    import capo_codebuild.types.sandbox_session_phase

    out: SandboxSessionPhases = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codebuild.types.sandbox_session_phase.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SandboxSessionPhases) -> list:
    import capo_codebuild.types.sandbox_session_phase

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.sandbox_session_phase.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SandboxSessionPhases:
    import capo_codebuild.types.sandbox_session_phase

    out: SandboxSessionPhases = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.sandbox_session_phase.deserialize_cbor(item))
    return out
