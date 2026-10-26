"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleBooleanExpression``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.rule_boolean_operator
    import capo_mailmanager.types.rule_boolean_to_evaluate


class RuleBooleanExpression(TypedDict, closed=True):
    evaluate: "capo_mailmanager.types.rule_boolean_to_evaluate.RuleBooleanToEvaluate"
    """<p>The operand on which to perform a boolean condition operation.</p>"""
    operator: "capo_mailmanager.types.rule_boolean_operator.RuleBooleanOperator"
    """<p>The matching operator for a boolean condition expression.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleBooleanExpression) -> dict:
    out: dict = {}
    import capo_mailmanager.types.rule_boolean_to_evaluate

    out["Evaluate"] = (
        capo_mailmanager.types.rule_boolean_to_evaluate.serialize_aws_json_1_0(
            value["evaluate"]
        )
    )
    import capo_mailmanager.types.rule_boolean_operator

    out["Operator"] = (
        capo_mailmanager.types.rule_boolean_operator.serialize_aws_json_1_0(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleBooleanExpression:
    out: RuleBooleanExpression = {}  # type: ignore[typeddict-item]
    if data.get("Evaluate") is not None:
        import capo_mailmanager.types.rule_boolean_to_evaluate

        out["evaluate"] = (
            capo_mailmanager.types.rule_boolean_to_evaluate.deserialize_aws_json_1_0(
                data["Evaluate"]
            )
        )
    else:
        out["evaluate"] = {"$unknown": {"name": ""}}
    if data.get("Operator") is not None:
        import capo_mailmanager.types.rule_boolean_operator

        out["operator"] = (
            capo_mailmanager.types.rule_boolean_operator.deserialize_aws_json_1_0(
                data["Operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_mailmanager.types.rule_boolean_operator.RuleBooleanOperator", ""
        )
    return out
