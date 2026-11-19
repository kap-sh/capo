"""Generated from Smithy shape ``com.amazonaws.codebuild#Sandboxes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codebuild.types.sandbox

Sandboxes: TypeAlias = list["capo_codebuild.types.sandbox.Sandbox"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Sandboxes) -> list:
    import capo_codebuild.types.sandbox

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.sandbox.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Sandboxes:
    import capo_codebuild.types.sandbox

    out: Sandboxes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.sandbox.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Sandboxes) -> list:
    import capo_codebuild.types.sandbox

    out: list = []
    for item in value:
        out.append(capo_codebuild.types.sandbox.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Sandboxes:
    import capo_codebuild.types.sandbox

    out: Sandboxes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codebuild.types.sandbox.deserialize_cbor(item))
    return out
