"""Generated from Smithy shape ``com.amazonaws.codepipeline#StageActionDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.action_declaration

StageActionDeclarationList: TypeAlias = list[
    "capo_codepipeline.types.action_declaration.ActionDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StageActionDeclarationList) -> list:
    import capo_codepipeline.types.action_declaration

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.action_declaration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> StageActionDeclarationList:
    import capo_codepipeline.types.action_declaration

    out: StageActionDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.action_declaration.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StageActionDeclarationList) -> list:
    import capo_codepipeline.types.action_declaration

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.action_declaration.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> StageActionDeclarationList:
    import capo_codepipeline.types.action_declaration

    out: StageActionDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.action_declaration.deserialize_cbor(item))
    return out
