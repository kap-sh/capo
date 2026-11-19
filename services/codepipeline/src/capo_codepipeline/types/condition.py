"""Generated from Smithy shape ``com.amazonaws.codepipeline#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.result
    import capo_codepipeline.types.rule_declaration_list


class Condition(TypedDict, closed=True):
    result: NotRequired["capo_codepipeline.types.result.Result"]
    """<p>The action to be done when the condition is met. For example, rolling back an execution for a failure condition.</p>"""
    rules: NotRequired[
        "capo_codepipeline.types.rule_declaration_list.RuleDeclarationList"
    ]
    """<p>The rules that make up the condition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Condition) -> dict:
    out: dict = {}
    if "result" in value:
        import capo_codepipeline.types.result

        out["result"] = capo_codepipeline.types.result.serialize_aws_json_1_1(
            value["result"]
        )
    if "rules" in value:
        import capo_codepipeline.types.rule_declaration_list

        out["rules"] = (
            capo_codepipeline.types.rule_declaration_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if data.get("result") is not None:
        import capo_codepipeline.types.result

        out["result"] = capo_codepipeline.types.result.deserialize_aws_json_1_1(
            data["result"]
        )
    if data.get("rules") is not None:
        import capo_codepipeline.types.rule_declaration_list

        out["rules"] = (
            capo_codepipeline.types.rule_declaration_list.deserialize_aws_json_1_1(
                data["rules"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Condition) -> dict:
    out: dict = {}
    if "result" in value:
        import capo_codepipeline.types.result

        out["result"] = capo_codepipeline.types.result.serialize_cbor(value["result"])
    if "rules" in value:
        import capo_codepipeline.types.rule_declaration_list

        out["rules"] = capo_codepipeline.types.rule_declaration_list.serialize_cbor(
            value["rules"]
        )
    return out


def deserialize_cbor(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if data.get("result") is not None:
        import capo_codepipeline.types.result

        out["result"] = capo_codepipeline.types.result.deserialize_cbor(data["result"])
    if data.get("rules") is not None:
        import capo_codepipeline.types.rule_declaration_list

        out["rules"] = capo_codepipeline.types.rule_declaration_list.deserialize_cbor(
            data["rules"]
        )
    return out
