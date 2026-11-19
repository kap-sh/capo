"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageBlockerDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.blocker_declaration

StageBlockerDeclarationList: TypeAlias = list[
    "capo_codepipeline.types.blocker_declaration.BlockerDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageBlockerDeclarationList) -> list:
    import capo_codepipeline.types.blocker_declaration

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.blocker_declaration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StageBlockerDeclarationList:
    import capo_codepipeline.types.blocker_declaration

    out: StageBlockerDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.blocker_declaration.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StageBlockerDeclarationList) -> list:
    import capo_codepipeline.types.blocker_declaration

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.blocker_declaration.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> StageBlockerDeclarationList:
    import capo_codepipeline.types.blocker_declaration

    out: StageBlockerDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.blocker_declaration.deserialize_cbor(item))
    return out
