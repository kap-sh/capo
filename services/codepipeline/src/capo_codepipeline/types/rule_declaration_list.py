"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.rule_declaration

RuleDeclarationList: TypeAlias = list[
    "capo_codepipeline.types.rule_declaration.RuleDeclaration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleDeclarationList) -> list:
    import capo_codepipeline.types.rule_declaration

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.rule_declaration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RuleDeclarationList:
    import capo_codepipeline.types.rule_declaration

    out: RuleDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.rule_declaration.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleDeclarationList) -> list:
    import capo_codepipeline.types.rule_declaration

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.rule_declaration.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> RuleDeclarationList:
    import capo_codepipeline.types.rule_declaration

    out: RuleDeclarationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.rule_declaration.deserialize_cbor(item))
    return out
